# Rocket Configurations

## Overview

The Apogee Peregrine is designed for dual-deployment but can be flown in simplified configuration.

!!! success "L1 & L2 Certification Complete"
    **L2 flight (22 Feb 2026):** Full-length configuration (175cm), dual deploy electronic recovery (CATS Vega). See [Certification](certification/index.md) for details.
    **L1 flight (24 Jan 2026):** Full-length configuration (175cm), motor ejection recovery.

### Configurations Flown

| Level | Configuration | Recovery | Rocket Length |
|-------|--------------|----------|---------------|
| **L1** | Full length, no e-bay deployment | Motor ejection | 175 cm |
| **L2** | Full length, dual deploy | Electronic dual-deploy | 175 cm |

## L1 Configuration (as flown)

**Flight:** 24 January 2026

### Hardware
- Full-length airframe with e-bay (carried CATS Vega for logging only)
- Single 48" main parachute
- Motor ejection delay
- Nose ballast for stability (~300-600g epoxy)

### Recovery Sequence
1. Motor burns out
2. Delay charge burns (selected delay time)
3. Ejection charge fires
4. Nose cone separates, main chute deploys
5. Rocket descends under single parachute

### Why This Configuration
- Fewer failure modes for first certification
- Swedish safety rules required ejection charge testing — motor ejection as fallback
- Traditional L1 approach
- Proves basic HPR competency

### Stability Challenge
Removing e-bay deployment function moves risk profile. See [OpenRocket Analysis](../simulations/openrocket.md).

## L2 Configuration (as flown)

**Flight:** 22 February 2026

### Hardware
- Full airframe with electronics bay
- CATS Vega flight computer controlling deployment
- 18" drogue parachute (upper section)
- 48" main parachute (lower section)

### Recovery Sequence
1. Motor burns out
2. Rocket coasts to apogee
3. **Apogee:** Flight computer fires drogue charge
4. Drogue deploys, fast descent (~15-20 m/s)
5. **Lower altitude:** Flight computer fires main charge
6. Main chute deploys, slow descent (~5 m/s)
7. Rocket lands close to pad

### Why Dual Deployment
- Smaller landing footprint
- Reduced wind drift
- What Peregrine is designed for

## Component Summary

| Component | L1 Config | L2 Config |
|-----------|-----------|-----------|
| Body tube | Full length | Full length |
| Electronics bay | ✓ Installed (logging only) | ✓ Controls deployment |
| CATS Vega | Data logging only | ✓ Controls deployment |
| Drogue chute | ❌ None | ✓ 18" at apogee |
| Main chute | ✓ 48" | ✓ 48" at lower altitude |
| Deployment | Motor delay | Electronic |
| Nose ballast | ✓ Included | ✓ Included |

## Flight Parameters

| Parameter | L1 (actual) | L2 (actual) |
|-----------|-------------|-------------|
| Rocket mass (no motor) | ~2350g (liftoff) | ~3100g (liftoff) |
| Length | 175 cm | 175 cm |
| Motor | H128W-14A | J350 |
| Apogee | 141.6 m | ~1000 m (estimated) |

## References

- [L1 Configuration Decision](../decisions/l1-configuration.md)
- [Flight Computer Decision](../decisions/flight-computer.md)
- [OpenRocket Stability Analysis](../simulations/openrocket.md)
- [Weight Budget](../calculations/l1-weight-budget.md)
