# Rail Exit Velocity

## Why It Matters

The rocket must achieve sufficient velocity before leaving the launch rail for the fins to provide aerodynamic stability. Below this velocity, the rocket may:

- Weathercock into wind
- Fly unstable trajectory
- Tip over on the pad

## Minimum Rail Exit Velocity

!!! success "Rule of Thumb"
    Minimum rail exit velocity: **50 ft/s (15 m/s)**
    
    Recommended: **60-80 ft/s** for margin of safety

## Physics

Rail exit velocity depends on:

$$V_{exit} = \sqrt{V_0^2 + 2 \cdot a_{avg} \cdot L_{rail}}$$

Where:

- $V_0$ = Initial velocity (0 for standing start)
- $a_{avg}$ = Average acceleration during rail travel
- $L_{rail}$ = Effective rail length

Simplified:

$$V_{exit} = \sqrt{\frac{2 \cdot F_{avg} \cdot L_{rail}}{m}}$$

Where:

- $F_{avg}$ = Average thrust force (N)
- $m$ = Liftoff mass (kg)

## Minimum Rail Length

Rearranging for rail length:

$$L_{rail} = \frac{m \cdot V_{exit}^2}{2 \cdot F_{avg}}$$

## Peregrine Calculations

### Estimated Values

| Parameter | Value |
|-----------|-------|
| Liftoff Mass | ~6 lbs (~2.7 kg) with H motor |
| Target Exit Velocity | 60 ft/s (18 m/s) |

### Example: AeroTech H180W

| Parameter | Value |
|-----------|-------|
| Average Thrust | 180 N (40 lbf) |
| Liftoff Mass | ~2.7 kg |
| Min Rail Length | Calculate below |

$$L_{rail} = \frac{2.7 \cdot 18^2}{2 \cdot 180} = \frac{874.8}{360} = 2.4 m \approx 8 ft$$

!!! note "Rail Length"
    An 8-foot (2.4m) rail should provide adequate exit velocity for the Peregrine on H motors.
    
    Standard high-power rail lengths:
    - 6 ft (1.8m) - marginal for heavy rockets
    - 8 ft (2.4m) - good for most HPR
    - 10 ft (3m) - excellent margin

## Simulation Verification

OpenRocket/RockSim calculate rail exit velocity:

*Insert simulation results here*

| Motor | Rail Length | Exit Velocity | Status |
|-------|-------------|---------------|--------|
| H180W | 6 ft | TBD | TBD |
| H180W | 8 ft | TBD | TBD |
| H100W | 8 ft | TBD | TBD |

## Wind Considerations

In windy conditions:

- Higher exit velocity needed
- Consider longer rail
- Or postpone launch if marginal

Rule: Add 10 ft/s to minimum for each 10 mph wind.
