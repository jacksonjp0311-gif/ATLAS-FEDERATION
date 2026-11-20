# 09. Optimal control: scalar discrete LQR

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Linear quadratic regulation (LQR) chooses feedback for a **known** linear model and quadratic objective. In discrete time, a scalar model is `x[k+1]=a*x[k]+b*u[k]` and an infinite-horizon cost is `Σ (q*x[k]^2+r*u[k]^2)`. With q>0, r>0 and b nonzero, a stabilizing scalar Riccati solution P and linear control `u=-K*x` can be computed exactly within numeric limits. This is an **unconstrained** problem: the optimum may require physically impossible actuator commands.

The scalar discrete algebraic Riccati equation is `P=q+a²P−(a*b*P)²/(r+b²P)`. The solution with P>0 yields `K=(b*P*a)/(r+b²P)`. The Atlas's `scalar_lqr` computes the positive stabilizing solution and rejects unactuated scalar cases and numeric overflow. Python-control's `dlqr` and MIT's LQR chapter supply the authoritative general matrix context; the installed package implements only the scalar special case, not a general Riccati solver or model predictive controller.

**Example:** for a=1.2, b=1, q=r=1, the controller can find a K that places the nominal closed-loop pole inside the unit circle. But if |u|<=0.2 and the state starts large, the command may saturate; the scalar LQR guarantee does not apply to the saturated system. Penalizing control effort more heavily also changes the optimal gain, not necessarily the actual closed-loop safety margin.

LQR is a controller solution conditional on an assumed model and a chosen objective. The weights are design choices, not learned moral preferences or absolute engineering importance. Before deployment, perform plant identification, uncertainty modeling, constraint handling, disturbance tests, robust stability analysis and independent safety review. Advanced multiparameter optimization and MPC remain reference topics, not implemented capabilities.

**Publisher/documentation scope:** [MIT-LQR](https://underactuated.mit.edu/lqr.html) · [PYCTR-DLQR](https://python-control.readthedocs.io/en/stable/generated/control.dlqr.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
