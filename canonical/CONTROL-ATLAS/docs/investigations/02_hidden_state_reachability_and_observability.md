# Investigation 02: Hidden-state reachability and observability

**Origin:** synthetic authored model, no real equipment.

The discrete double integrator A=[[1,1],[0,1]], B=[0.5,1], C=[1,0] gives nonzero controllability and observability determinants. If B=[0,0], the state is not controllable no matter what gain is chosen; if C=[0,0], no state is visible. These are algebraic statements, not sensor-placement certification. Determinant tolerance is scale-dependent; report state/actuator/measurement units.

**Source:** https://python-control.readthedocs.io/en/latest/generated/control.ctrb.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.
