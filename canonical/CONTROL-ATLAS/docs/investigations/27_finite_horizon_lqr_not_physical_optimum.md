# Investigation 27 — The Riccati cost identity does not certify an actuator

A constructed two-state integrator uses A=[[1,1],[0,1]], B=[.5,1], Q=diag(10,1), R=.25, Qf=diag(10,1), x0=[2,0] and horizon eight. A backward Riccati recursion generates optimal feedback gains for this **unconstrained** finite-horizon linear model. Its predicted total quadratic cost equals x0ᵀP0x0 within numerical precision. Separate SciPy full-control-sequence minimizations agree on randomly generated models.

That identity verifies the optimization calculation. It does not indicate that the resulting input could be delivered by a physical actuator or that the state is safe. Motor torque, current limits, heat, actuator lag, encoder noise and sample clocks are absent. Nor does a finite-horizon nominal optimum prove global robust stability after the horizon.

An evidence-rich engineering study would compare physical input limits with the predicted first action, identify plant matrices and uncertainties, include timing and disturbances, and test admissibility with a qualified constrained controller. The Atlas exports a method result with limitations, not an actuator command.
