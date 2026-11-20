# Chapter 03: Stability, equilibria, and model boundaries

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Stability must refer to a specific system and equilibrium. In the scalar autonomous recurrence `x[k+1]=a x[k]`, `x[k]=a^k x0`; hence asymptotic convergence to zero occurs exactly when `|a|<1`. For `|a|=1` the state need not decay, and for `|a|>1` nonzero states diverge in magnitude. This exact proof does **not** generalize to arbitrary nonlinear, time-varying or saturated systems by simply inspecting one number.

Continuous-time linear systems are stable when the relevant closed-loop poles have negative real parts, under usual finite-dimensional LTI assumptions. A nonlinear local linearization can be useful near an operating point, but a plant may have multiple equilibria, regions of attraction, actuator limits and physical states that cannot be expressed by the linear model. Lyapunov-function methods can certify specific regions if assumptions and derivative conditions are established; the existence of a simulation trace with bounded states is not itself a Lyapunov proof.

A supervisor-facing safety question should identify whether “stable” means bounded internal states, asymptotic regulation, robust stability across parameter variation, input-output boundedness or tolerance of sensor failures. These are not equivalent. A controller tuned on a stable simulated first-order process could still destabilize a plant with ignored dead time or wrong feedback polarity.

**Atlas refusal:** If actual poles, sampled operating point or physical constraints are not validated, do not label equipment safe, stable or production-ready. Report the model's mathematical pole condition and list missing physical checks.

## Bound reference topics

- **A scalar discrete pole strictly inside the unit circle is asymptotically stable** (`equation`): scalar-stability
- **Unit-circle boundary is not an asymptotic stability certificate** (`concept`): marginal-pole
- **Linearized local stability need not imply global nonlinear stability** (`concept`): local-stability
- **Open-loop stability cannot establish closed-loop safety** (`concept`): closed-loop-vs-plant

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MIT-STABILITY](https://underactuated.mit.edu/lyapunov.html)

**Limit:** no new experiments or independent control review.
