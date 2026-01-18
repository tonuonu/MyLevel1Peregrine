# MyLevel1Peregrine Project Overview

## Launch Plan
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

## Key Rocket Specifications
- Length: 68.8" (175 cm)
- Diameter: 4.0" (98mm)
- Motor mount: 38mm (29mm with adapter)
- Weight: ~5+ lbs dry
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
- `docs/photos/` - Build photos with documentation (IMG_7726-7729 = packaging)
- `docs/decisions/` - Decision log entries (why Sweden, motor procurement, flight computer, etc.)
- `docs/references.md` - External links (Rocketry Forum threads, purchase source)
- `openrocket/` - .ork simulation files
- `mkdocs.yml` - Site configuration

## External Resources
- Rocketry Forum: Wally Ferrer build thread (Feb 2021) - detailed photos
- Rocketry Forum: Stability measurement thread - contains Peregrine.ork file
- OpenRocket displays rounded values; actual diameter is 10.16cm not 10.2cm
- Thingiverse #6780161: Motor retainer + rail guides
- CATS Vega: Open source flight computer (catsystems.io)