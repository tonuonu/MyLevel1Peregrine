# MyLevel1Peregrine Project Overview

## Status: L1 CERTIFIED ✓

Certification achieved 24 January 2026 at Enköping, Sweden. L2 written exam passed 27 January 2026.

## Certification Flight Summary
- **Date**: 24 January 2026
- **Location**: Enköping, Sweden (SMRK event)
- **Motor**: AeroTech H128W-14A
- **Altitude**: 140.8 m (predicted 208 m - extra weight from dual flight computers)
- **Recovery**: Motor ejection (pivoted from planned electronic dual-deploy due to cold weather)
- **Certifying Authority**: Rolf Örell (TRA# 3728, first European Tripoli Prefect)
- **Helpers**: Peter Steen, Anton Vannesjö

## Original Launch Plan
- **Date**: Saturday, 24 January 2026 (Sunday backup for weather)
- **Location**: Långtora Airfield, Sweden ([SMRK event](https://smrk.space/kalender/raketflygdag-langtora_20260124))
- **Motor**: AeroTech H128W (29mm, White Lightning) - purchased locally in Sweden

## Purpose
Documentation repository for a Tripoli Level 1 certification rocket build using the Apogee Peregrine dual deployment kit. Kit purchased from Sierra Fox Hobbies (Italy) - listed as L2 but L1 capable. Designed for CRO (Club Range Officer) review with calculations and formulas for verification, plus photo documentation of build methods to judge structural rigidity.

## Tech Stack
- **Documentation**: MkDocs with Material theme
- **Math rendering**: MathJax for LaTeX formulas
- **Diagrams**: Mermaid for flowcharts
- **Hosting**: GitHub Pages static site

## Rocket Configurations

| Config | Length | Recovery | Stability | Use |
|--------|--------|----------|-----------|-----|
| **L1** | 126 cm | Motor ejection | ~1.0 cal (with ballast) | Certification |
| **L2** | 175 cm | CATS Vega dual-deploy | 3.69 cal | After L1 cert |

## L1 Flight Configuration (Actual)
Based on certification form, flew full-length configuration:
- Length: 175 cm
- Diameter: 100 mm
- Liftoff weight: 2350 g
- CG: 115 cm from nose tip
- CP: 130 cm from nose tip
- Stability: ~1.5 calibers
- Motor: AeroTech H128W-14A
- Recovery: Motor ejection (pivoted from planned electronic dual-deploy)
- Delay: ~8s (14s factory - 8s drilled + 2s disk in tool)

## Key Rocket Specifications (Full L2)
- Length: 68.8" (175 cm)
- Diameter: 4.0" (102mm OD, 99.1mm ID)
- Motor mount: 38mm (29mm with adapter)
- Weight: ~1900g L2, ~2100g L1 (with ballast)
- Dual deployment capable

## Known Discrepancies (Packaging vs Website)
- Skill Level: packaging says 4, website says 3
- Height: packaging says "Over 65"", actual is 68.8"

## L2 Certification Planning
- **Target date**: 7 February 2026 (tentative, pending motor delivery)
- **Motor**: AeroTech J420R-14A ordered from Space Rocket Technology (Germany), shipping to Peter Steen in Sweden
- **Written exam**: Passed 27 January 2026, Certificate #2343
- **Hardware**: 38/720 and 29/180 casings purchased from Rolf Örell

## Motor Hardware
Purchased Aerotech reloadable casings from Rolf Örell:
- **38/720** — 38mm, 720 N-s max, for J motors (L2)
- **29/180** — 29mm, 180 N-s max, for H motors (L1)

## Transport Constraint
Tallink passenger ferries have blanket ban on dangerous substances. Contacted them directly - no procedure exists, no exceptions. Motors must be purchased/shipped within Sweden.

## Key Decisions
- **Why Sweden**: Daughter in Stockholm, boat discounts, local motor purchase, no ferry transport of motors
- **Flight computer**: CATS Vega (open source, Altium format)
- **Motor retainer**: 3D printed ASA from Thingiverse
- **Rail guides**: Kit 6.2mm buttons installed, 3D printed backup
- **Color**: Blue (Sipsik-themed for teaching daughters Liza 5 and Elsa 2)
- **Payload**: Small "Sipsik of Sipsik" flew on L1 - real doll too valuable to risk

## Structure
- `docs/` - MkDocs markdown content
- `docs/blog/` - Flight reports and updates
- `docs/certification/` - L1 certified, L2 planning
- `docs/configurations.md` - L1 vs L2 comparison
- `docs/photos/` - Build and flight photos, certificates
- `docs/decisions/` - Decision log entries
- `openrocket/` - Simulation files
  - `PeregrineL1.ork` - L1 configuration
  - `PeregrineL2.ork` - L2 configuration
- `openscad/` - 3D printable parts
  - `PeregrineNoseCone.scad` - Simple ballast-only nose cone
  - `PeregrineNoseConeElectronics.scad` - Nose cone with CATS Vega mount
  - `H128W.scad` - Mass dummy motor for ground testing
  - `J420R.scad` - Mass dummy motor for ground testing
- `mkdocs.yml` - Site configuration

## Mass Dummy Motors
PLA prints at 100% infill are 20-25% lighter than real motors. Drill 8mm hole and insert steel rod (~0.4 g/mm) for weight adjustment:
- H128W: 208g real weight, needs ~100-130mm rod
- J420R: 635g real weight, needs ~300-400mm rod

## External Resources
- Rocketry Forum: Wally Ferrer build thread (Feb 2021) - detailed photos
- Rocketry Forum: Stability measurement thread - contains Peregrine.ork file
- OpenRocket displays rounded values; actual diameter is 10.16cm not 10.2cm
- Thingiverse #6780161: Motor retainer + rail guides
- CATS Vega: Open source flight computer (catsystems.io)