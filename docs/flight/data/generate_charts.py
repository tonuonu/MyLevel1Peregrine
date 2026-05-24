#!/usr/bin/env python3
"""CATS Vega .cfl flight log → telemetry chart + stats JSON.

Binary format reference: ../CATS_FORMAT.md (kept separate from this script
so a casual edit cannot silently erase the format spec — see commit
d80e0d5 / 862982f history if you need the cautionary tale).

Usage:
    python generate_charts.py <input.cfl> <output.png> [--motor "NAME"]
                              [--title "TITLE"] [--json out.json]
"""

import argparse
import json
import os
import struct
import sys

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Install with: pip install matplotlib numpy", file=sys.stderr)
    sys.exit(1)


REC_ID_MASK = 0x0F

# Record type → (name, payload_size_bytes, payload_struct_or_None)
# Sizes come from cats-embedded recorder.hpp and types.hpp on firmware 3.0.2.
# If you add a type, also update CATS_FORMAT.md.
RECORDS = {
    0x010: ("IMU",                  12, "<6h"),
    0x020: ("BARO",                  8, "<2i"),
    0x040: ("FLIGHT_INFO",          12, "<3f"),
    0x080: ("ORIENTATION_INFO",      8, "<4h"),
    0x100: ("FILTERED_DATA_INFO",    8, "<2f"),
    0x200: ("FLIGHT_STATE",          4, "<I"),
    0x400: ("EVENT_INFO",            8, None),
    0x800: ("ERROR_INFO",            4, "<I"),
    0x1000: ("GNSS_INFO",            9, "<2fB"),   # packed: float lat, float lon, uint8 sats
    0x2000: ("VOLTAGE_INFO",         2, "<H"),
}

FSM_STATES = {
    0: "INVALID", 1: "CALIBRATING", 2: "READY", 3: "THRUSTING",
    4: "COASTING", 5: "DROGUE", 6: "MAIN", 7: "TOUCHDOWN",
}


def parse_cfl(path):
    with open(path, "rb") as f:
        data = f.read()

    # Header: null-terminated version string
    null = data.index(b"\x00")
    version = data[:null].decode("ascii", errors="replace")
    pos = null + 1

    records = {name: [] for _, (name, _, _) in RECORDS.items()}
    unknown_types = {}

    while pos + 8 <= len(data):
        ts = struct.unpack_from("<I", data, pos)[0]
        rec_type_raw = struct.unpack_from("<I", data, pos + 4)[0]
        rec_type = rec_type_raw & ~REC_ID_MASK
        sensor_id = rec_type_raw & REC_ID_MASK

        if rec_type not in RECORDS:
            unknown_types[rec_type_raw] = unknown_types.get(rec_type_raw, 0) + 1
            # Strict: stop on first unknown. Do NOT slide bytes — that loses
            # alignment forever and produces garbage downstream.
            break

        name, payload_size, payload_fmt = RECORDS[rec_type]
        payload_start = pos + 8
        payload_end = payload_start + payload_size
        if payload_end > len(data):
            break

        if payload_fmt is not None:
            values = struct.unpack_from(payload_fmt, data, payload_start)
        else:
            values = tuple(data[payload_start:payload_end])
        records[name].append((ts, sensor_id) + values)
        pos = payload_end

    return {
        "version": version,
        "bytes_read": pos,
        "bytes_total": len(data),
        "records": records,
        "unknown_types": unknown_types,
    }


def find_state_transitions(records):
    """Return dict of state_name → first ts where FSM entered that state."""
    out = {}
    for row in records.get("FLIGHT_STATE", []):
        ts, _sensor_id, state = row
        name = FSM_STATES.get(state, f"UNKNOWN({state})")
        if name not in out:
            out[name] = ts
    return out


