# CLAUDE.md - Project Guidelines

This repository documents a Tripoli Level 1 certification rocket build using the Apogee Peregrine dual deployment kit.

## Repository Purpose

- Document rocket build for CRO (Club Range Officer) review
- Provide calculations with formulas for verification
- Store OpenRocket simulation files and results
- Maintain flight logs and checklists

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
│   ├── configurations.md   # L1 vs L2 config comparison
│   ├── specifications/     # Rocket specs
│   ├── construction/       # Build log
│   ├── calculations/       # Formulas and calculations
│   ├── simulations/        # OpenRocket results
│   ├── decisions/          # Design decisions and rationale
│   ├── flight/             # Checklists and logs
│   └── photos/             # Images
├── openrocket/             # .ork simulation files
├── openscad/               # 3D printable parts (nose cone, etc.)
├── mkdocs.yml              # Site configuration
└── CLAUDE.md               # This file
```

## Building the Documentation

```bash
# Install MkDocs with Material theme
pip install mkdocs-material

# Serve locally
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## Key Specifications (Apogee Peregrine)

- Length: 68.8" (175 cm) full L2 config, 126 cm L1 config
- Diameter: 4.0" (102mm OD, 99.1mm ID)
- Motor mount: 38mm (29mm with adapter)
- Weight: ~1900g L2, ~2100g L1 (with ballast)
- Dual deployment capable

## Configurations

| Config | Length | Recovery | Electronics |
|--------|--------|----------|-------------|
| **L1** | 126 cm | Motor ejection | None (nose ballast for stability) |
| **L2** | 175 cm | Dual-deploy | CATS Vega flight computer |

## L1 Flight Parameters (H128W motor, 180cm rail)

- Rail exit velocity: 16.6 m/s ✓
- Stability at rail exit: 1.0 caliber ✓
- Thrust-to-weight: 5.6:1 ✓
- Apogee: ~235m

## Conventions

- All measurements in metric (imperial retained only when from original source)
- Formulas shown with variable definitions
- Photos named descriptively: `YYYYMMDD-description.jpg`
- Flight data recorded with altimeter downloads
