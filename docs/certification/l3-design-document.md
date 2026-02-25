# L3 Certification Design Document

**Candidate**: Tõnu Samuel (TRA# 38105)
**TAP Member #1**: Rolf Örell (TRA# 3728)
**TAP Member #2**: TBD
**Date**: February 2026 (Draft)
**Status**: DRAFT — Not yet submitted for TAP review

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Airframe Construction Details](#2-airframe-construction-details)
3. [Bill of Materials](#3-bill-of-materials)
4. [Recovery System](#4-recovery-system)
5. [Recovery Electronics Schematic](#5-recovery-electronics-schematic)
6. [Motor](#6-motor)
7. [Stability Analysis](#7-stability-analysis)
8. [Flight Simulations](#8-flight-simulations)
9. [Fin Flutter Analysis](#9-fin-flutter-analysis)
10. [Construction Documentation](#10-construction-documentation)
11. [L2 Flight Log](#11-l2-flight-log)
12. [Pre-Flight Checklist](#12-pre-flight-checklist)
13. [Safety Analysis](#13-safety-analysis)

---

## 1. Project Overview

### 1.1 Objective

Tripoli Level 3 high-power certification using a scratch-built rocket with a single AeroTech M1350W-PS motor, dual-deployment recovery controlled by dual redundant electronics.

### 1.2 Rocket Summary

| Parameter | Value |
|-----------|-------|
| Name | TBD |
| Designer/Builder | Tõnu Samuel |
| Construction | Scratch-built |
| Length | TBD |
| Diameter | TBD |
| Dry weight (no motor) | TBD |
| Liftoff weight (with motor) | TBD |
| Motor | AeroTech M1350W-PS (75mm, 5178 N-s) |
| Recovery | Dual deploy, dual redundant electronics, dual-half bayonet spring release |
| Expected altitude | TBD |
| Number of fins | TBD |
| Fin material | Spectrum PC CF (3D printed polycarbonate + carbon fiber) |

### 1.3 Design Philosophy

- Minimum motor class (barely M at 5178 N-s) to keep velocities and forces manageable
- Progressive flight testing on J and L motors before cert flight
- 3D printed fin can in PC CF with carbon rod reinforcement for flutter resistance
- Dual redundant electronics as required by Tripoli L3 rules
- Symmetric dual-half bayonet spring release — one design, two identical halves, true independent redundancy
- Single-use motor to avoid reloadable hardware risk

---

## 2. Airframe Construction Details

*Per Tripoli L3 requirement 1.a.i: Dimensioned drawings*

### 2.1 General Arrangement Drawing

*TODO: Dimensioned side-view drawing showing all major sections and dimensions*

- Overall length
- Body tube OD/ID
- Nose cone length and shape
- Fin dimensions and positions
- CP and CG locations marked
- Electronics bay location
- Recovery section layout
- Motor mount position and length
- Separation mechanism locations

### 2.2 Body Tube

| Parameter | Value |
|-----------|-------|
| Material | TBD (commercial prebuilt tube) |
| Outer diameter | TBD |
| Inner diameter | TBD |
| Wall thickness | TBD |
| Total length | TBD |

### 2.3 Nose Cone

| Parameter | Value |
|-----------|-------|
| Type | TBD (ogive/Von Kármán/conical) |
| Material | TBD (3D printed or commercial) |
| Length | TBD |
| Shoulder length | TBD |

Electronics may be housed in the nose cone — see section 2.8.

### 2.4 Fin Can Assembly

The fin can is 3D printed by the candidate using OpenSCAD for parametric design and Bambu P1S for printing.

| Parameter | Value |
|-----------|-------|
| Material | Spectrum PC CF (polycarbonate + carbon fiber) |
| Number of fins | TBD |
| Fin shape | TBD |
| Root chord | TBD |
| Tip chord | TBD |
| Span | TBD |
| Thickness | TBD |
| Sweep angle | TBD |
| Reinforcement | Carbon rod channels (2× per fin, at 25% and 60% chord) |
| Infill | 70% |
| Print orientation | TBD |

**Multi-part assembly**: The fin can body is printed in multiple sections (each ≤250mm tall, Bambu P1S limit with AMS) and bonded together. Fins are printed individually and bonded to the assembled can.

### 2.5 Centering Rings and Bulkheads

| Component | Material | Dimensions | Notes |
|-----------|----------|------------|-------|
| Forward centering ring | TBD | TBD | |
| Aft centering ring | TBD | TBD | |
| E-bay forward bulkhead | TBD | TBD | |
| E-bay aft bulkhead | TBD | TBD | |

### 2.6 Motor Mount

| Parameter | Value |
|-----------|-------|
| Motor tube ID | 75mm |
| Motor tube material | TBD |
| Length | TBD (≥622mm for M1350W-PS) |
| Motor retention | TBD |

### 2.7 Motor Adapters

For pre-certification test flights:

| Adapter | For Motor | Inner Diameter |
|---------|-----------|----------------|
| 75→54mm | AeroTech L1000W-18A | 54mm |
| 75→38mm | AeroTech J420R | 38mm |

### 2.8 Electronics Bay

| Parameter | Value |
|-----------|-------|
| Location | TBD — either mid-body or nose cone |
| Length | TBD |
| Sled material | TBD |
| Switch access | External key switches (2×, one per system) |

**Nose cone option**: Placing electronics in the nose cone simplifies wiring (all forward), and the electronics mass helps CG stay forward for stability. Trade-off is accessibility and nose cone structural requirements.

**Mid-body option**: Traditional e-bay between recovery sections. Easier access, standard approach.

*TODO: Decide based on airframe layout and CG analysis.*

### 2.9 Rail Guides

| Parameter | Value |
|-----------|-------|
| Type | TBD |
| Quantity | TBD |
| Positions | TBD |

---

## 3. Bill of Materials

*Per Tripoli L3 requirement 1.a.ii*

### 3.1 Airframe Components

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| Body tube | TBD (commercial prebuilt) | TBD | TBD |
| Nose cone | TBD | 1 | TBD |
| Fin can body (printed) | Spectrum PC CF | 1 set | Printed by candidate |
| Fins (printed) | Spectrum PC CF | TBD | Printed by candidate |
| Carbon reinforcement rods | 2.0mm carbon rod | TBD | TBD |
| Centering rings | TBD | TBD | TBD |
| Motor mount tube | 75mm ID | 1 | TBD |
| Motor retainer | TBD | 1 | TBD |
| E-bay structure | TBD | 1 | TBD |
| Bulkheads | TBD | 2 | TBD |
| Rail guides | TBD | TBD | TBD |
| Shock cord | TBD | TBD | TBD |
| Quick links / hardware | TBD | TBD | TBD |

### 3.2 Recovery Components

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| Drogue parachute | TBD size | 1 | TBD |
| Main parachute | TBD size | 1 | TBD |
| Separation springs | TBD | TBD per joint | TBD |
| Bayonet half (printed) | Spectrum PC CF, identical part | 2 per joint (4 total for dual deploy) | Printed by candidate |
| Servos (separation) | TBD | 1 per bayonet half (4 total) | TBD |
| Tether cord (mechanism retention) | TBD | As needed | TBD |

### 3.3 Electronics

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| Primary flight computer | Custom (CATS Vega clone, improved) | 1 | Built by candidate |
| Backup flight computer | CATS Vega (original) or second custom clone | 1 | TBD |
| Battery (primary) | TBD | 1 | TBD |
| Battery (backup) | TBD | 1 | TBD |
| Key switch (primary) | TBD | 1 | TBD |
| Key switch (backup) | TBD | 1 | TBD |

### 3.4 Motor

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| AeroTech M1350W-PS | 75mm single-use DMS | 1 | TBD (requires L3 to purchase — sourced via TAP) |

---

## 4. Recovery System

*Per Tripoli L3 recovery requirements: parachute recovery required, dual deployment allowed with apogee destabilization event*

### 4.1 Recovery Architecture

Dual deployment using symmetric dual-half bayonet release mechanisms with spring separation, controlled by dual redundant electronics:

| Event | Altitude | Device | Action |
|-------|----------|--------|--------|
| Apogee | Apogee detection | Primary FC + Backup FC | Either servo releases its bayonet half → spring separates body → drogue deploys |
| Main | TBD (e.g., 300m AGL) | Primary FC + Backup FC | Either servo releases its bayonet half → spring separates body → main deploys |

### 4.2 Separation Mechanism Concept

Instead of black powder ejection charges, separation is achieved mechanically:

1. **Springs** are preloaded between body sections during assembly, providing separation force
2. **Dual-half bayonet** holds the sections together against the spring preload during flight
3. **Servos** release the bayonet halves on command from the flight computer
4. Once either half is released, the remaining half cannot hold against the spring force alone, and the sections separate

**Advantages over BP charges**:

- No pyrotechnics — simpler handling, no e-matches, no charge sizing
- Repeatable and testable — same force every time
- No hot gas near parachutes — no Nomex protectors needed
- Clean separation — no soot, no pressure spike

### 4.3 Selected Mechanism: Symmetric Dual-Half Bayonet

The bayonet joint is split into two identical halves, positioned 180° apart. Each half is an independent latch controlled by its own servo and FC system.

#### Operating Principle

```
    LOCKED STATE                    EITHER HALF RELEASED
    ┌──────────┐                    ┌──────────┐
    │  Body A  │                    │  Body A  │
    ├──┐    ┌──┤                    ├──┐       │
    │H1│    │H2│  ← both halves    │H1│       │  ← half 2 released
    ├──┘    └──┤    engaged         ├──┘       │    by servo #2
    │  Body B  │                    │  Body B  │ ←── springs push apart
    └──────────┘                    └──────────┘
```

- **Locked**: Both bayonet halves (H1, H2) engaged. Together they carry full flight loads (axial thrust, drag, bending)
- **Released**: Either servo releases its half. One half alone cannot resist the spring preload → sections separate
- Each half is designed to carry approximately 50% of the axial load when both are engaged, but is deliberately unable to resist the full spring force alone

#### Key Design Properties

| Property | Value |
|----------|-------|
| Number of halves per joint | 2 (identical parts) |
| Halves per separation event | 2 (drogue joint + main joint) |
| Total bayonet halves | 4 (2 joints × 2 halves) |
| Servos total | 4 (one per half) |
| Parts to design | **1** (same part used everywhere) |
| FC #1 controls | Half A at drogue joint + Half A at main joint |
| FC #2 controls | Half B at drogue joint + Half B at main joint |

#### Redundancy Analysis

| Scenario | Result |
|----------|--------|
| Both FCs fire normally | Both halves release simultaneously → clean separation |
| FC #1 fires, FC #2 fails | Half A releases → half B alone cannot hold → separation |
| FC #2 fires, FC #1 fails | Half B releases → half A alone cannot hold → separation |
| Both FCs fail | Both halves remain locked → no separation (ballistic) |
| Servo #1 jams (mechanical) | FC #2 releases half B → half A alone cannot hold → separation |
| Servo #2 jams (mechanical) | FC #1 releases half A → half B alone cannot hold → separation |

True independent redundancy: no single electrical or mechanical failure prevents separation.

#### Manufacturing Advantage

One OpenSCAD design, one STL/3MF, print multiples. All four bayonet halves (2 per joint) are the same part. Spares are trivial — bring extras to the launch.

#### Design Challenges — TODO

- **Lug geometry**: Each half carries ~50% of flight loads when locked. Lug shape must be strong enough for this but unable to resist spring force alone. This is the critical design parameter — lug engagement depth and spring force must be carefully matched
- **Rotational vs. linear release**: Decide whether the servo rotates the half (traditional bayonet twist) or pulls it linearly (slide out). Rotation may be simpler for a 3D printed part; linear pull may be more reliable with a servo arm
- **Anti-vibration**: Each half must not creep toward release under motor vibration. Options: detent, friction fit, slight interference, servo holding torque
- **Spring sizing**: Springs must overcome friction of one remaining half plus parachute packing resistance. Must separate reliably at all altitudes. Ground test required
- **Servo torque/force**: Must overcome detent + friction to release the half. Must not back-drive under vibration. Servo selection and torque analysis needed
- **Tolerances**: 3D printed parts — test fit, iterate. Print several and measure variation
- **Cold weather**: Verify mechanism operation at expected Swedish winter temperatures (-10 to -20°C at altitude). PC CF should be fine, but servo grease and spring rate may change
- **Discuss with Rolf**: Get TAP approval of non-pyro separation concept before detailed design

#### Considered Alternatives

The following approaches were evaluated before selecting the symmetric dual-half bayonet:

- **Dual pin**: Two independent pins, each pulled by one servo. Simpler mechanically, but harder to ensure one pin alone cannot hold against springs while both together resist flight loads. Pin geometry is fussy.
- **Single bayonet with dual servos**: One bayonet ring, two servos rotating it in opposite directions. Cleaner single mechanism, but a jammed bayonet blocks both systems — not truly independent failure paths.
- **Hybrid (bayonet + pin bypass)**: Primary via bayonet rotation, backup via pin pull releasing entire bayonet assembly. True mechanical independence, but more complex, more parts, tether management concerns.

The symmetric dual-half bayonet was selected because it combines true independent redundancy with manufacturing simplicity — one part printed multiple times.

### 4.4 Design Challenges — TODO

General challenges regardless of mechanism specifics:

- **Structural analysis**: Combined halves must handle boost loads (axial: motor thrust + drag, bending: wind loads, vibration: motor resonance)
- **Spring force**: Must reliably push sections apart and deploy parachute at all expected altitudes. Validated by ground testing
- **Servo selection**: Must reliably actuate in cold weather (Swedish winter), under vibration, after sustaining boost G-loads. Torque margin needed
- **Tolerances**: 3D printed mechanism parts have different tolerances than machined parts. Test under realistic conditions, print spares
- **Tethering**: All released mechanism parts (bayonet halves, servos) must remain attached to a rocket section via tether. No parts may descend without a recovery system (Tripoli non-certification condition)
- **Discuss with Rolf early**: Non-pyro separation is less common for L3. TAP approval of the concept is needed before detailed design

### 4.5 Drogue Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Apogee detection (barometric) |
| Mechanism | Dual-half bayonet release + spring separation |
| Parachute | TBD size drogue |
| Descent rate under drogue | TBD m/s |
| Separation point | TBD |

### 4.6 Main Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Altitude-based (TBD meters AGL) |
| Mechanism | Dual-half bayonet release + spring separation |
| Parachute | TBD size main |
| Descent rate under main | TBD m/s (must not exceed 35 ft/s = 10.7 m/s per Tripoli rules) |
| Separation point | TBD |

### 4.7 Landing Velocity

| Parameter | Value |
|-----------|-------|
| Maximum allowed | 35 ft/s (10.7 m/s) per Tripoli TUSC |
| Expected landing velocity | TBD |
| Liftoff weight | TBD |
| Main parachute Cd | TBD |

### 4.8 Redundancy Architecture

Per Tripoli L3 rules: *"Dual redundant electronics are required for all recovery events. Two completely independent and separate electronic recovery systems must be incorporated. Neither system must adversely affect the other. Redundancy means completely separate systems, including batteries, switches, avionics, and energetics."*

With the dual-half bayonet, "energetics" is replaced by servo + bayonet half + spring. Each system controls its own bayonet halves across both separation joints.

| Component | Primary System (FC #1) | Backup System (FC #2) |
|-----------|----------------------|---------------------|
| Flight computer | Custom FC (CATS Vega clone, improved) | CATS Vega (original) or second custom clone |
| Battery | Dedicated battery #1 | Dedicated battery #2 |
| Arming switch | Key switch #1 | Key switch #2 |
| Drogue release | Servo #1 → bayonet half A (drogue joint) | Servo #2 → bayonet half B (drogue joint) |
| Main release | Servo #3 → bayonet half A (main joint) | Servo #4 → bayonet half B (main joint) |

The two systems share no electrical connections. Each has independent power, switching, sensing, and servo output. Each controls one of the two identical bayonet halves at each joint. Either system alone triggers separation.

### 4.9 Motor Note

The M1350W-PS is a plugged motor — no motor ejection charge. All recovery depends entirely on the dual redundant electronic systems. There is no motor backup.

---

## 5. Recovery Electronics Schematic

*Per Tripoli L3 requirement 1.a.iii: "A wiring diagram that accurately reflects the wiring provided by the candidate from the power source, switches, and ejection charges."*

*Note: With servo-actuated separation, the wiring diagram shows servo connections instead of e-match/charge connections. Schematics of the actual flight computer internals are NOT required — only the wiring from power source, through switches, to the flight computers and servos.*

### 5.1 Wiring Diagram

*TODO: Create wiring diagram showing:*

- Battery #1 → Key switch #1 → Primary FC → Servo #1 (drogue half A) + Servo #3 (main half A)
- Battery #2 → Key switch #2 → Backup FC → Servo #2 (drogue half B) + Servo #4 (main half B)
- Physical separation between systems
- Servo connections (signal + power)
- Mechanical linkage to bayonet halves (conceptual)

### 5.2 Primary System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #1 (TBD V) | Key switch #1 |
| Switched power | Key switch #1 | Primary FC power input |
| Servo channel 1 | Primary FC drogue output | Servo #1 → drogue joint bayonet half A |
| Servo channel 2 | Primary FC main output | Servo #3 → main joint bayonet half A |

### 5.3 Backup System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #2 (TBD V) | Key switch #2 |
| Switched power | Key switch #2 | Backup FC power input |
| Servo channel 1 | Backup FC drogue output | Servo #2 → drogue joint bayonet half B |
| Servo channel 2 | Backup FC main output | Servo #4 → main joint bayonet half B |

---

## 6. Motor

### 6.1 Motor Specifications

| Parameter | Value |
|-----------|-------|
| Motor | AeroTech M1350W-PS |
| Type | Single-use DMS (Plugged + Smoke) |
| Diameter | 75mm |
| Length | 622mm |
| Total impulse | 5178 N-s (1% M-class) |
| Average thrust | 1357 N |
| Maximum thrust | 1766 N |
| Burn time | 3.8 s |
| Total weight | 4808 g |
| Propellant | White Lightning |
| Ejection | **Plugged — no ejection charge** |
| Certification | TRA certified, June 2014 |

### 6.2 Motor Retention

| Parameter | Value |
|-----------|-------|
| Method | TBD |
| Rating | Must retain motor under full thrust loads |

### 6.3 Thrust-to-Weight Ratio

| Parameter | Value |
|-----------|-------|
| Average thrust | 1357 N |
| Liftoff weight | TBD kg |
| Thrust-to-weight ratio | TBD (minimum 5:1 required) |

---

## 7. Stability Analysis

### 7.1 Center of Gravity (CG)

| Condition | CG Location (from nose tip) |
|-----------|----------------------------|
| Without motor | TBD |
| With motor (loaded) | TBD |
| With motor (burnout) | TBD |

### 7.2 Center of Pressure (CP)

| Method | CP Location (from nose tip) |
|--------|----------------------------|
| Barrowman method | TBD |
| OpenRocket | TBD |

### 7.3 Stability Margin

| Condition | Margin (calibers) | Assessment |
|-----------|--------------------|------------|
| At launch (loaded) | TBD | Must be ≥1.0 cal |
| At burnout | TBD | |

*Note: CP must be marked on the rocket per Tripoli rules.*

### 7.4 Rail Exit Velocity

| Parameter | Value |
|-----------|-------|
| Rail length | TBD |
| Rail exit velocity | TBD (must be sufficient for stable flight) |

---

## 8. Flight Simulations

*Per Tripoli L3 requirement 1.a.iv*

### 8.1 Simulation Software

| Software | Version | Purpose |
|----------|---------|---------|
| OpenRocket | TBD | Primary flight simulation |

### 8.2 Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Motor | AeroTech M1350W (thrust curve from ThrustCurve.org) |
| Liftoff weight | TBD |
| Launch rod length | TBD |
| Launch angle | TBD |
| Wind speed | TBD (simulate range of conditions) |

### 8.3 Simulation Results

| Parameter | Value |
|-----------|-------|
| Maximum altitude | TBD |
| Maximum velocity | TBD |
| Maximum Mach number | TBD |
| Maximum acceleration | TBD |
| Time to apogee | TBD |
| Rail exit velocity | TBD |
| Optimal drogue delay | N/A (electronic deployment) |
| Landing distance (no wind) | TBD |
| Landing distance (TBD m/s wind) | TBD |

### 8.4 Thrust Curve

*TODO: Include M1350W thrust curve plot*

### 8.5 Altitude vs. Time Plot

*TODO: Include simulation altitude plot*

### 8.6 Velocity vs. Time Plot

*TODO: Include simulation velocity plot (critical for flutter analysis)*

### 8.7 Wind Sensitivity Analysis

*TODO: Simulate at multiple wind speeds to verify landing within waiver radius*

---

## 9. Fin Flutter Analysis

### 9.1 Maximum Airspeed

From flight simulations:

| Parameter | Value |
|-----------|-------|
| Max velocity | TBD m/s |
| Mach at max velocity | TBD |
| Altitude at max velocity | TBD |

### 9.2 Material Properties

| Property | Spectrum PC CF | Source |
|----------|---------------|--------|
| Elastic modulus (E) | TBD GPa | Datasheet / testing |
| Density | TBD g/cm³ | Datasheet |
| Poisson's ratio | TBD | Estimated |

### 9.3 Fin Geometry

| Parameter | Value |
|-----------|-------|
| Root chord (Cr) | TBD |
| Tip chord (Ct) | TBD |
| Semi-span (b) | TBD |
| Thickness (t) | TBD |
| Taper ratio (λ = Ct/Cr) | TBD |

### 9.4 Flutter Speed Calculation

*TODO: Calculate flutter speed using NACA/Air Force flutter boundary equation and compare to maximum expected airspeed. Target safety factor ≥2.0.*

### 9.5 Carbon Rod Reinforcement

If flutter margin insufficient with PC CF alone:

| Parameter | Value |
|-----------|-------|
| Rod diameter | 2.0-2.2mm carbon |
| Number per fin | 2 |
| Positions | 25% and 60% chord |
| Channel design | Span-wise, accessible from tab face |
| Effect on flutter speed | TBD |

---

## 10. Construction Documentation

*Per Tripoli L3 requirements: candidate shall personally assemble all assemblies, frequently communicate with TAPs, and provide photos of construction progress.*

### 10.1 Construction Log

*TODO: Dated entries with photos for each construction phase:*

- [ ] Fin can 3D printing (OpenSCAD design → 3MF export → Bambu P1S print)
- [ ] Fin printing and carbon rod installation
- [ ] Fin can assembly (bonding sections and fins)
- [ ] Motor mount assembly
- [ ] Centering ring installation
- [ ] Body tube preparation
- [ ] Bayonet half printing and fit testing
- [ ] Separation mechanism assembly and bench testing
- [ ] Electronics bay / nose cone electronics construction
- [ ] Dual flight computer installation and wiring
- [ ] Servo installation and testing
- [ ] Recovery harness assembly
- [ ] Parachute packing
- [ ] Spring preload and bayonet engagement testing
- [ ] Final assembly
- [ ] Weight and CG measurements
- [ ] CP marking on airframe
- [ ] Ground test of electronics (both systems independently)
- [ ] Separation mechanism ground testing (each half independently)

### 10.2 Construction Photos

*TODO: Photos of candidate working on each assembly per Tripoli requirement*

---

## 11. L2 Flight Log

*Per Tripoli L3 requirement: 3 flights on L2 impulse (J/K/L), at least 2 with electronic deployment. Submit with Tripoli L2-to-L3 Flight Log form.*

| Flight | Date | Motor | Impulse | Electronic Deploy | Status |
|--------|------|-------|---------|-------------------|--------|
| 1 | 22 Feb 2026 | AeroTech J350 | J (658 N-s) | ✓ CATS Vega dual deploy | ✅ Complete |
| 2 | TBD | AeroTech J420R | J (658 N-s) | ✓ Custom FC | Planned |
| 3 | TBD | AeroTech L1000W | L (2714 N-s) | ✓ Custom FC | Planned |

Electronic deployment count: 1 of 2 minimum complete.

---

## 12. Pre-Flight Checklist

*Based on [Tripoli Pre-Flight Data Capture Form](https://www.tripoli.org/docs.ashx?id=891494) and [Pre-Flight Review Checklist](https://www.tripoli.org/content.aspx?page_id=22&club_id=795696&module_id=496546)*

### 12.1 Before Leaving Home

- [ ] Design packet (this document, approved and signed by both TAPs)
- [ ] Signed Universal Certification Form (UCF) — top portion completed
- [ ] Completed Pre-Flight Data Capture Form
- [ ] L2-to-L3 Flight Log Form (with 3 flights documented)
- [ ] Rocket fully assembled and inspected
- [ ] Motor (M1350W-PS)
- [ ] Igniter (FirstFire)
- [ ] Batteries charged (2×, one per system)
- [ ] Key switches and keys (2×)
- [ ] Spare bayonet halves and servos
- [ ] Tools for field assembly

### 12.2 At Launch Site — Before Assembly

- [ ] Present design packet to certifying TAP
- [ ] Present completed Data Capture Form
- [ ] TAP reviews predicted flight characteristics
- [ ] Verify compliance with TUSC and FAR 101.25
- [ ] Verify launch site dimensions support required safe distances

### 12.3 Assembly and Arming

- [ ] Assemble motor per instructions
- [ ] TAP inspection of motor assembly
- [ ] Install motor in rocket with retention
- [ ] Pack drogue parachute
- [ ] Pack main parachute
- [ ] Preload separation springs
- [ ] Engage both bayonet halves at drogue joint
- [ ] Engage both bayonet halves at main joint
- [ ] Verify bayonet engagement at both joints
- [ ] Verify all tethers attached
- [ ] Connect servo mechanisms to bayonet halves
- [ ] Connect primary FC wiring and servos (#1, #3)
- [ ] Connect backup FC wiring and servos (#2, #4)
- [ ] Arm primary system (key switch #1)
- [ ] Verify primary FC status (LED/beep)
- [ ] Arm backup system (key switch #2)
- [ ] Verify backup FC status (LED/beep)
- [ ] Final visual inspection
- [ ] Place on launch rail

### 12.4 Post-Flight

- [ ] Recover rocket (all parts)
- [ ] Present to TAP as recovered
- [ ] TAP inspects for excessive damage
- [ ] TAP determines certification result
- [ ] If successful: TAP signs UCF
- [ ] Candidate emails signed UCF to Tripoli HQ

---

## 13. Safety Analysis

### 13.1 Failure Modes

| Failure Mode | Mitigation | Consequence |
|-------------|------------|-------------|
| Motor CATO | Single-use motor, proper assembly | Non-certification |
| Motor retention failure | Adequate retention hardware, inspection | Non-certification |
| Primary electronics failure | Backup system releases half B → separation | Successful recovery |
| Backup electronics failure | Primary system releases half A → separation | Successful recovery |
| Both electronics fail | Design for reliability, ground test | Non-certification (ballistic descent) |
| Single servo failure | Other system's servo releases its half → one half cannot hold alone → separation | Successful recovery |
| Both servos fail on same joint | Ground testing, servo selection, cold testing | Failed separation |
| Bayonet half jammed | Tolerances, lubrication, vibration testing, print spares, test fit | Failed separation (mitigated: other half release still causes separation) |
| Spring insufficient | Ground testing at various temperatures, margin in spring force | Incomplete separation |
| Premature bayonet release (vibration/G) | Detent design, lug geometry, servo holding torque, vibration testing | Drag separation during boost |
| Tether tangle with parachute | Tether routing, length management, ground test | Tangled recovery |
| Fin flutter | Flutter analysis, carbon reinforcement, progressive test flights | Structural failure |
| Unstable flight | Stability analysis, CP/CG verification, OpenRocket sim | Unsafe flight |
| Parachute tangle | Proper packing, ground test | Failed recovery |

### 13.2 Risk Mitigation Through Testing

| Test | Purpose | When |
|------|---------|------|
| Bayonet half fit test | Verify printed parts engage/release cleanly | After printing |
| Separation bench test (both halves) | Verify spring separates when both released | During construction |
| Redundancy test (half A only) | Verify releasing half A alone causes separation | During construction |
| Redundancy test (half B only) | Verify releasing half B alone causes separation | During construction |
| Cold temperature test | Verify servo and mechanism operation at -10 to -20°C | During construction |
| Vibration/shake test | Verify bayonet halves don't disengage under simulated flight loads | During construction |
| Tether deployment test | Verify tethered parts don't tangle with parachute | During construction |
| Flight #2 (J420R) | Validate airframe, electronics, separation mechanism in flight | Before L flight |
| Flight #3 (L1000W) | Stress test at higher loads and speeds | Before M flight |
| Electronics ground test | Verify both systems detect apogee/altitude correctly | Before each flight |

### 13.3 Compliance

| Requirement | Compliance Method |
|-------------|------------------|
| Tripoli Unified Safety Code (TUSC) | Design review, simulation |
| FAR 101.25 | Altitude prediction within waiver |
| Waiver radius | Wind simulation, dual deploy for tight landing |
| Landing velocity ≤ 35 ft/s | Parachute sizing calculation |
| Dual redundant electronics | Two independent systems, each controlling one bayonet half |
| No untethered components | All mechanism parts tethered to rocket sections |
| CP marked on rocket | External marking |

---

## Appendices

### A. OpenRocket Simulation Files

*TODO: Include .ork file or simulation output*

### B. OpenSCAD Design Files

*TODO: Include .scad source for fin can, fins, and bayonet half*

### C. Thrust Curve Data

*TODO: Include M1350W RASP file from ThrustCurve.org*

### D. Material Datasheets

*TODO: Spectrum PC CF filament datasheet*

### E. Flight Computer Documentation

*TODO: Custom FC schematic, PCB layout, firmware overview*

### F. Separation Mechanism Design

*TODO: Detailed drawings of dual-half bayonet mechanism, including:*

- Bayonet half geometry (OpenSCAD parametric design)
- Lug engagement depth and load analysis
- Spring selection and force calculations (must overcome single-half friction)
- Servo selection and torque requirements
- Anti-vibration detent design
- Redundancy verification test results (each half independently)
- Tether routing plan
- Assembly and preload procedure
- Print settings and tolerance measurements
- Cold weather test results

### G. Forms

- [Universal Certification Form (UCF)](https://www.tripoli.org/docs.ashx?id=859597)
- [Pre-Flight Data Capture Form](https://www.tripoli.org/docs.ashx?id=891494)
- [L2 to L3 Flight Log Form](https://www.tripoli.org/docs.ashx?id=1566254)
