#!/usr/bin/env python3
"""
Flight #1 Telemetry Chart Generator
====================================

Parses CATS Vega binary flight log (fl001.cfl) and generates flight profile charts.

Usage:
    python3 generate_charts.py

Requirements:
    pip install matplotlib numpy

Input:
    fl001.cfl - CATS Vega binary flight log (same directory)

Output:
    ../flight1_charts.png - 4-panel flight profile chart

CATS Vega Binary Format (v3.0.2):
---------------------------------
Header: 6 bytes (magic + version)
Records: variable length, each starts with:
    - timestamp: uint32 (milliseconds since boot)
    - record_type: uint32

Record Types:
    32 (0x20)  - RAW: 6x int16 (ax, ay, az, gx, gy, gz) - 20 bytes total
    64 (0x40)  - IMU: 6x int16 - 20 bytes total  
    128 (0x80) - BARO: int32 (pressure Pa) - 12 bytes total
    256 (0x100) - FILTERED: 2x float32 (altitude m, velocity m/s) - 16 bytes total

Sensor Information:
-------------------
IMU: STMicroelectronics LSM6DSO32 (from CATS firmware lsm6dso32.hpp)
  - Configured at ±32g range (AccelerometerFs::kFs32G)
  - Sensitivity: 0.976 mg/LSB = 1024 LSB/g (from datasheet)
  - 16-bit output: ±32768 LSB maps to ±32g
  - ODR: 104 Hz

Barometer: MS5607 (temperature-compensated pressure sensor)
  - Altitude formula uses hardcoded 15°C (TEMPERATURE_0 constant)
  - Does not use actual measured temperature for altitude calculation

Known Issues / TODO:
--------------------
1. Liftoff doesn't start exactly at 0m AGL - sensor settling time
2. Velocity shows 0 during descent in some phases - FILTERED data limitation
3. Raw accelerometer data in log has unexpected offset (~-28662 LSB at rest vs expected ~-1024 LSB)
   - May be firmware-specific encoding or uncalibrated offset
   - Needs investigation in CATS firmware data_processing.cpp
4. Temperature not compensated in altitude (hardcoded 15°C in firmware)

Flight Parameters (hardcoded - update for other flights):
---------------------------------------------------------
- liftoff_ts: 278340 ms (timestamp when rocket left pad)
- Motor: AeroTech H128W-14A
- Parachute: 48" diameter
"""

import struct
import os
import sys

# Check for required libraries
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Missing required libraries. Install with:")
    print("  pip install matplotlib numpy")
    sys.exit(1)


def parse_cats_log(filepath):
    """
    Parse CATS Vega binary flight log.
    
    Returns:
        dict with 'filtered' and 'raw' record lists
    """
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Skip 6-byte header
    pos = 6
    filtered_records = []
    raw_records = []
    
    while pos < len(data) - 24:
        try:
            ts = struct.unpack('<I', data[pos:pos+4])[0]
            rec_type = struct.unpack('<I', data[pos+4:pos+8])[0]
            
            # Only process records in flight time window
            if 270000 < ts < 350000:
                if rec_type == 256:  # FILTERED
                    alt = struct.unpack('<f', data[pos+8:pos+12])[0]
                    vel = struct.unpack('<f', data[pos+12:pos+16])[0]
                    filtered_records.append((ts, alt, vel))
                    pos += 16
                elif rec_type == 32:  # RAW
                    vals = struct.unpack('<6h', data[pos+8:pos+20])
                    raw_records.append((ts, vals))
                    pos += 20
                elif rec_type == 64:  # IMU
                    pos += 20
                elif rec_type == 128:  # BARO
                    pos += 12
                else:
                    pos += 4
            else:
                pos += 4
        except:
            pos += 4
    
    return {
        'filtered': filtered_records,
        'raw': raw_records
    }


