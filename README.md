# Peregrine L1

Documentation for my Tripoli Level 1 certification attempt using the Apogee Peregrine dual deployment rocket.

**📖 Documentation Site: [tonuonu.github.io/MyLevel1Peregrine](https://tonuonu.github.io/MyLevel1Peregrine/)**

## Quick Info

| | |
|---|---|
| **Rocket** | Apogee Peregrine |
| **Motor** | AeroTech H128W (29mm) |
| **Launch Date** | 24 January 2026 |
| **Location** | Långtora, Sweden ([SMRK](https://smrk.space/)) |
| **Tripoli #** | 38105 |

## Repository Contents

- `docs/` — MkDocs documentation source
- `openrocket/` — OpenRocket simulation files
- `openscad/` — 3D printable parts (nose cone with CATS Vega mount)
- `.github/workflows/` — CI for automatic deployment

## L1 Configuration

Flying in simplified configuration for certification:
- Shortened airframe (126cm vs 175cm full length)
- Motor ejection (no electronics)
- Nose ballast (~600g epoxy) for stability
- Single 48" main parachute

**Flight Parameters:**
- Rail exit velocity: 16.6 m/s (180cm rail)
- Stability: 1.0 caliber
- Expected apogee: ~235m

## Documentation Sections

- **Certification** — Tripoli membership, L1 requirements
- **Specifications** — Rocket specs, kit contents, dimensions
- **Construction** — Build log, motor mount, fins, e-bay
- **Calculations** — Stability, ejection charges, vent holes
- **Simulations** — OpenRocket results, motor selection
- **Decisions** — Technical choices and reasoning

## Local Development

```bash
# Install MkDocs
brew install mkdocs
brew install mkdocs-material

# Serve locally
mkdocs serve

# View at http://127.0.0.1:8000/MyLevel1Peregrine/
```

## Author

[Tõnu Samuel](https://www.linkedin.com/in/tonusamuel/) — Tallinn, Estonia
