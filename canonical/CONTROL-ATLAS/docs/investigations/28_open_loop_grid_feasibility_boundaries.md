# Investigation 28 — Finite-grid feasibility is a deliberately weaker claim than MPC

A toy scalar plant x+=x+u starts at x=1.5. With |x|≤2, |u|≤.75, horizon 4 and grid {−.75,−.5,0,.5,.75}, exhaustive search returns a low-cost admissible grid sequence. The result is optimal only among **the explicit finitely many grid candidates**; it is not necessarily optimal among all continuous admissible inputs. The method does not execute a receding-horizon loop.

Another toy plant has a=1.3, b=1, x0=1.9, |x|≤2, |u|≤.1 and grid {−.1,0,.1}. No grid candidate stays within the state bound at its first step. The program returns `no_feasible_candidate_on_grid`. It intentionally does not claim all conceivable continuous or redesigned control strategies are infeasible.

**Failure test:** treating an infeasible *grid* as proof of a globally infeasible physical plant is a category error. A real design needs independently verified bounds, disturbances, actuator dynamics, timing and terminal safety constraints; no physical safe state is known from this data.
