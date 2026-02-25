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
| Recovery | Dual deploy, dual redundant electronics, servo-actuated spring release (mechanism TBD) |
| Expected altitude | TBD |
| Number of fins | TBD |
| Fin material | Spectrum PC CF (3D printed polycarbonate + carbon fiber) |

### 1.3 Design Philosophy

- Minimum motor class (barely M at 5178 N-s) to keep velocities and forces manageable
- Progressive flight testing on J and L motors before cert flight
- 3D printed fin can in PC CF with carbon rod reinforcement for flutter resistance
- Dual redundant electronics as required by Tripoli L3 rules
- Servo-actuated spring release instead of black powder ejection charges — mechanism under evaluation (C-hinge with lateral pins or dual-half bayonet)
- Symmetric design: identical parts for both redundancy halves to simplify manufacturing and spares
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

### 2.9 Servo and Battery Enclosures in Parachute Bay

The separation servos and their batteries must be located near the separation joints, which are inside the parachute storage bays. To prevent parachutes and shock cords from snagging on electronics hardware:

**Wall-hugging enclosure concept**: A 3D printed fairing mounts the servo and battery flush against the inner tube wall. The enclosure has a smooth, snag-free outer surface facing inward, so the parachute slides past without catching. Essentially a streamlined bump on the inside of the body tube.

| Parameter | Value |
|-----------|-------|
| Material | Spectrum PC CF (same as other printed parts) |
| Contents per enclosure | 1 servo + 1 battery (or battery located elsewhere with wiring routed through) |
| Enclosures per joint | 2 (one per FC system, 180° apart) |
| Total enclosures | 4 (2 joints × 2 per joint) |
| Design | Parametric OpenSCAD, matched to tube ID curvature |
| Mounting | Bonded or mechanically fastened to tube wall |
| Outer surface | Smooth, radiused edges, no exposed screws or wires |

*TODO: Determine whether battery is co-located with servo in the enclosure or kept in the main e-bay with wiring routed to the servo. Co-location is simpler (shorter wires, fewer failure points) but adds mass in the parachute bay.*

### 2.10 Rail Guides

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
| Separation mechanism parts (printed) | Spectrum PC CF, identical parts | 2 per joint (4 total) | Printed by candidate |
| Lateral pins | TBD (steel or carbon rod) | 2 per joint (4 total) | TBD |
| Servo wall-hugging enclosures (printed) | Spectrum PC CF, matched to tube ID | 4 total (2 per joint) | Printed by candidate |
| Servos (separation) | TBD | 4 total (1 per mechanism half) | TBD |
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

Dual deployment using servo-actuated spring release mechanisms, controlled by dual redundant electronics:

| Event | Altitude | Device | Action |
|-------|----------|--------|--------|
| Apogee | Apogee detection | Primary FC + Backup FC | Either servo pulls its lateral pin → C-hinge separates → springs push sections apart → drogue deploys |
| Main | TBD (e.g., 300m AGL) | Primary FC + Backup FC | Either servo pulls its lateral pin → C-hinge separates → springs push sections apart → main deploys |

### 4.2 Separation Mechanism Concept

Instead of black powder ejection charges, separation is achieved mechanically:

1. **Springs** are preloaded between body sections during assembly, providing separation force
2. **Retention mechanism** (two identical C-hinge pairs at 180° apart) holds the sections together against the spring preload during flight
3. **Servos** pull lateral pins on command from the flight computer
4. Once either pin is pulled, the C-loops at that position fall apart — one remaining C-hinge pair cannot hold against the spring force alone → sections separate axially

**Why not black powder ejection charges?**

The conventional approach for HPR recovery separation uses black powder (BP) ejection charges. This design uses mechanical separation instead, for two reasons:

1. **Legal constraint (Estonia)**: Black powder is classified as an explosive under Estonian law. The candidate has no legal basis to possess even small quantities. Rocket motors are classified separately as pyrotechnics and are legally permissible. This is a hard constraint — BP-based separation is not an option for a builder based in Estonia
2. **Electronics protection**: BP charges deposit soot and combustion residue throughout the recovery bay. This rocket carries custom-built flight computers that are expensive and difficult to replace. Mechanical separation keeps the interior clean

