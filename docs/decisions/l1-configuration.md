# L1 Minimal Configuration

## Decision

Fly the certification flight in **minimal L1 configuration** rather than full dual-deployment setup.

## Configuration Differences

### Full L2 Configuration (IMG_6434)

- Main body tube
- Electronics bay (e-bay) with altimeter
- Coupler tube between e-bay and nose cone  
- Nose cone
- 18" drogue parachute (upper section)
- 48" main parachute (lower section)
- Dual deployment (altimeter-controlled)

### Minimal L1 Configuration (IMG_7824)

- Main body tube (shortened - no e-bay section)
- Nose cone attached directly to body tube
- 48" main parachute only
- Motor ejection charge deployment (no electronics)

## Removed Components

| Component | Weight Estimate | Reason |
|-----------|----------------|--------|
| Electronics bay tube | ~100g | Not needed for motor ejection |
| E-bay bulkheads, sled, hardware | ~150g | No altimeter deployment |
| 18" drogue parachute | ~30g | Single deployment only |
| Coupler tube (e-bay to nose) | ~80g | Shorter rocket |
| Altimeter | ~50g | Motor ejection is sufficient |

**Total removed:** ~400g estimated

## Rationale

### Simplicity

L1 certification demonstrates basic HPR competency. Adding dual-deployment electronics introduces failure modes:

- Altimeter malfunction
- Wiring issues  
- Battery problems
- Charge firing timing
- Multiple separation events

For certification, minimize variables.

### Reliability

Motor ejection is proven technology:

- No electronics to fail
- No batteries to die
- No wiring to disconnect
- Single separation event

### Regulatory

No pyrotechnic electronics to explain to Swedish authorities. Simpler = less questions.

### Reversibility

After L1 certification:

- Re-install electronics bay
- Add drogue parachute
- Full dual-deployment for L2

All removed components are stored safely.

## Weight Impact

| Configuration | Approximate Mass |
|--------------|------------------|
| Full L2 config (empty) | ~1.9 kg |
| L1 minimal (empty) | ~1.46 kg |
| L1 with motor (H128W) | ~1.67 kg |

The lighter rocket with H128W will fly higher than needed for a conservative certification flight. See [L1 Weight Budget](../calculations/l1-weight-budget.md) for ballast calculations.

## Photos

| Configuration | Photo |
|--------------|-------|
| Full L2 (painted) | ![L2 configuration](../photos/IMG_6434.JPG) |
| L1 minimal (window view) | ![L1 configuration](../photos/IMG_7824.JPG) |

## References

- [Stability Calculations](../calculations/stability.md) - CG/CP for L1 config
- [L1 Weight Budget](../calculations/l1-weight-budget.md) - Mass budget and ballast
- [Motor Selection](../simulations/motors.md) - H128W specifications
