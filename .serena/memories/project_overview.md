# MyLevel1Peregrine Project Overview

## Purpose
Documentation repository for a Tripoli Level 1 certification rocket build using the Apogee Peregrine dual deployment kit. Kit purchased from Sierra Fox Hobbies (Spain) - listed as L2 but L1 capable. Designed for CRO (Club Range Officer) review with calculations and formulas for verification.

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

## Structure
- `docs/` - MkDocs markdown content
- `docs/photos/` - Build photos with documentation (IMG_7726-7729 = packaging)
- `docs/references.md` - External links (Rocketry Forum threads, purchase source)
- `openrocket/` - .ork simulation files
- `mkdocs.yml` - Site configuration

## External Resources
- Rocketry Forum: Wally Ferrer build thread (Feb 2021) - detailed photos
- Rocketry Forum: Stability measurement thread - contains Peregrine.ork file
- OpenRocket displays rounded values; actual diameter is 10.16cm not 10.2cm