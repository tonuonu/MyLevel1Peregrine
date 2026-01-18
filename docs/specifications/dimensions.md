# Dimensions

## Overall Dimensions

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  ◄──────────────────────── 68.8" (175 cm) ────────────────────────────► │
│                                                                         │
│     ╭──────╮                                                            │
│    ╱        ╲    ┌──────────────────────────────────────────┐   ╲      │
│   ╱   NOSE   ╲   │              BODY TUBE                   │    ╲╲╲   │
│   ╲   CONE   ╱   │              + E-BAY                     │    ╱╱╱   │
│    ╲        ╱    └──────────────────────────────────────────┘   ╱      │
│     ╰──────╯                                                            │
│                                                                         │
│  ◄── 19.8" ──►   ◄─────────────────────────────────────────────────►   │
│   (exposed)                                                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

                              ◄── 4.0" (98mm) ──►
                                  (diameter)
```

## Detailed Measurements

| Dimension | Imperial | Metric |
|-----------|----------|--------|
| Total Length | 68.8" | 175 cm |
| Body Diameter (OD) | 4.0" | 98mm |
| Nose Cone (exposed) | 19.8" | 50 cm |
| Nose Cone Shape | 5:1 Ogive | - |
| Motor Tube (ID) | 38mm | - |
| Motor Tube Length | 11" | 28 cm |

## Fin Dimensions

The Peregrine features distinctive swept-back curved fins that extend below the body tube base.

!!! info "Fin Geometry"
    The curved fin profile requires freeform or spline definition in OpenRocket.
    RockSim file from Apogee contains accurate fin geometry.

| Parameter | Value |
|-----------|-------|
| Fin Count | 3 |
| Material | Birch plywood |
| Attachment | Through-the-wall (TTW) |
| Extends Below Tube | Yes |

## Electronics Bay Dimensions

| Dimension | Value |
|-----------|-------|
| E-Bay Diameter | 98mm (4") |
| Coupler OD | Fits 98mm body tube |
| Sled Width | Fits inside coupler |

## Recovery Bay Volumes

These volumes are important for calculating ejection charges:

| Bay | Location | Notes |
|-----|----------|-------|
| Drogue Bay | Forward (nose to e-bay) | 18" drogue + protector |
| Main Bay | Aft (e-bay to fins) | 48" main + protector |

!!! note "Volume Calculation"
    Use RockSim or OpenRocket to calculate exact bay volumes.
    See [Ejection Charges](../calculations/ejection-charges.md) for charge sizing.
