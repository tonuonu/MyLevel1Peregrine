# CLAUDE.md - Project Guidelines

This repository documents a Tripoli Level 1 certification rocket build using the Apogee Peregrine dual deployment kit.

**Status: L1 CERTIFIED** ✓ — 24 January 2026

## Repository Purpose

- Document rocket build for CRO (Club Range Officer) review
- Provide calculations with formulas for verification
- Store OpenRocket simulation files and results
- Maintain flight logs and checklists
- Track L2 certification progress

## Documentation System

- **Framework**: MkDocs with Material theme
- **Math**: MathJax for LaTeX formulas
- **Diagrams**: Mermaid for flowcharts
- **Output**: GitHub Pages static site

## File Structure

```
MyLevel1Peregrine/
├── docs/                    # MkDocs content
│   ├── index.md            # Home page
│   ├── blog/               # Flight reports and updates
│   ├── certification/      # L1 certified, L2 planning
│   ├── configurations.md   # L1 vs L2 config comparison
│   ├── specifications/     # Rocket specs
│   ├── construction/       # Build log
│   ├── calculations/       # Formulas and calculations
│   ├── simulations/        # OpenRocket results
│   ├── decisions/          # Design decisions and rationale
│   ├── flight/             # Checklists and logs
│   └── photos/             # Images and certificates
├── openrocket/             # .ork simulation files
│   ├── PeregrineL1.ork
│   └── PeregrineL2.ork
├── openscad/               # 3D printable parts
│   ├── PeregrineNoseCone*.scad
│   ├── H128W.scad          # Mass dummy motor
│   └── J420R.scad          # Mass dummy motor
├── mkdocs.yml              # Site configuration
└── CLAUDE.md               # This file
```

## Building the Documentation

```bash
# Install MkDocs with Material theme
pip install mkdocs-material --break-system-packages

# Serve locally
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages (handled by CI)
mkdocs gh-deploy
```

## Key Specifications (Apogee Peregrine)

- Length: 175 cm
- Diameter: 100 mm (4.0")
- Motor mount: 38mm (29mm with adapter)
- Flight computer: CATS Vega
- Rocket name: SIPSIK

## L1 Certification Flight (24 January 2026)

| Parameter | Value |
|-----------|-------|
| Location | Enköping, Sweden |
| Motor | AeroTech H128W-14A |
| Liftoff weight | 2350 g |
| Altitude | 140.8 m |
| Recovery | Motor ejection |
| Certifying Authority | Rolf Örell (TRA# 3728) |

## L2 Certification (In Progress)

- Written exam: Passed (27 Jan 2026)
- Target flight: 7 February 2026 (tentative)
- Motor: AeroTech J420R-14A (ordered)

## Motor Hardware

Aerotech reloadable casings (purchased from Rolf Örell):
- **38/720** — J motors
- **29/180** — H motors

## Mass Dummy Motors

3D printed PLA at 100% infill, with 8mm hole for steel rod weight adjustment:
- H128W: 208g target
- J420R: 635g target

## Conventions

- All measurements in metric
- Formulas shown with variable definitions
- Flight data recorded with altimeter downloads
- Photos: `YYYYMMDD-description.jpg` or descriptive names
