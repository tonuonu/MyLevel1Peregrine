# Peregrine L1

**L1 CERTIFIED** ✓ — 24 January 2026, Enköping, Sweden

Documentation for my Tripoli Level 1 certification using the Apogee Peregrine dual deployment rocket, named **SIPSIK** after the beloved Estonian cartoon character.

**📖 Documentation Site: [tonuonu.github.io/MyLevel1Peregrine](https://tonuonu.github.io/MyLevel1Peregrine/)**

## L1 Certification Flight

| | |
|---|---|
| **Date** | 24 January 2026 |
| **Location** | Enköping, Sweden (SMRK) |
| **Motor** | AeroTech H128W-14A |
| **Altitude** | 140.8 m |
| **Recovery** | Motor ejection, single chute |
| **Certifying Authority** | Rolf Örell (TRA# 3728) |
| **Result** | **CERTIFIED** |

## Next: L2 Certification

| | |
|---|---|
| **Written Exam** | ✅ Passed (27 Jan 2026) |
| **Target Flight** | 7 February 2026 (tentative) |
| **Motor** | AeroTech J420R-14A (ordered) |

## Repository Contents

- `docs/` — MkDocs documentation source
- `openrocket/` — OpenRocket simulation files (.ork)
- `openscad/` — 3D printable parts:
  - Nose cone with CATS Vega mount
  - Motor retainer
  - Mass dummy motors (H128W, J420R) for ground testing
- `.github/workflows/` — CI for automatic deployment

## Rocket Specs

| | |
|---|---|
| **Kit** | Apogee Peregrine |
| **Length** | 175 cm |
| **Diameter** | 100 mm |
| **Motor mount** | 38mm (29mm with adapter) |
| **Flight computer** | CATS Vega |
| **Tripoli #** | 38105 |

## Hardware

Motor casings purchased from Rolf Örell:
- **38/720** — J motors (L2 certification)
- **29/180** — H motors (L1 class)

## The Story

This blue rocket teaches my daughters Liza (5) and Elsa (2) real engineering through the Estonian cartoon character Sipsik. In the cartoon, siblings build a cardboard rocket to send their toy to the moon. Now we're doing it for real.

A small "Sipsik of Sipsik" flew on the L1 certification flight — the real doll was too valuable to risk.

## Local Development

```bash
# Install MkDocs
brew install mkdocs
pip install mkdocs-material --break-system-packages

# Serve locally
mkdocs serve

# View at http://127.0.0.1:8000/MyLevel1Peregrine/
```

## Author

[Tõnu Samuel](https://www.linkedin.com/in/tonusamuel/) — Tallinn, Estonia
