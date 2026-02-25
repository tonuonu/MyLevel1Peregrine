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
| Recovery | Dual deploy, dual redundant electronics, servo-actuated spring release |
| Expected altitude | TBD |
| Number of fins | TBD |
| Fin material | Spectrum PC CF (3D printed polycarbonate + carbon fiber) |

### 1.3 Design Philosophy

- Minimum motor class (barely M at 5178 N-s) to keep velocities and forces manageable
- Progressive flight testing on J and L motors before cert flight
- 3D printed fin can in PC CF with carbon rod reinforcement for flutter resistance
- Dual redundant electronics as required by Tripoli L3 rules
- Servo-actuated spring release instead of black powder ejection charges
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
| Nomex chute protectors | TBD | 2 | TBD |
| Separation springs | TBD | TBD | TBD |
| Retention pins | TBD | TBD | TBD |
| Servos (separation) | TBD | TBD | TBD |

### 3.3 Electronics

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| Primary flight computer | Custom (CATS Vega clone, improved) | 1 | Built by candidate |
| Backup flight computer | CATS Vega (original) or second custom clone | 1 | TBD |
| Battery (primary) | TBD | 1 | TBD |
| Battery (backup) | TBD | 1 | TBD |
| Key switch (primary) | TBD | 1 | TBD |
| Key switch (backup) | TBD | 1 | TBD |
| Servos (drogue separation) | TBD | TBD per system | TBD |
| Servos (main separation) | TBD | TBD per system | TBD |

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
| Apogee | Apogee detection | Primary FC + Backup FC | Servo releases pin → spring separates body → drogue deploys |
| Main | TBD (e.g., 300m AGL) | Primary FC + Backup FC | Servo releases pin → spring separates body → main deploys |

### 4.2 Separation Mechanism Concept

Instead of black powder ejection charges, separation is achieved mechanically:

1. **Springs** are preloaded between body sections during assembly, providing separation force
2. **Retention pins** hold the sections together against the spring preload during flight
3. **Servos** pull the pins out on command from the flight computer
4. Once pins are removed, springs push the sections apart and deploy the parachute

**Advantages over BP charges**:

- No pyrotechnics — simpler handling, no e-matches, no charge sizing
- Repeatable and testable — same force every time
- No hot gas near parachutes — no Nomex protectors needed
- Clean separation — no soot, no pressure spike

**Design challenges — TODO**:

- **Redundancy logic problem**: Tripoli requires each system to independently trigger recovery. This means each FC must be able to independently release the pins. But if two independent servos can each release, the pin retention is only as strong as the weaker servo holding mechanism. Need a design where:
  - Either servo can independently release the pin (true redundancy)
  - But the pin cannot accidentally release under flight loads (vibration, G-forces)
  - And one servo failure does not jam the other servo's ability to release
- **Possible approaches (all need analysis)**:
  - Two pins per joint, each controlled by one servo — either pin removal destabilizes enough for separation, but both pins together handle flight loads
  - Single pin with two independent pull mechanisms (e.g., two cables to same pin, either can pull it)
  - Rotary latch with two independent release paths
  - Other mechanisms TBD
- **Pin structural requirements**: Pins must withstand aerodynamic loads, motor thrust loads, and vibration during boost without premature release. Shear strength analysis needed.
- **Spring force**: Must be sufficient to overcome friction and reliably push sections apart and deploy parachute at all expected altitudes (varying air density). Must be validated by ground testing.
- **Servo reliability**: Servo must reliably actuate in cold weather (Swedish winter conditions), under vibration, and after sustaining boost G-loads. Servo selection and testing critical.
- **Discuss with Rolf early**: Non-pyro separation is less common for L3. TAP approval of the concept is needed before detailed design.

### 4.3 Drogue Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Apogee detection (barometric) |
| Mechanism | Servo-actuated pin release + spring separation |
| Parachute | TBD size drogue |
| Descent rate under drogue | TBD m/s |
| Separation point | TBD |

### 4.4 Main Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Altitude-based (TBD meters AGL) |
| Mechanism | Servo-actuated pin release + spring separation |
| Parachute | TBD size main |
| Descent rate under main | TBD m/s (must not exceed 35 ft/s = 10.7 m/s per Tripoli rules) |
| Separation point | TBD |

### 4.5 Landing Velocity

| Parameter | Value |
|-----------|-------|
| Maximum allowed | 35 ft/s (10.7 m/s) per Tripoli TUSC |
| Expected landing velocity | TBD |
| Liftoff weight | TBD |
| Main parachute Cd | TBD |

### 4.6 Redundancy Architecture

Per Tripoli L3 rules: *"Dual redundant electronics are required for all recovery events. Two completely independent and separate electronic recovery systems must be incorporated. Neither system must adversely affect the other. Redundancy means completely separate systems, including batteries, switches, avionics, and energetics."*

Note: "energetics" in the Tripoli rules refers to ejection charges. With servo-actuated separation, the equivalent is the servo + pin + spring mechanism. Each system must independently be capable of triggering separation.

| Component | Primary System | Backup System |
|-----------|---------------|---------------|
| Flight computer | Custom FC (CATS Vega clone, improved) | CATS Vega (original) or second custom clone |
| Battery | Dedicated battery #1 | Dedicated battery #2 |
| Arming switch | Key switch #1 | Key switch #2 |
| Drogue release | Servo #1 → pin/mechanism | Servo #2 → pin/mechanism |
| Main release | Servo #3 → pin/mechanism | Servo #4 → pin/mechanism |

The two systems share no electrical connections. Each has independent power, switching, sensing, and servo output.

