# Chapter 09: State estimation and scalar Kalman filtering

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A state estimator combines a process prediction and a noisy measurement to estimate an unobserved state. The Kalman filter is a mathematically optimal linear mean-square estimator under **specific** linearity and noise assumptions. Its gain depends on covariance inputs, not merely on sensor trust. Small reported posterior variance indicates confidence *within the stipulated model*; it does not establish that sensor calibration, state dynamics, or noise correlation are correct.

The v0.1 scalar filter assumes `x[k]=a x[k-1]+w[k]`, `z[k]=c x[k]+v[k]` with supplied variances `Q` and `R`. It first predicts `x-=a x`, `P-=a²P+Q`, forms `S=c²P-+R` and gain `K=P- c/S`, then corrects estimate and covariance. It uses the scalar Joseph form `(1−Kc)² P-+K²R` for numerical nonnegativity. It refuses missing or nonpositive R and nonfinite observations.

The casebook supplies five synthetic readings and reports posterior means/variances; no real sensor or calibration was used. If there is an unknown constant bias, the filter can converge confidently toward an incorrect value. A real implementation should consider bias-state augmentation, covariance estimation from calibration and residual data, outlier policies, dropout, time synchronization and numerical conditioning.

**Control-specific interpretation:** estimating state is not controlling it. The estimator output must have reliable uncertainty and timestamps before any controller acts. This package does not integrate the Kalman output with an actual actuator or safety loop.

## Bound reference topics

- **A Kalman covariance is conditional on specified process and measurement noises** (`concept`): kalman-conditional
- **A scalar linear-Gaussian filter uses prediction, innovation and correction** (`equation`): kalman-scalar
- **An unmodeled sensor bias can defeat a seemingly small posterior variance** (`concept`): kalman-bias
- **Joseph covariance update can preserve nonnegative variance numerically** (`method`): kalman-joseph

## Source pointers

- [MIT-STATE](https://underactuated.mit.edu/state_estimation.html)
- [FBS-WIKI](https://fbswiki.org/)

**Limit:** no new experiments or independent control review.
