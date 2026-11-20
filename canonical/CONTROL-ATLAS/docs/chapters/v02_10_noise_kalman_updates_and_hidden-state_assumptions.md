# 10. Noise, Kalman updates and hidden-state assumptions

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A Kalman filter is an estimation framework under linear dynamics with specified process and measurement noise statistics. An observer can reduce mean-squared estimation error when its model and covariances are appropriate; it cannot magically recover information that the sensor does not provide. If a sensor has an unknown bias or shares disturbances with the process, a simple Kalman model with independent zero-mean noise may be confidently wrong.

For a scalar discrete step, predict mean μ−=a μ and variance P−=a²P+Q. With direct measurement y and independent measurement-noise variance R>0, the gain is `K=P−/(P−+R)`, posterior mean μ+=μ−+K(y−μ−), and posterior variance `(1−K)P−`. The Atlas computes this one step. It does not estimate Q or R from data, implement covariance cross-terms, detect outliers, handle missing measurements, estimate delay or fuse sensors.

**Variance interpretation:** P is conditional on the stated model. A small posterior variance is not a guarantee of closeness to truth if process noise, sensor bias, or the dynamics matrix are wrong. Noise may be colored, heteroscedastic or state dependent. During calibration drift a filter may report unrealistically small uncertainty. A safe research report should compare predicted residuals to actual holdout measurements, inspect innovation autocorrelation and test parameter sensitivity.

Control Atlas therefore separates observed measurement records from estimated state records. Measurement Atlas holds calibration conventions, uncertainty budgets and source provenance. The AI context assembler must preserve both the predicted state and its assumptions rather than rendering the estimated mean as “the sensor measured X.”

**Publisher/documentation scope:** [PYCTR-LQE](https://python-control.readthedocs.io/en/latest/generated/control.lqe.html) · [MIT-STATE](https://underactuated.mit.edu/state_estimation.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
