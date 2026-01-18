# Ejection Charge Calculations

## Black Powder Charge Formula

The standard formula for calculating black powder ejection charge:

$$m_{BP} = \frac{\Delta P \cdot V \cdot C}{R \cdot T}$$

Simplified practical formula:

$$m_{BP} (grams) = \frac{D^2 \cdot L}{2270}$$

Where:

- $D$ = Tube inside diameter (inches)
- $L$ = Bay length (inches)

!!! note "Safety Factor"
    Add 10-20% to calculated charge for reliable deployment.

## Peregrine Bay Calculations

### Known Values

| Parameter | Value |
|-----------|-------|
| Body Tube ID | ~3.9" (actual ID of 98mm tube) |
| Pressure | 15 psi (typical) |

### Drogue Bay (Forward)

*To be measured during build*

| Parameter | Value |
|-----------|-------|
| Length | TBD inches |
| Volume | TBD in³ |
| BP Charge | TBD grams |

### Main Bay (Aft)

*To be measured during build*

| Parameter | Value |
|-----------|-------|
| Length | TBD inches |
| Volume | TBD in³ |
| BP Charge | TBD grams |

## RockSim Calculation

RockSim includes a built-in ejection charge calculator:

1. Open Peregrine design file
2. Go to Simulation menu
3. Select "Ejection Charge Calculator"
4. Enter bay dimensions
5. Get recommended charge size

## Ground Test Procedure

!!! warning "Always Ground Test"
    Never fly without ground testing ejection charges!

### Test Procedure

1. Assemble rocket without motor
2. Load recovery gear as for flight
3. Install e-match with calculated charge
4. Secure rocket horizontally
5. Clear area and fire charge
6. Verify clean separation and chute deployment

### Test Criteria

- [ ] Clean separation
- [ ] All sections stay connected via shock cord
- [ ] Parachute(s) fully deploy
- [ ] No damage to components
- [ ] Adequate force (increase charge if weak)

## Alternative: CO2 Ejection

Apogee offers a CO2 ejection system:

- No black powder required
- Peregrine Starter Kit includes:
  - 4x 8-gram cartridges
  - 4x 12-gram cartridges
  - Hardware for 2 systems

## Charge Quantities Summary

*To be filled after bay measurements*

| Bay | Primary | Backup (+15%) |
|-----|---------|---------------|
| Drogue | TBD g | TBD g |
| Main | TBD g | TBD g |
