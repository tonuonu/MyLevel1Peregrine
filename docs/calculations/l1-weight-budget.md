# L1 Weight Budget and Ballast Calculations

## Motor Data: AeroTech H128W

### Reload Specifications (from ThrustCurve)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Designation | H128W | White Lightning propellant |
| Motor Type | Reload | Requires RMS-29/180 casing |
| Diameter | 29 mm | Needs 29→38mm adapter |
| Length | 194 mm | |
| **Total Weight** | **206 g** | Complete loaded motor |
| Propellant Weight | 94 g | Burns during flight |
| Average Thrust | 128.0 N | |
| Max Thrust | 168.7 N | |
| Total Impulse | 172.9 N·s | 95% H-class |
| Burn Time | 1.3 s | |
| Delay | 14 s adjustable | Drill to desired delay |

### Weight Breakdown

| Component | Weight | Notes |
|-----------|--------|-------|
| Propellant grains | 94 g | Consumed during burn |
| Nozzle, liner, delay, seals | ~112 g | Reload kit non-propellant |
| **Reload kit total** | **206 g** | As packaged |

### RMS-29/180 Hardware

| Component | Approx Weight | Notes |
|-----------|---------------|-------|
| Aluminum casing (tube) | ~60 g | 29mm × ~180mm |
| Forward closure | ~25 g | |
| Aft closure | ~25 g | |
| **Hardware set total** | **~110 g** | Reusable |

!!! note "Weight Clarification"
    ThrustCurve's "Total Weight: 206g" is the **complete assembled motor** (casing + reload). This is what goes in the rocket.
    
    Post-burn motor weight: 206g - 94g = **112g**

## L1 Configuration Mass Budget

### Measured Weights

| Item | Mass | Method |
|------|------|--------|
| Rocket ready to fly (no motor) | 1460 g | Kitchen scale, includes: |
| | | - Airframe (shortened L1 config) |
| | | - Nose cone |
| | | - Fins |
| | | - Motor mount |
| | | - 48" main parachute (packed) |
| | | - Shock cord |
| | | - Nomex protector |
| | | - Rail buttons |
| | | - 29→38mm motor adapter |

### Motor Weight

| Item | Mass |
|------|------|
| H128W complete (pre-burn) | 206 g |
| H128W post-burn (casing + hardware) | 112 g |

### Pre-Flight Weight (No Ballast)

$$W_{rocket} + W_{motor} = 1460g + 206g = 1666g = \mathbf{1.67\ kg}$$

## Tripoli 5:1 Thrust-to-Weight Rule

### Requirement

Tripoli RSO (Range Safety Officer) requires:

$$\frac{\text{Average Thrust}}{\text{Liftoff Weight}} \geq 5:1$$

This ensures adequate velocity off the launch rail for stable flight.

### Maximum Allowed Weight

$$W_{max} = \frac{F_{avg}}{5} = \frac{128\ N}{5} = 25.6\ N = \mathbf{2.61\ kg}$$

### Current Status

| Parameter | Value | Status |
|-----------|-------|--------|
| Current liftoff weight | 1.67 kg | ✓ Under limit |
| Maximum allowed | 2.61 kg | |
| Available margin | 0.94 kg | Room for ballast |

## Why Add Ballast?

### Flight Altitude Concern

Lighter rocket = higher altitude = longer recovery walk.

For a **certification flight**:

- Want predictable, moderate altitude
- Want to **see** the rocket throughout flight
- Want quick recovery (less walking)
- Want to stay well within field boundaries

### Target Weight

To fly conservatively low:

$$W_{target} \approx 2.5\ kg$$

This gives:

- Thrust-to-weight ratio: $\frac{128}{2.5 \times 9.81} = 5.2:1$ ✓
- Lower apogee than minimum weight config
- Still meets 5:1 requirement

## Ballast Calculation

### Required Ballast Mass

$$W_{ballast} = W_{target} - W_{rocket} - W_{motor}$$
$$W_{ballast} = 2500g - 1460g - 206g = \mathbf{834g}$$

### Ballast Options

| Material | Density | Volume for 834g |
|----------|---------|-----------------|
| Lead shot | 11.3 g/cm³ | 74 cm³ |
| Steel shot | 7.8 g/cm³ | 107 cm³ |
| Sand | 1.6 g/cm³ | 521 cm³ |
| Steel bolts/nuts | 7.8 g/cm³ | 107 cm³ |

### Ballast Placement

!!! warning "CG/CP Impact"
    Ballast location affects Center of Gravity!
    
    - Nose ballast: moves CG forward → more stable
    - Tail ballast: moves CG aft → less stable

**Recommendation:** Place ballast in or near nose cone to maintain/increase stability margin.

See [Stability Calculations](stability.md) for CG/CP analysis with ballast.

## Weight Summary Table

| Configuration | Pre-Flight | Post-Burn |
|--------------|------------|-----------|
| Rocket (no motor, no ballast) | 1460 g | 1460 g |
| + Motor (H128W) | +206 g | +112 g |
| **Minimum config** | **1666 g** | **1572 g** |
| + Ballast (target) | +834 g | +834 g |
| **With ballast** | **2500 g** | **2406 g** |

## Action Items

- [ ] Verify rocket weight measurement (re-weigh)
- [ ] Confirm motor weight when received
- [ ] Calculate CG with ballast in nose cone
- [ ] Verify CP in OpenRocket for L1 config
- [ ] Confirm stability margin ≥ 1.5 calibers with ballast
- [ ] Source appropriate ballast material

## References

- [ThrustCurve H128W Data](https://www.thrustcurve.org/motors/AeroTech/H128W/)
- [Tripoli Safety Code](https://www.tripoli.org/content.aspx?page_id=22&club_id=795696&module_id=462822)
- [L1 Configuration Decision](../decisions/l1-configuration.md)
