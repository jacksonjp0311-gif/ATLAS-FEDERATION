# 06. Observability and state estimation

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A system can contain internal states that are not directly measured. Linear observability asks whether state trajectories can be reconstructed in principle from a known dynamics matrix A and output C across time, under the model and appropriate input information. The classical observability matrix is `[C; CA; ...; CA^(n−1)]`; full column rank n gives the unconstrained linear observability criterion. Observability does not guarantee a practical observer will perform acceptably under noise, poor sampling, quantization or uncertain dynamics.

Our two-state single-output tool computes the determinant of `[C;CA]` alongside controllability and the nominal matrix poles. The result is an explicit teaching calculation rather than a general numerical rank solver. Coordinate scaling can make a determinant small even when mathematical rank is full, so the result must carry the chosen tolerance and state units.

**Example:** if A is diagonal and C=[1,0], only the first autonomous state is measured; the second cannot be inferred from output history in this uncoupled model. If dynamics couple the second state into the observed state, it may become observable. Merely increasing the sensor sampling rate cannot resolve an unobservable mode with no measurement pathway.

The scalar Kalman update included in this Atlas predicts one state and variance, then combines a directly observed measurement through a supplied process-noise variance Q and measurement-noise variance R. It is a one-step model with known dynamics and declared covariance—not a calibrated multi-sensor state estimator. Estimation uncertainty is conditional on process and measurement assumptions, and bad noise covariances produce misleading confidence even when code is numerically stable.

A physical state observer needs sensor placement, calibration, actual noise spectra, latency and an independent validation record. A state inferred by an observer is not a measurement, nor does a filtered signal identify its physical cause automatically.

**Publisher/documentation scope:** [PYCTR-OBSV](https://python-control.readthedocs.io/en/stable/generated/control.obsv.html) · [PYCTR-LQE](https://python-control.readthedocs.io/en/latest/generated/control.lqe.html) · [MIT-STATE](https://underactuated.mit.edu/state_estimation.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
