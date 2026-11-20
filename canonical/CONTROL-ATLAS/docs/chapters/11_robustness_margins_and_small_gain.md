# Chapter 11: Robustness, margins, and small gain

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Control robustness asks whether intended behavior persists when model parameters, disturbances, delay, unmodeled dynamics or operating conditions vary. A nominally stable loop can fail under parameter drift, large excursions, actuator saturation or a new sensor configuration. Robustness is not identical to small nominal tracking error. It must be stated relative to an **uncertainty set**, a plant family and a performance/safety metric.

The small-gain theorem offers a useful **sufficient** stability condition for the feedback interconnection of suitably stable operators: if compatible induced-gain bounds satisfy `||G||·||Δ||<1`, the appropriate feedback system is stable under its assumptions. The simple helper multiplies two supplied nonnegative bounds; it does not estimate induced norms or verify that the interconnection matches the theorem. If the product is ≥1, this particular sufficient test fails, but that **does not prove** the actual system unstable.

This is a recurring evidence trap in agent-assisted engineering: a controller may optimize a toy robustness proxy and report a confident claim while the physical uncertainty set remains unknown. A credible statement should identify model uncertainty, structured/unstructured perturbations, delays, actuator limits, sensor noise, required frequency range and experimental evidence. The absolute values and model validity of any gain bounds need review.

A strong research program would compare robust performance across measured, uncertain plants with real test logs. This first edition has no real uncertain-plant dataset and no `H∞` synthesis. Its robustness chapter is a reference and refusal framework, not a new control theorem.

## Bound reference topics

- **Strict small-gain product is sufficient only for stable operator interconnection norms** (`equation`): small-gain
- **A failed sufficient small-gain check does not prove real instability** (`concept`): small-gain-not-necessary
- **Physical saturation/delay/noise invalidate simplistic gain arguments** (`concept`): robustness-nonlinear
- **Robustness results require uncertainty sets, frequencies and operating domain** (`method`): robust-design-ledger

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MIT-STABILITY](https://underactuated.mit.edu/lyapunov.html)

**Limit:** no new experiments or independent control review.
