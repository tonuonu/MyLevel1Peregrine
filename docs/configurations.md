# Rocket Configurations

## Overview

The Apogee Peregrine is designed for dual-deployment but can be flown in simplified configuration. This project uses two configurations:

| Level | Configuration | Recovery | Rocket Length |
|-------|--------------|----------|---------------|
| **L1** | Minimal | Motor ejection | 126 cm |
| **L2** | Full | Electronic dual-deploy | 175 cm |

## L1 Certification Configuration

**Goal:** Simple, reliable certification flight

### Hardware
- Shortened airframe (no e-bay section)
- Single 48" main parachute
- Motor ejection delay (no electronics)
- Nose ballast for stability (~300-600g epoxy)

### Recovery Sequence
1. Motor burns out
2. Delay charge burns (selected delay time)
3. Ejection charge fires
4. Nose cone separates, main chute deploys
5. Rocket descends under single parachute

### Why This Configuration
- Fewer failure modes
- No electronics to malfunction
- Traditional L1 approach
- Proves basic HPR competency

### Stability Challenge
Removing e-bay section moves CP forward → rocket becomes unstable without nose ballast. See [OpenRocket Analysis](../simulations/openrocket.md).

## L2 Certification Configuration

**Goal:** Demonstrate dual-deployment competency

### Hardware
- Full airframe with electronics bay
- CATS Vega flight computer
- 18" drogue parachute (upper section)
- 48" main parachute (lower section)
- Redundant deployment charges

### Recovery Sequence
1. Motor burns out
2. Rocket coasts to apogee
3. **Apogee:** Flight computer fires drogue charge
4. Drogue deploys, fast descent (~15-20 m/s)
5. **~300m AGL:** Flight computer fires main charge
6. Main chute deploys, slow descent (~5 m/s)
7. Rocket lands close to pad

### Why Dual Deployment
- Smaller landing footprint
- Reduced wind drift
- Required skill for L2 certification
- What Peregrine is designed for

## Component Summary

| Component | L1 Config | L2 Config |
|-----------|-----------|-----------|
| Body tube | Shortened | Full length |
| Electronics bay | ❌ Removed | ✓ Installed |
| CATS Vega | ❌ Not used | ✓ Controls deployment |
| Drogue chute | ❌ None | ✓ 18" at apogee |
| Main chute | ✓ 48" | ✓ 48" at 300m |
| Deployment | Motor delay | Electronic |
| Nose ballast | ✓ Required | Optional |

## Upgrade Path

After L1 certification:

1. Re-install electronics bay section
2. Install CATS Vega on e-bay sled
3. Wire pyro channels to deployment charges
4. Add drogue parachute to upper section
5. Configure flight computer events
6. Test deployment on ground
7. Fly L2 certification

## Flight Parameters

| Parameter | L1 Config | L2 Config |
|-----------|-----------|-----------|
| Rocket mass (no motor) | ~2100g* | ~1900g |
| Length | 126 cm | 175 cm |
| Stability | ~1.0 cal* | 3.69 cal |
| Motor | H128W | H or I class |
| Expected altitude | ~235m | ~400-600m |

*With nose ballast

## References

- [L1 Configuration Decision](../decisions/l1-configuration.md)
- [Flight Computer Decision](../decisions/flight-computer.md)
- [OpenRocket Stability Analysis](../simulations/openrocket.md)
- [Weight Budget](../calculations/l1-weight-budget.md)
