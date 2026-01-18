# Flight Computer

## Context

Dual deployment requires electronic altimeter to fire ejection charges at correct altitudes. Alternative is single deployment using motor delay.

## Equipment Ordered

- [CATS Vega](https://www.catsystems.io/vega) - Flight computer
- [CATS Ground Station](https://www.catsystems.io/ground-station-1) - Telemetry receiver

### Why CATS

Fully **Open Source** - hardware designs in Altium format. This fits my background perfectly. Could copy designs and order own PCBs, but purchased to support the project.

### Shipping Status

Package shipping from Switzerland, may arrive too late for 24 Jan launch.

- [Swiss Post tracking](https://service.post.ch/ekp-web/ui/list/detail/6vP0B2MCKrAQ1l95htrmWZBZApVbTksjexEmzQ90saKFDkRfnZzFLA)
- [Omniva tracking (Estonia)](https://minu.omniva.ee/track/LA055535535CH)

## Decision: Pending

### Option A: Motor Delay (Simple)

Single chute deployment using motor ejection delay. Often recommended for L1 certification to keep it failproof.

**Pros:**

- Simpler, fewer failure modes
- Traditional L1 approach
- No electronics dependency

### Option B: Electronic Dual Deployment

Use CATS Vega for drogue at apogee, main at lower altitude.

**Pros:**

- Closer-to-pad recovery (what Peregrine is designed for)
- Decades of sensor/actuator experience gives me an edge
- Arguably safer *for someone with electronics background*

**Cons:**

- More complexity for certification flight
- Equipment may not arrive in time

## Outcome

If CATS arrives in time → likely go electronic dual deployment

If not → motor delay single deployment