**Additional advantages of mechanical separation**:

- Repeatable and testable — same force every time, no charge sizing uncertainty
- No hot gas near parachutes — no Nomex protectors needed
- No e-matches — simpler wiring, no igniter reliability concerns
- No pressure spike — gentler on airframe and recovery harness

### 4.3 Separation Mechanism Candidates

Two leading candidates are under evaluation. Both share the same core principle: two identical halves per joint, each controlled by one FC system, either half's release alone causes separation. The selection will be made after prototyping and discussion with Rolf.

#### Option A: C-Hinge with Lateral Pin (Preferred)

Interlocking C-shaped hinge loops at two positions 180° apart around the separation joint. Each C-hinge pair is held together by a lateral pin. The servo pulls the pin sideways to release.

**Operating principle:**

```
    CROSS-SECTION AT ONE C-HINGE PAIR

    LOCKED (pin inserted)            RELEASED (pin pulled sideways)

    Body A      Body B               Body A      Body B
    ┌───┐       ┌───┐               ┌───┐       ┌───┐
    │   ╰─╮ ╭─╯   │               │   ╰─╮   ╭─╯   │
    │     │P│     │               │     │   │     │  ← C-loops separate,
    │   ╭─╯ ╰─╮   │               │   ╭─╯   ╰─╮   │    nothing to interlock
    └───┘       └───┘               └───┘       └───┘

    P = lateral pin through           Pin pulled sideways by servo
        interlocking C-loops          C-loops fall apart


    FULL JOINT (top view, looking down into tube)

         C-hinge #1 (FC #1)
              ┌─┐
         ╭────┤P├────╮
        │    └─┘    │
    Body A           Body A
        │            │
         ╰────┤P├────╯
              └─┘
         C-hinge #2 (FC #2)

    Two C-hinge pairs at 180° apart
    Each has its own lateral pin
    Either pin removal → that pair falls apart → other pair can't hold → separation
```

- **Locked**: Both C-hinge pairs engaged with lateral pins. Together they carry full flight loads (axial thrust, drag, bending). The interlocking C-loops transfer axial loads through the pin in shear
- **Released**: Either servo pulls its pin sideways. The C-loops at that position have nothing to interlock around — they simply separate. One remaining C-hinge pair cannot resist the full spring preload → sections push apart axially
- **Geometry guarantee**: Unlike the bayonet (which requires careful force-balancing between lug engagement and spring force), the C-hinge release is binary — with pin present, the loops interlock and carry load; with pin removed, there is physically nothing connecting the loops. No force engineering needed for the release

**Key design properties:**

| Property | Value |
|----------|-------|
| C-hinge pairs per joint | 2 (at 180° apart) |
| Lateral pins per joint | 2 (one per C-hinge pair) |
| Total C-hinge pairs | 4 (2 joints × 2 pairs) |
| Total lateral pins | 4 |
| Servos total | 4 (one per pin) |
| Unique parts to design | **1 C-hinge half** (same part on both body sections, both joints) + **1 pin** |
| FC #1 controls | Pin at C-hinge #1 (drogue joint) + Pin at C-hinge #1 (main joint) |
| FC #2 controls | Pin at C-hinge #2 (drogue joint) + Pin at C-hinge #2 (main joint) |

**Advantages:**

- **Binary release**: Pin in = locked, pin out = separated. No force balancing, no partial engagement, no "can one half hold?" uncertainty. The geometry guarantees separation when a pin is removed
- **Simple servo action**: Linear pin pull (sideways). No rotation, no twist, no complex mechanism. Servo arm pulls pin through a short linear stroke
- **Strong when locked**: C-loops transfer axial load through the pin in shear. Pin shear strength is well-understood and easy to calculate
- **Symmetric**: Same C-hinge part printed multiple times. Same pin used everywhere
- **Full axial separation**: Body sections push apart completely, standard parachute deployment geometry
- **No tube cutout**: Joint is at the separation plane, no weakening of the body tube

