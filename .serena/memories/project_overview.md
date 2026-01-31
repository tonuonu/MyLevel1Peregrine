# MyLevel1Peregrine Project Overview

## Status: L1 CERTIFIED ✓

Certification achieved 22 January 2026 at Enköping, Sweden. L2 written exam passed 27 January 2026.

## Certification Flight Summary
- **Date**: 22 January 2026
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

## L1 Configuration Details
- Shortened airframe (no e-bay section)
- Nose ballast required (~600g epoxy) for stability
- Motor: AeroTech H128W-14
- Rail: 180cm minimum
- Rail exit velocity: 16.6 m/s ✓
- Stability at exit: 1.0 cal ✓
- Thrust-to-weight: 5.6:1 ✓
- Expected apogee: ~235m

## Key Rocket Specifications (Full L2)
- Length: 68.8" (175 cm)
- Diameter: 4.0" (102mm OD, 99.1mm ID)
- Motor mount: 38mm (29mm with adapter)
- Weight: ~1900g L2, ~2100g L1 (with ballast)
- Dual deployment capable

## Known Discrepancies (Packaging vs Website)
- Skill Level: packaging says 4, website says 3
- Height: packaging says "Over 65"", actual is 68.8"

## Key Decisions
- **Why Sweden**: Daughter in Stockholm, boat discounts, local motor purchase
- **Flight computer**: CATS Vega ordered (open source, Altium format) - may use motor delay if doesn't arrive
- **Motor retainer**: 3D printed ASA from Thingiverse
- **Rail guides**: Kit 6.2mm buttons installed, 3D printed backup
- **Color**: Blue (Sipsik-themed for teaching daughters Liza 5 and Elsa 2)
- **Payload**: Plan to fly Sipsik toy (packaging TBD)

## Structure
- `docs/` - MkDocs markdown content
- `docs/configurations.md` - L1 vs L2 comparison
- `docs/photos/` - Build photos with documentation
- `docs/decisions/` - Decision log entries
- `openrocket/` - .ork simulation files (PeregrineL1.ork)
- `openscad/` - 3D printable parts
  - `PeregrineNoseCone.scad` - Simple ballast-only nose cone
  - `PeregrineNoseConeElectronics.scad` - Nose cone with CATS Vega mount
- `mkdocs.yml` - Site configuration

## External Resources
- Rocketry Forum: Wally Ferrer build thread (Feb 2021) - detailed photos
- Rocketry Forum: Stability measurement thread - contains Peregrine.ork file
- OpenRocket displays rounded values; actual diameter is 10.16cm not 10.2cm
- Thingiverse #6780161: Motor retainer + rail guides
- CATS Vega: Open source flight computer (catsystems.io)