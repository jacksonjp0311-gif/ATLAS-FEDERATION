# Chapter 10: Finite-horizon optimal control and constraints

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

For a scalar discrete plant `x[k+1]=a x[k]+b u[k]`, consider a finite-horizon quadratic objective `Σ(q x[k]²+r u[k]²)+q_f x[N]²` with q and q_f nonnegative and r strictly positive. The optimal unconstrained policy under this exact model is `u[k]=−K[k] x[k]`, obtained from backward scalar Riccati recursion. With `S[N]=q_f`, `K[k]=b S[k+1] a/(r+b² S[k+1])`, `S[k]=q+a² S[k+1]−a b S[k+1]K[k]`.

The implemented function returns the gain sequence, cost-to-go coefficients, rollout trace and total cost. It verifies that the simulated quadratic cost agrees with `x0² S[0]` under floating-point tolerance. The casebook demonstrates an unstable open-loop coefficient a=1.1 stabilized over a short finite horizon by chosen gains—but no infinite-horizon certificate or real hardware data follows.

A true application must handle actuator and state constraints, disturbances, model mismatch, delay and safety barriers. If an unconstrained LQR asks for a physically impossible command, simply clipping it does **not** preserve optimality or the Riccati proof. Model predictive control solves a constrained optimization at each step but requires reliable computation timing and feasibility management. MIT Underactuated Robotics distinguishes unconstrained discrete Riccati methods from these harder constrained variants.

**Evidence gate:** record which cost is optimized, units and meanings of q/r, terminal cost assumptions, plant identification, constraints, disturbances, and worst-case numerical execution before making any deployment claim.

## Bound reference topics

- **Finite-horizon scalar LQR uses backward Riccati recursion** (`equation`): finite-lqr
- **Unconstrained LQR ignores actuator saturation and state constraints** (`concept`): lqr-unconstrained
- **Cost-to-go is defined by a user-chosen Q/R weighting, not universal optimality** (`concept`): lqr-cost
- **A low quadratic model cost is not evidence of good production control** (`concept`): lqr-no-real

## Source pointers

- [MIT-LQR](https://underactuated.mit.edu/lqr.html)
- [FBS-SUPPLEMENTS](https://fbswiki.org/wiki/index.php/Main_Page)

**Limit:** no new experiments or independent control review.
