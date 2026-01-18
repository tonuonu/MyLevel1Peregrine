# OpenRocket Simulations

## Design File

The Peregrine design file is available from Apogee as a RockSim (.rkt) file.

### Converting RockSim to OpenRocket

1. Download RockSim file from Apogee product page
2. Open OpenRocket
3. File → Open → Select .rkt file
4. OpenRocket imports automatically
5. Save as .ork file

!!! note "Fin Import"
    The curved Peregrine fins import correctly via this method.
    Manual recreation of the spline fin shape is difficult.

## Simulation Parameters

### Launch Site Conditions

*Configure for your launch site*

| Parameter | Value |
|-----------|-------|
| Location | TBD |
| Altitude | TBD m ASL |
| Temperature | TBD °C |
| Pressure | 1013 hPa (std) |
| Wind | TBD m/s |

### Mass Override

!!! important "Accurate Mass"
    After building, weigh rocket and update:
    
    1. Click on Stage at top
    2. Go to Override tab
    3. Enter measured mass and CG
    4. Re-run simulations

## Flight Predictions

### Motor: AeroTech H180W

*Simulation results to be added*

| Parameter | Value |
|-----------|-------|
| Max Altitude | TBD ft |
| Max Velocity | TBD ft/s |
| Max Mach | TBD |
| Time to Apogee | TBD s |
| Optimal Delay | TBD s |
| Rail Exit Velocity | TBD ft/s |
| Stability (off rod) | TBD cal |

### Motor: AeroTech H100W

*Simulation results to be added*

### Motor: AeroTech H210 Redline

*Simulation results to be added*

## Graphs

*Insert simulation graphs here*

- Altitude vs Time
- Velocity vs Time
- Stability vs Time
- Flight trajectory

## OpenRocket File

*Link to .ork file in repository*

```
openrocket/peregrine.ork
```
