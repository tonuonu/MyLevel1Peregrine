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
| Recovery | Dual deploy, dual redundant electronics |
| Expected altitude | TBD |
| Number of fins | TBD |
| Fin material | Spectrum PC CF (3D printed polycarbonate + carbon fiber) |

### 1.3 Design Philosophy

- Minimum motor class (barely M at 5178 N-s) to keep velocities and forces manageable
- Progressive flight testing on J and L motors before cert flight
- 3D printed fin can in PC CF with carbon rod reinforcement for flutter resistance
- Dual redundant electronics as required by Tripoli L3 rules
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

### 2.2 Body Tube

| Parameter | Value |
|-----------|-------|
| Material | TBD |
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
| Location | TBD (typically mid-body between recovery sections) |
| Length | TBD |
| Sled material | TBD |
| Switch access | External key switches (2×, one per system) |
| Charge wells | 4× (2 drogue + 2 main, one per system) |

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
| Body tube | TBD | TBD | TBD |
| Nose cone | TBD | 1 | TBD |
| Fin can body (printed) | Spectrum PC CF | 1 set | Printed by candidate |
| Fins (printed) | Spectrum PC CF | TBD | Printed by candidate |
| Carbon reinforcement rods | 2.0mm carbon rod | TBD | TBD |
| Centering rings | TBD | TBD | TBD |
| Motor mount tube | 75mm ID | 1 | TBD |
| Motor retainer | TBD | 1 | TBD |
| E-bay sled | TBD | 1 | TBD |
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
| Shear pins | TBD | TBD | TBD |
| Ejection charges (BP) | TBD grams each | 4 (2 per system) | TBD |

### 3.3 Electronics

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| Primary flight computer | Custom (CATS Vega-based) | 1 | Built by candidate |
| Backup flight computer | TBD | 1 | TBD |
| Battery (primary) | TBD | 1 | TBD |
| Battery (backup) | TBD | 1 | TBD |
| Key switch (primary) | TBD | 1 | TBD |
| Key switch (backup) | TBD | 1 | TBD |
| E-matches / igniters | TBD | 4 | TBD |

### 3.4 Motor

| Item | Specification | Quantity | Source |
|------|--------------|----------|--------|
| AeroTech M1350W-PS | 75mm single-use DMS | 1 | TBD (requires L3 to purchase — sourced via TAP) |

---

## 4. Recovery System

*Per Tripoli L3 recovery requirements: parachute recovery required, dual deployment allowed with apogee destabilization event*

### 4.1 Recovery Architecture

Dual deployment with dual redundant electronics:

| Event | Altitude | Device | Action |
|-------|----------|--------|--------|
| Apogee | Apogee detection | Primary FC + Backup FC | Drogue parachute deployment |
| Main | TBD (e.g., 300m AGL) | Primary FC + Backup FC | Main parachute deployment |

### 4.2 Drogue Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Apogee detection (barometric) |
| Parachute | TBD size drogue |
| Descent rate under drogue | TBD m/s |
| Separation point | TBD |
| Charge size | TBD grams BP (×2, one per system) |

### 4.3 Main Deployment

| Parameter | Value |
|-----------|-------|
| Trigger | Altitude-based (TBD meters AGL) |
| Parachute | TBD size main |
| Descent rate under main | TBD m/s (must not exceed 35 ft/s = 10.7 m/s per Tripoli rules) |
| Separation point | TBD |
| Charge size | TBD grams BP (×2, one per system) |

### 4.4 Landing Velocity

| Parameter | Value |
|-----------|-------|
| Maximum allowed | 35 ft/s (10.7 m/s) per Tripoli TUSC |
| Expected landing velocity | TBD |
| Liftoff weight | TBD |
| Main parachute Cd | TBD |

### 4.5 Redundancy Architecture

Per Tripoli L3 rules: *"Dual redundant electronics are required for all recovery events. Two completely independent and separate electronic recovery systems must be incorporated. Neither system must adversely affect the other. Redundancy means completely separate systems, including batteries, switches, avionics, and energetics."*

| Component | Primary System | Backup System |
|-----------|---------------|---------------|
| Flight computer | Custom FC #1 | TBD (Custom FC #2 or commercial) |
| Battery | Dedicated battery #1 | Dedicated battery #2 |
| Arming switch | Key switch #1 | Key switch #2 |
| Drogue charge | Charge #1 | Charge #2 |
| Main charge | Charge #3 | Charge #4 |

