# CATS Vega Binary Log Format (`.cfl`)

This is the parsing reference for CATS Vega flight log files (`fl001.cfl`, `fl002.cfl`, ...). It is intentionally kept as a separate document — NOT inside any script docstring — so a future "small parser fix" cannot silently overwrite the format spec.

**Source of truth**: [catsystems/cats-embedded](https://github.com/catsystems/cats-embedded) — specifically:

- [`flight_computer/src/flash/recorder.hpp`](https://github.com/catsystems/cats-embedded/blob/main/flight_computer/src/flash/recorder.hpp) — `rec_entry_type_e` enum, payload structs
- [`flight_computer/src/util/types.hpp`](https://github.com/catsystems/cats-embedded/blob/main/flight_computer/src/util/types.hpp) — `imu_data_t`, `baro_data_t`, `flight_fsm_e`
- [`flight_computer/src/tasks/task_recorder.cpp`](https://github.com/catsystems/cats-embedded/blob/main/flight_computer/src/tasks/task_recorder.cpp) — write path

Firmware version of `fl001.cfl` and `fl002.cfl`: **3.0.2**.

---

## File Layout

```
[ Version string, null-terminated ]   e.g. "3.0.2\0"  → 6 bytes
[ Record 1 ]
[ Record 2 ]
...
[ Record N ]
```

Records are written to flash in 256-byte buffer blocks, but individual records can span block boundaries — the format on disk is a continuous byte stream with no inter-block padding.

## Record Layout

Every record:

```
+----------------+----------------+-------------------------+
| ts (uint32_t)  | rec_type_raw   | payload (variable size) |
| 4 bytes        | 4 bytes        |                         |
+----------------+----------------+-------------------------+
```

- `ts` — timestamp in milliseconds since CATS boot
- `rec_type_raw` — 32-bit value combining record type and sensor ID:
  - **Lower 4 bits** = sensor ID (`REC_ID_MASK = 0x0F`) — distinguishes multiple sensors of the same type (e.g. IMU 0, IMU 1)
  - **Upper bits** = record type from the enum below

To extract the pure record type: `rec_type = rec_type_raw & ~0x0F`.

## Record Types

> ⚠️ **The firmware comments are misleading.** `recorder.hpp` shows e.g. `IMU = 1U << 4U,  // 0x20`. The expression `1U << 4U` is `0x10` (= 16), NOT `0x20`. The comment is wrong; trust the expression. Every value below is `1U << N` for N starting at 4.

| Enum                  | Value   | Total bytes | Payload                                                                 |
|-----------------------|---------|-------------|-------------------------------------------------------------------------|
| `IMU`                 | `0x10`  = 16   | 20  | `imu_data_t`: 3 × `int16` acc + 3 × `int16` gyro = **12 B**             |
| `BARO`                | `0x20`  = 32   | 16  | `baro_data_t`: `int32` pressure (Pa) + `int32` temperature = **8 B**    |
| `FLIGHT_INFO`         | `0x40`  = 64   | 20  | 3 × `float32` height, **velocity**, acceleration (Kalman filter) = **12 B** |
| `ORIENTATION_INFO`    | `0x80`  = 128  | 16  | 4 × `int16` quaternion = **8 B**                                        |
| `FILTERED_DATA_INFO`  | `0x100` = 256  | 16  | 2 × `float32` altitude_AGL + **acceleration** (median filt.) = **8 B**  |
| `FLIGHT_STATE`        | `0x200` = 512  | 12  | 1 × `uint32` state (see FSM table) = **4 B**                            |
| `EVENT_INFO`          | `0x400` = 1024 | varies | `cats_event_e event` + `peripheral_act_t action` — pyro firings, beeper |
| `ERROR_INFO`          | `0x800` = 2048 | varies | `cats_error_e error`                                                    |
| `GNSS_INFO`           | `0x1000` = 4096 | varies | `gnss_position_t` (lat, lon, alt, etc.)                                |
| `VOLTAGE_INFO`        | `0x2000` = 8192 | varies | `uint16` battery voltage in mV                                          |

For the four "sporadic" types (EVENT, ERROR, GNSS, VOLTAGE) the exact payload size depends on subsidiary enum/struct sizes that vary across firmware versions. The parser in `generate_charts.py` knows the five periodic types + FLIGHT_STATE + EVENT_INFO; unknown types cause a clean stop with a diagnostic, never silent drift.

## Flight State Enum (`flight_fsm_e`)

Payload of a `FLIGHT_STATE` record:

| Value | State           | Meaning                                        |
|-------|-----------------|------------------------------------------------|
| 0     | `INVALID`       | Uninitialised                                  |
| 1     | `CALIBRATING`   | Sensor calibration                             |
| 2     | `READY`         | Armed, on the pad, waiting for liftoff        |
| 3     | `THRUSTING`     | Motor burning — **liftoff event**             |
| 4     | `COASTING`      | Motor burned out, ballistic ascent            |
| 5     | `DROGUE`        | Apogee reached, drogue charge fired           |
| 6     | `MAIN`          | Main charge fired (electronic deploy only)    |
| 7     | `TOUCHDOWN`     | Landed                                         |

**Use FLIGHT_STATE transitions, not velocity heuristics, for accurate event timestamps.**

## Hardware Notes

- **IMU**: STMicroelectronics LSM6DSO32 at ±32g range
  - Sensitivity: 0.976 mg/LSB ≈ 1024 LSB/g
  - 16-bit signed: ±32768 LSB maps to ±32g
  - ODR: 104 Hz
- **Barometer**: MS5607
  - Altitude formula in firmware uses **hardcoded 15 °C** (`TEMPERATURE_0`), not actual sensor temperature → causes apparent overestimate of ~7.5% at -5 °C ambient

## Common Pitfalls

These bugs have been observed and fixed before — re-read this if a future parse goes wrong:

1. **Wrong type constants.** Reading `1U << 4U` as `0x20` because the firmware comment says so. Always trust the expression, not the comment.
2. **Sliding 4 bytes on unknown record type.** Once the parser slides, alignment is lost forever; subsequent records appear as garbage. The correct behaviour is to **stop and report** an unknown type so the format gap can be fixed.
3. **`FILTERED_DATA_INFO` second field is acceleration, NOT velocity.** Velocity is in `FLIGHT_INFO`.
4. **Hardcoded `liftoff_ts`.** Each flight has a different boot-to-liftoff time. Use `FLIGHT_STATE = THRUSTING` transition, or fall back to first `flight_info.velocity > threshold`.

## Companion `st00N.txt` Stats File

The CATS Configurator writes a small `stXXX.txt` alongside each `flXXX.cfl`. It gives ground-truth max values straight from on-board calculation:

```
Flight #N Stats
  Height        Time Since Bootup: <ms>   Max. Height [m]: <m>
  Velocity      Time Since Bootup: <ms>   Max. Velocity [m/s]: <m/s>
  Acceleration  Time Since Bootup: <ms>   Max. Acceleration [m/s^2]: <m/s²>
  Calibration Values
    Height_0 [m ASL]: <ground level>
    IMU/Gyro calibration
  Liftoff Time: <HH:MM:SS UTC>
```

Always cross-check parser output against `stXXX.txt`. If they disagree, the parser is wrong.
