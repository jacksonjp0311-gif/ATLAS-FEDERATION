# Investigation 05: LQR model objective versus hard physical constraints

**Origin:** synthetic authored model, no real equipment.

For an assumed discrete scalar plant a=1.1,b=1 and weights q=1,r=.1,terminal=1 over eight steps, backward Riccati gains minimize the *unconstrained* quadratic objective. Its rollout cost matches x0^2 S0. If the first command exceeds actuator limits, clipping invalidates the unconstrained optimum; this package does not silently call clipped LQR optimal. A real model-predictive controller would need constrained optimization with feasibility, latency and safety checks.

**Source:** https://underactuated.mit.edu/lqr.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.