The two systems share no electrical connections. Each has independent power, switching, sensing, and pyro output.

### 4.6 Motor Note

The M1350W-PS is a plugged motor — no motor ejection charge. All recovery depends entirely on the dual redundant electronic systems. There is no motor backup.

---

## 5. Recovery Electronics Schematic

*Per Tripoli L3 requirement 1.a.iii: "A wiring diagram that accurately reflects the wiring provided by the candidate from the power source, switches, and ejection charges."*

*Note: Schematics of the actual flight computer internals are NOT required — only the wiring from power source, through switches, to the flight computers and ejection charges.*

### 5.1 Wiring Diagram

*TODO: Create wiring diagram showing:*

- Battery #1 → Key switch #1 → Primary FC → Drogue charge #1 + Main charge #1
- Battery #2 → Key switch #2 → Backup FC → Drogue charge #2 + Main charge #2
- Physical separation between systems
- E-match connections
- Charge well layout

### 5.2 Primary System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #1 (TBD V) | Key switch #1 |
| Switched power | Key switch #1 | Primary FC power input |
| Pyro channel 1 | Primary FC drogue output | E-match → drogue charge #1 |
| Pyro channel 2 | Primary FC main output | E-match → main charge #1 |

### 5.3 Backup System

| Connection | From | To |
|-----------|------|-----|
| Power | Battery #2 (TBD V) | Key switch #2 |
| Switched power | Key switch #2 | Backup FC power input |
| Pyro channel 1 | Backup FC drogue output | E-match → drogue charge #2 |
| Pyro channel 2 | Backup FC main output | E-match → main charge #2 |

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
| Rating | Must retain motor under full thrust + ejection loads |

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
- [ ] Electronics bay construction
- [ ] E-bay sled with dual flight computers
- [ ] Wiring of dual redundant systems
- [ ] Recovery harness assembly
- [ ] Parachute packing
- [ ] Final assembly
- [ ] Weight and CG measurements
- [ ] CP marking on airframe
- [ ] Ground test of electronics
- [ ] Ejection charge ground testing

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
- [ ] Ejection charges prepared (4×: 2 drogue + 2 main)
- [ ] E-matches (4×)
- [ ] Batteries charged (2×, one per system)
- [ ] Key switches and keys (2×)
- [ ] Tools for field assembly
- [ ] Recovery wadding / Nomex protectors

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
- [ ] Install ejection charges (4×)
- [ ] Install e-matches in charges
- [ ] Connect primary FC wiring
- [ ] Connect backup FC wiring
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
| Primary electronics failure | Backup system fires charges | Successful recovery |
| Backup electronics failure | Primary system fires charges | Successful recovery |
| Both electronics fail | Design for reliability, ground test | Non-certification (ballistic descent) |
| Fin flutter | Flutter analysis, carbon reinforcement, progressive test flights | Structural failure |
| Unstable flight | Stability analysis, CP/CG verification, OpenRocket sim | Unsafe flight |
| Parachute tangle | Proper packing, Nomex protectors, ground test | Failed recovery |
| Shear pin failure (premature separation) | Correct shear pin sizing, ground test | Drag separation |
| Ejection charge insufficient | Ground test charges, calculate volume | Failed deployment |
| Ejection charge excessive | Ground test charges, calculate volume | Structural damage |

### 13.2 Risk Mitigation Through Testing

| Test | Purpose | When |
|------|---------|------|
| Flight #2 (J420R) | Validate airframe, electronics, recovery | Before L flight |
| Flight #3 (L1000W) | Stress test at higher loads and speeds | Before M flight |
| Ejection charge ground test | Verify charge sizes separate rocket | Before each flight |
| Electronics ground test | Verify both systems detect apogee/altitude correctly | Before each flight |

### 13.3 Compliance

| Requirement | Compliance Method |
|-------------|------------------|
| Tripoli Unified Safety Code (TUSC) | Design review, simulation |
| FAR 101.25 | Altitude prediction within waiver |
| Waiver radius | Wind simulation, dual deploy for tight landing |
| Landing velocity ≤ 35 ft/s | Parachute sizing calculation |
| Dual redundant electronics | Two independent systems |
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

### F. Forms

- [Universal Certification Form (UCF)](https://www.tripoli.org/docs.ashx?id=859597)
- [Pre-Flight Data Capture Form](https://www.tripoli.org/docs.ashx?id=891494)
- [L2 to L3 Flight Log Form](https://www.tripoli.org/docs.ashx?id=1566254)
