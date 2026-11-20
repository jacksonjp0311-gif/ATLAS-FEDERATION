# CONTROL ATLAS · Unified scientific reference 0.2.0

**James Paul Jackson research program.** 26 substantive chapters and 18 constructed investigations. Scientific content and numerical examples are *not* measured hardware, external control-agent tests or independently reviewed engineering guidelines. No retrieved reference text is executed.

# CONTROL ATLAS — Unified Reference Guide v0.2.0

Two previously separate 0.1 research lineages have been **merged without overwriting either**. They share the same scientific evidence format, but have different model choices and complementary numerical methods. The old 12 chapters and 6 investigations are preserved, alongside 14 new chapters and 12 new investigations. This is a bounded scientific reference, not equipment-control permission.

## Previously published foundations (preserved)

- [01 systems interventions and evidential scope](chapters/01_systems_interventions_and_evidential_scope.md)
- [02 continuous and sampled plant dynamics](chapters/02_continuous_and_sampled_plant_dynamics.md)
- [03 stability equilibria and model boundaries](chapters/03_stability_equilibria_and_model_boundaries.md)
- [04 feedback disturbances and error](chapters/04_feedback_disturbances_and_error.md)
- [05 state space reachability and observation](chapters/05_state_space_reachability_and_observation.md)
- [06 sampling delays and zoh](chapters/06_sampling_delays_and_zoh.md)
- [07 pi pid saturation and anti windup](chapters/07_pi_pid_saturation_and_anti_windup.md)
- [08 system identification and uncertainty](chapters/08_system_identification_and_uncertainty.md)
- [09 state estimation and scalar kalman filtering](chapters/09_state_estimation_and_scalar_kalman_filtering.md)
- [10 finite horizon optimal control and constraints](chapters/10_finite_horizon_optimal_control_and_constraints.md)
- [11 robustness margins and small gain](chapters/11_robustness_margins_and_small_gain.md)
- [12 verification industrial safety and ai knowledge reuse](chapters/12_verification_industrial_safety_and_ai_knowledge_reuse.md)

## v0.2 extended methods

- [01 the control question plant and measurable target](chapters/v02_01_the_control_question_plant_and_measurable_target.md)
- [02 continuous-time responses and exact sampled holds](chapters/v02_02_continuous-time_responses_and_exact_sampled_holds.md)
- [03 feedback stability poles and unmodeled disturbances](chapters/v02_03_feedback_stability_poles_and_unmodeled_disturbances.md)
- [04 sample rates aliasing delay and digital clocks](chapters/v02_04_sample_rates_aliasing_delay_and_digital_clocks.md)
- [05 state-space reachability and controllability](chapters/v02_05_state-space_reachability_and_controllability.md)
- [06 observability and state estimation](chapters/v02_06_observability_and_state_estimation.md)
- [07 pid control saturation windup derivative noise](chapters/v02_07_pid_control_saturation_windup_derivative_noise.md)
- [08 system identification- excitation bias and validation](chapters/v02_08_system_identification-_excitation_bias_and_validation.md)
- [09 optimal control- scalar discrete lqr](chapters/v02_09_optimal_control-_scalar_discrete_lqr.md)
- [10 noise kalman updates and hidden-state assumptions](chapters/v02_10_noise_kalman_updates_and_hidden-state_assumptions.md)
- [11 robustness uncertainty delay and safety limits](chapters/v02_11_robustness_uncertainty_delay_and_safety_limits.md)
- [12 constrained control and model predictive planning](chapters/v02_12_constrained_control_and_model_predictive_planning.md)
- [13 fault detection diagnosis and operational evidence](chapters/v02_13_fault_detection_diagnosis_and_operational_evidence.md)
- [14 evidence maturity integration contracts and method selection](chapters/v02_14_evidence_maturity_integration_contracts_and_method_selection.md)

## Previously published investigations (preserved)

- [01 first order response versus sampled model claims](investigations/01_first_order_response_versus_sampled_model_claims.md)
- [02 hidden state reachability and observability](investigations/02_hidden_state_reachability_and_observability.md)
- [03 saturated pi and anti windup counterexample](investigations/03_saturated_pi_and_anti_windup_counterexample.md)
- [04 kalman confidence under a wrong sensor model](investigations/04_kalman_confidence_under_a_wrong_sensor_model.md)
- [05 lqr model objective versus hard physical constraints](investigations/05_lqr_model_objective_versus_hard_physical_constraints.md)
- [06 sampling and robustness logical refusal](investigations/06_sampling_and_robustness_logical_refusal.md)

## v0.2 new investigations

- [01 exact sampled response](investigations/v02_01_exact_sampled_response.md)
- [02 nominal gain misread](investigations/v02_02_nominal_gain_misread.md)
- [03 reachability vs constraints](investigations/v02_03_reachability_vs_constraints.md)
- [04 antiwindup trace](investigations/v02_04_antiwindup_trace.md)
- [05 sampling ambiguity](investigations/v02_05_sampling_ambiguity.md)
- [06 identification experiment](investigations/v02_06_identification_experiment.md)
- [07 scalar lqr unconstrained](investigations/v02_07_scalar_lqr_unconstrained.md)
- [08 state estimation and sensor bias](investigations/v02_08_state_estimation_and_sensor_bias.md)
- [09 feedback delay and saturation](investigations/v02_09_feedback_delay_and_saturation.md)
- [10 fault residual not root cause](investigations/v02_10_fault_residual_not_root_cause.md)
- [11 context package safety](investigations/v02_11_context_package_safety.md)
- [12 method selection review](investigations/v02_12_method_selection_review.md)

[Source register](SOURCE_REGISTER.md) · [Evidence coverage](COVERAGE_MATRIX.md) · [Old manual preserved](legacy_v0.1.0/DEPTH_MANUAL_v0.1.0.md) · [Release limitations](VALIDATION_v0.2.0.md). The eventual Bitwork navigation and external model evaluation are deferred until all thirty domain content libraries are built.


---

# Chapter 01: Systems, interventions, and evidential scope

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Control engineering starts by identifying a **plant** (system being influenced), measurable outputs, controllable actuators, goals, disturbances, sensor latency and hard safety limits. For example, a temperature loop requires a thermal mass, heater/fan limits, sensing locations and thermal coupling assumptions. A symbolic transfer function can describe a limited operating region but does not certify that those assumptions hold during operation.

A controller is a policy mapping measured state or tracking error to an action. In negative feedback, the controller uses error between setpoint and measured output to correct a disturbance. The loop may reduce sensitivity to some uncertainties, yet it can amplify high-frequency noise, excite unmodeled modes or destabilize if sign, gain or delays are wrong. A controller is not necessarily safe merely because its output approaches the requested setpoint in a simulation.

The Atlas documents models, hypotheses and design methods as source-linked records. It never drives physical equipment. Its public casebook is a set of authored synthetic tests; no PLC, factory machine, robot, device, agent or other live plant was operated. An AI may use these records as context but cannot treat retrieved text as executable instructions, and the deferred Bitwork routing system is separate.

**Evidence gate:** A real control recommendation needs identified dynamics or credible first-principles model, actual actuator/sensor constraints, testing across relevant operating states, disturbance and uncertainty analysis, interlocks, qualified review and a recorded change-control plan. Without those, the appropriate result is a model-level explanation or an unresolved decision.

## Bound reference topics

- **A feedback question requires plant, actuator, sensor, target and operating range** (`concept`): feedback-question
- **A simulated controlled plant is not a test of real equipment** (`concept`): model-vs-hardware
- **Controller success claims require explicit model and disturbance scope** (`concept`): controller-evidence
- **Control Atlas methods must not be mistaken for a live Atlas or Bitwork router** (`method`): non-routing-domain

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [FBS-PRESS](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems)

**Limit:** no new experiments or independent control review.


---

# Chapter 02: Continuous and sampled plant dynamics

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A standard teaching plant is `τ ẏ = -y + K u`, with time constant τ>0 and constant input u. For a settled step to final value, `y(t)=y∞+(y0−y∞)exp(−t/τ)`. This is not a measured response curve and excludes dead time, nonlinearity, hidden poles and measurement noise. In this limited model, at `t=τ` the state has completed about 63.2% of the difference between initial and final values.

For piecewise constant inputs held over a sample period Δ, the exact discrete update is `y[k+1]=a y[k]+b u[k]`, with `a=exp(−Δ/τ)` and `b=K(1−a)`. This zero-order-hold conversion follows by integrating the first-order differential equation. It is not the same as Euler approximation `a≈1−Δ/τ`, which can produce misleading behavior at large Δ. MathWorks documents the ZOH convention for conversion of continuous LTI models to sampled systems. A real digital controller also has conversion, sampling jitter, computational latency, quantization, scheduling and delay; none are present in the toy update.

**Failure experiment:** sample one measured system at two rates, then claim that the faster rate always gives a better controller. With unknown high-frequency dynamics or noise, higher sampling can amplify bandwidth demands. Without measured sensor/actuator dynamics and processing delay, the model cannot predict real loop performance.

**Reusable packet:** provide τ, K, operating point, perturbation range, hold convention, Δ, actuator and sensor units, and whether parameters are observed, fitted or guessed. The calculator returns exactly this bounded model—not an unrestricted continuous-to-discrete converter.

## Bound reference topics