def derive_flight_summary(parsed):
    rec = parsed["records"]
    states = find_state_transitions(rec)

    # FLIGHT_INFO: (ts, sensor_id, height, velocity, accel)
    fi = rec["FLIGHT_INFO"]
    if not fi:
        raise RuntimeError("No FLIGHT_INFO records found")

    # Prefer FLIGHT_STATE for liftoff; otherwise first velocity > 5 m/s
    if "THRUSTING" in states:
        liftoff_ts = states["THRUSTING"]
    else:
        liftoff_ts = next((r[0] for r in fi if r[3] > 5.0), fi[0][0])

    arr = np.array([(r[0], r[2], r[3], r[4]) for r in fi], dtype=float)
    t_rel = (arr[:, 0] - liftoff_ts) / 1000.0
    height = arr[:, 1]
    velocity = arr[:, 2]
    accel = arr[:, 3]

    apogee_idx = int(np.argmax(height))
    apogee_t = float(t_rel[apogee_idx])
    apogee_h = float(height[apogee_idx])

    boost_mask = (t_rel >= 0) & (t_rel < 5)
    if boost_mask.any():
        i = int(np.argmax(velocity[boost_mask]))
        max_vel_t = float(t_rel[boost_mask][i])
        max_vel = float(velocity[boost_mask][i])
    else:
        i = int(np.argmax(velocity))
        max_vel_t = float(t_rel[i])
        max_vel = float(velocity[i])

    summary = {
        "liftoff_ts_ms": liftoff_ts,
        "apogee_m": apogee_h,
        "apogee_t_s": apogee_t,
        "max_velocity_m_s": max_vel,
        "max_velocity_t_s": max_vel_t,
        "max_acceleration_m_s2": float(np.max(accel)),
        "state_transitions": {k: (v - liftoff_ts) / 1000.0 for k, v in states.items()},
        "state_transitions_raw_ms": states,
        "flight_info_count": len(fi),
        "imu_count": len(rec["IMU"]),
        "baro_count": len(rec["BARO"]),
        "filtered_count": len(rec["FILTERED_DATA_INFO"]),
        "voltage_count": len(rec["VOLTAGE_INFO"]),
        "duration_s": float(t_rel[-1]),
    }
    return summary, t_rel, height, velocity, accel


