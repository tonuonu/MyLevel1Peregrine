# Flight Log

## Flight Records

---

## Flight #1 - 2026-01-24 (L1 Certification)

### Conditions

| Parameter | Value |
|-----------|-------|
| Location | Enköping, Sweden |
| Weather | Winter, snow on ground, -5°C |
| Event | SMRK Launch Day |

### Configuration

| Parameter | Value |
|-----------|-------|
| Motor | AeroTech H128W-14A |
| Liftoff weight | 2350 g |
| CG location | 115 cm from nose tip |
| CP location | 130 cm from nose tip |
| Stability | ~1.5 calibers |
| Recovery mode | Single deploy (motor ejection) |
| Delay | ~8s (14s factory - 8s drilled + 2s disk) |

### Flight Data

| Parameter | Predicted | Actual (CATS) |
|-----------|-----------|---------------|
| Apogee | 208 m | 141.58 m |
| Burnout velocity | — | 45.69 m/s |
| Burnout altitude | — | 39.84 m |
| Burn time | 1.4 s | 1.33 s |

Altitude recorded by CATS Vega flight computer (file: fl001.cfl).

### Results

- [x] Successful launch
- [x] Stable flight
- [x] Recovery deployed
- [x] Recovered intact
- [x] **L1 CERTIFICATION ACHIEVED**

### Analysis Summary

The 32% altitude shortfall (208m predicted → 141.58m actual) has three identified causes:

1. **Mass discrepancy (primary)**: Burnout velocity of 45.69 m/s at 39.84m gives theoretical max of ~146m (no drag). Reaching 208m would require ~58-60 m/s burnout velocity, indicating rocket was heavier than simulated.

2. **Temperature compensation gap**: MS5607 barometer uses hardcoded 15°C in altitude formula, but flight was at -5°C. This causes +7.5% altitude overestimate (~10m). True apogee approximately 132m.

3. **Venting lag**: No venting holes in rocket body. Evidence: altitude plateau at apogee (141.4-141.6m for ~1 second), pressure oscillation 100680-100730 Pa for 1.5s. Ascent velocities appear artificially low with only 4.6m apparent drag loss vs expected 15-25m.

See [Flight #1 Analysis](flight1-analysis.md) for detailed telemetry and recommendations.

### Certification

| Field | Value |
|-------|-------|
| Certification | Tripoli L1 |
| Certifying Authority | Rolf Örell (TRA# 3728) |
| Flyer | Tõnu Samuel (TRA# 38105) |

### Photos

Launch photo and recovery photo with Liza holding "SIPSIK" rocket - see certification documentation.

---

## Future Flights

### Planned: L2 Certification Flight

- L2 written exam passed (27 January 2026, Certificate #2343)
- Motor class: J, K, or L required
- Location: Sweden (motor procurement constraint)
