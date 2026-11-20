# Chapter 04: Feedback, disturbances, and error

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A feedback loop observes an output, compares it to a reference and applies an action. The control objective should say whether it values setpoint tracking, disturbance rejection, energy consumption, actuator wear, transient overshoot or steady-state error. The same gains can perform differently across these tasks. Improving one objective can worsen another: increasing feedback gain often reduces low-frequency error, yet may amplify measurement noise or destabilize unmodeled dynamics.

A useful experiment prescribes separate **reference step**, **disturbance step**, **measurement-noise** and **model-uncertainty** trials with consistent units and recordable response metrics. Integrated absolute error, settling time, overshoot, actuation range and the number of saturated steps help compare specified simulations. None alone establishes safety. For example, a controller that quickly reaches setpoint might overshoot a safe process temperature or use an actuator at its maximum for too long.

Treat each performance measure as dependent on simulation time grid and disturbance design. Integrated absolute error with timestep Δ can be approximated as `Σ |r[k]−y[k]|Δ`, but the result should report whether error is sampled before or after actuation. Comparing different sampling rates without a common continuous physical metric can distort rankings.

A contextual package for AI should carry the declared performance objective, underlying model, actuator limits, observed versus estimated parameters, logs of failures and changes to controller gains. A toy gain optimization is not evidence that a real plant meets a reliability or regulatory requirement.

## Bound reference topics

- **Negative feedback regulates a chosen output but may excite dynamics or noise** (`concept`): negative-feedback
- **Setpoint tracking and disturbance rejection are different tests** (`concept`): reference-vs-disturbance
- **Integrated absolute error is a metric, not a safety criterion** (`method`): error-metrics
- **Sensor noise and high-frequency control action require a separate model** (`concept`): noise-sensitivity

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [FBS-PRESS](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems)

**Limit:** no new experiments or independent control review.