def generate_chart(parsed, output_png, title=None, motor=None):
    summary, t_rel, height, velocity, accel = derive_flight_summary(parsed)
    states = summary["state_transitions"]

    # Zero altitude at liftoff
    t0_idx = int(np.argmin(np.abs(t_rel)))
    alt = height - height[t0_idx]

    apogee_t = summary["apogee_t_s"]
    apogee_h = summary["apogee_m"]
    burnout_t = states.get("COASTING", summary["max_velocity_t_s"])
    drogue_t = states.get("DROGUE", apogee_t)
    main_t = states.get("MAIN")
    touchdown_t = states.get("TOUCHDOWN", float(t_rel[-1]))

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Altitude
    ax1 = axes[0, 0]
    ax1.plot(t_rel, alt, "b-", linewidth=2)
    ax1.fill_between(t_rel, 0, alt, alpha=0.2)
    ax1.axhline(y=0, color="black", linewidth=1)
    ax1.axvline(x=0, color="green", linewidth=2, label="Liftoff")
    ax1.axvline(x=burnout_t, color="orange", linewidth=2, label=f"Burnout (+{burnout_t:.2f}s)")
    ax1.axvline(x=apogee_t, color="red", linewidth=2, label=f"Apogee (+{apogee_t:.2f}s)")
    ax1.axvline(x=drogue_t, color="purple", linewidth=2, label=f"Drogue (+{drogue_t:.2f}s)")
    if main_t is not None and main_t != drogue_t:
        ax1.axvline(x=main_t, color="magenta", linewidth=2, label=f"Main (+{main_t:.2f}s)")
    ax1.axvline(x=touchdown_t, color="brown", linewidth=2, label=f"Touchdown (+{touchdown_t:.2f}s)")
    ax1.set_xlabel("Time from Liftoff (s)")
    ax1.set_ylabel("Altitude AGL (m)")
    ax1.set_title("Altitude Profile")
    ax1.legend(loc="upper right", fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.annotate(f"Apogee\n{apogee_h:.1f} m",
                 xy=(apogee_t, apogee_h),
                 xytext=(apogee_t + 1.5, apogee_h * 1.02),
                 fontsize=10, arrowprops=dict(arrowstyle="->", color="red"))

    # Panel 2: Velocity
    ax2 = axes[0, 1]
    ax2.plot(t_rel, velocity, "g-", linewidth=2)
    ax2.axhline(y=0, color="gray", linestyle="--", alpha=0.5)
    for x, c in [(0, "green"), (burnout_t, "orange"), (apogee_t, "red"),
                 (drogue_t, "purple"), (touchdown_t, "brown")]:
        ax2.axvline(x=x, color=c, linewidth=2)
    if main_t is not None and main_t != drogue_t:
        ax2.axvline(x=main_t, color="magenta", linewidth=2)
    ax2.set_xlabel("Time from Liftoff (s)")
    ax2.set_ylabel("Velocity (m/s)")
    ax2.set_title("Velocity Profile (Kalman filter)")
    ax2.grid(True, alpha=0.3)
    ax2.annotate(f"Max: {summary['max_velocity_m_s']:.1f} m/s",
                 xy=(summary["max_velocity_t_s"], summary["max_velocity_m_s"]),
                 xytext=(summary["max_velocity_t_s"] + 2, summary["max_velocity_m_s"] - 10),
                 fontsize=9, arrowprops=dict(arrowstyle="->", color="green"))

    # Panel 3: Boost detail
    ax3 = axes[1, 0]
    mask = (t_rel >= -0.2) & (t_rel <= burnout_t + 1.2)
    ax3.plot(t_rel[mask], velocity[mask], "g-", linewidth=2, label="Velocity")
    ax3b = ax3.twinx()
    ax3b.plot(t_rel[mask], alt[mask], "b-", linewidth=2, alpha=0.7)
    ax3.axvline(x=0, color="green", linewidth=2)
    ax3.axvline(x=burnout_t, color="orange", linewidth=2)
    ax3.set_xlabel("Time from Liftoff (s)")
    ax3.set_ylabel("Velocity (m/s)", color="green")
    ax3b.set_ylabel("Altitude (m)", color="blue")
    boost_title = "Boost Phase"
    if motor:
        boost_title += f" — {motor}"
    ax3.set_title(boost_title)
    ax3.grid(True, alpha=0.3)

    # Panel 4: Recovery detail (apogee → touchdown)
    ax4 = axes[1, 1]
    rec_mask = (t_rel >= apogee_t - 1) & (t_rel <= touchdown_t + 1)
    ax4.plot(t_rel[rec_mask], alt[rec_mask], "b-", linewidth=2, label="Altitude")
    ax4.axvline(x=drogue_t, color="purple", linewidth=2, label=f"Drogue (+{drogue_t:.2f}s)")
    if main_t is not None and main_t != drogue_t:
        ax4.axvline(x=main_t, color="magenta", linewidth=2, label=f"Main (+{main_t:.2f}s)")
    ax4.axvline(x=touchdown_t, color="brown", linewidth=2, label=f"Touchdown (+{touchdown_t:.2f}s)")
    ax4.set_xlabel("Time from Liftoff (s)")
    ax4.set_ylabel("Altitude AGL (m)")
    ax4.set_title("Recovery Phase")
    ax4.legend(loc="upper right", fontsize=8)
    ax4.grid(True, alpha=0.3)

    if title is None:
        title = f"{apogee_h:.1f} m Apogee | {summary['max_velocity_m_s']:.1f} m/s Max Velocity"
    plt.suptitle(title, fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(output_png, dpi=150, bbox_inches="tight")
    plt.close()

    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cfl")
    p.add_argument("png")
    p.add_argument("--motor", default=None)
    p.add_argument("--title", default=None)
    p.add_argument("--json", default=None, help="Optional summary JSON output path")
    args = p.parse_args()

    if not os.path.exists(args.cfl):
        print(f"Error: {args.cfl} not found", file=sys.stderr)
        sys.exit(1)

    parsed = parse_cfl(args.cfl)
    print(f"Firmware: {parsed['version']}")
    print(f"Parsed:   {parsed['bytes_read']} / {parsed['bytes_total']} bytes "
          f"({100 * parsed['bytes_read'] / parsed['bytes_total']:.2f}%)")
    if parsed["unknown_types"]:
        for rt, n in parsed["unknown_types"].items():
            print(f"  ! Unknown rec_type_raw=0x{rt:x} (count {n}) — parser stopped here")

    counts = {name: len(rs) for name, rs in parsed["records"].items() if rs}
    print(f"Records:  {counts}")

    summary = generate_chart(parsed, args.png, title=args.title, motor=args.motor)
    print(f"\nApogee:        {summary['apogee_m']:.2f} m at T+{summary['apogee_t_s']:.2f} s")
    print(f"Max velocity:  {summary['max_velocity_m_s']:.2f} m/s at T+{summary['max_velocity_t_s']:.2f} s")
    print(f"Max accel:     {summary['max_acceleration_m_s2']:.2f} m/s² ({summary['max_acceleration_m_s2']/9.81:.1f} g)")
    print(f"Duration:      {summary['duration_s']:.2f} s")
    print(f"FSM events:    {summary['state_transitions']}")
    print(f"Chart:         {args.png}")

    if args.json:
        with open(args.json, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"JSON:          {args.json}")


if __name__ == "__main__":
    main()
