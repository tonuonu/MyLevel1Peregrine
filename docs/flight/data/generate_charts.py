#!/usr/bin/env python3
"""
CATS Vega Flight Data Chart Generator
=====================================

Generates telemetry charts from CATS Vega .cfl binary log files.

CATS Data Format Reference (from cats-embedded/flight_computer/src/flash/recorder.hpp):

Record Types (lower 4 bits are sensor ID, masked with 0x0F):
  - 0x10 (16)  IMU:               6 x int16 (acc_xyz, gyro_xyz) in raw LSB
  - 0x20 (32)  BARO:              2 x int32 (pressure in Pa, temperature)  
  - 0x40 (64)  FLIGHT_INFO:       3 x float32 (height, velocity, acceleration) ← Kalman filter
  - 0x80 (128) ORIENTATION_INFO:  4 x int16 (quaternion)
  - 0x100(256) FILTERED_DATA_INFO: 2 x float32 (altitude_AGL, acceleration) ← median filtered

IMPORTANT: Use FLIGHT_INFO (type 0x40) for velocity data!
           FILTERED_DATA_INFO (type 0x100) contains acceleration, NOT velocity.

Hardware:
  - IMU: LSM6DSO32 at ±32g range, sensitivity 1024 LSB/g (0.976 mg/LSB)
  - Barometer: MS5607 (altitude uses hardcoded 15°C, not actual temperature)

Usage:
  python generate_charts.py fl001.cfl [output.png]

Reference:
  https://github.com/catsystems/cats-embedded/blob/main/flight_computer/src/flash/recorder.hpp
"""

import struct
import sys
import os

# Check for matplotlib
try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Error: matplotlib and numpy required. Install with:")
    print("  pip install matplotlib numpy")
    sys.exit(1)

# CATS record type constants (upper bits, lower 4 bits are sensor ID)
REC_ID_MASK = 0x0F
IMU = 0x10                  # 16: acc + gyro (6 x int16)
BARO = 0x20                 # 32: pressure + temperature (2 x int32)
FLIGHT_INFO = 0x40          # 64: height + velocity + acceleration (3 x float32)
ORIENTATION_INFO = 0x80     # 128: quaternion (4 x int16)
FILTERED_DATA_INFO = 0x100  # 256: altitude + acceleration (2 x float32)
FLIGHT_STATE = 0x200        # 512: state enum (1 x uint32)
EVENT_INFO = 0x400          # 1024: event + action (uint32 + uint16 + int16)


def parse_cfl(filename):
    """Parse CATS .cfl binary log file.
    
    Returns dict with parsed records for each type.
    """
    with open(filename, 'rb') as f:
        data = f.read()
    
    # Skip version string header (null-terminated)
    pos = 0
    while pos < len(data) and data[pos] != 0:
        pos += 1
    pos += 1  # Skip null terminator
    
    records = {
        'imu': [],
        'baro': [],
        'flight_info': [],
        'orientation': [],
        'filtered': [],
        'events': [],
        'states': []
    }
    
    while pos < len(data) - 8:
        try:
            ts = struct.unpack('<I', data[pos:pos+4])[0]
            rec_type_raw = struct.unpack('<I', data[pos+4:pos+8])[0]
            rec_type = rec_type_raw & ~REC_ID_MASK
            sensor_id = rec_type_raw & REC_ID_MASK
            
            if rec_type == IMU:
                vals = struct.unpack('<6h', data[pos+8:pos+20])
                records['imu'].append((ts, sensor_id, vals))
                pos += 20
            elif rec_type == BARO:
                pressure, temp = struct.unpack('<2i', data[pos+8:pos+16])
                records['baro'].append((ts, sensor_id, pressure, temp))
                pos += 16
            elif rec_type == FLIGHT_INFO:
                height, velocity, accel = struct.unpack('<3f', data[pos+8:pos+20])
                records['flight_info'].append((ts, height, velocity, accel))
                pos += 20
            elif rec_type == ORIENTATION_INFO:
                quat = struct.unpack('<4h', data[pos+8:pos+16])
                records['orientation'].append((ts, quat))
                pos += 16
            elif rec_type == FILTERED_DATA_INFO:
                alt, accel = struct.unpack('<2f', data[pos+8:pos+16])
                records['filtered'].append((ts, alt, accel))
                pos += 16
            elif rec_type == FLIGHT_STATE:
                state = struct.unpack('<I', data[pos+8:pos+12])[0]
                records['states'].append((ts, state))
                pos += 12
            elif rec_type == EVENT_INFO:
                event = struct.unpack('<I', data[pos+8:pos+12])[0]
                records['events'].append((ts, event))
                pos += 16
            else:
                pos += 4
        except (struct.error, IndexError):
            pos += 4
    
    return records