*TODO: Design the mechanical interface so that either servo can independently cause separation without the other. See section 4.2 design challenges.*

### 4.7 Motor Note

The M1350W-PS is a plugged motor — no motor ejection charge. All recovery depends entirely on the dual redundant electronic systems. There is no motor backup.

---

## 5. Recovery Electronics Schematic

*Per Tripoli L3 requirement 1.a.iii: "A wiring diagram that accurately reflects the wiring provided by the candidate from the power source, switches, and ejection charges."*

*Note: With servo-actuated separation, the wiring diagram shows servo connections instead of e-match/charge connections. Schematics of the actual flight computer internals are NOT required — only the wiring from power source, through switches, to the flight computers and servos.*

### 5.1 Wiring Diagram

*TODO: Create wiring diagram showing:*

- Battery #1 → Key switch #1 → Primary FC → Drogue servo #1 + Main servo #1
- Battery #2 → Key switch #2 → Backup FC → Drogue servo #2 + Main servo #2
- Physical separation between systems
- Servo connections (signal + power)
- Mechanical linkage to pins (conceptual)

### 5.2 Primary System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #1 (TBD V) | Key switch #1 |
| Switched power | Key switch #1 | Primary FC power input |
| Servo channel 1 | Primary FC drogue output | Servo #1 → drogue pin release |
| Servo channel 2 | Primary FC main output | Servo #3 → main pin release |

### 5.3 Backup System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #2 (TBD V) | Key switch #2 |
| Switched power | Key switch #2 | Backup FC power input |
| Servo channel 1 | Backup FC drogue output | Servo #2 → drogue pin release |
| Servo channel 2 | Backup FC main output | Servo #4 → main pin release |

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
- [ ] Separation mechanism fabrication and testing
- [ ] Electronics bay / nose cone electronics construction
- [ ] Dual flight computer installation and wiring
- [ ] Servo mechanism installation and testing
- [ ] Recovery harness assembly
- [ ] Parachute packing
- [ ] Spring preload and pin retention testing
- [ ] Final assembly
- [ ] Weight and CG measurements
- [ ] CP marking on airframe
- [ ] Ground test of electronics (both systems independently)
- [ ] Separation mechanism ground testing (both systems independently)

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
- [ ] Spare servos
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
- [ ] Install retention pins
- [ ] Verify pin engagement
- [ ] Connect servo mechanisms
- [ ] Connect primary FC wiring and servos
- [ ] Connect backup FC wiring and servos
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
| Primary electronics failure | Backup system actuates servos | Successful recovery |
| Backup electronics failure | Primary system actuates servos | Successful recovery |
| Both electronics fail | Design for reliability, ground test | Non-certification (ballistic descent) |
| Servo failure (single) | Redundant servo on other system releases same joint | Successful recovery |
| Servo failure (both on same joint) | Ground testing, servo selection, cold testing | Failed separation |
| Pin jammed | Design for clean release, lubrication, vibration testing | Failed separation |
| Spring insufficient | Ground testing at various temperatures, margin in spring force | Incomplete separation |
| Premature pin release (vibration/G) | Pin shear strength analysis, locking mechanism | Drag separation during boost |
| Fin flutter | Flutter analysis, carbon reinforcement, progressive test flights | Structural failure |
| Unstable flight | Stability analysis, CP/CG verification, OpenRocket sim | Unsafe flight |
| Parachute tangle | Proper packing, ground test | Failed recovery |

### 13.2 Risk Mitigation Through Testing

| Test | Purpose | When |
|------|---------|------|
| Separation mechanism bench test | Verify servo releases pin, spring separates sections | During construction |
| Redundancy test | Verify each system independently triggers separation | During construction |
| Cold temperature test | Verify servo and spring operation at expected launch temps | During construction |
| Vibration/shake test | Verify pins don't release under simulated flight loads | During construction |
| Flight #2 (J420R) | Validate airframe, electronics, separation mechanism | Before L flight |
| Flight #3 (L1000W) | Stress test at higher loads and speeds | Before M flight |
| Electronics ground test | Verify both systems detect apogee/altitude correctly | Before each flight |

### 13.3 Compliance

| Requirement | Compliance Method |
|-------------|------------------|
| Tripoli Unified Safety Code (TUSC) | Design review, simulation |
| FAR 101.25 | Altitude prediction within waiver |
| Waiver radius | Wind simulation, dual deploy for tight landing |
| Landing velocity ≤ 35 ft/s | Parachute sizing calculation |
| Dual redundant electronics | Two independent systems with independent servos |
| CP marked on rocket | External marking |

---

## Appendices

### A. OpenRocket Simulation Files

*TODO: Include .ork file or simulation output*

### B. OpenSCAD Design Files

*TODO: Include .scad source for fin can and fins*

### C. Thrust Curve Data

*TODO: Include M1350W RASP file from ThrustCurve.org*

### D. Material Datasheets

*TODO: Spectrum PC CF filament datasheet*

### E. Flight Computer Documentation

*TODO: Custom FC schematic, PCB layout, firmware overview*

### F. Separation Mechanism Design

*TODO: Detailed drawings of servo-actuated pin release mechanism, including:*

- Pin geometry and shear strength analysis
- Spring selection and force calculations
- Servo selection and torque requirements
- Redundancy solution (how either FC independently triggers release)
- Assembly and preload procedure

### G. Forms

- [Universal Certification Form (UCF)](https://www.tripoli.org/docs.ashx?id=859597)
- [Pre-Flight Data Capture Form](https://www.tripoli.org/docs.ashx?id=891494)
- [L2 to L3 Flight Log Form](https://www.tripoli.org/docs.ashx?id=1566254)
