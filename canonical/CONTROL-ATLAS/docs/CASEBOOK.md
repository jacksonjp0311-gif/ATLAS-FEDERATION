# Control Atlas synthetic casebook

Run `python -m control_atlas casebook`. Nine original cases cover first-order steps, exact first-order ZOH, an unstable discrete pole, two-state control/observation rank, anti-windup comparison, scalar Kalman, finite-horizon LQR, Nyquist strict boundary and conditional small gain. The input models are invented. Data origin: `synthetic_authored_test`. No physical experiment, robot actuation, industrial controller deployment or real AI agent benchmark occurred.

- **1. First-order response versus sampled-model claims**: First-order step with tau=10 s reaches about 63.2% of the step by t=10 s. Exact ZOH for tau=5 s, gain=2 and dt=.5 s gives a=e^-0.1 and b=2(1-a). This checks the *stipulated model*, not real machine dynamics. If a second unmodeled pole or delay exists, the same response data may not support these calculations for future excitation. Require measured frequency/step data, actuator calibration, latency and independent holdout disturbances before using for control.
- **2. Hidden-state reachability and observability**: The discrete double integrator A=[[1,1],[0,1]], B=[0.5,1], C=[1,0] gives nonzero controllability and observability determinants. If B=[0,0], the state is not controllable no matter what gain is chosen; if C=[0,0], no state is visible. These are algebraic statements, not sensor-placement certification. Determinant tolerance is scale-dependent; report state/actuator/measurement units.
- **3. Saturated PI and anti-windup counterexample**: A constructed first-order process receives an unreachable reference followed by a smaller one. The simple PI implementation accumulates integral error if configured without anti-windup. Clamping freezes further integration when error pushes beyond a saturated rail, improving the selected integrated absolute error in this particular test. No generalized optimal-gain theorem follows. Add actuator delay, rate limits, sensor bias, interlocks and failure trace to test real equipment.
- **4. Kalman confidence under a wrong sensor model**: A scalar filter given process variance .01, measurement variance .1 and selected synthetic readings produces a decreasing variance and a posterior estimate. If the sensor has an unmodeled constant bias, its reported covariance need not cover the true state; increasing the number of readings can make it confidently wrong. The local filter does not estimate covariance from data, handle correlated noise or filter a real sensor stream.
- **5. LQR model objective versus hard physical constraints**: For an assumed discrete scalar plant a=1.1,b=1 and weights q=1,r=.1,terminal=1 over eight steps, backward Riccati gains minimize the *unconstrained* quadratic objective. Its rollout cost matches x0^2 S0. If the first command exceeds actuator limits, clipping invalidates the unconstrained optimum; this package does not silently call clipped LQR optimal. A real model-predictive controller would need constrained optimization with feasibility, latency and safety checks.
- **6. Sampling and robustness logical refusal**: A 10 Hz sample rate fails the strict ideal sampling condition for a 5 Hz bandlimited signal. An 11 Hz sample rate passes that condition but does not prove any feedback controller stable. Likewise, hypothetical stable-gain bounds .6 and .7 multiply to .42 (<1), a sufficient *conditional* small-gain test; product above 1 is inconclusive about instability. These tools prevent replacing qualified engineering reasoning with generic green status flags.


## v0.2 extension material

# Control Atlas computational casebook v0.1.0

There are **nine numerical cases** and **twelve research investigations**. These are authored model demonstrations and study protocols, not publisher experimental datasets, physical equipment trials or live control execution. Run `python -m control_atlas casebook` from the source package. Each numerical result includes model assumptions/limits. The research investigations are independent explanatory documents, not additional numerical cases.

- 1. **01_exact_sampled_response** — Exact sampled response versus unstable approximation
- 2. **02_nominal_gain_misread** — A feedback pole moves, but actuator safety is unproven
- 3. **03_reachability_vs_constraints** — Controllable model, unreachable constrained state
- 4. **04_antiwindup_trace** — A saturated controller can accumulate hidden integral error
- 5. **05_sampling_ambiguity** — A 70 Hz oscillation appears at 30 Hz after sampling
- 6. **06_identification_experiment** — A perfectly fitted teaching plant may still identify nothing real
- 7. **07_scalar_lqr_unconstrained** — A stabilizing LQR gain can demand impossible input
- 8. **08_state_estimation_and_sensor_bias** — A Kalman covariance is conditional, not truth
- 9. **09_feedback_delay_and_saturation** — Modeling a delay matters more than a larger gain
- 10. **10_fault_residual_not_root_cause** — A changing residual is not proof of a faulty component
- 11. **11_context_package_safety** — A retrieved feedback formula must keep its operating assumptions
- 12. **12_method_selection_review** — Designing the next experiment rather than inventing a controller

Numerical output from the explicitly authored calculator should not be interpreted as a certified controller or algorithmic performance result.


## v0.3.0 robust counterexamples

Eight new cases are available via `python -m control_atlas robust-casebook`: two exact scalar coefficient-box tests; one exact single-sample delay instability counterexample; two Lyapunov candidate results including an intentionally failed P that does not imply instability; a pointwise sensitivity identity; alternating residuals without whiteness inference; and an offline invalid/stale/innovation fault-gate trace. All are authored mathematical cases, not physical tests. The full descriptions are investigations 19–24.


## 0.4.0: multivariable robustness, constrained planning and sensor ambiguity

The new `python -m control_atlas advanced-casebook` runs nine synthetic cases: return difference with singular values 3.99/0.01; positive common-P certificate for an independent 2x2 matrix box; a failed P=I candidate for a stable upper triangular matrix; two-state finite-horizon LQR and Riccati identity; feasible and no-grid-candidate scalar plans; correlated two-sensor NIS=4/3; observationally equivalent sensor bias and plant-state hypotheses; and a training/validation model drift example. Source pages and domain limits are in Chapters 34–40 and Investigations 25–31. No real sensor readings, controller or physical fault were measured or operated.


## v0.5: robust invariant-box investigations

Use `python -m control_atlas invariance-casebook`. Seven original synthetic cases test robust 2×2 model-bounded invariance, actuator amplitude veto, scalar interval, state/observer bias mismatch, and refusal when full state is not available. The 64-vertex certificate is for the exact mathematical class, not equipment safety. See Investigations 32–36 and Chapters 41–46.


## v0.6 output-feedback investigations

`python -m control_atlas output-feedback-casebook` executes 12 **authored synthetic model cases**, including observer error, stationary bound absence, magnitude/rate/lag differences, finite-horizon tube checks, and sensor-reading ambiguity. These are not real physical measurements or claimed fault isolations. The new investigations 37–42 preserve what could be calculated, what was refused, and which evidence is missing. The complete code is `control_atlas/output_feedback.py` and the separate numerical oracle is `tools/output_feedback_v06_oracle.py`.


## v1 candidate: public-data integrity, multivariable observer and chronological ARX

`python -m control_atlas v1-casebook` runs six cases: a source-derived summary of 3×49 public third-party RPM records with no per-row input, a synthetic 180-row OpenMCT-style parser/fit, a constant-input identifiability refusal, a bounded 2×2 observer, a sensor-mismatch non-diagnosis case, and a conservative sufficient-condition counterexample. Only the descriptive 3×49 summary is derived from reported external experimental data; the rest are original synthetic numerical exercises. No full raw third-party data are redistributed or fetched by the tool. The more strongly instrumented OpenMCT dataset v2 is a documented scientific target but its files are not available here, so its numerical model-fitting case is not claimed complete.