def find_liftoff_timestamp(records):
    """Find liftoff timestamp from flight state transitions."""
    # Look for THRUSTING state (state=3)
    for ts, state in records['states']:
        if state == 3:  # THRUSTING
            return ts
    
    # Fallback: find when velocity first exceeds threshold
    for ts, h, v, a in records['flight_info']:
        if v > 5.0:  # 5 m/s threshold
            return ts - 100  # Back up slightly
    
    # Last resort: first flight_info record
    if records['flight_info']:
        return records['flight_info'][0][0]
    return 0


def generate_charts(cfl_file, output_file='flight_charts.png', motor_name=''):
    """Generate 4-panel telemetry chart from CATS .cfl file."""
    
    print(f"Parsing {cfl_file}...")
    records = parse_cfl(cfl_file)
    
    if not records['flight_info']:
        print("Error: No FLIGHT_INFO records found")
        return False
    
    print(f"  Found {len(records['flight_info'])} FLIGHT_INFO records")
    print(f"  Found {len(records['imu'])} IMU records")
    
    liftoff_ts = find_liftoff_timestamp(records)
    print(f"  Liftoff timestamp: {liftoff_ts} ms")
    
    # Extract FLIGHT_INFO data (has correct velocity from Kalman filter)
    fi_times = np.array([(r[0] - liftoff_ts) / 1000 for r in records['flight_info']])
    fi_height = np.array([r[1] for r in records['flight_info']])
    fi_velocity = np.array([r[2] for r in records['flight_info']])
    fi_accel = np.array([r[3] for r in records['flight_info']])
    
    # Zero altitude at liftoff (T=0)
    t0_idx = np.argmin(np.abs(fi_times))
    altitude = fi_height - fi_height[t0_idx]
    
    # Extract IMU data for deployment detail
    if records['imu']:
        imu_times = np.array([(r[0] - liftoff_ts) / 1000 for r in records['imu']])
        imu_ax = np.array([r[2][0] for r in records['imu']])
    else:
        imu_times = fi_times
        imu_ax = np.zeros_like(fi_times)
    
    # Calculate key flight events
    apogee_idx = np.argmax(altitude)
    apogee_time = fi_times[apogee_idx]
    apogee_alt = altitude[apogee_idx]
    
    # Max velocity during boost (first 3 seconds)
    boost_mask = (fi_times > 0) & (fi_times < 3.0)
    if np.any(boost_mask):
        max_vel = fi_velocity[boost_mask].max()
        max_vel_time = fi_times[boost_mask][np.argmax(fi_velocity[boost_mask])]
    else:
        max_vel = fi_velocity.max()
        max_vel_time = fi_times[np.argmax(fi_velocity)]
    
    # Burnout detection (velocity peak in first 3 seconds)
    burnout_time = max_vel_time
    
    # Deployment detection (large velocity change after apogee)
    post_apogee = fi_times > apogee_time + 2
    if np.any(post_apogee):
        vel_post = fi_velocity[post_apogee]
        vel_diff = np.abs(np.diff(vel_post))
        if len(vel_diff) > 0:
            deploy_rel_idx = np.argmax(vel_diff)
            deploy_time = fi_times[post_apogee][deploy_rel_idx]
        else:
            deploy_time = apogee_time + 5
    else:
        deploy_time = apogee_time + 5
    
    # Landing detection
    late_flight = fi_times > deploy_time + 5
    if np.any(late_flight):
        landing_mask = late_flight & (altitude < 10)
        if np.any(landing_mask):
            landing_time = fi_times[landing_mask][0]
        else:
            landing_time = fi_times[-1]
    else:
        landing_time = fi_times[-1]
    
    # Descent rate under canopy
    canopy_mask = (fi_times > deploy_time + 3) & (fi_times < landing_time - 2)
    if np.any(canopy_mask):
        descent_rate = fi_velocity[canopy_mask].mean()
    else:
        descent_rate = -5.5
    
    # Print flight summary
    print(f"\nFlight Summary:")
    print(f"  Apogee: {apogee_alt:.1f}m at T+{apogee_time:.2f}s")
    print(f"  Max velocity: {max_vel:.1f} m/s at T+{max_vel_time:.2f}s")
    print(f"  Burnout: T+{burnout_time:.2f}s")
    print(f"  Deployment: T+{deploy_time:.2f}s")
    print(f"  Descent rate: {descent_rate:.1f} m/s")
    print(f"  Landing: T+{landing_time:.2f}s")
    
    # Create 4-panel chart
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Panel 1: Altitude Profile
    ax1 = axes[0, 0]
    ax1.plot(fi_times, altitude, 'b-', linewidth=2)
    ax1.fill_between(fi_times, 0, altitude, alpha=0.2)
    ax1.axhline(y=0, color='black', linewidth=1)
    ax1.axvline(x=0, color='green', linewidth=2, label='Liftoff')
    ax1.axvline(x=burnout_time, color='orange', linewidth=2, label=f'Burnout (+{burnout_time:.2f}s)')
    ax1.axvline(x=apogee_time, color='red', linewidth=2, label=f'Apogee (+{apogee_time:.2f}s)')
    ax1.axvline(x=deploy_time, color='purple', linewidth=2, label=f'Deploy (+{deploy_time:.2f}s)')
    ax1.axvline(x=landing_time, color='brown', linewidth=2, label=f'Landing (+{landing_time:.2f}s)')
    ax1.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax1.set_ylabel('Altitude AGL (meters)', fontsize=11)
    ax1.set_title('Altitude Profile', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=8)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-1, landing_time + 2)
    ax1.set_ylim(-5, apogee_alt * 1.15)
    ax1.annotate(f'Apogee\n{apogee_alt:.1f} m', xy=(apogee_time, apogee_alt),
                 xytext=(apogee_time + 1.5, apogee_alt * 1.02),
                 fontsize=10, arrowprops=dict(arrowstyle='->', color='red'))
    
    # Panel 2: Velocity Profile
    ax2 = axes[0, 1]
    ax2.plot(fi_times, fi_velocity, 'g-', linewidth=2)
    ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax2.axvline(x=0, color='green', linewidth=2, label='Liftoff')
    ax2.axvline(x=burnout_time, color='orange', linewidth=2, label='Burnout')
    ax2.axvline(x=apogee_time, color='red', linewidth=2, label='Apogee')
    ax2.axvline(x=deploy_time, color='purple', linewidth=2, label='Deploy')
    ax2.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax2.set_ylabel('Velocity (m/s)', fontsize=11)
    ax2.set_title('Velocity Profile (CATS Kalman Filter)', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=8)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-1, landing_time + 2)
    ax2.annotate(f'Max: {max_vel:.1f} m/s', xy=(max_vel_time, max_vel),
                 xytext=(max_vel_time + 1, max_vel - 5),
                 fontsize=9, arrowprops=dict(arrowstyle='->', color='green'))
    ax2.annotate(f'Descent: {descent_rate:.1f} m/s', 
                 xy=(landing_time - 4, descent_rate),
                 xytext=(landing_time - 2, descent_rate + 8),
                 fontsize=9, arrowprops=dict(arrowstyle='->', color='purple'))
    
    # Panel 3: Boost Phase Detail
    ax3 = axes[1, 0]
    boost_end = burnout_time + 1.2
    mask = (fi_times >= -0.2) & (fi_times <= boost_end)
    ax3.plot(fi_times[mask], fi_velocity[mask], 'g-', linewidth=2, label='Velocity')
    ax3_alt = ax3.twinx()
    ax3_alt.plot(fi_times[mask], altitude[mask], 'b-', linewidth=2, alpha=0.7)
    ax3.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
    ax3.axvline(x=0, color='green', linewidth=2)
    ax3.axvline(x=burnout_time, color='orange', linewidth=2)
    ax3.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax3.set_ylabel('Velocity (m/s)', fontsize=11, color='green')
    ax3_alt.set_ylabel('Altitude (m)', fontsize=11, color='blue')
    title = 'Boost Phase - Motor Burn'
    if motor_name:
        title += f' ({motor_name})'
    ax3.set_title(title, fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='center right', fontsize=8)
    
    # Panel 4: Deployment Event Detail
    ax4 = axes[1, 1]
    deploy_mask_f = (fi_times >= deploy_time - 1) & (fi_times <= deploy_time + 4)
    deploy_mask_i = (imu_times >= deploy_time - 1) & (imu_times <= deploy_time + 4)
    
    ax4.plot(fi_times[deploy_mask_f], altitude[deploy_mask_f], 'b-', linewidth=2, label='Altitude')
    
    if np.any(deploy_mask_i) and len(imu_ax[deploy_mask_i]) > 0:
        # Scale accelerometer for display
        imu_segment = imu_ax[deploy_mask_i]
        if len(imu_segment) > 50:
            imu_baseline = imu_segment[-50:].mean()
        else:
            imu_baseline = imu_segment.mean()
        imu_scaled = -(imu_segment - imu_baseline) / 7000 * 20
        alt_center = altitude[deploy_mask_f].mean()
        ax4.plot(imu_times[deploy_mask_i], alt_center - 10 + imu_scaled, 
                 'r-', linewidth=1, alpha=0.7, label='Accelerometer (scaled)')
    
    ax4.axvline(x=deploy_time, color='purple', linewidth=2)
    ax4.annotate('Ejection', xy=(deploy_time, altitude[deploy_mask_f].max() - 2),
                 xytext=(deploy_time - 0.5, altitude[deploy_mask_f].max() + 3),
                 fontsize=9, ha='right', arrowprops=dict(arrowstyle='->', color='purple'))
    ax4.set_xlabel('Time from Liftoff (seconds)', fontsize=11)
    ax4.set_ylabel('Altitude (m) / Accel (scaled)', fontsize=11)
    ax4.set_title('Deployment Event - Parachute Inflation', fontsize=12, fontweight='bold')
    ax4.legend(loc='upper right', fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    # Main title
    title = f'Flight Telemetry Analysis\n{apogee_alt:.1f}m Apogee | {max_vel:.1f} m/s Max Velocity'
    if motor_name:
        title = f'Flight Telemetry - {motor_name}\n{apogee_alt:.1f}m Apogee | {max_vel:.1f} m/s Max Velocity'
    plt.suptitle(title, fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\nChart saved to: {output_file}")
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUsage: python generate_charts.py <flight.cfl> [output.png] [motor_name]")
        print("\nExample:")
        print("  python generate_charts.py fl001.cfl flight1_charts.png 'AeroTech H128W-14A'")
        sys.exit(1)
    
    cfl_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'flight_charts.png'
    motor_name = sys.argv[3] if len(sys.argv) > 3 else ''
    
    if not os.path.exists(cfl_file):
        print(f"Error: File not found: {cfl_file}")
        sys.exit(1)
    
    success = generate_charts(cfl_file, output_file, motor_name)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
