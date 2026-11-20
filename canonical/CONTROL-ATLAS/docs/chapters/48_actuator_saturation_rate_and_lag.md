# 48. The requested input is not the applied input

A controller computes a requested action. A physical actuator has amplitude limits, rate limits, energy constraints, latency, hysteresis, dead zones and possible failures. It may deliver something different. An infinite-horizon LQR design or PID gain that ignores these limits cannot directly inherit a guarantee when the actuator saturates. Actuation should be represented as a dynamical state and its behavior treated as an experimentally validated model before deployment.

## An explicit discrete teaching model

This edition implements three successive transformations of a scalar command. First the requested command `r[k]` is magnitude-clipped to the specified interval `[-U,U]`. Second the *target* is constrained to `u_applied[k] +/- D`, where D is a maximum allowed change in the sampled interval. Third a first-order response parameter `alpha` in `(0,1]` gives the next applied input: `u_applied[k+1]=u_applied[k]+alpha*(target-u_applied[k])`. This is an authored, causal discrete actuator model. It is not a source-supplied real actuator transfer function. The realized plant uses `u_applied[k]` for the present step, while the updated actuator state becomes available for the next step.

For a nominal requested input of 10 units, magnitude bound U=1, per-step D=0.2, previous applied input 0, and alpha=0.5, the magnitude-clipped target is 1, the slew-limited target is 0.2, and the next applied input is **0.1**. These are four distinct quantities. Replacing the applied input in the plant with the requested input of 10 is a model error, not a harmless optimization shortcut.

The model's update preserves `|u_applied|<=U` when its initial applied state satisfies the amplitude limit and alpha is between zero and one. It also preserves an applied per-step change no greater than D. These are properties of a mathematical recurrence, not of any motor, valve or PLC. If an actuator begins outside the declared bound, the function refuses the claimed premise instead of silently clipping its historical state. A zero D freezes the target. A hidden mechanical lag may differ from the chosen alpha; response fraction should be identified and validated.

## Why this matters for robust control

Actuator dynamics can increase phase lag, affect damping and invalidate a controller synthesized under an instantaneous-input assumption. A speed or saturation constraint can render a nominally reachable state unreachable under the real actuator. Rate limits can contribute to oscillatory behavior; the AIAA 2023 paper by Newton and Kroo discusses pilot-induced oscillation tendencies due to control-surface rate limits in a specific aerospace context. That is not experimental evidence for a factory valve.

**Source scope:** Newton and Kroo, *Model Reference Control for Reducing Pilot-Induced Oscillation Tendencies Due to Actuator Rate Limits*, AIAA 2023 published abstract https://doi.org/10.2514/6.2023-2512 ; Åström and Murray, *Feedback Systems* reference overview https://fbsbook.org/ . The local scalar lag and slew model is original synthetic teaching code and is not attributed as a published physical implementation.
