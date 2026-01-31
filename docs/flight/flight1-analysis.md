# Flight #1 Analysis

Detailed analysis of CATS Vega telemetry data from the L1 certification flight.

## Problem Statement

Simulation predicted 208m apogee, flight computer logged 141.5m — a 32% shortfall.

## Flight Event Timeline

Data from CATS Vega log file `fl001.cfl`:

| Event | Time (ms) | From Liftoff | Altitude (m) | Velocity (m/s) |
|-------|-----------|--------------|--------------|----------------|
| Liftoff | 278340 | 0.00s | 0 | 0 |
| Max Velocity | 279570 | 1.23s | — | 46.2 |
| Burnout | 279670 | 1.33s | 39.84 | — |
| Apogee | 283990 | 5.65s | 141.5 | 0 |
| Drogue | 284320 | 5.98s | 141.4 | — |
| Main | 284630 | 6.29s | 141.4 | — |
| Deployment (accel) | 289130 | 10.79s | — | — |
| Landing | 301200 | 22.86s | 0 | -5.5 |

**Burn time**: 1.33s (matches H128W specification of ~1.4s)

**Motor delay**: 9.46s (from burnout to deployment shock in accelerometer)

**Deployment after apogee**: 5.14s

## Telemetry Charts

![Flight #1 Telemetry](flight1_charts.png)

*Altitude, velocity, boost phase, and parachute deployment profiles from CATS Vega data.*

## Data Format Notes

The CATS Vega .cfl binary log contains multiple record types. For telemetry analysis:

| Record Type | Value | Contents | Use |
|-------------|-------|----------|-----|
| FLIGHT_INFO | 0x40 (64) | height, **velocity**, acceleration | Kalman filter output - use for velocity! |
| FILTERED_DATA_INFO | 0x100 (256) | altitude, **acceleration** | Median filtered - NOT velocity |
| IMU | 0x10 (16) | raw accelerometer, gyroscope | Deployment shock detection |

**Important**: The velocity data comes from FLIGHT_INFO records, not FILTERED_DATA_INFO. 
See `recorder.hpp` in [cats-embedded](https://github.com/catsystems/cats-embedded/blob/main/flight_computer/src/flash/recorder.hpp) for details.

## Accelerometer Deployment Signature

The parachute deployment is clearly visible in the raw accelerometer data as a sudden deceleration shock:

| Time (ms) | From Liftoff | Raw Accel X | Notes |
|-----------|--------------|-------------|-------|
| 289115 | +10.78s | -29698 | Pre-deployment baseline |
| 289125 | +10.79s | -27657 | Shock begins |
| 289135 | +10.79s | -24535 | Deceleration increasing |
| 289145 | +10.80s | -22717 | Peak shock (~7000 LSB change) |
| 289155 | +10.81s | -29504 | Recovery to descent |

The ~7000 LSB change in 30ms represents the sudden deceleration as the parachute opens and catches air. This provides independent confirmation of deployment timing separate from the barometric data.

**Note**: The actual motor delay (9.46s) was longer than intended (8s), possibly due to cold weather (-5°C) slowing the delay grain burn rate.

## Root Cause Analysis

### 1. Mass Discrepancy (Primary Cause)

Physics verification using burnout conditions:

- Max velocity: 46.2 m/s at 1.23s (during motor burn)
- Burnout altitude: ~40m
- Theoretical coast (no drag): $h = \frac{v^2}{2g} + h_0 = \frac{46.2^2}{2 \times 9.81} + 40 = 149\text{m}$
- To reach 208m would require burnout velocity of ~58-60 m/s

**Conclusion**: Rocket was significantly heavier than simulation assumed. Additional mass from:

- Two flight computers instead of one
- Additional LiPo batteries
- Other small items not accounted for

### 2. Temperature Compensation Gap

The CATS Vega MS5607 barometric sensor has two temperature-related behaviors:

| Component | Status | Notes |
|-----------|--------|-------|
| MS5607 sensor temperature compensation | ✅ Working | Internal calibration |
| Ambient air temperature in altitude formula | ❌ Hardcoded 15°C | `TEMPERATURE_0` constant |

**Flight conditions**: -5°C

The barometric altitude formula uses temperature to calculate air density. Using 15°C instead of -5°C causes approximately **+7.5% altitude overestimate** (~10m at this altitude).

**Temperature-corrected apogee**: ~132m true altitude

### 3. Venting Lag

The rocket body has no venting holes, causing pressure equalization lag during rapid altitude changes.

**Evidence from telemetry**:

- Altitude plateau at apogee: 141.4-141.6m sustained for ~1 second
- Pressure oscillated between 100680-100730 Pa for 1.5s around apogee
- Ascent velocities appear artificially low
- Only 4.6m apparent drag loss vs expected 15-25m for this rocket/velocity

The internal pressure cannot equalize fast enough, causing the barometer to "see" incorrect ambient pressure.

## Timing Analysis

| Parameter | Simulated | Actual | Difference |
|-----------|-----------|--------|------------|
| Time to apogee | 6.0s | 5.65s | -0.35s (6% faster) |
| Motor delay | 8.0s | 9.46s | +1.46s (18% slower) |

The simulation was accurate on flight timing — the altitude shortfall is primarily from mass discrepancy, not aerodynamics. The longer motor delay is likely due to cold weather affecting the delay grain burn rate.

## Recommendations

### Hardware

1. **Add venting holes** to rocket body for accurate barometric readings
2. **Verify actual flight mass** vs simulation input before future flights
3. **Account for cold weather** when setting motor delays (add margin)

### Firmware

Potential code improvement in CATS firmware — use MS5607 temperature reading in `calculate_height()` instead of hardcoded 15°C constant.

**Relevant code locations** (CATS firmware repository):

| File | Purpose |
|------|---------|
| `flight_computer/src/sensors/ms5607.hpp` | Barometer driver |
| `flight_computer/src/control/data_processing.cpp` | Height calculation |
| `flight_computer/src/config/control_config.hpp` | Config constants (`TEMPERATURE_0`) |
| `flight_computer/src/control/kalman_filter.cpp` | State estimation |

Firmware repository: [tonuonu/cats-embedded](https://github.com/tonuonu/cats-embedded)

## Summary

| Factor | Effect | Correctable |
|--------|--------|-------------|
| Mass discrepancy | Primary cause of altitude shortfall | Pre-flight weighing |
| Temperature compensation | +7.5% overestimate (~10m) | Firmware fix |
| Venting lag | Distorted pressure readings | Add vent holes |
| Cold weather delay | +18% longer burn time | Add safety margin |

Despite the altitude discrepancy, the flight was successful and achieved L1 certification.
