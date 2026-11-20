# Investigation 37 — A stable observer still has a nonzero error envelope

**Origin:** synthetic scalar discrete-time model. Let a=0.8, observer gain L=0.6, initial error radius E0=0.1, bounded process disturbance W=0.02, and bounded sensor error V=0.01. Under the same known applied actuator input in the plant and observer, the error dynamics are `e[k+1]=(a-L)e[k]+w[k]-L v[k]`. The absolute error radius therefore updates as `E[k+1]=0.2 E[k]+0.026`, giving a limiting sufficient radius of **0.0325** model units.

The error begins at 0.1 and approaches 0.0325, not zero. A nominal observer pole of 0.2 is compatible with residual error caused by bounded disturbances and sensor error. If a-L becomes 1.2, the recurrence remains numerically defined over a short interval but does not admit a finite stationary bound under the same argument. The `scalar_observer_error_bound` program explicitly reports `None` for that stationary certificate.

**What was not measured:** no physical sensor noise maximum, process disturbance envelope, time synchronization or applied actuator log. If V were a Gaussian standard deviation rather than a hard bound, this deterministic certificate would not follow. A downstream AI must carry those assumptions with the 0.0325 result.

**Sources:** MIT *Underactuated Robotics* state-estimation reference; Mayne et al. 2006 output-feedback constrained-control abstract. The recurrence and synthetic values are authored, not source-reported measurements.
