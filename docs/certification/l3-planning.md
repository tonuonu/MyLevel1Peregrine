# L3 Certification Planning

## Status: DESIGN PHASE

L1 and L2 were verification that fundamentals were understood correctly — kit-based flights with known parameters. L3 is a different challenge: designing and building a rocket from scratch.

## Requirements

Per [Tripoli L3 certification rules](https://www.tripoli.org/Level3):

- [x] Current L2 certification
- [ ] **3 flights on L2 impulse range** (J/K/L motors), documented in Tripoli Flight Log (L2 to L3)
- [ ] **At least 2 of those flights must use electronic deployment** (electronic flight controller controlling parachute ejection — motor-ejected chute with electronic release does NOT count)
- [ ] Written project report reviewed by 2 TAP members before flight
- [ ] Scratch-built rocket (no kits)
- [ ] Successfully fly and recover using M, N, or O motor
- [ ] Witnessed and approved by 2 TAP members

### TAP Committee

| Role | Name | Status |
|------|------|--------|
| TAP member #1 | Rolf Örell (TRA# 3728) | Confirmed |
| TAP member #2 | TBD | Rolf to introduce |

## Flight Progression

Incremental approach: build the L3 airframe early, fly it on progressively larger motors to validate the design before the certification flight.

| # | Motor | Diameter | Adapter | Airframe | Purpose | Electronic | Status |
|---|-------|----------|---------|----------|---------|------------|--------|
| 1 | AeroTech J350 | 38mm | — | Peregrine | L2 certification | ✓ CATS Vega | ✅ Done |
| 2 | AeroTech J420R | 38mm | 75→38mm | L3 airframe | Test new airframe, electronic deploy #2 | ✓ Custom FC | Planned |
| 3 | AeroTech L1000W | 54mm | 75→54mm | L3 airframe | Stress test at higher impulse, electronic deploy #3 | ✓ Custom FC | Planned |
| 4 | AeroTech M1350W-PS | 75mm | None | L3 airframe | **L3 certification flight** | ✓ Custom FC | Planned |

### Flight #2: J420R in L3 Airframe

Thrust-to-weight check: J420R average thrust 420N, 5:1 minimum ratio → max liftoff mass 8.56 kg. The L3 airframe will be heavier than the Peregrine but without the M-class motor. Need to keep dry weight + adapter + J420R motor weight under 8.5 kg. May be tight — requires weight estimate once airframe design is more mature.

### Flight #3: L1000W Stress Test

The AeroTech L1000W-18A is the primary candidate for the L-class stress test flight:

| Parameter | Value |
|-----------|-------|
| Designation | HP-L1000W |
| Diameter | 54mm |
| Length | 635mm |
| Total impulse | 2714 N-s (mid L-class) |
| Average thrust | 1000 N |
| Max thrust | 1261 N |
| Burn time | 2.7 s |
| Total weight | 2194 g |
| Propellant | White Lightning |
| Type | Single-use DMS |
| Delay | 10-18s adjustable (UDDT required) |

Thrust-to-weight: 1000N average, 5:1 minimum → max liftoff mass 20.4 kg. Very generous margin.

This flight validates the airframe under significantly higher loads and speeds before committing to the M-class cert flight.

### Flight #4: M1350W-PS Certification

The AeroTech M1350W-PS is the selected M-class motor for the L3 certification flight:

| Parameter | Value |
|-----------|-------|
| Designation | M1350W |
| Diameter | 75mm (native — no adapter) |
| Length | 622mm |
| Total impulse | 5178 N-s (1% into M-class) |
| Average thrust | 1357 N |
| Max thrust | 1766 N |
| Burn time | 3.8 s |
| Total weight | 4808 g |
| Propellant | White Lightning |
| Type | Single-use DMS |
| Delay | **Plugged + Smoke** (no ejection charge) |

Thrust-to-weight: 1357N average, 5:1 minimum → max liftoff mass 27.7 kg. Very generous margin.

**Important notes**:

- "-PS" = Plugged + Smoke. No motor ejection charge — electronic deployment is the **only** recovery mechanism. No motor backup unlike L2 flight. This makes flight computer reliability critical.
- Requires L3 certification to purchase. Must be sourced through TAP members or prefect for the certification attempt.
- Barely into M-class (5178 N-s vs 5120 N-s M threshold) — keeps velocities and forces as low as possible while meeting the requirement.
- Built-in 3/8-16 threaded aluminum bulkhead for eye bolt attachment.

### Motor Adapter Strategy

The 75mm motor mount is the native size for the L3 cert flight. Smaller motors require centering adapters:

| Adapter | For Motors | Flights |
|---------|-----------|---------|
| 75mm → 38mm | J420R and other 38mm J motors | Flight #2 |
| 75mm → 54mm | L1000W and other 54mm L motors | Flight #3 |
| None (native 75mm) | M1350W-PS | Flight #4 (cert) |

Adapters can be 3D printed in PC CF or machined from phenolic/aluminum.

## Motor Selection

### Motor Type: Single-Use

Single-use (disposable casing) rather than reloadable, for several reasons:

- No need to purchase expensive reloadable casing hardware
- No borrowed equipment at risk in a CATO
- Simpler preparation on launch day
- Acceptable cost for a one-off certification flight

## Electronics

### Custom Flight Computer

A custom flight computer will be developed, based on the CATS Vega design but with improvements:

- **Improved power-up system**: Based on power management approach used for NASA Centennial Challenge robots — details TBD
- **Dual pyro channels**: For drogue and main deployment
- **Data logging**: Barometer, IMU, full flight telemetry
- Open source design, custom PCB

The custom flight computer will be validated on flights #2 and #3 before the L3 cert flight.

### Redundancy

For flights #2 and #3 (with delay-equipped motors): electronic dual deployment as primary, with motor delay charge as independent safety backup.

For flight #4 (M1350W-PS, plugged): **no motor backup available**. Recovery depends entirely on electronic deployment. This makes dual redundant electronics critical — consider flying two independent flight computers (primary + backup) for the cert flight.

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

### Validation Through Flight Progression

The stepped flight approach (J → L → M) provides empirical validation of fin structural integrity at progressively higher speeds before the cert flight.

## Documentation Package

Tripoli L3 requires a comprehensive written project report. Planned sections:

- [ ] Project overview and objectives
- [ ] Stability analysis (CP/CG calculations, margin)
- [ ] Structural analysis (fin flutter, airframe loads)
- [ ] Recovery system design (dual deploy, redundancy)
- [ ] Electronics and avionics (custom flight computer design)
- [ ] Construction documentation with photos
- [ ] Ground testing results
- [ ] Flight simulation results
- [ ] Safety analysis
- [ ] L2 flight log (3 flights, demonstrating electronic deployment)

### Repository

This documentation will live in this repo initially. May move to a separate repository if the L3 project scope warrants it.

## Open Questions

1. ~~Specific 75mm single-use M motor selection for cert flight~~ → AeroTech M1350W-PS
2. Airframe material and diameter
3. Nose cone — 3D printed or purchased?
4. Custom flight computer detailed design
5. Second TAP member
6. Launch site — Enköping (SMRK) or elsewhere?
7. J420R weight budget — will L3 airframe stay under 8.56 kg for 5:1 T/W?
8. Dual redundant electronics for cert flight (plugged motor, no backup)?
9. Motor procurement logistics — M1350W-PS requires L3 cert to buy
10. Timeline
