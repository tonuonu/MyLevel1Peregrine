# External References

## Kit Purchase

Purchased from [Sierra Fox Hobbies](https://www.sierrafoxhobbies.com/en/high-power-rockets/2109-peregrine-hpr-apogee.html) (Italy) - listed as L2 kit but also L1 capable (flies on H motors). Was the only kit in stock from their [HPR selection](https://www.sierrafoxhobbies.com/en/19-high-power-rockets).

## Community Resources and discussions related to the Apogee Peregrine.

## Rocketry Forum Threads

### Build Threads

- [Apogee Peregrine Build](https://www.rocketryforum.com/threads/apogee-peregrine-build.164948/) - Wally Ferrer (Feb 2021)
    - Detailed photo documentation of complete build
    - Tips: CA glue on tube edges, Kevlar string method for centering ring removal
    - Rocketpoxy fillet technique with fondant ball
    - Badass Rocketry fin guides mentioned

### Technical Discussions

- [Trying to find an OpenRocket file for the Apogee Peregrine](https://www.rocketryforum.com/threads/trying-to-find-an-openrocket-file-for-the-apogee-peregrine.166457/) - laxmax51 (May 2021)
    - Discussion about importing RockSim .rkt files into OpenRocket
    - **Key tip**: OpenRocket can open RockSim .rkt files directly, then save as .ork
    - Note: Fancy fin shapes may not import perfectly

- [Stability measurement as a caliber or as a percentage](https://www.rocketryforum.com/threads/stability-measurement-as-a-caliber-or-as-a-percentage.177665/) - MetricRocketeer (Jan 2023)
    - Discusses caliber vs percentage stability display in OpenRocket
    - **Contains Peregrine.ork file** shared by user
    - Explains apparent CP/CG calculation discrepancies are due to OpenRocket rounding display values
    - Actual values: diameter 10.16cm (not 10.2cm), CG 113.79cm, CP 130.25cm

!!! note "OpenRocket Rounding"
    OpenRocket displays rounded values but calculates with full precision. This explains why manual calculations from displayed values may not match the stability shown.

!!! tip "RockSim to OpenRocket"
    OpenRocket is **free open-source software** that can import RockSim .rkt files directly. Apogee provides RockSim files for their kits - these can be opened in OpenRocket and saved as .ork files. Fin shapes may need minor cleanup after import.

## Flight Electronics

- [CATS Vega](https://www.catsystems.io/vega) - Open source flight computer (ordered)
- [CATS Ground Station](https://www.catsystems.io/ground-station-1) - Telemetry receiver (ordered)

## 3D Printed Parts

- [38mm Motor Retainer + Rail Guides](https://www.thingiverse.com/thing:6780161) - Thingiverse model for motor retention (printed in ASA) and backup rail guides

## Motors

### H128W (L1 Certification)

- [AeroTech H128W on ThrustCurve](https://www.thrustcurve.org/motors/AeroTech/H128W/) - Technical specs, thrust curve data

| Spec | Value |
|------|-------|
| Diameter | 29mm |
| Total Impulse | 172.9 Ns |
| Avg Thrust | 128 N |
| Burn Time | 1.3 s |
| Propellant | White Lightning |
| Case | RMS-29/180 |
| Total Mass | 208 g |

### J420R (L2 Certification)

- [AeroTech J420R on ThrustCurve](https://www.thrustcurve.org/motors/AeroTech/J420R/) - Technical specs, thrust curve data
- [Space Rocket Technology Shop](https://www.spacerockettechnology-shop.de/en/J420R-14A.html) - German retailer

| Spec | Value |
|------|-------|
| Diameter | 38mm |
| Total Impulse | 658 Ns |
| Avg Thrust | 420 N |
| Burn Time | 1.6 s |
| Propellant | Redline |
| Case | RMS-38/720 |
| Total Mass | 635 g |

!!! note "Motor Classifications"
    - **H class**: 160-320 Ns total impulse
    - **J class**: 640-1280 Ns total impulse
    - **EU Pyrotechnics**: P2 (requires specialist knowledge)

## Launch Events

- [SMRK - Svenska ModellRaketKlubben](https://smrk.space/) - Swedish Model Rocket Club
- [Raketflygdag Långtora 24 Jan 2026](https://smrk.space/kalender/raketflygdag-langtora_20260124) - L1 certification flight

## Certification

- [Tripoli Rocketry Association](https://www.tripoli.org/) - Certification organization
- [Tripoli Lifetime Members](https://tripoli.clubexpress.com/content.aspx?page_id=22&club_id=795696&module_id=494497) - Includes Rolf Örell (TRA# 3728), first European Tripoli Prefect

## Manufacturer Resources

- [Apogee Components - Peregrine Product Page](https://www.apogeerockets.com/Rocket-Kits/Skill-Level-3-Kits/Peregrine)
- [Peregrine Instruction Manual (PDF)](https://www.apogeerockets.com/downloads/PDFs/04998-Peregrine-instructs.pdf) - Official assembly instructions
- [Apogee Peak of Flight Newsletter](https://www.apogeerockets.com/education/newsletter)

## Regulatory

- [EU Directive 2013/29/EU](https://eur-lex.europa.eu/eli/dir/2013/29/oj) - Pyrotechnic articles regulation (P1/P2 categories)

## Related Threads

- Completing the trifecta: the Apogee Peregrine coming together (novahobbies, Jul 2025)
- Apogee Nike-Hercules build thread (spullen, Nov 2024)
- "455" - Apogee Zephyr for TRA Level 1 (MikeMcP, Nov 2025)
