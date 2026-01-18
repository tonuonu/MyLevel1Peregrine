# Stability Calculations

## Stability Criteria

For a stable rocket flight:

$$\text{Stability Margin} = \frac{X_{CP} - X_{CG}}{d} \geq 1.0$$

Where:

- $X_{CP}$ = Center of Pressure location (from nose tip)
- $X_{CG}$ = Center of Gravity location (from nose tip)
- $d$ = Body tube diameter (caliber)

!!! success "Target"
    CG should be **1 to 2 calibers** ahead of CP
    
    - Less than 1 caliber: marginally stable
    - More than 2 calibers: will weathercock

## Peregrine Stability

With 4" diameter body:

- 1 caliber = 4 inches
- Target: CG 4-8" ahead of CP

| Configuration | CG | CP | Margin | Status |
|--------------|-----|-----|--------|--------|
| *To be filled from OpenRocket* | | | | |

## Measuring CG

### Method: Balance Point

1. Fully load rocket (motor, recovery, electronics)
2. Balance on finger or rod
3. Mark balance point
4. Measure from nose tip

### Weight Considerations

| Item | Approx Weight | Notes |
|------|---------------|-------|
| Airframe (empty) | ~5 lbs | As built |
| Altimeter | 0.5-2 oz | Varies by model |
| Motor (H180) | ~8 oz | Loaded |
| Recovery gear | ~4 oz | Packed |

## CP Calculation Methods

### Barrowman Equations

Classic analytical method for CP location. Implemented in:

- RockSim
- OpenRocket

### Cardboard Cutout Method

Simple physical approximation:

1. Draw rocket profile on cardboard
2. Cut out profile
3. Balance cutout
4. Balance point ≈ CP

!!! note "Conservative Method"
    Cardboard cutout gives a conservative estimate.
    Actual CP is usually further aft.

## Dynamic Stability

Beyond static stability, dynamic factors include:

- Launch velocity (affects weathercocking)
- Wind conditions
- Fin size and shape
- Mass distribution

RockSim/OpenRocket simulate these factors.

## Simulation Results

*Insert OpenRocket stability analysis here*

See [OpenRocket Results](../simulations/openrocket.md) for full simulation data.
