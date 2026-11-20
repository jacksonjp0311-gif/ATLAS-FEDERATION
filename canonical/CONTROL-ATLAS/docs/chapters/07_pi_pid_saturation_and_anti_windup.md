# Chapter 07: PI/PID, saturation, and anti-windup

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Proportional action reacts to current tracking error; integral action accumulates error to eliminate persistent bias under applicable conditions; derivative action can anticipate a changing signal but is sensitive to noise and must be filtered. The gains depend on process dynamics and units. A controller with an integral term can accumulate a large internal value while the actuator remains saturated, then recover slowly when the reference drops.

MathWorks presents two documented anti-windup approaches—back-calculation and clamping—on a first-order process with actuator saturation and dead time. This Atlas implements only a **specific, discrete conditional integration** convention in a synthetic first-order, no-delay plant: `u=clip(kp*(r−y)+I, umin, umax)`. It freezes I when the proposed command is beyond a rail and the error would push it farther out; otherwise it integrates `I += ki Δt (r−y)`. The state update occurs after actuation via a zero-order-hold discrete model. The `none` mode integrates regardless of saturation.

The casebook gives an unreachable reference for a fixed interval and then lowers it. It compares model-integrated absolute error and final integrator values. Under the selected gains and synthetic plant, clamping improves its selected error metric. This is **not proof** that clamping always outperforms every other anti-windup design or that those gains are safe for an actual valve, heater or motor.

Any real controller change needs actuator limit and rate data, saturation strategy, reference range, sign of feedback, sensor noise, delays, failures, emergency interlocks, fail-safe mode, and approval. Never replace an existing safety loop's controller from a local Atlas numerical illustration.

## Bound reference topics

- **Integral action can wind up when actuator command exceeds physical limits** (`concept`): integral-windup
- **Conditional integration can limit integrator buildup in a saturated model** (`method`): clamping-antiwindup
- **A finite-step PI simulation must declare update order, limits, and sampling** (`equation`): pi-discrete-model
- **Anti-windup does not prove physical loop stability or optimality** (`concept`): antiwindup-not-proof

## Source pointers

- [MATLAB-AW](https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html)
- [FBS-WIKI](https://fbswiki.org/)

**Limit:** no new experiments or independent control review.
