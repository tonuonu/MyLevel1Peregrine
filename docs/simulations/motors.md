# Motor Selection

## Motor Requirements

### L1 Certification

- **H class** (160.01-320 N·s) or **I class** (320.01-640 N·s)
- Must be 18+ to purchase
- Single motor allowed for certification attempt with club membership

### Peregrine Motor Mount

- Native: **38mm**
- With adapter: **29mm** (using Aero Pack 29/38mm adapter)

## Recommended Motors

### 38mm Motors (Primary)

| Motor | Impulse | Avg Thrust | Burn | Est. Altitude |
|-------|---------|------------|------|---------------|
| AeroTech H100W | 186 N·s | 100 N | 1.9s | ~800 ft |
| AeroTech H180W | 219 N·s | 180 N | 1.2s | ~900 ft |
| AeroTech H210 Redline | 240 N·s | 210 N | 1.1s | ~950 ft |
| AeroTech H220T | 224 N·s | 220 N | 1.0s | ~900 ft |
| Cesaroni H180-SK | 226 N·s | 180 N | 1.3s | ~900 ft |

!!! tip "First Flight Recommendation"
    For L1 certification, the **H180W** or **H210 Redline** are popular choices:
    
    - Good thrust-to-weight ratio
    - Reasonable altitude (visible, recoverable)
    - Proven reliability

### 29mm Motors (Test Flights)

With 29/38mm adapter:

| Motor | Impulse | Notes |
|-------|---------|-------|
| AeroTech G80T | 120 N·s | Largest non-HP motor |
| AeroTech G79W | 112 N·s | White lightning |
| AeroTech G77R | 108 N·s | Redline (visible flame) |

!!! warning "Low Impulse"
    G motors may result in marginal rail exit velocity.
    Check simulations before flying.

## Motor Selection Criteria

1. **Rail Exit Velocity** ≥ 50 ft/s
2. **Maximum Altitude** within field boundaries
3. **Stability** margin throughout flight
4. **Recovery** drift within recovery area
5. **Cost** and availability

## Ejection Delay

Match motor delay to time-to-apogee:

| Motor Designation | Available Delays |
|-------------------|------------------|
| H180W-14 | 14 second |
| H210-14 | 14 second |

!!! note "Delay Adjustment"
    AeroTech DMS motors include adjustable delay:
    
    - Use delay adjustment tool
    - Match to RockSim/OpenRocket prediction
    - Or use "Optimal Delay" from simulation

## Motor Propellant Types

| Code | Propellant | Characteristics |
|------|------------|------------------|
| W | White Lightning | White exhaust, good visibility |
| T | Blue Thunder | Blue exhaust, some smoke |
| R | Redline | Red flame, high visibility |
| SK | Skidmark | Smoky (Cesaroni) |

## Cost Comparison

*Prices vary - check current pricing*

| Motor Type | Approximate Cost |
|------------|------------------|
| Single Use (DMS) | $50-70 |
| Reload (requires hardware) | $25-40 reload + hardware |