**Concerns:**

- **Pin extraction force**: Pin must slide out cleanly under servo pull. Friction, corrosion, or deformation under load could impede extraction. Smooth pin surface, correct tolerances, and lubrication needed. Pin should not be under compression when loaded axially (C-loop geometry should transfer loads through shear, not clamping)
- **C-loop strength**: The printed C-loops must handle flight loads without cracking or deforming. Wall thickness, infill, and print orientation critical. PC CF should have adequate strength, but needs analysis
- **Pin retention during flight**: Pin must not slide out under vibration or G-loads. Options: friction fit, slight taper, detent notch, or servo holding the pin in place. The pin pull direction should be perpendicular to the primary load direction (axial) so flight loads don't tend to push the pin out
- **Servo torque**: Must overcome pin friction + any detent. Linear pull via servo arm — calculate required force and arm geometry
- **Tolerances**: C-loops must interlock cleanly. 3D printing tolerance for the loop gap and pin hole diameter. Print and test iterate
- **Cold weather**: Pin friction and servo performance at -10 to -20°C
- **Tethering**: After pin extraction, the pin itself must be tethered (to the servo arm or enclosure). Released C-loop halves separate with the body sections they're attached to — inherently tethered

#### Option B: Symmetric Dual-Half Bayonet (Alternative)

The bayonet joint is split into two identical halves, positioned 180° apart. Each half is an independent rotary latch controlled by its own servo and FC system.

- **Locked**: Both bayonet halves engaged. Together they carry full flight loads
- **Released**: Either servo releases its half (rotary or linear disengage). One half alone cannot resist the spring preload → sections separate axially
- Each half carries ~50% of axial load when both engaged, but cannot resist spring force alone

**Advantages:**

- Full axial separation
- Bayonet lugs are strong load-bearing surfaces
- One part design, print four copies

**Concerns:**

- Lug geometry is the critical design parameter — must hold flight loads with two halves but release under spring force with one half. This is the key weakness vs. the C-hinge: the bayonet requires careful force-balancing between lug engagement depth and spring force, whereas the C-hinge release is binary (pin in/out)
- Must not creep under vibration — needs detent or servo holding torque
- Bayonet parts stay in the bay after release — potential tangle with parachute

#### Common Design Elements

Both options share:

| Element | Description |
|---------|-------------|
| **Identical halves** | Same part printed multiple times. One design, multiple prints |
| **Spring deployment** | Preloaded springs push body sections apart after release |
| **Wall-hugging servo enclosures** | Servo + battery in smooth 3D printed fairings against tube wall (see section 2.9) |
| **4 servos total** | One per mechanism half, 2 per joint, 2 joints |
| **Tethering** | All released parts remain attached to a rocket section |
| **FC mapping** | FC #1 controls half A at both joints, FC #2 controls half B at both joints |

### 4.4 Redundancy Analysis

Applies to both mechanism options:

| Scenario | Result |
|----------|--------|
| Both FCs fire normally | Both halves release → clean separation |
| FC #1 fires, FC #2 fails | Half A releases → separation (C-hinge: loops fall apart; bayonet: one half can't hold) |
| FC #2 fires, FC #1 fails | Half B releases → separation (same logic) |
| Both FCs fail | Both halves remain locked → no separation (ballistic) |
| Servo #1 jams (mechanical) | FC #2 releases half B → separation |
| Servo #2 jams (mechanical) | FC #1 releases half A → separation |

True independent redundancy in both options: no single electrical or mechanical failure prevents recovery.

### 4.5 Mechanism Selection — TODO

Decision criteria for selecting between Option A (C-hinge) and Option B (bayonet):

1. **Prototype both** — print test versions of each, test fit and release on a body tube section
2. **Release reliability** — C-hinge has binary release (pin in/out), bayonet requires force-balancing. This strongly favors Option A
3. **Structural analysis** — compare load capacity of C-loops vs. bayonet lugs under flight loads
4. **Pin extraction testing** — verify pin pulls cleanly under realistic conditions (load, cold, vibration)
5. **TAP feedback** — discuss both with Rolf before committing
6. **Ease of field assembly** — which is simpler to set up and verify at the launch site?

