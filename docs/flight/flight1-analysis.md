# Flight #1 Analysis

Detailed analysis of CATS Vega telemetry data from the L1 certification flight.

## Problem Statement

Simulation predicted 208m apogee, flight computer logged 141.58m — a 32% shortfall.

## Flight Event Timeline

Data from CATS Vega log file `fl001.cfl`:

| Event | Time (ms) | Altitude (m) | Velocity (m/s) |
|-------|-----------|--------------|----------------|
| Liftoff | 278340 | 0 | 0 |
| Burnout | 279670 | 39.84 | 45.69 |
| Apogee | 284020 | 141.58 | 0 |
| Drogue | 284320 | 141.41 | — |
| Main | 284630 | 141.43 | — |

**Burn time**: 1.33s (matches H128W specification of ~1.4s)

## Root Cause Analysis

### 1. Mass Discrepancy (Primary Cause)

Physics verification using burnout conditions:

- Burnout velocity: 45.69 m/s at 39.84m altitude
- Theoretical maximum (no drag): $h = \frac{v^2}{2g} + h_0 = \frac{45.69^2}{2 \times 9.81} + 39.84 = 146\text{m}$
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

## Recommendations

### Hardware

1. **Add venting holes** to rocket body for accurate barometric readings
2. **Verify actual flight mass** vs simulation input before future flights

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

Despite the altitude discrepancy, the flight was successful and achieved L1 certification.