def generate_charts(records, output_path, liftoff_ts=278340):
    """
    Generate 4-panel flight profile chart.
    
    Args:
        records: dict from parse_cats_log()
        output_path: where to save PNG
        liftoff_ts: timestamp of liftoff in milliseconds
    """
    # Convert filtered data to arrays
    f_times = np.array([(r[0] - liftoff_ts) / 1000 for r in records['filtered']])
    f_alt = np.array([r[1] for r in records['filtered']])
    f_vel = np.array([r[2] for r in records['filtered']])
    
    # Convert raw accelerometer data
    r_times = np.array([(r[0] - liftoff_ts) / 1000 for r in records['raw']])
    ax_raw = np.array([r[1][0] for r in records['raw']])
    
    # Calculate descent rate from altitude change (after chute inflated)
    descent_mask = (f_times > 12) & (f_times < 22)
    if descent_mask.sum() > 2:
        t1, t2 = f_times[descent_mask][0], f_times[descent_mask][-1]
        a1, a2 = f_alt[descent_mask][0], f_alt[descent_mask][-1]
        descent_rate = (a1 - a2) / (t2 - t1)
    else:
        descent_rate = 5.7  # fallback
    
    # Flight events (adjust these for other flights)
    events = {
        'liftoff': 0,
        'burnout': 1.33,
        'apogee': 5.68,
        'deploy': 10.79,
        'landing': 22.86
    }
    
    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Panel 1: Altitude profile
    ax1 = axes[0, 0]
    ax1.plot(f_times, f_alt, 'b-', linewidth=2)
    ax1.fill_between(f_times, 0, f_alt, alpha=0.2)
    ax1.axvline(x=events['liftoff'], color='green', linewidth=2, label='Liftoff')
    ax1.axvline(x=events['burnout'], color='orange', linewidth=2, label=f"Burnout (+{events['burnout']}s)")
    ax1.axvline(x=events['apogee'], color='red', linewidth=2, label=f"Apogee (+{events['apogee']}s)")
    ax1.axvline(x=events['deploy'], color='purple', linewidth=2, label=f"Deploy (+{events['deploy']}s)")
    ax1.axvline(x=events['landing'], color='brown', linewidth=2, label=f"Landing (+{events['landing']}s)")
    ax1.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax1.set_ylabel('Altitude AGL (meters)', fontsize=11)
    ax1.set_title('Altitude Profile', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-1, 24)
    ax1.set_ylim(0, 160)
    
    apogee_alt = f_alt.max()
    ax1.annotate(f'Apogee\n{apogee_alt:.1f} m', 
                 xy=(events['apogee'], apogee_alt), xytext=(7, 145),
                 fontsize=10, ha='left', arrowprops=dict(arrowstyle='->', color='red'))
    
    # Panel 2: Velocity profile
    ax2 = axes[0, 1]
    ax2.plot(f_times, f_vel, 'g-', linewidth=2)
    ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax2.axvline(x=events['liftoff'], color='green', linewidth=2)
    ax2.axvline(x=events['burnout'], color='orange', linewidth=2)
    ax2.axvline(x=events['apogee'], color='red', linewidth=2)
    ax2.axvline(x=events['deploy'], color='purple', linewidth=2)
    ax2.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax2.set_ylabel('Velocity (m/s)', fontsize=11)
    ax2.set_title('Velocity Profile', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-1, 24)
    ax2.annotate(f'Under canopy\n~{descent_rate:.1f} m/s descent', 
                 xy=(16, f_vel[(f_times > 15) & (f_times < 17)].mean()),
                 xytext=(17, -3), fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='purple'))
    
    # Panel 3: Boost phase detail
    ax3 = axes[1, 0]
    mask = (f_times >= -0.1) & (f_times <= 2.5)
    ax3.plot(f_times[mask], f_vel[mask], 'g-', linewidth=2, label='Velocity')
    ax3_alt = ax3.twinx()
    ax3_alt.plot(f_times[mask], f_alt[mask], 'b-', linewidth=2, alpha=0.7, label='Altitude')
    ax3.axvline(x=events['liftoff'], color='green', linewidth=2, label='Liftoff')
    ax3.axvline(x=events['burnout'], color='orange', linewidth=2, label='Burnout')
    ax3.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax3.set_ylabel('Velocity (m/s)', fontsize=11, color='green')
    ax3_alt.set_ylabel('Altitude (m)', fontsize=11, color='blue')
    ax3.set_title('Boost Phase - Motor Burn (AeroTech H128W-14A)', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='center right', fontsize=8)
    
    # Panel 4: Deployment & chute inflation
    ax4 = axes[1, 1]
    mask_r = (r_times >= 10.0) & (r_times <= 14.0)
    mask_f = (f_times >= 10.0) & (f_times <= 14.0)
    
    # Scale accelerometer for visualization
    ax_baseline = ax_raw[mask_r][-100:].mean() if mask_r.sum() > 100 else ax_raw[mask_r].mean()
    ax_display = -(ax_raw[mask_r] - ax_baseline) / 7000 * 20
    
    ax4.plot(f_times[mask_f], f_alt[mask_f], 'b-', linewidth=2, label='Altitude')
    ax4.plot(r_times[mask_r], 80 + ax_display, 'r-', linewidth=1, alpha=0.7, label='Accelerometer (scaled)')
    ax4.axvline(x=events['deploy'], color='purple', linewidth=2)
    ax4.annotate('Ejection charge fires', xy=(events['deploy'], 90), xytext=(10.3, 95),
                 fontsize=9, ha='right', arrowprops=dict(arrowstyle='->', color='purple'))
    ax4.annotate('48" chute\ninflation\noscillations', xy=(11.5, 85), xytext=(12.5, 90),
                 fontsize=9, arrowprops=dict(arrowstyle='->', color='red'))
    ax4.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax4.set_ylabel('Altitude (m) / Accel (scaled)', fontsize=11)
    ax4.set_title('Deployment Event - Parachute Inflation', fontsize=12, fontweight='bold')
    ax4.legend(loc='upper right', fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('MyLevel1Peregrine Flight #1 - L1 Certification\nAeroTech H128W-14A | 141.6m Apogee | 48" Parachute', 
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")


def print_flight_summary(records, liftoff_ts=278340):
    """Print flight timeline and statistics."""
    f_times = np.array([(r[0] - liftoff_ts) / 1000 for r in records['filtered']])
    f_alt = np.array([r[1] for r in records['filtered']])
    f_vel = np.array([r[2] for r in records['filtered']])
    
    print("\n" + "="*50)
    print("FLIGHT #1 SUMMARY")
    print("="*50)
    print(f"Motor: AeroTech H128W-14A")
    print(f"Apogee: {f_alt.max():.1f} m at T+{f_times[np.argmax(f_alt)]:.2f}s")
    print(f"Max velocity: {f_vel.max():.1f} m/s at T+{f_times[np.argmax(f_vel)]:.2f}s")
    print(f"\nTimeline:")
    print(f"  T+0.00s    Liftoff")
    print(f"  T+1.33s    Motor burnout")
    print(f"  T+5.68s    Apogee (141.6m)")
    print(f"  T+10.79s   Ejection charge fires")
    print(f"  T+10.8-12s Chute inflation")
    print(f"  T+22.86s   Landing (CATS stops logging)")


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'fl001.cfl')
    output_file = os.path.join(script_dir, '..', 'flight1_charts.png')
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        sys.exit(1)
    
    print(f"Parsing: {input_file}")
    records = parse_cats_log(input_file)
    print(f"Found {len(records['filtered'])} filtered records, {len(records['raw'])} raw records")
    
    print_flight_summary(records)
    generate_charts(records, output_file)
