# L3 Certification Planning

## Status: DESIGN PHASE

L1 and L2 were verification that fundamentals were understood correctly — kit-based flights with known parameters. L3 is a different challenge: designing and building a rocket from scratch.

## Requirements

Per Tripoli L3 certification:

- [x] Current L2 certification
- [ ] Written project report reviewed by 2 TAP members before flight
- [ ] Scratch-built rocket (no kits)
- [ ] Successfully fly and recover using M, N, or O motor
- [ ] Witnessed and approved by 2 TAP members

### TAP Committee

| Role | Name | Status |
|------|------|--------|
| TAP member #1 | Rolf Örell (TRA# 3728) | Confirmed |
| TAP member #2 | TBD | Rolf to introduce |

## Motor Selection

### Sizing Constraints

M-class motors are the minimum for L3. These are not available below 75mm diameter. 98mm is also an option but drives a larger rocket. Since high power is not the goal (just meeting requirements), 75mm is preferred to keep the rocket as small as practical.

### Motor Type: Single-Use

Single-use (disposable casing) rather than reloadable, for several reasons:

- No need to purchase expensive reloadable casing hardware
- No borrowed equipment at risk in a CATO
- Simpler preparation on launch day
- Acceptable cost for a one-off certification flight

### Candidate Motors

| Motor | Diameter | Total Impulse | Notes |
|-------|----------|--------------|-------|
| TBD | 75mm | M-class (5120-10240 N-s) | Research needed |

98mm single-use motors are a fallback if 75mm options are insufficient.

## Airframe Design

### Minimum Dimensions

The 75mm motor mount sets the minimum body tube inner diameter. With typical wall thickness, this means a minimum airframe OD of approximately 80-85mm, though a larger airframe (e.g. 100-120mm) may be needed for stability, recovery hardware, and electronics bay space.

### Construction Approach

Scratch-built — all structural components designed and fabricated, not from a kit.

## Fin Can Design

### Design Tool: OpenSCAD

OpenSCAD chosen for fin can design because:

- C++-like syntax (familiar programming paradigm)
- Parametric design — dimensions driven by variables
- Direct export to 3MF for 3D printing
- Proven workflow from PeregrineFin and PeregrineFinCan75 projects

### 3D Printing: Bambu P1S

| Constraint | Value |
|-----------|-------|
| Printer | Bambu P1S (standard, not Plus) |
| Max print height | 250mm (with AMS) |
| Max print area | 256 × 256 mm |

The 250mm height limit means the fin can body must be split into two or more rings that are bonded together. Fins are printed separately and bonded to the assembled can.

### Multi-Part Assembly Strategy

For a 75mm motor fin can:

1. **Fin can body**: Split into 2+ cylindrical rings (each ≤250mm tall), bonded together
2. **Fins**: Printed individually, bonded to assembled can
3. **Joints**: Designed with alignment features (pins, keys, or overlapping sections)

This avoids printing any single part that exceeds the printer's build volume.

### Material: Spectrum PC CF

Polycarbonate with carbon fiber fill, chosen after evaluating multiple materials:

| Property | PC CF Advantage |
|----------|----------------|
| Temperature resistance | High — survives motor heat proximity |
| Toughness | High impact resistance |
| Cold weather | Does not become brittle (important for Swedish winter launches) |
| Stiffness | CF filler increases modulus, helps with fin flutter |
| Warping | CF filler reduces shrinkage anisotropy — the main problem with pure PC |

**Pure PC experience**: Printing large components from straight PC always produced some warping despite trying all common countermeasures (enclosure, bed adhesion, annealing, etc.). Spectrum PC CF largely solves this.

**Trade-off**: CF filler slightly reduces impact resistance compared to pure PC, but the increased stiffness is beneficial for flutter resistance.

**Printing notes**:

- Requires hardened steel nozzle (CF is abrasive)
- Print settings: 70% infill (consistent with PeregrineFinCan experience)
- Enclosure recommended (Bambu P1S has enclosure)

## Fin Flutter Analysis

### The Challenge

Fin flutter is the critical structural concern for L3. M-class motors produce significantly higher velocities than the J-class used for L2. Flutter occurs when aerodynamic forces couple with fin structural modes, and can destroy fins in milliseconds.

### Key Variables

- **Fin thickness**: Thicker = stiffer = higher flutter speed
- **Chord length**: Shorter chord helps
- **Span**: Shorter span helps (but reduces stability)
- **Material modulus**: Higher = better. PC CF is stiffer than pure PC
- **Airspeed**: Must analyze at maximum expected velocity (likely near burnout)

### Mitigation Strategies

1. **Material selection**: PC CF provides higher elastic modulus than most printable materials
2. **Carbon rod reinforcement**: Proven approach from PeregrineFin v0.7.0 (two 2.2mm channels at 25% and 60% chord). Same technique can scale to L3 fins
3. **Geometry optimization**: Shorter span, adequate thickness, appropriate taper ratio
4. **Conservative design**: Target flutter margin well above expected max velocity

### Previous Analysis Reference

PeregrineFin v0.7.0 analysis: span 137mm, area 23222mm², safety factor 1.65 at 10° AoA, flutter-safe to K-class motors with carbon rod reinforcement. L3 fin design must exceed this analysis for M-class speeds.

## Documentation Package

Tripoli L3 requires a comprehensive written project report. Planned sections:

- [ ] Project overview and objectives
- [ ] Stability analysis (CP/CG calculations, margin)
- [ ] Structural analysis (fin flutter, airframe loads)
- [ ] Recovery system design (dual deploy, redundancy)
- [ ] Electronics and avionics
- [ ] Construction documentation with photos
- [ ] Ground testing results
- [ ] Flight simulation results
- [ ] Safety analysis

### Repository

This documentation will live in this repo initially. May move to a separate repository if the L3 project scope warrants it.

## Open Questions

1. Specific 75mm single-use M motor selection
2. Airframe material and diameter
3. Nose cone — 3D printed or purchased?
4. Recovery system design (likely similar to L2: dual deploy with CATS Vega)
5. Second TAP member
6. Launch site — Enköping (SMRK) or elsewhere?
7. Timeline
