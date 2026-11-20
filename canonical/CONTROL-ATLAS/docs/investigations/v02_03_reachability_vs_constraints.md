# Investigation 03. Controllable model, unreachable constrained state

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A two-state sampled double-integrator model uses `A=[[1,dt],[0,1]]`, `B=[0,dt]` and a measured position `C=[1,0]`. For nonzero dt, the ideal controllability matrix has full rank and the observability matrix can be full rank as well. These properties describe the local unconstrained linear model. They do not say the state can be reached within a short horizon under finite force or that a motion plan avoids hazards.

Compare a decoupled pair of states with `A=diag(.8,.9)`, `B=[1,0]`, `C=[1,0]`. The second state is neither reachable through the given actuator nor observable through that output. Increasing K or improving arithmetic precision does not create a missing physical actuation or sensor path. Adding a new sensor or actuator would change the model and the engineering design.

**Evidence needed:** validated A/B/C matrices, state units/scaling, actuator limits, sensor positions and noise, and actual finite-horizon constraints. **Sources:** python-control `ctrb` and `obsv` documented rank tests.
