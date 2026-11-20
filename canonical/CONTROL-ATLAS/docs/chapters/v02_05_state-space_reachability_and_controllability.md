# 05. State-space reachability and controllability

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Reachability asks whether admissible inputs can move a state from one condition to another within a declared model and time horizon. For a finite-dimensional linear time-invariant pair (A,B), the classical controllability matrix is `[B, AB, A²B, ... A^(n−1)B]`. Full row rank n is the unconstrained linear controllability criterion. This does not establish that actuators have sufficient magnitude, satisfy rate limits, or can safely produce that trajectory.

The bounded Control tool implements only a **two-state, single-input** case: A is 2×2, B a two-vector, and the controllability determinant of `[B,AB]` indicates exact rank in ideal arithmetic. In floating-point arithmetic, a small determinant can also indicate poor scaling or conditioning; the tool's relative threshold is a declared heuristic rather than a rigorous numerical conditioning bound. The Python Control Systems Library documents `ctrb` for general state-space matrices, but no library here infers a real physical A/B model.

A simple double-integrator sampled position/velocity model is `A=[[1,Δt],[0,1]]`, `B=[[0],[Δt]]`. Under a nonzero Δt it is controllable algebraically. Yet if the actuator can accelerate only within a limited range, the set of reachable safe states in a fixed horizon may be far smaller. The system's state variables and coordinate units must be declared before comparing determinants across parameter choices.

**Counterexample:** choose B=[1,0] and diagonal A=diag(0.8,0.9). The second state cannot be influenced by this input; the determinant is zero. Increasing feedback gain cannot control an inaccessible state. Adding an unmodeled actuator that changes B would be a new system design, not a numerical improvement to the existing one.

When using this reference for industrial or agentic systems, note that mathematical state reachability is not evidence of goal achievement, agent reliability or a real device's actuators. Cross-domain metaphors must not be promoted into physical control claims.

**Publisher/documentation scope:** [PYCTR-CTRB](https://python-control.readthedocs.io/en/stable/generated/control.ctrb.html) · [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems). These are exact source pointers and original summaries, not redistributed source text or new measurements.
