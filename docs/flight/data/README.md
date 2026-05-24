# Flight Data — Workflow

This directory holds raw CATS Vega flight logs and the tools to turn them into charts and analysis numbers. The workflow is designed so that **next time a flight is logged, conversion just works** — no format re-discovery needed.

## Files

| File | Purpose |
|------|---------|
| `flXXX.cfl` | Raw binary flight log from CATS Vega (downloaded over USB) |
| `stXXX.txt` | CATS Configurator stats export — ground-truth max values |
| `CATS_FORMAT.md` | **Binary format specification** (read this before changing the parser) |
| `generate_charts.py` | Parser + chart generator. Strict; stops cleanly on unknown record types |
| `flXXX.summary.json` | Auto-generated per-flight summary (parser output) |
| `readme.txt` | Upstream CATS Configurator notice |

## Downloading a flight log from CATS Vega

1. Connect the CATS Vega to a computer via USB while pressing the boot button (puts it in Mass Storage Controller mode)
2. The device exposes the flash filesystem — copy `flXXX.cfl` and `stXXX.txt` for the flight(s) of interest
3. Drop both files into this directory

Up to 50 flight logs and 50 stats files are exposed per the firmware limit.

## Generating charts and analysis

```bash
cd docs/flight/data/
python generate_charts.py flXXX.cfl ../flightN_charts.png \
    --motor "AeroTech XYZ" \
    --title "Flight #N — L? Certification" \
    --json flXXX.summary.json
```

The script prints flight summary numbers (apogee, max velocity, max accel, FSM transitions) to stdout and writes the chart PNG and a JSON summary. Cross-check the JSON against `stXXX.txt` — they should agree to within rounding.

## Reproducing past flights

```bash
# L1 (Flight #1, 24 January 2026, AeroTech H128W-14A)
python generate_charts.py fl001.cfl ../flight1_charts.png \
    --motor "AeroTech H128W-14A" --title "Flight #1 — L1 Certification" \
    --json fl001.summary.json

# L2 (Flight #2, 22 February 2026, AeroTech J350)
python generate_charts.py fl002.cfl ../flight2_charts.png \
    --motor "AeroTech J350" --title "Flight #2 — L2 Certification" \
    --json fl002.summary.json
```

Expected output (verified against `stXXX.txt`):

| Flight | Apogee | Max velocity | Max accel |
|--------|--------|--------------|-----------|
| #1 (L1) | 141.58 m | 46.24 m/s | 4.5 g |
| #2 (L2) | 986.43 m | 172.56 m/s | 17.5 g |

## When the parser breaks

If `generate_charts.py` reports `Unknown rec_type_raw=0x…` and stops before the end of the file:

1. The CATS firmware has added or changed a record type
2. Read `CATS_FORMAT.md` for the format model
3. Find the new type definition in [catsystems/cats-embedded `recorder.hpp`](https://github.com/catsystems/cats-embedded/blob/main/flight_computer/src/flash/recorder.hpp)
4. Add an entry to the `RECORDS` dict in `generate_charts.py` (name, payload size, struct format string)
5. **Also update `CATS_FORMAT.md`** — that file is the spec, not a docstring

**Do NOT** make the parser slide bytes on unknown types. That hides the problem and produces silent garbage downstream — see `tasks/lessons.md` for the history.

## Format reference

See [`CATS_FORMAT.md`](CATS_FORMAT.md) for the complete binary format spec, FSM state enum, and hardware notes. That file is the authoritative reference — kept separate from any script so it cannot be erased by an accidental docstring edit.