Current preference: **Option A (C-hinge)** due to binary release guarantee.

### 4.6 Design Challenges — TODO

Regardless of which mechanism is selected:

- **Structural analysis**: Mechanism must handle boost loads (axial: motor thrust + drag, bending: wind loads, vibration: motor resonance)
- **Spring force**: Must reliably push sections apart and deploy parachute at all expected altitudes. Validated by ground testing
- **Servo selection**: Must reliably actuate in cold weather (Swedish winter, -10 to -20°C at altitude), under vibration, after sustaining boost G-loads. Torque margin needed
- **Tolerances**: 3D printed parts have different tolerances than machined parts. Test under realistic conditions, print spares
- **Tethering**: All released parts (pins, mechanism halves) must remain attached to a rocket section. No parts may descend without a recovery system (Tripoli non-certification condition)
- **Wall-hugging enclosures**: Must not snag parachute or shock cord. Ground test with actual parachute packing
- **Discuss with Rolf early**: Non-pyro separation is less common for L3. TAP approval of the concept is needed before detailed design

### 4.7 Drogue Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Apogee detection (barometric) |
| Mechanism | Servo-actuated release + spring separation (TBD: C-hinge or bayonet) |
| Parachute | TBD size drogue |
| Descent rate under drogue | TBD m/s |
| Separation point | TBD |

### 4.8 Main Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Altitude-based (TBD meters AGL) |
| Mechanism | Servo-actuated release + spring separation (TBD: C-hinge or bayonet) |
| Parachute | TBD size main |
| Descent rate under main | TBD m/s (must not exceed 35 ft/s = 10.7 m/s per Tripoli rules) |
| Separation point | TBD |

### 4.9 Landing Velocity

| Parameter | Value |
|-----------|-------|
| Maximum allowed | 35 ft/s (10.7 m/s) per Tripoli TUSC |
| Expected landing velocity | TBD |
| Liftoff weight | TBD |
| Main parachute Cd | TBD |

### 4.10 Redundancy Architecture

Per Tripoli L3 rules: *"Dual redundant electronics are required for all recovery events. Two completely independent and separate electronic recovery systems must be incorporated. Neither system must adversely affect the other. Redundancy means completely separate systems, including batteries, switches, avionics, and energetics."*

With servo-actuated separation, "energetics" is replaced by servo + pin/mechanism + spring. Each system controls its own mechanism halves across both separation joints.

