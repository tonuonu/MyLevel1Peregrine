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
│   ├── specifications/     # Rocket specs
│   ├── construction/       # Build log
│   ├── calculations/       # Formulas and calculations
│   ├── simulations/        # OpenRocket results
│   ├── flight/             # Checklists and logs
│   └── photos/             # Images
├── openrocket/             # .ork simulation files
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

- Length: 68.8" (175 cm)
- Diameter: 4.0" (98mm)
- Motor mount: 38mm (29mm with adapter)
- Weight: ~5+ lbs dry
- Dual deployment capable

## Conventions

- All measurements in metric (imperial retained only when from original source)
- Formulas shown with variable definitions
- Photos named descriptively: `YYYYMMDD-description.jpg`
- Flight data recorded with altimeter downloads
