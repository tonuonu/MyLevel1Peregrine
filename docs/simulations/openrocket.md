# OpenRocket Simulations

## Design Files

### Source

RockSim file downloaded from [Apogee Product Page](https://www.apogeerockets.com/Rocket-Kits/Skill-Level-3-Model-Rocket-Kits/Peregrine#rocksim):

- [Peregrine.rkt.zip](https://www.apogeerockets.com/downloads/rocksim_files/Peregrine.rkt.zip)

### Converting RockSim to OpenRocket

OpenRocket (free, open-source) can import RockSim .rkt files directly:

1. Download and unzip RockSim file from Apogee
2. Open OpenRocket
3. File → Open → Select .rkt file
4. OpenRocket imports automatically
5. Save as .ork file

!!! note "Fin Import"
    The curved Peregrine fins import correctly via this method.
    Manual recreation of the spline fin shape is difficult.

## Full L2 Configuration

Imported directly from Apogee's RockSim file.

![OpenRocket L2 configuration](../photos/Screenshot%202026-01-20%20at%2013.49.56.png)

| Parameter | OpenRocket Value |
|-----------|------------------|
| Length | 175 cm |
| Max Diameter | 10.2 cm |
| Mass (no motor) | 1096 g |
| CG | 92.7 cm |
| CP | 130 cm |
| **Stability** | **3.69 cal** ✓ |

## L1 Minimal Configuration

Modified from L2 config by removing:

- Electronics bay (E-bay coupler, bulkheads, sled, switch band)
- Drogue parachute and associated hardware
- Upper body tube section

![OpenRocket L1 configuration](../photos/Screenshot%202026-01-20%20at%2013.58.26.png)

| Parameter | OpenRocket Value | Issue |
|-----------|------------------|-------|
| Length | 126 cm | |
| Max Diameter | 10.2 cm | |
| Mass (no motor) | 1096 g | Model needs mass override |
| CG | 92.73 cm | |
| CP | 90.8 cm | |
| **Stability** | **-0.191 cal** | ⚠️ **UNSTABLE** |

!!! danger "L1 Configuration is Unstable"
    The shortened L1 rocket has CP *forward* of CG, resulting in negative stability.
    
    **Root cause:** Removing the e-bay section moves CP forward significantly (130cm → 90.8cm) while CG remains similar.
    
    **Solution:** Add nose ballast to move CG forward of CP.

## Mass Discrepancy

| Source | Mass |
|--------|------|
| OpenRocket model | 1096 g |
| Actual rocket (weighed) | 1460 g |
| **Difference** | **364 g** |

The 364g difference is accounted for by:

- Epoxy fillets and bonding (~200-250g typical for 4" HPR)
- Paint and primer (~50-100g)
- Additional hardware, quick links
- Nomex protector

!!! important "Mass Override Required"
    The OpenRocket model significantly underestimates actual built mass.
    
    After building, update the model:
    
    1. Click on top-level "Stage" in component tree
    2. Go to "Override" tab
    3. Check "Override mass"
    4. Enter measured mass: **1460 g**
    5. Re-run stability calculations

## Stability Analysis with Ballast

With actual mass (1460g) concentrated more forward (due to epoxy in nose, etc.), the CG will shift forward. Additional nose ballast will be required.

**Target:** Stability margin ≥ 1.5 calibers (15.3 cm for 10.2 cm diameter)

See [L1 Weight Budget](../calculations/l1-weight-budget.md) for ballast calculations.

## Simulation Parameters

### Launch Site Conditions

For Långtora, Sweden (SMRK launch site):

| Parameter | Value |
|-----------|-------|
| Location | Långtora, Sweden |
| Altitude | ~25 m ASL |
| Temperature | -5 to +5 °C (January) |
| Pressure | 1013 hPa (std) |
| Wind | Variable |

## Flight Predictions

### Motor: AeroTech H128W

*To be simulated with corrected mass*

| Parameter | Value |
|-----------|-------|
| Max Altitude | TBD |
| Max Velocity | TBD |
| Time to Apogee | TBD |
| Optimal Delay | TBD |
| Rail Exit Velocity | TBD |
| Stability (off rod) | TBD |

## Action Items

- [ ] Update OpenRocket model with actual mass (1460g)
- [ ] Add nose ballast component to achieve positive stability
- [ ] Calculate required ballast for 1.5+ caliber stability
- [ ] Run flight simulations with H128W motor
- [ ] Determine optimal delay time

## OpenRocket Files

| File | Description |
|------|-------------|
| `openrocket/Peregrine.ork` | Full L2 config (from RockSim import) |
| `openrocket/PeregrineL1.ork` | L1 minimal config (needs work) |