| Component | Primary System (FC #1) | Backup System (FC #2) |
|-----------|----------------------|---------------------|
| Flight computer | Custom FC (CATS Vega clone, improved) | CATS Vega (original) or second custom clone |
| Battery | Dedicated battery #1 | Dedicated battery #2 |
| Arming switch | Key switch #1 | Key switch #2 |
| Drogue release | Servo #1 → lateral pin at C-hinge #1 (drogue joint) | Servo #2 → lateral pin at C-hinge #2 (drogue joint) |
| Main release | Servo #3 → lateral pin at C-hinge #1 (main joint) | Servo #4 → lateral pin at C-hinge #2 (main joint) |

The two systems share no electrical connections. Each has independent power, switching, sensing, and servo output. Each controls one of the two identical C-hinge pairs at each joint. Either system alone triggers separation.

### 4.11 Motor Note

The M1350W-PS is a plugged motor — no motor ejection charge. All recovery depends entirely on the dual redundant electronic systems. There is no motor backup.

### 4.12 Considered and Rejected Alternatives

The following approaches were evaluated earlier and set aside:

- **Dual pin (without C-hinge)**: Two independent pins, each pulled by one servo. Simpler mechanically, but harder to ensure one pin alone cannot hold against springs while both together resist flight loads. The C-hinge solves this by making the release binary
- **Single bayonet with dual servos**: One bayonet ring, two servos rotating it in opposite directions. Cleaner single mechanism, but a jammed bayonet blocks both systems — not truly independent failure paths
- **Hybrid (bayonet + pin bypass)**: Primary via bayonet rotation, backup via pin pull releasing entire bayonet assembly. True mechanical independence, but asymmetric design — two different part types, more complex, tether management concerns
- **Hinged door**: Hatch in body tube wall with hinge pins on two sides. Pull either pin → door swings open → parachute deploys sideways. Mechanically elegant degraded mode, but the tube cutout weakens structural integrity, creates aerodynamic discontinuity, and requires sideways parachute deployment which is non-standard. The C-hinge achieves the same binary release guarantee while maintaining full axial separation and no tube cutout

---

## 5. Recovery Electronics Schematic

*Per Tripoli L3 requirement 1.a.iii: "A wiring diagram that accurately reflects the wiring provided by the candidate from the power source, switches, and ejection charges."*

*Note: With servo-actuated separation, the wiring diagram shows servo connections instead of e-match/charge connections. Schematics of the actual flight computer internals are NOT required — only the wiring from power source, through switches, to the flight computers and servos.*

### 5.1 Wiring Diagram

*TODO: Create wiring diagram showing:*

- Battery #1 → Key switch #1 → Primary FC → Servo #1 (drogue C-hinge #1 pin) + Servo #3 (main C-hinge #1 pin)
- Battery #2 → Key switch #2 → Backup FC → Servo #2 (drogue C-hinge #2 pin) + Servo #4 (main C-hinge #2 pin)
- Physical separation between systems
- Servo connections (signal + power)
- Mechanical linkage: servo arm → pin pull (conceptual)

### 5.2 Primary System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #1 (TBD V) | Key switch #1 |
| Switched power | Key switch #1 | Primary FC power input |
| Servo channel 1 | Primary FC drogue output | Servo #1 → pulls lateral pin at drogue C-hinge #1 |
| Servo channel 2 | Primary FC main output | Servo #3 → pulls lateral pin at main C-hinge #1 |

### 5.3 Backup System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #2 (TBD V) | Key switch #2 |
| Switched power | Key switch #2 | Backup FC power input |
| Servo channel 1 | Backup FC drogue output | Servo #2 → pulls lateral pin at drogue C-hinge #2 |
| Servo channel 2 | Backup FC main output | Servo #4 → pulls lateral pin at main C-hinge #2 |

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
- [ ] Separation mechanism prototype printing and testing (C-hinge and bayonet)
- [ ] Mechanism selection after prototyping
- [ ] Final mechanism parts printing and fit testing
- [ ] Wall-hugging servo enclosure printing and fit testing
- [ ] Electronics bay / nose cone electronics construction
- [ ] Dual flight computer installation and wiring
- [ ] Servo installation and testing
- [ ] Recovery harness assembly
- [ ] Parachute packing and deployment test through mechanism
- [ ] Spring preload and mechanism engagement testing
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
- [ ] Spare C-hinge halves, pins, and servos
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
- [ ] Engage C-hinge pairs and insert lateral pins at drogue joint
- [ ] Engage C-hinge pairs and insert lateral pins at main joint
- [ ] Verify pin engagement at both joints (visual + tactile check)
- [ ] Verify all tethers attached (pins tethered to servo arms/enclosures)
- [ ] Connect servo mechanisms to pins
- [ ] Connect primary FC wiring and servos (#1, #3)
- [ ] Connect backup FC wiring and servos (#2, #4)
- [ ] Arm primary system (key switch #1)
- [ ] Verify primary FC status (LED/beep)
- [ ] Arm backup system (key switch #2)
- [ ] Verify backup FC status (LED/beep)
- [ ] Final visual inspection
- [ ] Place on launch rail

### 12.4 Post-Flight

- [ ] Recover rocket (all parts, including pins)
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
| Primary electronics failure | Backup system pulls pin at C-hinge #2 → separation | Successful recovery |
| Backup electronics failure | Primary system pulls pin at C-hinge #1 → separation | Successful recovery |
| Both electronics fail | Design for reliability, ground test | Non-certification (ballistic descent) |
| Single servo failure | Other system's servo pulls its pin → separation | Successful recovery |
| Both servos fail on same joint | Ground testing, servo selection, cold testing | Failed separation |
| Pin stuck (friction/deformation) | Smooth pin surface, lubrication, tolerances, cold testing; other pin still releases | Successful recovery (degraded) |
| C-loop cracked/broken | PC CF strength analysis, print orientation, infill, test loads | Structural failure at joint |
| Spring insufficient | Ground testing at various temperatures, margin in spring force | Incomplete separation |
| Premature pin extraction (vibration/G) | Pin pull direction perpendicular to axial loads, detent, servo holding | Premature separation during boost |
| Tether tangle with parachute | Tether routing, length management, ground test | Tangled recovery |
| Parachute snags on servo enclosure | Wall-hugging smooth fairing, ground test with actual packing | Failed deployment |
| Fin flutter | Flutter analysis, carbon reinforcement, progressive test flights | Structural failure |
| Unstable flight | Stability analysis, CP/CG verification, OpenRocket sim | Unsafe flight |
| Parachute tangle | Proper packing, ground test | Failed recovery |

### 13.2 Risk Mitigation Through Testing

| Test | Purpose | When |
|------|---------|------|
| C-hinge prototype | Print and test C-loop engagement, pin insertion/extraction | Early prototyping |
| Bayonet prototype | Print and test bayonet half engagement/release | Early prototyping |
| Mechanism selection | Compare prototypes, select winner | After prototyping |
| Pin extraction force measurement | Quantify force needed to pull pin under load and no-load | After mechanism selection |
| Servo enclosure fit test | Verify parachute slides past without snagging | During construction |
| Separation bench test (both pins) | Verify spring separates when both pins pulled | During construction |
| Redundancy test (pin #1 only) | Verify pulling pin #1 alone causes separation | During construction |
| Redundancy test (pin #2 only) | Verify pulling pin #2 alone causes separation | During construction |
| Cold temperature test | Verify servo and mechanism operation at -10 to -20°C | During construction |
| Vibration/shake test | Verify pins don't extract under simulated flight loads | During construction |
| Tether deployment test | Verify tethered pins/parts don't tangle with parachute | During construction |
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
| Dual redundant electronics | Two independent systems, each controlling one C-hinge pin |
| No untethered components | All pins and mechanism parts tethered to rocket sections |
| CP marked on rocket | External marking |

---

## Appendices

### A. OpenRocket Simulation Files

*TODO: Include .ork file or simulation output*

### B. OpenSCAD Design Files

*TODO: Include .scad source for fin can, fins, C-hinge halves, and servo enclosures*

### C. Thrust Curve Data

*TODO: Include M1350W RASP file from ThrustCurve.org*

### D. Material Datasheets

*TODO: Spectrum PC CF filament datasheet*

### E. Flight Computer Documentation

*TODO: Custom FC schematic, PCB layout, firmware overview*

### F. Separation Mechanism Design

*TODO: Detailed drawings of selected separation mechanism, including:*

- C-hinge loop geometry (OpenSCAD parametric design)
- Lateral pin dimensions and material (shear strength analysis)
- Pin extraction force analysis (friction, detent, servo torque margin)
- Spring selection and force calculations
- Servo selection and arm geometry for linear pin pull
- Anti-vibration pin retention design
- Wall-hugging servo enclosure design
- Redundancy verification test results (each pin independently)
- Tether routing plan (pins tethered to servo arms)
- Assembly and preload procedure
- Print settings and tolerance measurements
- Cold weather test results
- Prototype comparison results (C-hinge vs. bayonet)

### G. Forms

- [Universal Certification Form (UCF)](https://www.tripoli.org/docs.ashx?id=859597)
- [Pre-Flight Data Capture Form](https://www.tripoli.org/docs.ashx?id=891494)
- [L2 to L3 Flight Log Form](https://www.tripoli.org/docs.ashx?id=1566254)
