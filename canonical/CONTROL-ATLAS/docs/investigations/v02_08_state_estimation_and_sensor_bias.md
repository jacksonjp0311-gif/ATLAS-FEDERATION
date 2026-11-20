# Investigation 08. A Kalman covariance is conditional, not truth

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A scalar filter begins with prior mean 0, prior variance 1, known a=1, process variance Q=.25 and measurement variance R=.25. Given a measurement y=2, its predicted variance is 1.25, Kalman gain 5/6, posterior mean 5/3 and posterior variance 5/24. Each value follows the specified noise model. A real sensor could have drift or correlated noise that the model omits. In that case the reported posterior variance can be much smaller than the true estimation error.

A state estimator must not turn an inferred latent variable into a direct sensor measurement. Real validation requires residual distributions, calibration, timing and independent reference measurements, plus assessment of assumptions such as Gaussian noise and unbiased direct observation. The included method is a one-step scalar update, not a deployed multi-sensor tracker.

**Source:** python-control Kalman estimator reference and MIT state-estimation chapter navigation. **Refusal:** a small posterior covariance alone is not a calibration or accuracy certificate.
