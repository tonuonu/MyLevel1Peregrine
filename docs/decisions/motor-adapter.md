# Motor Adapter (38mm to 29mm)

## Context

Peregrine motor mount is 38mm diameter. Selected motor (AeroTech H128W) is 29mm diameter.

Need an adapter to center the 29mm motor in the 38mm tube.

## Decision

3D printed clamshell adapter from [Thingiverse Thing:5971997](https://www.thingiverse.com/thing:5971997)

## Implementation

| Parameter | Value |
|-----------|-------|
| Design | Clamshell (two halves) |
| Material | Translucent PETG |
| Printer | Bambu Lab P1S |
| Infill | TBD |
| Layer height | TBD |

## Material Selection: PETG vs ASA

**Preferred material would be ASA** (better heat resistance, UV stable), but:

!!! warning "Printer Limitation"
    Bambu Lab P1S lacks chamber heating. Tall ASA prints warp and fail ("spaghetti") after reaching certain height without enclosure temperature control.

**PETG characteristics:**

- Adequate temperature resistance for adapter (not in exhaust path)
- Prints reliably without heated chamber
- Translucent allows visual inspection of motor position
- Sufficient strength for centering function

## Clamshell Design Benefits

- Two-piece design simplifies installation/removal
- No need to slide motor through adapter
- Can inspect motor centering before flight
- Easy to replace if damaged

## Photos

*To be added*