- **The exact first-order stable response assumes one real pole and no disturbance** (`equation`): firstorder-response
- **Exact first-order ZOH depends on held-constant input between samples** (`equation`): zoh-response
- **Continuous-time dynamics and sampled dynamics require an explicit hold convention** (`concept`): continuous-vs-discrete
- **Exact model discretization does not identify the actual plant** (`concept`): unknown-plant

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MATLAB-ZOH](https://www.mathworks.com/help/control/ref/dynamicsystem.c2d.html)
- [MATLAB-DISC](https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html)

**Limit:** no new experiments or independent control review.


---

# Chapter 03: Stability, equilibria, and model boundaries

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Stability must refer to a specific system and equilibrium. In the scalar autonomous recurrence `x[k+1]=a x[k]`, `x[k]=a^k x0`; hence asymptotic convergence to zero occurs exactly when `|a|<1`. For `|a|=1` the state need not decay, and for `|a|>1` nonzero states diverge in magnitude. This exact proof does **not** generalize to arbitrary nonlinear, time-varying or saturated systems by simply inspecting one number.

Continuous-time linear systems are stable when the relevant closed-loop poles have negative real parts, under usual finite-dimensional LTI assumptions. A nonlinear local linearization can be useful near an operating point, but a plant may have multiple equilibria, regions of attraction, actuator limits and physical states that cannot be expressed by the linear model. Lyapunov-function methods can certify specific regions if assumptions and derivative conditions are established; the existence of a simulation trace with bounded states is not itself a Lyapunov proof.

A supervisor-facing safety question should identify whether “stable” means bounded internal states, asymptotic regulation, robust stability across parameter variation, input-output boundedness or tolerance of sensor failures. These are not equivalent. A controller tuned on a stable simulated first-order process could still destabilize a plant with ignored dead time or wrong feedback polarity.

**Atlas refusal:** If actual poles, sampled operating point or physical constraints are not validated, do not label equipment safe, stable or production-ready. Report the model's mathematical pole condition and list missing physical checks.

## Bound reference topics

- **A scalar discrete pole strictly inside the unit circle is asymptotically stable** (`equation`): scalar-stability
- **Unit-circle boundary is not an asymptotic stability certificate** (`concept`): marginal-pole
- **Linearized local stability need not imply global nonlinear stability** (`concept`): local-stability
- **Open-loop stability cannot establish closed-loop safety** (`concept`): closed-loop-vs-plant

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MIT-STABILITY](https://underactuated.mit.edu/lyapunov.html)

**Limit:** no new experiments or independent control review.


---

# Chapter 04: Feedback, disturbances, and error

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A feedback loop observes an output, compares it to a reference and applies an action. The control objective should say whether it values setpoint tracking, disturbance rejection, energy consumption, actuator wear, transient overshoot or steady-state error. The same gains can perform differently across these tasks. Improving one objective can worsen another: increasing feedback gain often reduces low-frequency error, yet may amplify measurement noise or destabilize unmodeled dynamics.

A useful experiment prescribes separate **reference step**, **disturbance step**, **measurement-noise** and **model-uncertainty** trials with consistent units and recordable response metrics. Integrated absolute error, settling time, overshoot, actuation range and the number of saturated steps help compare specified simulations. None alone establishes safety. For example, a controller that quickly reaches setpoint might overshoot a safe process temperature or use an actuator at its maximum for too long.

Treat each performance measure as dependent on simulation time grid and disturbance design. Integrated absolute error with timestep Δ can be approximated as `Σ |r[k]−y[k]|Δ`, but the result should report whether error is sampled before or after actuation. Comparing different sampling rates without a common continuous physical metric can distort rankings.

A contextual package for AI should carry the declared performance objective, underlying model, actuator limits, observed versus estimated parameters, logs of failures and changes to controller gains. A toy gain optimization is not evidence that a real plant meets a reliability or regulatory requirement.

## Bound reference topics

- **Negative feedback regulates a chosen output but may excite dynamics or noise** (`concept`): negative-feedback
- **Setpoint tracking and disturbance rejection are different tests** (`concept`): reference-vs-disturbance
- **Integrated absolute error is a metric, not a safety criterion** (`method`): error-metrics
- **Sensor noise and high-frequency control action require a separate model** (`concept`): noise-sensitivity

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [FBS-PRESS](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems)

**Limit:** no new experiments or independent control review.


---

# Chapter 05: State-space reachability and observation

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

For a linear time-invariant state-space system, `x[k+1]=A x[k]+B u[k]`, `y[k]=C x[k]`, controllability asks whether permitted inputs can transfer the modeled state, and observability asks whether modeled internal states can be reconstructed from output history under assumptions. The general algebraic tests involve the controllability matrix `[B, AB, ..., A^(n−1)B]` and observability matrix stacking `[C; CA; ...; CA^(n−1)]`.

The v0.1 calculator specializes to exactly **two states, one input and one output**. It reports determinants of `[B,AB]` and `[C;CA]`, and compares absolute determinants against a caller-provided numeric threshold. A nonzero determinant is a mathematical full-rank condition in exact arithmetic. Near-singular matrices are numerically delicate, and absolute determinant tolerance changes under state scaling: this tool is a teaching calculation, not a condition-number-aware diagnostic for a calibrated system.

**Failure example:** measure only one output of a two-state system with an unstable hidden state; satisfactory output tracking does not prove all states remain bounded. Similarly, a controller cannot stabilize an uncontrollable unstable mode by wishing for a higher gain. Before trusting an observer, identify sensor geometry, units, noise and actual process dynamics. A model chosen by an agent is not validated merely by matching a short input/output trace.

Code records must remain paired with rank assumptions and explicit state-space units. The generic Forge retrieval layer should return those qualifications to an AI, not only the single boolean `controllable`.

## Bound reference topics

- **Controllability depends on A and B, not an attractive controller name** (`equation`): controllability
- **Observability depends on A and C, not merely repeated sensor readings** (`equation`): observability
- **Numerical rank thresholds depend on scaling and matrix conditioning** (`concept`): rank-tolerance
- **A visible output can hide unobservable internal instability** (`concept`): unobserved-modes

## Source pointers

- [PY-CTRB](https://python-control.readthedocs.io/en/latest/generated/control.ctrb.html)
- [PY-OBSV](https://python-control.readthedocs.io/en/latest/generated/control.obsv.html)
- [FBS-WIKI](https://fbswiki.org/)

**Limit:** no new experiments or independent control review.


---

# Chapter 06: Sampling, delays, and ZOH

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Ideal sampling theory states that a signal bandlimited below B hertz can in principle be reconstructed without aliasing if the sample rate exceeds `2B`, assuming appropriate anti-aliasing and reconstruction conditions. A safety controller must satisfy more than this. Its closed-loop bandwidth, delays, sensor filters, computation jitter and discretization errors affect stability and performance.

A sampled loop can alias high-frequency sensor disturbances into low-frequency readings. An actuator may hold its previous command between updates, creating a zero-order hold, or may follow interpolation or pulse-width modulation. The difference matters when modeling high-frequency behavior. Modern toolboxes expose multiple continuous-to-discrete conversion assumptions; selecting a method does not identify unmodeled fast modes.

**Worked distinction:** an ideal bandlimited signal with B=4 Hz, sampled at 10 Hz, satisfies `fs>2B`. That says nothing about whether a 10 Hz controller can regulate a high-bandwidth motor safely. Conversely, sampling a supposedly B=5 Hz signal at exactly 10 Hz does not satisfy the strict inequality used by the Atlas. A finite delay and narrow phase margin can defeat an otherwise plausible proportional controller.

A credible digital deployment report needs measured or bounded worst-case scheduling delays, sensor timestamps, actuator response, anti-alias filters, sample/hold behavior and an uncertainty model. The educational `nyquist_information` function returns a condition and its limits; it is not a control design tool.

## Bound reference topics

- **Nyquist strictly applies to a known bandlimited ideal-sampling signal** (`equation`): sampling-bandlimited
- **Sampling above twice bandwidth is not a controller-stability guarantee** (`concept`): sampling-not-control
- **A digital actuator command held between samples is a physical hold assumption** (`concept`): zoh-hold
- **Delays can consume phase margin even for a stable instantaneous plant** (`concept`): delay-phase

## Source pointers

- [MATLAB-ZOH](https://www.mathworks.com/help/control/ref/dynamicsystem.c2d.html)
- [MATLAB-DISC](https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html)
- [MATLAB-ALIAS](https://www.mathworks.com/help/signal/ug/aliasing.html)

**Limit:** no new experiments or independent control review.


---

# Chapter 07: PI/PID, saturation, and anti-windup

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Proportional action reacts to current tracking error; integral action accumulates error to eliminate persistent bias under applicable conditions; derivative action can anticipate a changing signal but is sensitive to noise and must be filtered. The gains depend on process dynamics and units. A controller with an integral term can accumulate a large internal value while the actuator remains saturated, then recover slowly when the reference drops.

MathWorks presents two documented anti-windup approaches—back-calculation and clamping—on a first-order process with actuator saturation and dead time. This Atlas implements only a **specific, discrete conditional integration** convention in a synthetic first-order, no-delay plant: `u=clip(kp*(r−y)+I, umin, umax)`. It freezes I when the proposed command is beyond a rail and the error would push it farther out; otherwise it integrates `I += ki Δt (r−y)`. The state update occurs after actuation via a zero-order-hold discrete model. The `none` mode integrates regardless of saturation.

The casebook gives an unreachable reference for a fixed interval and then lowers it. It compares model-integrated absolute error and final integrator values. Under the selected gains and synthetic plant, clamping improves its selected error metric. This is **not proof** that clamping always outperforms every other anti-windup design or that those gains are safe for an actual valve, heater or motor.

Any real controller change needs actuator limit and rate data, saturation strategy, reference range, sign of feedback, sensor noise, delays, failures, emergency interlocks, fail-safe mode, and approval. Never replace an existing safety loop's controller from a local Atlas numerical illustration.

## Bound reference topics

- **Integral action can wind up when actuator command exceeds physical limits** (`concept`): integral-windup
- **Conditional integration can limit integrator buildup in a saturated model** (`method`): clamping-antiwindup
- **A finite-step PI simulation must declare update order, limits, and sampling** (`equation`): pi-discrete-model
- **Anti-windup does not prove physical loop stability or optimality** (`concept`): antiwindup-not-proof

## Source pointers

- [MATLAB-AW](https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html)
- [FBS-WIKI](https://fbswiki.org/)

**Limit:** no new experiments or independent control review.


---

# Chapter 08: System identification and uncertainty

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A system-identification study attempts to infer a model from inputs and observed outputs. Even if the dataset is accurate, different models may fit the same limited trajectory. For example, a first-order process response observed over a narrow timespan may not reveal an ignored slow thermal mode or a delay. A single closed-loop trace may make actuator changes correlated with disturbances, complicating inference about the open-loop plant.

The experiment design must define excitation range, the steady operating point, measurement units, sampling clock, disturbance history and candidate model class. Parameter uncertainty should include instrument calibration, sensor drift, saturation, unmodeled modes, noise assumptions, and any prior engineering constraints. A fitted mean squared error is not a guarantee of correct uncertainty bounds, physical interpretation, robustness or ability to stabilize the actual machine.

A reasonable sequence is to collect timestamped excitation/response data under supervised and safe operating conditions; fit multiple physically plausible models; compare residuals and holdout behavior; challenge the models with independent disturbance cases; and conduct bounded sensitivity analysis for the intended controller. If an identification experiment cannot be done without violating production safety constraints, that is a limitation, not a reason to invent parameter values.

The current Control Atlas deliberately **does not fit plants from data**. All demo coefficients are supplied. This separation is an engineering safety boundary: a mathematical solver may work perfectly on a false or incomplete plant model.

## Bound reference topics

- **Identifiability requires informative excitation and an explicit candidate model** (`concept`): excitation-identification
- **Disturbance and controller action can confound a closed-loop identification** (`concept`): confounding-control
- **A good fitted response is not physical-model validation** (`concept`): fit-not-validity
- **Compare fitted dynamics on holdout inputs and disturbances** (`method`): heldout-disturbance

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MATLAB-DISC](https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html)

**Limit:** no new experiments or independent control review.


---

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


---

# Chapter 10: Finite-horizon optimal control and constraints

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

For a scalar discrete plant `x[k+1]=a x[k]+b u[k]`, consider a finite-horizon quadratic objective `Σ(q x[k]²+r u[k]²)+q_f x[N]²` with q and q_f nonnegative and r strictly positive. The optimal unconstrained policy under this exact model is `u[k]=−K[k] x[k]`, obtained from backward scalar Riccati recursion. With `S[N]=q_f`, `K[k]=b S[k+1] a/(r+b² S[k+1])`, `S[k]=q+a² S[k+1]−a b S[k+1]K[k]`.

The implemented function returns the gain sequence, cost-to-go coefficients, rollout trace and total cost. It verifies that the simulated quadratic cost agrees with `x0² S[0]` under floating-point tolerance. The casebook demonstrates an unstable open-loop coefficient a=1.1 stabilized over a short finite horizon by chosen gains—but no infinite-horizon certificate or real hardware data follows.

A true application must handle actuator and state constraints, disturbances, model mismatch, delay and safety barriers. If an unconstrained LQR asks for a physically impossible command, simply clipping it does **not** preserve optimality or the Riccati proof. Model predictive control solves a constrained optimization at each step but requires reliable computation timing and feasibility management. MIT Underactuated Robotics distinguishes unconstrained discrete Riccati methods from these harder constrained variants.

**Evidence gate:** record which cost is optimized, units and meanings of q/r, terminal cost assumptions, plant identification, constraints, disturbances, and worst-case numerical execution before making any deployment claim.

## Bound reference topics

- **Finite-horizon scalar LQR uses backward Riccati recursion** (`equation`): finite-lqr
- **Unconstrained LQR ignores actuator saturation and state constraints** (`concept`): lqr-unconstrained
- **Cost-to-go is defined by a user-chosen Q/R weighting, not universal optimality** (`concept`): lqr-cost
- **A low quadratic model cost is not evidence of good production control** (`concept`): lqr-no-real

## Source pointers

- [MIT-LQR](https://underactuated.mit.edu/lqr.html)
- [FBS-SUPPLEMENTS](https://fbswiki.org/wiki/index.php/Main_Page)

**Limit:** no new experiments or independent control review.


---

# Chapter 11: Robustness, margins, and small gain

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Control robustness asks whether intended behavior persists when model parameters, disturbances, delay, unmodeled dynamics or operating conditions vary. A nominally stable loop can fail under parameter drift, large excursions, actuator saturation or a new sensor configuration. Robustness is not identical to small nominal tracking error. It must be stated relative to an **uncertainty set**, a plant family and a performance/safety metric.

The small-gain theorem offers a useful **sufficient** stability condition for the feedback interconnection of suitably stable operators: if compatible induced-gain bounds satisfy `||G||·||Δ||<1`, the appropriate feedback system is stable under its assumptions. The simple helper multiplies two supplied nonnegative bounds; it does not estimate induced norms or verify that the interconnection matches the theorem. If the product is ≥1, this particular sufficient test fails, but that **does not prove** the actual system unstable.

This is a recurring evidence trap in agent-assisted engineering: a controller may optimize a toy robustness proxy and report a confident claim while the physical uncertainty set remains unknown. A credible statement should identify model uncertainty, structured/unstructured perturbations, delays, actuator limits, sensor noise, required frequency range and experimental evidence. The absolute values and model validity of any gain bounds need review.

A strong research program would compare robust performance across measured, uncertain plants with real test logs. This first edition has no real uncertain-plant dataset and no `H∞` synthesis. Its robustness chapter is a reference and refusal framework, not a new control theorem.

## Bound reference topics

- **Strict small-gain product is sufficient only for stable operator interconnection norms** (`equation`): small-gain
- **A failed sufficient small-gain check does not prove real instability** (`concept`): small-gain-not-necessary
- **Physical saturation/delay/noise invalidate simplistic gain arguments** (`concept`): robustness-nonlinear
- **Robustness results require uncertainty sets, frequencies and operating domain** (`method`): robust-design-ledger

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MIT-STABILITY](https://underactuated.mit.edu/lyapunov.html)

**Limit:** no new experiments or independent control review.


---

# Chapter 12: Verification, industrial safety, and AI knowledge reuse

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A control reference should help investigate systems and choose further evidence, not automatically deploy code. Industrial controls require verified physical failure modes, actuator design limits, sensor calibration, safe state, emergency stops/interlocks, operator review and validated rollback procedures. The Atlas does not provide hardware interfaces, PLC logic, network access or unattended actuation.

For each proposed controller, preserve the exact source model, parameter estimation method, controller revision, sampling period, actuator saturation and slew limits, anti-windup convention, sensor delay/noise, test protocols, observed outputs and uncertainty, and any safety rules governing the controlled plant. A system that passes its own unit tests still may be unsafe because the model omits the actual causes of failure.

**Knowledge and routing separation:** Signal, Cymatics, Measurement, Causal, Materials and Control remain independent source-bound domains behind one Forge contract. They expose versioned, qualified reference records that can be fetched and assembled without losing evidence limits. The future Bitwork-driven router should select candidate records, not overwrite the original statements or upgrade evidence maturity. Per the research-program owner, complete all thirty domain content libraries **before** new routing work, and transfer to desktop only after routing and integrated testing.

**Unresolved:** independent control-engineer review, experimental plant dataset, identified feedback controller test, robust stability verification across an uncertainty set, physical safety and regulatory approval, live AI answer-quality measurements, and Windows acceptance. These are scientific/deployment gates, not silently passed by a semantic version number.

## Bound reference topics

- **Controller deployment requires change control and monitored evidence** (`method`): controller-review
- **Retrieved reference text is data, never authority to actuate hardware** (`concept`): agent-tool-boundary
- **All thirty domain content libraries precede Bitwork routing and desktop transfer** (`method`): routing-last
- **Control v0.1 is source-linked scientific content, not complete control certification** (`concept`): control-maturity

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MATLAB-AW](https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html)
- [MIT-LQR](https://underactuated.mit.edu/lqr.html)

**Limit:** no new experiments or independent control review.


---

# 01. The control question, plant, and measurable target

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A controller is only meaningful relative to a physical or simulated **plant**, a desired **output**, a control input that can actually be applied, and disturbances and limits that can occur. A question such as “make the valve stable” does not define a measurable acceptance condition. Specify which measured variable should remain near which reference trajectory, what disturbance matters, what time scale is relevant, and which actuator and sensor are available. A controller can regulate a controlled output successfully while damaging equipment or increasing energy consumption elsewhere.

Basic notation: `x` is internal state; `u` is the commanded input; `y` is the measured or modeled output; `r` is the reference; `d` is a disturbance. In linear state-space representation, a locally valid model may be written `dot(x)=A x+B u+E d`, `y=C x+D u`. The matrices describe a declared model in given state coordinates. The user should not infer `A`, `B` and `C` from the hardware's name or from a chart screenshot. Different parameterizations can describe the same input-output behavior but give different internal-state interpretations.

Control design is a contract on **time** and **measurement**. An actuator can saturate, exhibit backlash, introduce delay, or respond asymmetrically. A sensor can drift, saturate, quantize, filter, or have a latency longer than the intended loop period. An unknown time base can reverse cause and effect in telemetry. Without calibrated measurements, claims of “99% improvement” can be false even when simulation errors shrink.

Declare four types of evidence separately: analytical identities; simulated behavior under stated models; recorded signals from actual equipment; independently validated closed-loop outcomes. A stable eigenvalue is an analytical model fact, not real plant stability. A well-fitted regression may still omit crucial dynamics. An author-created simulation is not a field trial. The control engineer needs versioned control code, equipment configuration and a rollback plan before any physical implementation.

**Worked framing:** a hypothetical thermal chamber should regulate measured air temperature after a door opening, subject to heater power, chamber heat capacity, fan dynamics, sensor delay and overtemperature protection. A first-order plant can be a starting approximation, not permission to disable independent hardware interlocks. A Control Atlas result should name the missing physical variables before suggesting tuning.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [CTMS-METHODS](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 02. Continuous-time responses and exact sampled holds

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A first-order model `tau dy/dt + y=K u` has time constant `tau>0`, static gain `K` and output `y`. With a constant step input held after t=0 and known initial y0, its exact continuous response is `y(t)=K u+(y0−K u)exp(−t/tau)`. Under this *single model*, the difference from the final value has decayed to 1/e after one time constant. It does not establish an actual device's response after one step because many physical systems include delay, higher-order dynamics, nonlinearities and disturbances.

Sampling changes the implementation. Under a **zero-order hold**, input u[k] stays constant during each interval of length Δt; the corresponding exact first-order difference equation is `y[k+1]=a y[k]+b u[k]`, with `a=exp(−Δt/tau)` and `b=K(1−a)`. Explicit Euler would give `a≈1−Δt/tau`, which can become unstable at coarse sampling even if the original continuous model is stable. This is a numerical-approximation defect, not a change in physical plant stability. The SciPy reference documents ZOH separately from Euler, backward difference and Tustin methods.

The Control package supplies analytic scalar solutions and the exact ZOH coefficients and iterates. It does **not** fit a real time constant, compensate sensor delay, simulate dead-time, or choose a safe controller for a device. Users must provide model units and sample timing. It rejects nonpositive time constants and sampling intervals, nonfinite inputs and excessive step sequences.

**Verification example:** set K=2, tau=3 s, Δt=.5 s, u[k]=1, y0=0. The exact discrete model has `a=exp(−1/6)` and `b=2(1−a)`. After six input holds, y[6]=2(1−exp(−1)) matches the continuous response at t=3 s. An independent SciPy `cont2discrete` calculation checks the same coefficients. The result is a unit test of the mathematical model, not experimental identification.

An input record should include sampling hardware clock, hold policy, actuator mapping, sensor filter, input/output data units, and evidence that the first-order approximation is applicable. Without those details, future context consumers may apply an algebraically correct equation in the wrong system.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [SCIPY-ZOH](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cont2discrete.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 03. Feedback, stability, poles and unmodeled disturbances

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A discrete scalar linear system `x[k+1]=a x[k]+b u[k]` under feedback `u[k]=−K x[k]` has transition `a−bK`. With the autonomous scalar closed loop, its deviations converge toward zero if `|a−bK|<1`. This **nominal model** statement is distinct from disturbance rejection, robust stability, safe actuator behavior, or local nonlinear stability. The model can be inaccurate or have unmodeled delays, and a gain that stabilizes one operating point can destabilize another.

In a two-dimensional linear discrete system, spectral radius of A below one is the usual asymptotic eigenvalue stability condition. The implemented two-by-two eigenvalue tool computes both real and complex conjugate poles and labels this a nominal autonomous system test. It does not handle a general high-order system, parameter uncertainty or actuator saturation. Pole location and oscillatory response should be interpreted with the sampling interval and physical state scaling.

Disturbances enter through unknown pathways as well as declared inputs. Negative feedback can reduce sensitivity to some disturbances but amplify sensor noise in others; some performance and robustness tradeoffs are unavoidable. Commanding high gain is not automatically better. Track both output error and control effort, plus equipment limits, sensor variance, delay and failure modes.

**Counterexample:** a synthetic unstable open-loop scalar has a=1.2 and b=0.5. Gain K=1 gives a closed-loop pole 0.7, nominally stable. If the actuator saturates so that `u=−Kx` is not physically implemented, the pole test is no longer the actual closed-loop dynamics. Conversely, a stable plant can be made unstable by overly aggressive feedback. These counterexamples prevent blanket recommendations based solely on sign or magnitude of gain.

A stability claim about a physical machine requires linearization validity, relevant operating regions, measurement of dynamics, uncertainty, constraints, fail-safe independent protection, and a controlled test procedure. This library does not operate equipment or claim safe deployment.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [PYCTR-DLQR](https://python-control.readthedocs.io/en/stable/generated/control.dlqr.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 04. Sample rates, aliasing, delay and digital clocks

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A digital control system records and acts at discrete times. The sample interval Δt and sample rate fs=1/Δt are not mere file metadata: they determine the discrete model, ability to observe changes and delay from sensing to actuation. If the sensor or controller clock slips, a model designed for uniform sampling may mis-estimate state or provide control too late. Sampling jitter, packet delays and asynchronous loops require their own verification.

For an ideal sinusoid of frequency f sampled exactly at rate fs, frequencies separated by multiples of fs can produce the same sample sequence, and a positive-frequency alias may be folded into `[0,fs/2]`. For instance a 70-Hz sinusoid sampled at 100 Hz has an alias magnitude of 30 Hz. The scalar `alias_frequency` function shows this arithmetic and explicitly refuses to identify the original physical frequency from samples. It does not undo aliasing or model finite-window spectral leakage, quantization, or nonuniform sampling. Proper anti-alias analog filtering is needed when the sampled input contains frequencies above the measurement bandwidth.

Time delay affects the phase relationship of plant and controller and can erode stability margins. A one-sample computational delay is not equivalent to no delay; a networked actuation path may have jitter and dropped commands. Increasing sampling frequency without sufficient CPU time, sensor bandwidth or anti-alias filtering can increase load without improving control quality.

**Practical test plan:** timestamp *both* command and measurement at acquisition and arrival; use calibrated clocks; record sample interval distribution and burst gaps; measure disturbance-bandwidth and sensor response; compare offline replay under real latency to assumed delay; monitor overruns and failover behavior. A frequency-domain margin estimate based on a nominal delay-free transfer function cannot be used for a controller with unmeasured network delay.

A source record should preserve units in hertz, seconds, sample index and radians/sample separately. Mixing these conventions is a serious, preventable error, especially when interpreting phase and frequency plots.

**Publisher/documentation scope:** [SCIPY-ZOH](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cont2discrete.html) · [MATH-ALIAS](https://www.mathworks.com/help/daq/making-quality-measurements.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 05. State-space reachability and controllability

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Reachability asks whether admissible inputs can move a state from one condition to another within a declared model and time horizon. For a finite-dimensional linear time-invariant pair (A,B), the classical controllability matrix is `[B, AB, A²B, ... A^(n−1)B]`. Full row rank n is the unconstrained linear controllability criterion. This does not establish that actuators have sufficient magnitude, satisfy rate limits, or can safely produce that trajectory.

The bounded Control tool implements only a **two-state, single-input** case: A is 2×2, B a two-vector, and the controllability determinant of `[B,AB]` indicates exact rank in ideal arithmetic. In floating-point arithmetic, a small determinant can also indicate poor scaling or conditioning; the tool's relative threshold is a declared heuristic rather than a rigorous numerical conditioning bound. The Python Control Systems Library documents `ctrb` for general state-space matrices, but no library here infers a real physical A/B model.

A simple double-integrator sampled position/velocity model is `A=[[1,Δt],[0,1]]`, `B=[[0],[Δt]]`. Under a nonzero Δt it is controllable algebraically. Yet if the actuator can accelerate only within a limited range, the set of reachable safe states in a fixed horizon may be far smaller. The system's state variables and coordinate units must be declared before comparing determinants across parameter choices.

**Counterexample:** choose B=[1,0] and diagonal A=diag(0.8,0.9). The second state cannot be influenced by this input; the determinant is zero. Increasing feedback gain cannot control an inaccessible state. Adding an unmodeled actuator that changes B would be a new system design, not a numerical improvement to the existing one.

When using this reference for industrial or agentic systems, note that mathematical state reachability is not evidence of goal achievement, agent reliability or a real device's actuators. Cross-domain metaphors must not be promoted into physical control claims.

**Publisher/documentation scope:** [PYCTR-CTRB](https://python-control.readthedocs.io/en/stable/generated/control.ctrb.html) · [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 06. Observability and state estimation

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A system can contain internal states that are not directly measured. Linear observability asks whether state trajectories can be reconstructed in principle from a known dynamics matrix A and output C across time, under the model and appropriate input information. The classical observability matrix is `[C; CA; ...; CA^(n−1)]`; full column rank n gives the unconstrained linear observability criterion. Observability does not guarantee a practical observer will perform acceptably under noise, poor sampling, quantization or uncertain dynamics.

Our two-state single-output tool computes the determinant of `[C;CA]` alongside controllability and the nominal matrix poles. The result is an explicit teaching calculation rather than a general numerical rank solver. Coordinate scaling can make a determinant small even when mathematical rank is full, so the result must carry the chosen tolerance and state units.

**Example:** if A is diagonal and C=[1,0], only the first autonomous state is measured; the second cannot be inferred from output history in this uncoupled model. If dynamics couple the second state into the observed state, it may become observable. Merely increasing the sensor sampling rate cannot resolve an unobservable mode with no measurement pathway.

The scalar Kalman update included in this Atlas predicts one state and variance, then combines a directly observed measurement through a supplied process-noise variance Q and measurement-noise variance R. It is a one-step model with known dynamics and declared covariance—not a calibrated multi-sensor state estimator. Estimation uncertainty is conditional on process and measurement assumptions, and bad noise covariances produce misleading confidence even when code is numerically stable.

A physical state observer needs sensor placement, calibration, actual noise spectra, latency and an independent validation record. A state inferred by an observer is not a measurement, nor does a filtered signal identify its physical cause automatically.

**Publisher/documentation scope:** [PYCTR-OBSV](https://python-control.readthedocs.io/en/stable/generated/control.obsv.html) · [PYCTR-LQE](https://python-control.readthedocs.io/en/latest/generated/control.lqe.html) · [MIT-STATE](https://underactuated.mit.edu/state_estimation.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 07. PID control, saturation, windup, derivative noise

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Proportional-integral-derivative (PID) control combines a term proportional to tracking error, accumulated error and a rate term. It is widely useful but is not one universal algorithm: continuous/discrete implementation, error/measurement derivative choice, integral discretization, filtering, setpoint weighting and output saturation matter. A gain tuple with no sample time, actuator limits or derivative convention is underspecified.

Integral action can drive steady errors toward zero under suitable plant conditions, but an actuator with hard limits cannot produce any demanded command. If the integrator accumulates while the actuator remains saturated, the stored integral may delay recovery after the setpoint changes. MathWorks documents distinct clamping and back-calculation antiwindup policies; they are not interchangeable. Derivative action can amplify measurement noise and is commonly filtered or taken on measurement rather than setpoint to avoid derivative kick.

The Atlas's `pid_saturated_demo` applies a simple **conditional integration clamp** to supplied setpoint and measurement sequences, with derivative on measurement. It returns P, I, D, raw command, saturated command and a saturation flag. It **does not simulate a physical plant or close a feedback loop against measured device data**. Comparing traces with and without clamping demonstrates only internal controller arithmetic. The implementation is intentionally not an industrial PID tuning assistant.

**Teaching counterexample:** with a large positive error and a command constrained to ±1, an unconstrained integral term can grow without bound over repeated samples while the actual output stays at +1. Conditional integration prevents further accumulation when it would deepen saturation, but cannot determine whether the chosen gains are stable for an unknown plant. Actuator backlash, rate limits and dynamic dead-time remain outside the trace.

A real PID review must preserve controller sample time, controller form, saturation/tracking logic, derivative filtering, sensor calibration and placement, setpoint policy, disturbance tests and independent safety interlocks. No user should send these test commands directly to a real valve or heater.

**Publisher/documentation scope:** [MATH-PID-AW](https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html) · [MICH-PID](https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 08. System identification: excitation, bias and validation

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

System identification estimates dynamics from observed inputs and outputs. A fitted model is not simply a regression on any available log: experiment design, signal excitation, time alignment, missingness, feedback, nuisance disturbances, noise and model structure determine what is identifiable. MathWorks' workflow explicitly separates data assessment, model selection, model fitting and validation; it advises checking excitation and comparing different structures rather than declaring the best training fit correct.

The Atlas implements a narrow scalar no-intercept model `x[k+1]=a*x[k]+b*u[k]` with the state x known directly and an input u at the correct time. It solves an ordinary least-squares two-parameter normal equation and rejects a singular or poorly excited input/history design. It returns residual sum of squares and parameter estimates, **not** confidence intervals, an identified physical plant, or independent held-out validation. A perfect in-sample RSS can occur in a synthetic noise-free model that shares none of the real system's nonlinearities.

**Excitation counterexample:** with constant state history and input always zero, the data cannot separate a from b; a numerical solver could return arbitrary plausible values. This Atlas refuses. Another failure occurs if a feedback controller automatically responds to unmeasured disturbances; the input may correlate with disturbances, biasing simple least squares. Adding more of the same confounded data does not necessarily fix the model.

A realistic identification protocol begins with a timestamped experimental plan: input ranges and safe excitation, sensor clock accuracy, preparation state, held-out validation windows that cover relevant operating conditions, model selection criteria, residual tests, uncertainty and rollback of incorrect models. Distinguish data used to fit a model from data used to test it. If out-of-sample performance is not available, report the estimate as an in-sample teaching fit only.

System identification is not causal inference by default: model fitting can describe signal dynamics without proving an intervention's effect or mechanism. Causal Atlas should be consulted when changes in operations or treatment assignments are the scientific question.

**Publisher/documentation scope:** [MATH-ID](https://www.mathworks.com/help/ident/gs/system-identification-workflow.html) · [MATH-ID-QUALITY](https://www.mathworks.com/help/ident/gs/about-system-identification.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 09. Optimal control: scalar discrete LQR

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Linear quadratic regulation (LQR) chooses feedback for a **known** linear model and quadratic objective. In discrete time, a scalar model is `x[k+1]=a*x[k]+b*u[k]` and an infinite-horizon cost is `Σ (q*x[k]^2+r*u[k]^2)`. With q>0, r>0 and b nonzero, a stabilizing scalar Riccati solution P and linear control `u=-K*x` can be computed exactly within numeric limits. This is an **unconstrained** problem: the optimum may require physically impossible actuator commands.

The scalar discrete algebraic Riccati equation is `P=q+a²P−(a*b*P)²/(r+b²P)`. The solution with P>0 yields `K=(b*P*a)/(r+b²P)`. The Atlas's `scalar_lqr` computes the positive stabilizing solution and rejects unactuated scalar cases and numeric overflow. Python-control's `dlqr` and MIT's LQR chapter supply the authoritative general matrix context; the installed package implements only the scalar special case, not a general Riccati solver or model predictive controller.

**Example:** for a=1.2, b=1, q=r=1, the controller can find a K that places the nominal closed-loop pole inside the unit circle. But if |u|<=0.2 and the state starts large, the command may saturate; the scalar LQR guarantee does not apply to the saturated system. Penalizing control effort more heavily also changes the optimal gain, not necessarily the actual closed-loop safety margin.

LQR is a controller solution conditional on an assumed model and a chosen objective. The weights are design choices, not learned moral preferences or absolute engineering importance. Before deployment, perform plant identification, uncertainty modeling, constraint handling, disturbance tests, robust stability analysis and independent safety review. Advanced multiparameter optimization and MPC remain reference topics, not implemented capabilities.

**Publisher/documentation scope:** [MIT-LQR](https://underactuated.mit.edu/lqr.html) · [PYCTR-DLQR](https://python-control.readthedocs.io/en/stable/generated/control.dlqr.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 10. Noise, Kalman updates and hidden-state assumptions

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A Kalman filter is an estimation framework under linear dynamics with specified process and measurement noise statistics. An observer can reduce mean-squared estimation error when its model and covariances are appropriate; it cannot magically recover information that the sensor does not provide. If a sensor has an unknown bias or shares disturbances with the process, a simple Kalman model with independent zero-mean noise may be confidently wrong.

For a scalar discrete step, predict mean μ−=a μ and variance P−=a²P+Q. With direct measurement y and independent measurement-noise variance R>0, the gain is `K=P−/(P−+R)`, posterior mean μ+=μ−+K(y−μ−), and posterior variance `(1−K)P−`. The Atlas computes this one step. It does not estimate Q or R from data, implement covariance cross-terms, detect outliers, handle missing measurements, estimate delay or fuse sensors.

**Variance interpretation:** P is conditional on the stated model. A small posterior variance is not a guarantee of closeness to truth if process noise, sensor bias, or the dynamics matrix are wrong. Noise may be colored, heteroscedastic or state dependent. During calibration drift a filter may report unrealistically small uncertainty. A safe research report should compare predicted residuals to actual holdout measurements, inspect innovation autocorrelation and test parameter sensitivity.

Control Atlas therefore separates observed measurement records from estimated state records. Measurement Atlas holds calibration conventions, uncertainty budgets and source provenance. The AI context assembler must preserve both the predicted state and its assumptions rather than rendering the estimated mean as “the sensor measured X.”

**Publisher/documentation scope:** [PYCTR-LQE](https://python-control.readthedocs.io/en/latest/generated/control.lqe.html) · [MIT-STATE](https://underactuated.mit.edu/state_estimation.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 11. Robustness, uncertainty, delay and safety limits

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Nominal stability is a mathematical fact about a particular model. Robust stability concerns whether the controlled system remains stable for a declared set of plausible model perturbations. Robust performance additionally concerns tracking and disturbance responses under those perturbations. Neither follows solely from the fact that a nominal state matrix has eigenvalues inside the unit circle. Real systems experience gain variation, nonlinear friction, temperature-dependent parameters, timing delay, actuator saturation and sensor drift.

A first-order model can fail when a time delay dominates response. Controller gains tuned against a zero-delay model may increase oscillation or produce overshoot after delay is introduced. Similarly, nominal state feedback may demand unlimited input even though the motor/valve/controller has finite range or rate. The mismatch is a change in the implemented closed loop, not a violation of linear mathematics. Robust controller design requires a stated uncertainty family and the correct physical constraints.

A stability margin report should include measurement and model frequency ranges, gain/phase conventions, identified delay, sample frequency, actuator limits, variability among operating conditions, sensor noise, and validation against held-out response data. A single Bode plot is not a guarantee: phase wraps, noise and unmodeled resonances can distort estimates. A controller with no explicit fallback or independent safety limit should not be promoted into equipment operation based on synthetic testing.

The current release does not compute generic H-infinity controllers, structured singular values, root-locus tuning, Nyquist encirclements, nonlinear Lyapunov proofs, safety certificates, or time-delay margins. Those are documented future references. It does compute basic nominal poles, two-state reachability and one scalar LQR gain. The output labels prevent downstream AI users from silently upgrading this into robust-system certification.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [MICH-PID](https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 12. Constrained control and model predictive planning

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Model predictive control (MPC) repeatedly optimizes a finite-horizon control sequence under a model and constraints, applies the first action, and resolves as new state information becomes available. The mechanism is general but guarantees depend on objective, terminal conditions, model uncertainty, constraint feasibility, estimator accuracy and solver behavior. Merely simulating a model for several steps is not MPC; nor is a scalar LQR gain with clamping automatically an optimal constrained controller.

A realistic constrained plant has input limits, state constraints, rate constraints and sometimes mixed-integer operating modes. The optimization can become infeasible if no available actuation can satisfy all constraints, particularly with delayed or changed dynamics. A controller that silently returns any finite input after an infeasible problem may be unsafe. The correct behavior includes explicit feasibility status, fallback rules and independent enforcement of hard physical limits.

Our bounded LQR and PID demonstrations intentionally remain separate from an MPC implementation. They illustrate two key failure modes: an unconstrained optimal gain can request an impossible input; and a saturated integrator can accumulate error in ways that harm recovery. A future research implementation should not be adopted without measured model validity, solver timing budgets, infeasibility traces, adversarial disturbances and explicit shutdown policy.

Study questions: Can an MPC objective express an equipment safety requirement that is not modeled as a constraint? What happens if a late sensor packet arrives after the optimization horizon was formed? How should a controller distinguish an infeasible model from a temporarily unavailable sensor? These are design questions, not problems that adding more model parameters automatically solves.

**Publisher/documentation scope:** [MIT-LQR](https://underactuated.mit.edu/lqr.html) · [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 13. Fault detection, diagnosis and operational evidence

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Fault detection asks whether observed behavior deviates from a declared normal model. Fault isolation asks what mechanism caused the deviation. They are not the same task. A residual spike may reflect a stuck valve, instrument drift, changed input, material changes, calibration error or a shifted operating point. A high-dimensional model may predict a change without identifying the responsible physical component.

For a linear predictor, a residual `e[k]=y[k]−yhat[k]` can be examined across time, inputs and environmental conditions. Correlation and periodic structure in residuals can reveal unmodeled dynamics, but not all patterns are component-specific. Positive predictive power in an authored simulation is not evidence of real fault detection on independently measured equipment.

A defensible diagnostic plan preserves the timestamps of commands, measurements, maintenance, product batches and alarms; sensor and controller versions; model training and validation windows; the operating range; confounders; and a controlled comparison to a baseline or alternate sensor. Do not treat a changed software version as causal proof that software created a physical defect without controlled evidence.

This Atlas has no actual industrial fault dataset, no deployed fault detector and no authority to actuate or bypass safeguards. Manufacturing Atlas will cover physical process diagnosis, while Causal Atlas handles experimental attribution. Control Atlas holds dynamic-model reasoning and the measurement/observability conditions required to make a claim meaningful.

**Publisher/documentation scope:** [MATH-ID](https://www.mathworks.com/help/ident/gs/system-identification-workflow.html) · [MATH-ID-QUALITY](https://www.mathworks.com/help/ident/gs/about-system-identification.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# 14. Evidence maturity, integration contracts and method selection

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

An Atlas is a source-grounded research reference, not a single algorithm. Every control claim should identify plant class, time domain, state/input/output definitions, units, model-identification method, fit residuals, sensor/actuator constraints, uncertainty, source and inspected portion, and known unsupported conditions. Mathematically correct calculations receive a “conditional model result” status, not “experimentally verified control capability.” Synthetic test cases and installed wheel checks only show implementation behavior.

The shared Forge common contract already supports exact immutable record revisions, source links, typed relations and context assembly with assumptions and limitations. Control's first release must use that contract without changing existing domain-specific routing. The user has instructed that all thirty domain knowledge libraries be completed first; routing and Bitwork integration must be addressed only after that, followed by final integrated validation and computer transfer. Starting another node does not authorize modifying the user's desktop, publishing GitHub repositories or calling unfinished science complete.

**Method-selection examples:** for a first-order time constant, use the analytic/ZOH model and test the assumption against data. For unknown dynamics, design an identification experiment rather than guessing gains. For a two-state linear model, test reachability and observability before selecting a controller/observer. For a target under saturation, use a controller implementation that explicitly handles limits. For a stochastic hidden state, validate sensor noise assumptions before relying on an estimator. For complex constraints, research MPC rather than pretending scalar LQR is equivalent.

The next phase should deepen Control's source coverage, add actual appropriately licensed measured-system data with calibration records, compare independently estimated models, run real timing/constraint tests and expand robust control. v0.1 is a substantive foundation, not a finished v1. Scientific completeness, live Bitwork/AI routing and native Windows acceptance remain unresolved by design.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [MATH-ID](https://www.mathworks.com/help/ident/gs/system-identification-workflow.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.


---

# Investigation 01: First-order response versus sampled-model claims

**Origin:** synthetic authored model, no real equipment.

First-order step with tau=10 s reaches about 63.2% of the step by t=10 s. Exact ZOH for tau=5 s, gain=2 and dt=.5 s gives a=e^-0.1 and b=2(1-a). This checks the *stipulated model*, not real machine dynamics. If a second unmodeled pole or delay exists, the same response data may not support these calculations for future excitation. Require measured frequency/step data, actuator calibration, latency and independent holdout disturbances before using for control.

**Source:** https://www.mathworks.com/help/control/ref/dynamicsystem.c2d.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.


---

# Investigation 02: Hidden-state reachability and observability

**Origin:** synthetic authored model, no real equipment.

The discrete double integrator A=[[1,1],[0,1]], B=[0.5,1], C=[1,0] gives nonzero controllability and observability determinants. If B=[0,0], the state is not controllable no matter what gain is chosen; if C=[0,0], no state is visible. These are algebraic statements, not sensor-placement certification. Determinant tolerance is scale-dependent; report state/actuator/measurement units.

**Source:** https://python-control.readthedocs.io/en/latest/generated/control.ctrb.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.


---

# Investigation 03: Saturated PI and anti-windup counterexample

**Origin:** synthetic authored model, no real equipment.

A constructed first-order process receives an unreachable reference followed by a smaller one. The simple PI implementation accumulates integral error if configured without anti-windup. Clamping freezes further integration when error pushes beyond a saturated rail, improving the selected integrated absolute error in this particular test. No generalized optimal-gain theorem follows. Add actuator delay, rate limits, sensor bias, interlocks and failure trace to test real equipment.

**Source:** https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.


---

# Investigation 04: Kalman confidence under a wrong sensor model

**Origin:** synthetic authored model, no real equipment.

A scalar filter given process variance .01, measurement variance .1 and selected synthetic readings produces a decreasing variance and a posterior estimate. If the sensor has an unmodeled constant bias, its reported covariance need not cover the true state; increasing the number of readings can make it confidently wrong. The local filter does not estimate covariance from data, handle correlated noise or filter a real sensor stream.

**Source:** https://underactuated.mit.edu/state_estimation.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.


---

# Investigation 05: LQR model objective versus hard physical constraints

**Origin:** synthetic authored model, no real equipment.

For an assumed discrete scalar plant a=1.1,b=1 and weights q=1,r=.1,terminal=1 over eight steps, backward Riccati gains minimize the *unconstrained* quadratic objective. Its rollout cost matches x0^2 S0. If the first command exceeds actuator limits, clipping invalidates the unconstrained optimum; this package does not silently call clipped LQR optimal. A real model-predictive controller would need constrained optimization with feasibility, latency and safety checks.

**Source:** https://underactuated.mit.edu/lqr.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.


---

# Investigation 06: Sampling and robustness logical refusal

**Origin:** synthetic authored model, no real equipment.

A 10 Hz sample rate fails the strict ideal sampling condition for a 5 Hz bandlimited signal. An 11 Hz sample rate passes that condition but does not prove any feedback controller stable. Likewise, hypothetical stable-gain bounds .6 and .7 multiply to .42 (<1), a sufficient *conditional* small-gain test; product above 1 is inconclusive about instability. These tools prevent replacing qualified engineering reasoning with generic green status flags.

**Source:** https://www.mathworks.com/help/signal/ug/aliasing.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.


---

# Investigation 01. Exact sampled response versus unstable approximation

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A hypothetical system follows the specified first-order model `tau*dy/dt+y=K*u`, with gain K=2, time constant tau=3 s, zero initial state and a unit step. There are no measured physical signals. The continuous analytical response at three seconds is `2*(1-exp(-1))`. For a zero-order held input sampled every half-second, the exact discrete state uses `a=exp(-1/6)`, `b=2*(1-a)` and six input holds. The discrete result matches the analytic response to floating-point precision. This is a controlled internal numerical identity, not a plant identification or a controller-quality assessment.

A naive implementation might instead use explicit Euler with a sample interval much larger than the time constant, so its discrete coefficient `a_E=1-dt/tau` can fall outside the unit circle even though the original continuous first-order plant is stable. The correct investigation must distinguish an unstable numerical approximation from an unstable physical system. Check the chosen hold type and sample timing rather than treating every discretization as equivalent.

**Evidence needed for a real device:** timestamps, actuator hold policy, actual sampled input/output signals, sensor calibration, unknown dead-time and operating conditions. **Refusal:** the calculator cannot infer whether a real heating chamber responds as a first-order plant. **Sources:** SciPy `cont2discrete` documentation and Åström–Murray, *Feedback Systems* chapter scope.


---

# Investigation 02. A feedback pole moves, but actuator safety is unproven

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

The synthetic scalar discrete model has a=1.2 and b=0.5. With no state feedback, the pole has magnitude 1.2 and the ideal autonomous model is unstable. A gain K=1 in `u=-K*x` moves its pole to 0.7, nominally stable. The result says nothing about what happens if the actuator cannot deliver the requested input. If `|u|<=.1`, a large error cannot be corrected by unconstrained linear feedback as modeled. Declaring a safe system based solely on the pole test would change a mathematical label into a real-world claim it does not support.

A real acceptance test must use an identified plant with model uncertainty, actuator saturation, sensor delay, disturbance envelopes and appropriate hardware interlocks. The original synthetic numbers are deliberately chosen; the Atlas makes no claim that a particular motor, factory valve or temperature system has these parameters.

**Refusal:** no optimal gain or safety setting is authorized for an actual device. **Sources:** Åström–Murray, *Feedback Systems* and MIT's scalar LQR context.


---

# Investigation 03. Controllable model, unreachable constrained state

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A two-state sampled double-integrator model uses `A=[[1,dt],[0,1]]`, `B=[0,dt]` and a measured position `C=[1,0]`. For nonzero dt, the ideal controllability matrix has full rank and the observability matrix can be full rank as well. These properties describe the local unconstrained linear model. They do not say the state can be reached within a short horizon under finite force or that a motion plan avoids hazards.

Compare a decoupled pair of states with `A=diag(.8,.9)`, `B=[1,0]`, `C=[1,0]`. The second state is neither reachable through the given actuator nor observable through that output. Increasing K or improving arithmetic precision does not create a missing physical actuation or sensor path. Adding a new sensor or actuator would change the model and the engineering design.

**Evidence needed:** validated A/B/C matrices, state units/scaling, actuator limits, sensor positions and noise, and actual finite-horizon constraints. **Sources:** python-control `ctrb` and `obsv` documented rank tests.


---

# Investigation 04. A saturated controller can accumulate hidden integral error

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A synthetic PID trace holds setpoint 10 and measured output 0 for eight samples, using Kp=1, Ki=.5, Kd=0, dt=1 s and actuator bounds [-1,1]. Without antiwindup, the controller integral accumulates despite the actuator being pinned at +1. With the stated conditional-integration clamp, the integral is frozen while the candidate update would deepen saturation. Both traces have clamped physical *commands*, but very different stored controller state. A later reversal in error could therefore lead to different recovery behaviors if a real plant were attached.

The example is **controller arithmetic**, not a closed-loop experiment or automatic tuning result. A different PID implementation might integrate after saturation, use a back-calculation coefficient, filter derivative terms or implement separate tracking antiwindup. None is universally superior without plant-specific evidence and safety constraints.

**Missing evidence:** actuator transfer function, sample time jitter, rate constraints, plant delay, noise and real disturbance tests. **Source:** MathWorks Anti-Windup Control example, selected R2026b documentation.


---

# Investigation 05. A 70 Hz oscillation appears at 30 Hz after sampling

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

An ideal sinusoid at 70 Hz sampled at fs=100 Hz is represented by an alias frequency magnitude of 30 Hz. The samples alone can be compatible with a lower-frequency sinusoid under a suitable phase relationship. The Atlas computes the folded frequency but does not estimate the original physical frequency, resolve phases or recover information removed by undersampling.

A control engineer attempting to suppress a mechanical resonance from an aliased accelerometer trace could target the wrong mode. The solution begins with measuring actual sensor bandwidth, analog anti-alias filtering, clock jitter and sampling rates before fitting a model. An FFT of a short or gapped time series can also exhibit leakage and other artifacts not represented in this one-line formula.

**Refusal:** this package does not identify a physical resonance or reconstruct a unique signal. **Source:** MathWorks Making Quality Measurements antialiasing guidance.


---

# Investigation 06. A perfectly fitted teaching plant may still identify nothing real

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

Supply an authored noise-free sequence satisfying `x[k+1]=0.8*x[k]+0.3*u[k]` over several deliberately varied input values. A two-column least-squares fit recovers a and b and gives a residual sum of squares near zero. That is correct for the constructed dataset, not evidence that a manufacturing process has those dynamics. The data were generated from the same model being fitted, so no independent model validation has occurred.

Set every input and state to zero and infinitely many a/b pairs reproduce the same data. The regression matrix is rank deficient; a numerical solver could return finite coefficients but they would not be identified. The Atlas refuses this case. In closed-loop physical data, input commands may correlate with disturbances, biasing naive least squares even when the matrix has full rank. A credible study should use safe excitation, calibration, timestamp synchronization and separate testing periods across operating regimes.

**Source:** MathWorks System Identification Workflow and data-quality requirements. **Refusal:** in-sample fit is not a causal or robust plant identification certificate.


---

# Investigation 07. A stabilizing LQR gain can demand impossible input

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

For `x[k+1]=a*x[k]+b*u[k]` with a=1.2, b=1 and weights q=r=1, solve the scalar discrete algebraic Riccati equation and compute the stabilizing gain. The nominal closed-loop pole falls inside the unit circle. The mathematical result solves the stated infinite-horizon quadratic problem, not a constrained optimal-control problem. If the plant has limited actuator range, the commanded `u=-K*x` may be unavailable at a large state error.

The weights are choices reflecting a design objective, not automatically discovered values about the importance of comfort, reliability, cost or safety. Varying r changes the controller's willingness to use effort. The plant parameters themselves may change with temperature, load or wear. A real design needs uncertainty, feasibility, actuator limits and independent protection.

**Sources:** MIT Underactuated Robotics LQR chapter and python-control `dlqr`. **Refusal:** no hardware gain is recommended by this synthetic test.


---

# Investigation 08. A Kalman covariance is conditional, not truth

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A scalar filter begins with prior mean 0, prior variance 1, known a=1, process variance Q=.25 and measurement variance R=.25. Given a measurement y=2, its predicted variance is 1.25, Kalman gain 5/6, posterior mean 5/3 and posterior variance 5/24. Each value follows the specified noise model. A real sensor could have drift or correlated noise that the model omits. In that case the reported posterior variance can be much smaller than the true estimation error.

A state estimator must not turn an inferred latent variable into a direct sensor measurement. Real validation requires residual distributions, calibration, timing and independent reference measurements, plus assessment of assumptions such as Gaussian noise and unbiased direct observation. The included method is a one-step scalar update, not a deployed multi-sensor tracker.

**Source:** python-control Kalman estimator reference and MIT state-estimation chapter navigation. **Refusal:** a small posterior covariance alone is not a calibration or accuracy certificate.


---

# Investigation 09. Modeling a delay matters more than a larger gain

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A feedback design can appear well behaved in a simulated first-order plant with instantaneous sensing and actuation, then oscillate when a physical sensor and valve introduce dead-time. A sample arriving late is not equivalent to a timely state reading. Saturation can also break the assumed linear law, so eigenvalue checks of an unconstrained model no longer describe the actual controller.

This investigation is deliberately a **design audit rather than an implemented delay simulator**. It enumerates data needed to test a real system: command/response timestamp traces, actuator rate limits, sensor filtering, nonlinear operating regions, sample drops and protected fallback behavior. It refuses to infer a robust stability margin without such information, even if a nominal pole calculator returns “stable.”

**Sources:** Åström–Murray feedback scope, Michigan control tutorials and MathWorks antiwindup example. **Outcome:** risk and evidence list, no physical action.


---

# Investigation 10. A changing residual is not proof of a faulty component

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

Suppose a dynamic model predicts a stable process, but the measured output drifts after a software release. A residual increase may reflect a controller bug, a sensor calibration change, a different material lot, altered temperature, physical wear, unmodeled load, or timestamps being shifted by the logging pipeline. The residual is evidence of disagreement with the model, not a unique root cause.

A discriminating investigation would retain command and measurement time series across runs, controller and machine versions, maintenance/calibration logs, operating and environmental conditions, and a controlled rollback plan. Causal Atlas provides study-design principles for attributing intervention effects. Measurement Atlas provides uncertainty and calibration concepts. Control Atlas retains the dynamic explanation without conflating these domains.

**Source:** MathWorks System Identification documentation (model validation and residual analysis). **Refusal:** this package cannot diagnose a specific real machine or infer an equipment repair from a synthetic residual.


---

# Investigation 11. A retrieved feedback formula must keep its operating assumptions

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

An AI system searching for “PID gain” may retrieve a technically correct equation but omit actuator limits, dead-time or the controller discretization convention. An assembled reference that contains only the formula can be more misleading than no answer. The shared Forge contract requires exact record revisions, source closure, assumptions, limitations and explicit abstention when evidence is insufficient.

A control result must be rendered as a **conditional mathematical tool** with model type, sample interval, input/output units, nonlinearity and uncertainty limits. It must not be treated as a command to actuate a real system. The user has deferred Bitwork routing until all thirty domain libraries are complete. This investigation tests only static reference compatibility; it does not operate Bitwork or improve a measured AI answer.

**Sources:** original Atlas evidence contract and Åström–Murray control text scope. **Refusal:** no automatic real-world gain selection or tool execution is authorized.


---

# Investigation 12. Designing the next experiment rather than inventing a controller

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A new industrial process has a variable error and unknown plant dynamics. Which method should an investigator use? The research sequence is: (1) define target and hazard constraints; (2) inspect sensor/actuator bandwidth, time and units; (3) collect input/output data with safe excitation; (4) choose candidate model classes and compare held-out prediction; (5) test controllability and observability; (6) select a control strategy considering constraints and uncertainty; (7) validate with disturbances under independent protection; (8) record failures, rollback capability and model revisions.

If no plant data exist, there is no honest unique tuning answer. A first-order demonstration and scalar LQR can teach equations, but they cannot substitute for physical identification, robust control or a qualified commissioning plan. A larger model does not repair missing sensor paths, and a higher test count does not prove a field system safe.

**Sources:** System Identification Workflow (MathWorks R2026b), Caltech Feedback Systems (Åström–Murray) and Michigan Control tutorials. **Outcome:** research protocol and scoped abstention, no field implementation.


---

# Source register and limits

# Control Atlas selected source register — 2026-11-12

**Source-scope limits:** only cited public pages, summaries or identified sections were inspected; no full copyrighted books or restricted materials are mirrored. A source card does not confer independent peer review of this Atlas.

## FBS-WIKI: Feedback Systems, 2nd ed. author-maintained wiki

- Publisher/author: Åström and Murray
- URL: https://fbswiki.org/
- Inspected: Official text overview, listed chapter and supplement topics; full book text not independently audited
- Access: author-maintained home and topic overview
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## FBS-PRESS: Feedback Systems textbook edition metadata

- Publisher/author: Princeton University Press
- URL: https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems
- Inspected: Second edition publication metadata and table of contents; not copied book
- Access: publisher metadata
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## MIT-LQR: Underactuated Robotics, Chapter 8 LQR

- Publisher/author: MIT CSAIL / Russ Tedrake
- URL: https://underactuated.mit.edu/lqr.html
- Inspected: Discrete-time Riccati recursion, finite-horizon LQR, constrained extension; selected online chapter
- Access: public technical chapter portion
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## MIT-STATE: Underactuated Robotics, State Estimation

- Publisher/author: MIT CSAIL / Russ Tedrake
- URL: https://underactuated.mit.edu/state_estimation.html
- Inspected: Observer/Kalman filter topical framework; page overview, not full estimation derivation
- Access: author online chapter overview
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## MATLAB-ZOH: c2d continuous-discrete model conversion

- Publisher/author: MathWorks
- URL: https://www.mathworks.com/help/control/ref/dynamicsystem.c2d.html
- Inspected: Zero-order-hold default and model discretization assumptions
- Access: vendor technical documentation
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## MATLAB-DISC: Continuous-discrete conversion methods

- Publisher/author: MathWorks
- URL: https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html
- Inspected: Zero-order hold vs first-order hold and alternative methods; public usage overview
- Access: vendor method documentation
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## MATLAB-AW: Anti-windup PID with actuator saturation

- Publisher/author: MathWorks
- URL: https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html
- Inspected: Integral windup, back-calculation and clamping methods on saturated process; public example
- Access: vendor technical example
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## MIT-STABILITY: Underactuated Robotics, Lyapunov analysis

- Publisher/author: MIT CSAIL / Russ Tedrake
- URL: https://underactuated.mit.edu/lyapunov.html
- Inspected: Lyapunov stability topic and conservative certificates; conceptual outline, not independently verified derivation
- Access: technical chapter pointer
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## PY-CTRB: python-control ctrb documentation

- Publisher/author: Python Control Systems Library
- URL: https://python-control.readthedocs.io/en/latest/generated/control.ctrb.html
- Inspected: Controllability matrix A,B and rank computations; public API notes
- Access: open-source API documentation
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## PY-OBSV: python-control obsv documentation

- Publisher/author: Python Control Systems Library
- URL: https://python-control.readthedocs.io/en/latest/generated/control.obsv.html
- Inspected: Observability matrix A,C and rank computations; public API notes
- Access: open-source API documentation
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## MATLAB-ALIAS: Aliasing from sampling

- Publisher/author: MathWorks
- URL: https://www.mathworks.com/help/signal/ug/aliasing.html
- Inspected: Sampling and folding/aliasing under bandlimited assumptions; public tutorial
- Access: vendor tutorial overview
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.

## FBS-SUPPLEMENTS: Caltech Feedback Systems supplements and updates

- Publisher/author: Åström and Murray
- URL: https://fbswiki.org/wiki/index.php/Main_Page
- Inspected: Author wiki lists networked, optimization and linear-systems supplements; not detailed chapter review
- Access: author-maintained supplement index
- Rights: link only, newly authored explanation; source rights remain external.
- Original source bytes: not archived.
- Review status: AI-assisted scoped reading, not independent scientist audit.


## v0.2 extension material

# Control Atlas public source navigation · 2026-11-12

The sources below were inspected only to the stated scope. No complete textbooks, figures, source datasets or restricted content are mirrored. A source heading is not independent scientific review.

## ASTROM-2E: Feedback Systems, 2nd ed., Åström and Murray (2021)

- URL: https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems
- Inspected portion: Publisher description and table-of-contents scope: state-space, stability, controllability, observability, PID, frequency-domain robustness
- Status: `publisher_scope_only`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## CALTECH-FBS: Feedback Systems, 1st edition author-hosted text and chapter index

- URL: https://authors.library.caltech.edu/records/yzs24-xsx88
- Inspected portion: Author library page and chapter-files metadata; chapter topics checked as navigation, not entire text read
- Status: `publisher_library_metadata_only`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## MIT-LQR: MIT Underactuated Robotics Ch. 8: Linear Quadratic Regulators

- URL: https://underactuated.mit.edu/lqr.html
- Inspected portion: Discrete-time LQR infinite-horizon Riccati equation and feedback gain; selected HTML passage
- Status: `selected_full_html_portions`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## SCIPY-ZOH: SciPy signal.cont2discrete reference

- URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cont2discrete.html
- Inspected portion: ZOH and Euler/bilinear/FOH options, state-space arguments; public function documentation
- Status: `api_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## PYCTR-CTRB: Python Control Systems Library controllability matrix

- URL: https://python-control.readthedocs.io/en/stable/generated/control.ctrb.html
- Inspected portion: Controllability matrix definition and API, not a hardware validation
- Status: `api_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## PYCTR-OBSV: Python Control Systems Library observability matrix

- URL: https://python-control.readthedocs.io/en/stable/generated/control.obsv.html
- Inspected portion: Observability matrix definition and API, not an identification of a real plant
- Status: `api_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## PYCTR-DLQR: Python Control Systems Library discrete LQR documentation

- URL: https://python-control.readthedocs.io/en/stable/generated/control.dlqr.html
- Inspected portion: Discrete-time LQR cost, Riccati output and gain; selected documentation
- Status: `api_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## PYCTR-LQE: Python Control Systems Library linear quadratic estimator reference

- URL: https://python-control.readthedocs.io/en/latest/generated/control.lqe.html
- Inspected portion: Continuous-time Kalman estimator structure and noise covariances; not same as our discrete scalar step
- Status: `api_documentation_related_model`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## MATH-PID-AW: MathWorks Anti-Windup Control Using PID Controller Block

- URL: https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html
- Inspected portion: Clamping/back-calculation with saturated actuator and delayed first-order plant; selected R2026b HTML
- Status: `public_technical_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## MICH-PID: University of Michigan Control Tutorials: PID Controller Design

- URL: https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID
- Inspected portion: PID objectives and practical saturation/windup/noise caveats; public tutorial description
- Status: `public_tutorial_selected_scope`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## MATH-ID: MathWorks System Identification Workflow (R2026b)

- URL: https://www.mathworks.com/help/ident/gs/system-identification-workflow.html
- Inspected portion: Data preprocessing, model choice, estimation and validation; selected workflow HTML
- Status: `public_technical_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## MATH-ID-QUALITY: MathWorks System Identification Overview

- URL: https://www.mathworks.com/help/ident/gs/about-system-identification.html
- Inspected portion: Time-domain data quality, persistent excitation and sampling; selected HTML
- Status: `public_technical_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## MATH-ALIAS: MathWorks Making Quality Measurements, aliasing

- URL: https://www.mathworks.com/help/daq/making-quality-measurements.html
- Inspected portion: Bandwidth, analog anti-alias filtering and sampling at or above twice cutoff; selected public HTML
- Status: `public_technical_documentation`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## MIT-STATE: MIT Underactuated State Estimation Ch.19

- URL: https://underactuated.mit.edu/state_estimation.html
- Inspected portion: Chapter heading and overview on observers/Kalman; page is incomplete, not a verified full derivation
- Status: `chapter_navigation_only`
- Rights: link, bounded original paraphrase only
- Expert review: not performed

## CTMS-METHODS: University of Michigan Control Tutorials: index

- URL: https://ctms.engin.umich.edu/CTMS/index.php?aux=Home
- Inspected portion: Modeling, PID, state-space, digital controller design coverage; homepage only
- Status: `tutorial_index_only`
- Rights: link, bounded original paraphrase only
- Expert review: not performed


