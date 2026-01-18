# Vent Hole Calculations

## Purpose

Vent holes (static ports) allow the altimeter to sense ambient air pressure during flight. Without proper venting, pressure differentials can cause:

- Inaccurate altitude readings
- Premature or delayed deployment
- Structural stress on airframe

## Vent Hole Formula

Minimum vent hole area:

$$A_{vent} = \frac{A_{tube} \cdot V_{descent}}{V_{sound}} \cdot N$$

Simplified rule of thumb:

$$A_{vent} \geq \frac{V_{bay}}{100}$$

Where:

- $A_{vent}$ = Total vent area (in²)
- $V_{bay}$ = Bay internal volume (in³)

## Practical Guidelines

### Number of Holes

- Minimum: 2 holes (180° apart)
- Recommended: 3-4 holes (evenly spaced)
- Prevents asymmetric pressure effects

### Hole Size

Common sizes for 4" diameter rockets:

| Hole Diameter | Area per Hole | 4 Holes Total |
|---------------|---------------|---------------|
| 1/8" (3mm) | 0.012 in² | 0.049 in² |
| 3/16" (5mm) | 0.028 in² | 0.110 in² |
| 1/4" (6mm) | 0.049 in² | 0.196 in² |

### Placement

!!! tip "Hole Location"
    - Place in e-bay coupler section
    - Position near altimeter sensor
    - Avoid direct line to ejection charge
    - Not too close to tube joints

## Peregrine Vent Holes

*To be determined during build*

| Parameter | Value |
|-----------|-------|
| E-bay length | TBD inches |
| Number of holes | TBD |
| Hole diameter | TBD |
| Total vent area | TBD in² |

## Additional Considerations

### Breather Holes vs Static Ports

- **Static Ports**: For altimeter pressure sensing
- **Breather Holes**: For recovery bay equalization

Both may be needed in different locations.

### Switch Hole

If using external arming switch:

- Switch mounting hole also provides venting
- Account for this area in calculations
- Use switch band for clean installation

## Testing

Verify altimeter function after drilling:

1. Power on altimeter
2. Seal one end of e-bay
3. Gently blow into/suck on other end
4. Altimeter should show altitude change
5. Altitude should return to zero when released
