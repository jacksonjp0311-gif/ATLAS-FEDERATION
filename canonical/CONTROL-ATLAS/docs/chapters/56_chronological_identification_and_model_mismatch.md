# 56. System identification must be evaluated outside its training window

A useful system-identification result states the model, input-output experiment, excitation, sampling, parameter-estimation procedure, held-out evaluation and limitations. The new `validate_openmct_identification` method models **one** measured motor-speed channel with a one-step linear discrete ARX relation:

`MEAS[k+1]=a*MEAS[k]+b*PWM[k]+c+residual[k]`.

This form can be a local empirical predictor, but does not by itself establish motor physics or a causal input-to-output transfer function. In closed loop the plant input may correlate with disturbances, which biases naive least-squares identification. The code has no instrumental-variable or joint input-noise model, does not estimate physical inertia/friction, and cannot certify a controller. Strong input excitation and a model adequacy analysis remain prerequisites.

## Numerical pipeline

The first 70% of transitions provide one-step training observations, and the remaining 30% form a chronological held-out segment. To avoid arbitrary slopes for missing excitation, training requires a nontrivial applied PWM span and a full-rank centered regression matrix. The model fit uses centered two-predictor normal equations with a rank check; linear algebra precision and closed-loop bias remain known limitations. Validation computes **one-step RMSE** using observed previous speed, **free-run RMSE** using only the held-out initial speed and subsequent recorded applied PWM, and **persistence RMSE** as a reference baseline. One-step and free-run errors measure different questions and must not be substituted for each other.

A 20-ms dataset can include timestamp jitter; if its measured DT deviation is too large, the constant-discrete-coefficient model is refused. An unobserved deadband, actuator lag, friction changes or quantization can also produce residual structure. The same held-out record is not an independent apparatus or a new motor; cross-session validation is a separate later gate. ARX can appear excellent under certain regimes while behaving poorly after saturation or a large operating-range change.

## Scientific rejection criteria

The routine refuses less than 50 samples, fewer than 20 fit transitions, nonfinite or malformed channel values, excessive recorded sample-period variation, constant/insufficient PWM span, collinear regressor geometry, and numerical divergence. These refusals are expected scientific outputs: do not “fix” them by adding fabricated perturbations to published measurements. A known synthetic model is used to test the implementation; that is not a performed source-data validation.

The accessible 2026 OpenMCT paper explains the authors' own identification and controller tests. This Atlas does not claim to reproduce their fitted coefficients or RMSE because its raw data were not obtained. The validated parser and split will work on an explicitly supplied authentic archive once acquired and checked.
