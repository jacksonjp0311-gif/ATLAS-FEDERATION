# CONTROL ATLAS — Scientific Reference v1.0.0-rc.1
James Paul Jackson research program · 13 November 2026
**Scope:** source-linked offline control science, mathematical models, evidence and limitations. This is a scoped v1 *candidate*, not full physical/engineering/AI integration acceptance.
Real-data execution status: small public motor RPM source summaries calculated; raw OpenMCT v2 dataset unavailable in this runtime; no OpenMCT actual model fit, no physical intervention.
## Chapter navigation
- 01 Systems Interventions And Evidential Scope
- 02 Continuous And Sampled Plant Dynamics
- 03 Stability Equilibria And Model Boundaries
- 04 Feedback Disturbances And Error
- 05 State Space Reachability And Observation
- 06 Sampling Delays And Zoh
- 07 Pi Pid Saturation And Anti Windup
- 08 System Identification And Uncertainty
- 09 State Estimation And Scalar Kalman Filtering
- 10 Finite Horizon Optimal Control And Constraints
- 11 Robustness Margins And Small Gain
- 12 Verification Industrial Safety And Ai Knowledge Reuse
- 27 Interval Robust Stability
- 28 Feedback Delay And Augmented Dynamics
- 29 Lyapunov Certificates And Numerical Limits
- 30 Sensitivity Performance Vs Stability
- 31 Identification Residuals And Validation
- 32 Watchdog Sensors And Adversarial Inputs
- 33 Validation Hardware Safety And Ai Boundary
- 34 Mimo Return Difference Singular Values
- 35 Robust Common Lyapunov Matrix Box
- 36 Two State Finite Horizon Lqr
- 37 Constrained Grid Search Vs Mpc
- 38 Correlated Innovations And Fault Ambiguity
- 39 System Identification Train Validate And Drift
- 40 Ot Governance And Scientific Release Gates
- 41 Robust Invariant Sets Under Disturbance
- 42 Nominal Stability Vs Admissibility
- 43 State Estimation Breaks Full State Guarantees
- 44 Sampling And Disturbance Envelopes
- 45 Model Evidence And Claim Calibration
- 46 Scoped Control Release And Remaining Work
- 47 Observer Error Bounds And Information Limits
- 48 Actuator Saturation Rate And Lag
- 49 Finite Horizon Output Feedback Reachable Tubes
- 50 Sensor Consistency Fault Ambiguity And Provenance
- 51 Uncertainty Budget Timing Validation And Design Review
- 52 V06 Release Gates And Reference Scope
- 53 Real Control Data Identification Boundaries
- 54 Public Motor Observed Summary Without Input Claim
- 55 Strict Log Parsing Time And Dmm Alignment
- 56 Chronological Identification And Model Mismatch
- 57 Two State Two Sensor Observer Certificates
- 58 Observer Actuator And Planning Interface
- 59 Control Data Rights Provenance And Evidence Maturity
- 60 Safety Case Faults And Operational Boundaries
- 61 Control Scoped V1 Evaluation And Remaining Gates
- V02 01 The Control Question Plant And Measurable Target
- V02 02 Continuous-Time Responses And Exact Sampled Holds
- V02 03 Feedback Stability Poles And Unmodeled Disturbances
- V02 04 Sample Rates Aliasing Delay And Digital Clocks
- V02 05 State-Space Reachability And Controllability
- V02 06 Observability And State Estimation
- V02 07 Pid Control Saturation Windup Derivative Noise
- V02 08 System Identification- Excitation Bias And Validation
- V02 09 Optimal Control- Scalar Discrete Lqr
- V02 10 Noise Kalman Updates And Hidden-State Assumptions
- V02 11 Robustness Uncertainty Delay And Safety Limits
- V02 12 Constrained Control And Model Predictive Planning
- V02 13 Fault Detection Diagnosis And Operational Evidence
- V02 14 Evidence Maturity Integration Contracts And Method Selection

## Investigations
- 01 First Order Response Versus Sampled Model Claims
- 02 Hidden State Reachability And Observability
- 03 Saturated Pi And Anti Windup Counterexample
- 04 Kalman Confidence Under A Wrong Sensor Model
- 05 Lqr Model Objective Versus Hard Physical Constraints
- 06 Sampling And Robustness Logical Refusal
- 19 Uncertain Scalar Closed Loop
- 20 Delay Changes Plant Dynamics
- 21 Lyapunov Candidate Converse Trap
- 22 Sensitivity And Noise Tradeoff
- 23 Residual Whiteness Not Proven
- 24 Fault Gate Sensor Age Vs Truth
- 25 Mimo Direction Vs Single Gain
- 26 Common P Failure And Success
- 27 Finite Horizon Lqr Not Physical Optimum
- 28 Open Loop Grid Feasibility Boundaries
- 29 Ambiguity Of Sensor Fault Detection
- 30 Identification Drift In Later Samples
- 31 Safety Monitoring And Source Maturity
- 32 Robust Invariant Box
- 33 Saturation Veto
- 34 Sensor Bias Changes Closed Loop
- 35 Scalar Disturbance Bounds
- 36 Observations Cannot Prove Universal Safety
- 37 Scalar Observer Stable But Nonzero Error
- 38 Requested Command Vs Applied Actuator
- 39 Finite Horizon Output Feedback Tube
- 40 Sensor Reading Violates Bounds But Cause Unknown
- 41 Sensor Noise Bound Is Not A Standard Deviation
- 42 Model Boundary And Release Gate
- 43 Public Rpm Traces Identification Refusal
- 44 Openmct Parser And Replay Protocol
- 45 Applied Pwm Vs Reference Command
- 46 Mimo Observer Error Containment
- 47 Chronological Arx And Leakage
- 48 Async Meter Duplicate Replication Trap
- 49 Physical Fault Claim Is Not A Sensor Alarm
- V02 01 Exact Sampled Response
- V02 02 Nominal Gain Misread
- V02 03 Reachability Vs Constraints
- V02 04 Antiwindup Trace
- V02 05 Sampling Ambiguity
- V02 06 Identification Experiment
- V02 07 Scalar Lqr Unconstrained
- V02 08 State Estimation And Sensor Bias
- V02 09 Feedback Delay And Saturation
- V02 10 Fault Residual Not Root Cause
- V02 11 Context Package Safety
- V02 12 Method Selection Review

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

# 27. Robust scalar stability under bounded parameter uncertainty

A nominal feedback pole is not evidence that a real loop is stable under uncertainty. Consider the *specified* scalar sampled-time model `x[k+1]=a x[k]+b u[k]`, `u[k]=-K x[k]`. Then the closed-loop pole is `p=a-bK`, and the exact nominal asymptotic-stability criterion is `|p| < 1`. This statement requires that the model is linear time-invariant, its variables refer to one scalar state, the state is measured without delay, and no saturation or nonlinear modes occur. A stable mathematical pole does not establish the stability or safety of real equipment with missing dynamics.

## From a point to a parameter interval

Suppose a ranges independently within `[a_min,a_max]` and b within `[b_min,b_max]`. Because p is affine in the two independent parameters, the maximum of `|a-bK|` over the **assumed rectangular uncertainty set** is attained at a corner. Evaluate the four combinations of endpoints. If *every* vertex has pole magnitude strictly below one, then the entire set of scalar models is asymptotically stable under the stated fixed feedback law. If one vertex fails, the declared parameter box contains an unstable member; that does not prove the actual machine is unstable unless its parameters are known to inhabit that part of the box.

With the constructed bounds a∈[0.9,1.1], b∈[0.25,0.45] and K=1, all possible poles lie between 0.45 and 0.85, hence the strict test passes. The answer is conditional on **independence and completeness** of the parameter box. A plant with hidden time delay, friction, integral action or actuator saturation cannot be declared robust merely because this affine rectangle passed.

## Failure of an unjustified bound

Take a∈[1.35,1.8] and b∈[0.05,0.25], K=1. The largest pole magnitude is 1.75. One or more admissible scalar models are unstable. The program reports the worst-case corner and every vertex so another system can audit the numerical result. It does not project whether an actual motor will break or how an operator should respond.

A trustworthy range must be identified from physical experiments or justified design specifications, with units, timebase, uncertainty, sensor loading and sampling conditions. Correlated parameter uncertainty may form a nonrectangular set; using a rectangular overapproximation can be conservative. Parameter estimation errors are not interchangeable with an a priori guaranteed interval. A mean ± one standard deviation is not a hard uncertainty bound.

**Scientific connection:** Åström and Murray, *Feedback Systems*, second edition, author-maintained [FBSwiki](https://fbswiki.org/) and [Princeton Press second edition](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems), stability and robustness chapters (source-page scope, not an independently reviewed full-book derivation). The rectangle criterion is derived algebraically for this explicitly limited scalar case.


---

# 28. A one-sample delay can defeat a stable feedback design

A controller that computes its output from delayed measurements closes a **different dynamical system**. Using the scalar discrete plant `x[k+1]=a x[k]+b u[k]` with immediate state feedback `u[k]=-K x[k]`, its pole is `a-bK`. If instead `u[k]=-K x[k-1]`, the state must include the previous measurement. The augmented matrix is `[[a,-bK],[1,0]]`, and the characteristic equation is `z² - a z + bK = 0`. This is not an approximation of a general networked controller; it is a distinct exact, one-sample, constant-delay model.

With the invented parameters a=1.5, b=1, K=1.2, immediate feedback has pole 0.3, nominally stable. With one sample of delay the two roots are `0.75 ± 0.798436 i`, each having magnitude `sqrt(1.2) ≈ 1.095445`, outside the discrete-time unit circle. Thus the mathematical delayed loop is unstable. A change of **timing alone** changed the stability verdict. This counterexample matters because an AI or software controller can appear correct on a no-delay unit test while violating time assumptions in a real execution trace.

Sampling and communication delays are not always one exact sample. Networked systems may experience variable sampling intervals, packet drops, out-of-order messages, actuator dead time and asynchronous sensor acquisition. A model of those conditions may require switched, stochastic, hybrid or delay-differential tools, depending on the assumptions. This Atlas does **not** infer a stability margin for variable delays from the exact quadratic case. A passing sampled-time simulation with fixed intervals does not prove deadline or cyber-physical safety.

A useful investigation records command timestamp, physical actuation timestamp, sensor measurement timestamp, transmit and receipt time, control-cycle period, jitter distributions, saturation and fault recovery behavior. It should seek worst-case permitted age and delay rather than relying only on average network latency. Observed control output correlation is not proof of actuator activity.

**Source scope:** Åström–Murray [FBSwiki](https://fbswiki.org/), feedback delay/stability foundations; a [Journal of the Franklin Institute paper](https://www.sciencedirect.com/science/article/pii/S0016003213001920) on networked delays and packet drops, abstract only. The quadratic derivation and numeric example are original to this package, not a reproduction of that publication's full algorithm.


---

# 29. A Lyapunov candidate is a conditional proof object

For an exact real discrete-time autonomous system `x[k+1]=A x[k]`, consider the quadratic candidate `V(x)=xᵀP x`. If `P` is symmetric positive definite and `Q=P−AᵀP A` is positive definite, then `V(x[k+1])−V(x[k])=−xᵀQ x<0` for every nonzero x. For the assumed LTI model, this provides a sufficient strict asymptotic-stability result. It does not establish that the matrix A represents a real plant, the state is observed reliably, or actuator limits are absent.

The new calculator accepts a two-by-two A and a **supplied** symmetric P. It computes Q and symmetric 2×2 eigenvalues using a scale-dependent floating-point threshold. For the model `A=diag(0.7,0.9)` and `P=I`, Q=diag(0.51,0.19), so both P and Q are positive definite and a nominal quadratic certificate is returned. It does not search for P or verify an interval uncertainty set. It is a developer-level numeric screening tool, **not** a formally verified theorem prover; the arithmetic is floating-point and near-boundary eigenvalues are uncertain.

A crucial counterexample demonstrates logic discipline. Let `A=[[0.5,4],[0,0.5]]`. Its eigenvalues are both 0.5, so the mathematical linear system is asymptotically stable, but `P=I` gives a Q with a negative eigenvalue. That failure only means *this candidate* did not certify decay. It is invalid to assert the plant is unstable because one arbitrary P fails. More sophisticated solvers can search for P or produce structured parameter-dependent certificates, but their numerical condition and model validity still matter.

In a real control loop, linearization may hold only locally, disturbances can change equilibria, saturation can invalidate linear feedback, and hybrid transitions can violate a single quadratic model. Lyapunov analyses in nonlinear control use invariant sets, regions of attraction, and other tools; this node does not automatically certify them.

**Technical source:** MIT [Underactuated Robotics, Lyapunov Analysis](https://underactuated.mit.edu/lyapunov.html), selected online chapter, and Åström–Murray [FBSwiki](https://fbswiki.org/) stability topics. These citations support the method family, not an independent proof review of this implementation.


---

# 30. Sensitivity and complementary sensitivity are different measures

Feedback can suppress some disturbances while amplifying others. In a linear single-input single-output negative-feedback loop with open-loop transfer function L(s), sensitivity is `S=1/(1+L)` and complementary sensitivity is `T=L/(1+L)`. The identity `S+T=1` follows algebraically. It is not a physical proof that all disturbances are rejected or sensor noise disappears. The frequency and injection point matter: sensitivity often describes disturbance-to-error pathways, while complementary sensitivity also appears in reference tracking and measurement-noise transfer paths, under a correctly specified block diagram.

The bounded calculator considers only a stable first-order plant `G(s)=g/(1+τs)` with τ>0 and a **proportional** scalar controller Kp. For a supplied frequency ω in radians per second, it evaluates `L(jω)=Kp*g/(1+jωτ)`, computes magnitudes and complex S,T, and verifies `S+T≈1`. At g=2, τ=3s, Kp=1 and ω=0.5 rad/s, it reports |S|≈0.53748 and |T|≈0.59628. Both magnitudes can differ from unity even when S+T=1 as complex numbers; adding magnitudes is mathematically wrong.

A controller might reduce low-frequency load disturbance yet pass high-frequency measurement noise through a different channel. The balance is also constrained by plant poles, zeros, delay and achievable bandwidth. “Better disturbance rejection” without specifying frequency and noise injection is incomplete. An isolated frequency response at one ω does not give gain margin, phase margin, disk margin, or robust stability; computing these requires wider frequency-domain or state-space analysis and assumptions about stability of the loop.

If `1+L` is nearly zero, the ideal sensitivity is extremely large. The program refuses near singularity instead of emitting a confident, finite estimate. It does not compute PID derivative filtering, noisy sampled controllers, nonminimum-phase restrictions or actual hardware spectra.

**Sources:** Åström–Murray [Feedback Systems](https://fbswiki.org/), frequency-domain and feedback-performance chapters; [python-control `margin`](https://python-control.readthedocs.io/en/latest/generated/control.margin.html) and [stability-margins](https://python-control.readthedocs.io/en/stable/generated/control.stability_margins.html) public API documentation, which explicitly distinguishes single-loop margins from a pointwise magnitude.


---

# 31. An excellent training fit can hide a wrong dynamic model

A system-identification exercise must distinguish estimation, model selection and independent validation. The earlier Atlas offers an exact scalar ARX fit to supplied sequences `x[k+1]=a x[k]+b u[k]`; it refuses clearly singular two-column regressors. Those are useful numerical checks, but a near-zero residual sum of squares on training samples can occur even when a model is invalid for a different operating regime. A fitted parameter is not an instrument or disturbance model.

Model residuals are differences between observed outputs and model predictions under a stated prediction rule. Their distribution, autocorrelation, relation to past inputs, dependence on operating range and changes over time may reveal omitted dynamics, time delays or sensor drift. MathWorks' [What Is Residual Analysis?](https://www.mathworks.com/help/ident/ug/what-is-residual-analysis.html) distinguishes residual whiteness diagnostics from independence between residuals and inputs, with caveats for particular model families and closed-loop data. The Atlas tool is much narrower: it computes only a sample residual mean, root-mean-square magnitude and a centered lag-one correlation; **no statistical whiteness test or p-value** is claimed.

For deliberately alternating residuals `[1,-1,1,-1,...]`, the descriptive lag-one correlation is strongly negative. Such a pattern may indicate systematic errors, but the example is an authored sequence and no real sensor was involved. A constant sequence makes the centered correlation undefined; the method refuses it. A small lag-one correlation is not sufficient to show all lags are zero, the model is unbiased, or the one-step-ahead prediction is an accurate closed-loop model.

A serious experiment requires informative excitation across the modeled frequency range, explicit sampling/hold and delay definitions, sensor timestamp and calibration, input measurement, disturbances, exogenous operating conditions, held-out validation regimes, model order selection and residual uncertainty. Closed-loop identification presents special challenges because input commands may respond to sensor noise; ordinary regression assumptions can be violated. Repeating a synthetic exact-data fit is not independent real-plant evidence.

The revised workflow preserves both model-estimation evidence and *negative* tests. A future AI context should tell an agent when the data do not identify an actuator path or when a residual check suggests further measurement—not assert “system learned the plant” from a passing regression test.


---

# 32. Stale sensors and fault gates: evidence-aware command refusal

A supervisory control system may need to reject an unsafe or untrustworthy command when the sensor used for feedback is stale, marked invalid, or inconsistent with a supplied threshold. This Atlas contains an **offline demonstration of one such decision policy**. It does not connect to hardware, implement a safety-rated controller, replace an independent emergency stop, or establish that any selected fallback value is physically safe.

Each sample in the illustrative `watchdog_policy_trace` declares: the current time, the measurement timestamp, a Boolean validity marker, an innovation (observed minus predicted) value, and a requested output. The caller separately supplies a maximum allowable measurement age, a maximum absolute innovation, and a fallback output. A sample with `now - timestamp > max_age`, explicit invalidity, or `|innovation| > threshold` is rejected and its output is replaced by the supplied fallback. Future-dated timestamps and a nonmonotonic sample clock are refused. Returning a deterministic refusal demonstrates input validation, not a safety certification.

A concrete trace accepts the first command; then rejects a stale measurement, a sensor flagged invalid, and a large innovation; then accepts a fresh plausible sample. In a physical facility, each of those events must be interpreted in the context of equipment state, source clocks, sensor errors, command dynamics, available interlocks and operator response. An innovation threshold chosen arbitrarily can produce both missed failures and false alarms. Timestamp freshness does not prove sensor truthfulness. An apparently reasonable innovation can arise when the model and sensor share a common bias.

A fail-safe state is **plant-specific**. Commanding zero is not universally safe: a brake, cooling pump, flow valve or pressure-relief actuator may have quite different de-energized or safe behaviors. This library does not prescribe a real safe state, control a machine, or certify deadline enforcement. It is a reference for study design and for a software-quality test that explicit refusal flags are retained alongside the result.

**Sources:** Åström–Murray [FBSwiki](https://fbswiki.org/) on control modeling; MIT [Lyapunov notes](https://underactuated.mit.edu/lyapunov.html) on conditional stability methods; published networked-control [random-delay and packet-dropout abstract](https://www.sciencedirect.com/science/article/pii/S0016003213001920). These are method-context sources; this particular trace is an original teaching design, not an implementation from them.


---

# 33. The Control Atlas scientific acceptance and deployment boundary

The **software** can verify deterministic numeric properties: equation identities, vertex stability bounds, eigenvalues, input rejection, source/revision closure and installability. The **science** requires a different kind of evidence: representative plant data, calibrated sensors, tested actuators, known operating modes, model uncertainty, appropriate analysis of disturbances, time delays, and independent engineering review. Passing Python tests is evidence of the calculations under their assumptions, not proof a factory control loop is stable, safe or performant.

A practical safety-critical controller's acceptance requires hazard analysis; safe-state definition; control-system architecture and interlock design; fault detection coverage; timing guarantees; independent human verification; validated fallback/rollback; emergency-stop behavior; certification where required; and physical testing under controlled conditions. The present package is deliberately **read-only and simulation-only**. It contains no direct equipment interfaces and does not offer actuator commands to outside devices.

The relationship with other Atlas nodes is explicit. Measurement owns sensor calibration and uncertainty models. Materials owns physical constitutive and property context. Causal owns experimental inference when comparing process changes. Control owns feedback dynamics, stability, disturbance rejection and estimation. Manufacturing remains queued to cover the operational defect and maintenance records. The eventual Bitwork router should navigate these claims using immutable record IDs and retrieve source-qualified context, not blend a Lyapunov candidate into an unqualified deployment recommendation.

The owner has set a firm sequence: **all thirty knowledge domains first; the routing and Bitwork system last; integration tests and desktop transfer afterward**. This edition deepens Control from its merged v0.2 foundation to a v0.3 content checkpoint, but does not mark Control v1, physical system verification, actual downstream AI evaluation or Windows platform acceptance complete.

A new domain version can be a successful content increment while still having important missing coverage: root-locus and full Nyquist analysis, state-space multivariable robust control, general MPC, stochastic disturbances, fault diagnosis with real data, adaptive nonlinear methods, hybrid systems, large-sample identification, control cybersecurity and industrial safety standards. These are separate backlog items, not inferred from the number of chapter titles.


---

# 34. Multivariable feedback is directional, not one scalar gain

**Question:** What can a 2×2 return-difference matrix tell us, and what can it not establish?

In a declared *real-valued, static, two-input/two-output algebraic loop*, let G be the plant response matrix at one chosen operating or frequency point and K the feedback matrix. The loop is L=G K and return difference M=I+L. If M is invertible, the algebraic sensitivity S=M⁻¹ and complementary sensitivity T=I−S satisfy S+T=I. The product order is essential: in matrix systems GK need not equal KG. This Atlas calculator takes real 2×2 G and K, reports M, its singular values, S, T and a numerical identity residual. It is intentionally not a frequency sweep or an inverse of an actual sampled MIMO controller.

The singular values of M quantify amplification or attenuation in different input/output directions. They are *not* individual element gains. One direction may be poorly conditioned while other matrix entries look harmless. The program uses the 2×2 Gram matrix to compute σmax and the determinant relationship σmin=|det M|/σmax. If σmin is near numerical singularity, it refuses to invert, rather than return huge unstable numbers as reliable results.

**Constructed example.** With G=[[1,-1.99],[-1.99,1]] and K=I, M=[[2,-1.99],[-1.99,2]], and its singular values are 3.99 and 0.01. The condition number is **399**: one algebraic direction is weak. It does *not* follow that the dynamic plant is unstable, that the chosen feedback controls physical equipment, or that this is a full robust stability margin. Without plant poles, delays, frequency dependence and uncertainty bounds, no internal stability claim is possible.

To study a real MIMO system one needs the full transfer matrix or state-space realization, actuator and sensor units, operating point, timing and bandwidth, nonminimum-phase behavior, uncertainties, margins over frequency and appropriate stability proofs. A transfer-function point with seemingly comfortable σmin does not rule out an unstable internal mode, severe uncertainty elsewhere, or a hidden unstable sensor/actuator interaction. This is precisely why the source Stanford EE363 linear systems material distinguishes transfer-function algebra, Lyapunov and Riccati analyses; the result must stay inside that boundary.

**Evidence and applicability.** Source: [Stanford EE363 lecture archive](https://ee363.stanford.edu/archive/lectures.html), lectures on Lyapunov/LQR and system methods; [MIT Underactuated Robotics](https://underactuated.mit.edu/lqr.html), finite-horizon and constrained control overview. The equations and numerical example are original educational derivation; neither linked source supplies the invented matrices. Both are selected public web content, not full independent expert source review. The calculator does not claim dynamic-system identification, multivariable phase/gain margins or physical plant approval.


---

# 35. A common Lyapunov candidate over uncertain 2×2 matrices

A robust-stability statement must name its uncertainty set. A nominal discrete-time matrix A can be asymptotically stable while a plausible variation is unstable. Conversely, a proposed quadratic certificate can fail even when the actual matrix is stable. These are *different* failure modes and must not be flattened into a single “controller safe” label.

For the exact linear discrete-time state equation x[k+1]=A x[k] with no disturbance or saturation, a symmetric positive-definite P defines V=xᵀPx. Strict decrease for a fixed A follows from Q=P−AᵀPA positive definite. The code accepts **four independently bounded matrix-entry intervals** [lo,hi], a caller-supplied P and a strict numerical tolerance. It checks positive definiteness of P and the Q matrices at the 16 rectangle vertices. This is not an optimizer for P, and it does not infer the bounds or judge their physical validity.

**Why checking vertices is sufficient for the specified model.** Any matrix in an independent-entry rectangle is a convex combination A=Σ wᵢ Aᵢ of its vertices. For P≻0, the matrix quadratic mapping A↦AᵀPA is convex in Loewner order: (Σ wᵢ Aᵢ)ᵀP(Σ wᵢ Aᵢ)≼Σ wᵢ AᵢᵀPAᵢ. Consequently Q(A)≽Σ wᵢ Q(Aᵢ). A strictly positive lower bound at all vertices provides a sufficient common quadratic decrease statement for the entire modeled box. The same P is used for every A; the model therefore also addresses arbitrary switching among members **only while the exact discrete-time linear model and sampling convention remain valid**.

**A model-only pass.** For A11∈[0.5,0.6], A12,A21∈[−.03,.03], A22∈[.3,.4], and P=I, the 16 computed minimum eigenvalues of Q are all positive. The worst is approximately 0.634697. This is a sufficient *numerical* condition for the supplied box, not an independent proof that the equipment's parameters remain in the box, that the floating-point eigenvalues have certified interval bounds, or that a nonlinear hardware system is stable.

**A crucial failure case.** Take A=[[.8,1],[0,.8]], whose eigenvalues are both .8. The matrix is nominally stable, but P=I fails the strict decrease test. It would be wrong to declare A unstable because this **candidate** failed. A different P can certify nominal asymptotic stability. An analyst must distinguish “certificate found,” “supplied candidate failed,” and “system unstable by an independent counterexample.”

Real robust control can require structured uncertainty, parametric correlations, unmodeled actuator states, delay, constraints, disturbance envelopes, state-dependent nonlinearities and switched/hybrid logic. A common quadratic certificate is a sufficient result for the *declared* set, not a universal robust-stability procedure. The implementation uses floating point with an explicit threshold, not formal interval arithmetic.

**Source:** [MIT Underactuated Robotics, Lyapunov Analysis](https://underactuated.mit.edu/lyapunov.html), section on common Lyapunov functions and uncertain parameters. The vertex-convexity derivation above is an original finite-dimensional explanation, not a quote. Stanford [EE363 lecture archive](https://ee363.stanford.edu/archive/lectures.html) provides supporting educational linear-matrix and Lyapunov topic scope.


---

# 36. Finite-horizon LQR: an optimal model policy without physical constraints

For a discrete plant x[k+1]=A x[k]+B u[k], where x∈R² and u is a single scalar input, the finite-horizon quadratic problem minimizes J=Σₖ₌₀ᴺ⁻¹ (xₖᵀQxₖ+R uₖ²)+xᴺᵀQf xᴺ. The declared Q and Qf must be symmetric positive semidefinite, R strictly positive. State and input coordinates require stated physical units, and Q, R, Qf implicitly encode a cost tradeoff—not an objectively correct manufacturing goal.

The dynamic-programming recursion starts with P_N=Qf and proceeds backwards: K_k=[R+BᵀP_{k+1}B]⁻¹ BᵀP_{k+1}A, P_k=Q+AᵀP_{k+1}A−AᵀP_{k+1}B K_k, u_k=−K_k x_k. The code supports exactly **two states, one input**, horizon 1–128 and the named matrix/vector units supplied by the caller. It produces the gain sequence, optimal *model* open-loop trajectory and cost; it checks the identity J=x₀ᵀP₀x₀. The identity is a numerical cross-check, not a physical controller test.

**Constructed double-integrator illustration.** With A=[[1,1],[0,1]], B=[0.5,1], Q=diag(10,1), R=.25, terminal Qf=diag(10,1), x0=[2,0], H=8, the computed finite-horizon gains and trajectories solve this declared unconstrained problem. An independent SciPy minimization over the full input sequence reproduces costs across seeded synthetic systems. This is a useful algorithm test but does not certify model adequacy or closed-loop robustness under disturbances.

A large computed input can be physically impossible if the motor saturates or a valve cannot move that quickly. An optimal unconstrained sequence need not respect current, voltage, speed, temperature, state or slew-rate limits. Neither the Riccati recursion nor a success flag proves the system is stabilizable in its real operating envelope. Hard constraints require a separate, correctly formulated constrained optimization or safety mechanism.

The reference therefore distinguishes **optimal with respect to a mathematical cost** from **admissible in a physical system**. It never sends an input to a controller, PLC, vehicle, actuator or autonomous agent. A useful real study would first identify A and B with calibrated sensors, verify state and input units, timestamp samples, characterize noise/latency and disturbance bounds, choose Q/R with engineering stakeholders, and run independent simulation/hardware-in-the-loop with safety interlocks before considering commissioning.

**Reference:** [MIT Underactuated Robotics: Linear Quadratic Regulators](https://underactuated.mit.edu/lqr.html), discrete-time Riccati equations and constrained-input discussion; [Stanford EE363 lecture archive](https://ee363.stanford.edu/archive/lectures.html), discrete finite-horizon LQR lecture. Local code is a bounded Python derivation and retains the assumptions in returned data.


---

# 37. Grid-constrained planning is not full model-predictive control

When a controller faces hard actuator limits and state constraints, an unconstrained LQR input can be inadmissible even if the nominal dynamics are accurate. The ideal constrained problem requires a feasible set, a finite-horizon objective, and typically numerical optimization at each real sampling instant. That approach is called model predictive control (MPC) when repeatedly solved and applied with feedback. This Atlas **does not implement a real-time receding-horizon controller** or a general continuous-input quadratic program.

Its deliberately restricted arithmetic accepts a **scalar** discrete plant x[k+1]=a x[k]+b u[k], a finite input grid of 2–7 explicitly enumerated values, a horizon of 1–5 steps, symmetric bounds |u|≤umax and |x|≤xmax, and nonnegative state/terminal costs with strictly positive input cost. It enumerates every grid sequence, screens any state or input constraint violation, and returns the cheapest feasible *grid candidate*. The result is an offline teaching plan. This can demonstrate saturation and infeasibility under the chosen grid without pretending to achieve globally optimal continuous-input MPC.

An example begins at x0=1.5 with dynamics x+=x+u, limit |x|≤2 and grid u∈{−.75,−.5,0,.5,.75}. Four-step enumeration finds an admissible input sequence. Another example begins at x0=1.9, has a=1.3, b=1, |u|≤.1 and |x|≤2. Under a supplied three-value grid, every first step moves outside the state bound, so no grid candidate is found. The returned status is **`no_feasible_candidate_on_grid`**, not “all possible controllers are infeasible.” Continuous-input alternatives, different horizon, better state estimates or different assumptions are not checked.

The distinction matters operationally: a grid approximation might miss a feasible solution between grid points, and a feasible open-loop trajectory may cease to be feasible when process noise, model mismatch, actuator lag or sensor delay are introduced. A true industrial design must consider constraint tightening, terminal admissibility, warm starts, solver termination, timing deadlines, safe fallback and independent interlocks. Even a formal mathematical guarantee for a nominal optimization problem is not certification of an actual machine.

A good evidence record exposes the plant model, time step, input grid, physical units, sample-rate and delay assumptions, bounds, objective, checked candidate count and all failure states. The package exposes neither hardware drivers nor a network interface. No input from the knowledge corpus is ever automatically treated as an authorization to operate equipment.

**Reference:** [MIT Underactuated Robotics, LQR with input and state constraints](https://underactuated.mit.edu/lqr.html). This original grid-based exercise is intentionally far narrower than the full convex MPC method described by the source.


---

# 38. Correlated innovations are not a fault-localization oracle

A model residual is not automatically a sensor fault. In a linear-Gaussian estimation model, the innovation vector ν=y−ŷ and its predicted covariance S describe a *joint statistical discrepancy*. If S is positive definite, the normalized innovation squared is NIS=νᵀS⁻¹ν. For exactly two sensors, the Atlas accepts a finite 2-vector and a symmetric positive-definite 2×2 covariance and evaluates this number. The covariance is supplied; it is not estimated or checked against a real apparatus.

NIS can be used as part of a statistical consistency assessment **when the measurement model, distribution, covariance and independence/timing assumptions are justified**. In a correct Gaussian setting, an innovation-space quadratic has a chi-square sampling law with dimensions equal to the innovation vector size, but that result does not hold automatically under unknown bias, nonstationarity, heavy tails, correlation neglected by the model or adversarial inputs. Our code returns no p-value or categorical fault diagnosis. A threshold alone would be an externally selected decision rule with its own expected false-alert behavior.

**Constructed covariance case.** Let ν=[2,0] and S=[[4,1],[1,1]]. The calculated NIS is 4/3, while discarding the off-diagonal covariance and pretending S=diag(4,1) would yield NIS=1. That demonstrates why correlations matter even when one sensor's raw innovation is zero.

**Observational equivalence matters even more.** One scalar observation y=10 can be produced by a state x=10 and zero bias, or state x=8 and sensor bias 2. Both hypotheses exactly reproduce the same reading. A diagnostic that declares one of them true based solely on that reading has invented evidence. A second calibrated sensor, known process excitation, a physics-based independent measurement, different temporal patterns or a qualified inspection could discriminate the alternatives—but those observations are absent.

In operational technology, residual monitors are only one layer. They must be separated from physical interlocks, sensor-health indicators, alarm management, human authority and verified fail-safe behavior. A reading that is within the expected model envelope can still be false if an attacker or failed sensor produces a plausible value; a large residual may come from a real plant disturbance rather than a sensor failure. Cause attribution requires a model of faults and independent evidence.

**References:** [NIST, *Survey of Physics-Based Attack Detection in Cyber-Physical Systems*](https://csrc.nist.gov/pubs/journal/2018/07/a-survey-of-physicsbased-attack-detection-in-cps/final), public abstract; [Stanford EE363 estimation/Kalman lecture index](https://ee363.stanford.edu/archive/lectures.html), scope only; [Kalman-filter educational NIS definition](https://kalman-filter.com/normalized-innovation-squared/), accessible public mathematical explanation, not a standards document. No actual sensor diagnostics performed.


---

# 39. Time-split identification distinguishes fit from future prediction

System identification should establish whether the measured inputs excite the relevant dynamics and whether the model predicts *new* responses. A least-squares fit to a single historical trace can match its training data almost perfectly while failing when the plant changes. A controller designed around that fit can then appear sound in simulation while producing wrong actions when deployed. This reference intentionally keeps source-data provenance, training and validation periods separate.

The existing scalar ARX teaching model uses x[k+1]=a x[k]+b u[k]. Its least-squares fit requires sufficient variation in past x and u to identify separate coefficients; a determinant/conditioning guard refuses unexcited data. The v0.4 `arx_training_validation_split` accepts a state sequence and corresponding input sequence with a declared chronological split. It fits a and b on the first segment, then computes **one-step prediction residuals** on the later segment using the observed predecessor x[k]. It reports training and later root-mean-square errors, sample counts and a ratio when the training RMS is sufficiently nonzero.

The validation window is *not* independent scientific evidence merely because it appears later in time. Production drift, changes in sensor calibration, different operating conditions, closed-loop input selection, or disturbance correlated with commands can bias the regression and alter prediction error. Even a successful one-step validation is not the same as free-running multi-step accuracy, counterfactual plant identification or stable closed-loop control.

**Constructed drift example.** A 32-step synthetic trace uses a=.8, b=.2 for 24 steps and then a=.95 for eight. The first-segment regression has essentially zero residual RMS because the process exactly matches the declared noiseless model; later one-step RMS is about 0.129. A model that reported only the near-zero training error would conceal the shift. Another case with constant x and zero u fails the excitation/identifiability guard instead of returning a plausible unique plant model.

A real study should retain input excitation design, run/shift boundaries, process and sensor timing, output measurement uncertainty, operator interventions, commanded vs actual actuator values, sample-rate and missing-data flags, model selection and held-out regime coverage. For a biased closed-loop experiment, ordinary least squares need not estimate causal transfer parameters; instrumented identification or appropriate noise models may be required. The Atlas's current tool is intentionally narrow and does not prove its observed coefficients are physical constants.

**Source:** [Stanford EE363 archived lectures on estimation](https://ee363.stanford.edu/archive/lectures.html) and the [NIST survey of physics-based monitors](https://csrc.nist.gov/pubs/journal/2018/07/a-survey-of-physicsbased-attack-detection-in-cps/final). These support methodological boundaries, not the synthetic trace's numerical parameters.


---

# 40. Operational-technology evidence and the limits of AI-directed control

Control engineering interfaces with physical energy, human safety and operational security. A mathematical control algorithm can be perfectly implemented while the real system remains unsafe because an actuator saturates, sensor timestamps are false, material or component constraints are missing, the process has multiple operating states, or a safety interlock fails. This reference provides mathematical tools and source-qualified case studies only; it does not provide a runtime that commands actuators, changes machine configurations or bypasses site safety procedures.

**Current authoritative distinction.** NIST Special Publication 800-82 Revision 3 (September 2023) is the released *Guide to Operational Technology Security*. NIST's Revision 4 **Initial Public Draft**, published September 21, 2026, is not a final standard at this checkpoint; its public comment deadline is November 30, 2026. A source card must identify the review and publication status, not silently replace final Rev 3 requirements with provisional draft language. Different industrial or regulated equipment may also have governing sector-specific requirements.

NIST's industrial cybersecurity work describes anomaly detection, integrity checking, change management and other protective practices. None is a universal proof that observed measurements represent true plant states. Physical systems require a documented hazard analysis, independently validated safe states, interlocks outside the research code path, authenticated command authorization, synchronized clocks, actuator limits, response-time testing, alarm review and operator control. An agent's “will to continue” or procedural retry instruction is not a valid override of a real-world safety gate.

**Evidence levels must stay separate.** A checked algebraic identity demonstrates mathematical consistency; a numerical oracle agreement establishes implementation reliability for tested inputs; a synthetic simulation may falsify claims about a model; identified plant tests show only the studied operating envelope; qualified commissioning or regulatory approval has additional independent requirements. The Atlas must not promote one into another. A concise record should make the model/units, sources, validation status, input provenance and nonconclusions available to any downstream AI consumer.

The user's sequencing constraint remains **all 30 domain libraries first, then Bitwork/routing development, then integrated evaluation and desktop transfer**. This Control increment has no network, PLC, field-device access, background agent action or live Bitwork route. It does not connect to or modify the user's machines. Early navigation modules are preserved as-is, with no domain-dependent ranking patches.

**Sources:** [NIST SP 800-82r3, final September 2023](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [NIST SP 800-82r4 Initial Public Draft September 2026](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd); [NIST SP 1800-10, Manufacturing OT Integrity](https://csrc.nist.gov/pubs/sp/1800/10/final); [NIST Survey of Physics-Based Attack Detection](https://csrc.nist.gov/pubs/journal/2018/07/a-survey-of-physicsbased-attack-detection-in-cps/final). These are scoped public overview/abstract reviews, not reproduced manuals or proof of site compliance.


---

# 41. Robust positive invariance is a set property, not a nominal pole test

The control question is not only whether one equilibrium is stable. An operating system often needs its state to remain inside an admissible region in the presence of bounded disturbances and parameter uncertainty. A **robust positively invariant set** is a state set that maps into itself under every allowed disturbance and model realization, provided the controller's declared physical assumptions hold. This is stronger than watching a single simulated trajectory remain inside limits. It is not the same thing as an independently validated industrial safety guarantee.

For a discrete-time state model `x[k+1]=A x[k]+B u[k]+w[k]` with exact feedback `u[k]=-K x[k]`, the closed-loop matrix is `F=A-BK`. Let a candidate box be `|x_i|≤r_i` with `r_i>0` and disturbances independently bounded `|w_i|≤d_i`. For each state component, the maximum successor magnitude under a fixed F satisfies `max |x'_i| = sum_j |F_ij| r_j + d_i`. Thus `sum_j |F_ij| r_j + d_i ≤r_i` guarantees one-step containment. If the same conditions hold at each step, the box is positively invariant by induction. For a single input and `|u|≤U`, the worst requested input is `sum_j |K_j|r_j`. This input condition must be checked separately; otherwise a controller whose unconstrained feedback looks invariant may command physically unavailable actuator values.

When A's four entries and B's two entries vary independently inside closed intervals, the v0.5 reference enumerates **64 parameter-box vertices**. Because `sum_j |A_ij-B_i K_j|r_j` is a convex function of the affine parameters, its maximum on an independent rectangular parameter set is attained at a corner. The calculation is an exact corner analysis of the real-arithmetic model, with floating-point tolerances; it is not a formally machine-certified interval proof. The independence and upper/lower bounds are assumptions supplied by a caller; they cannot be inferred from a few identification records. If uncertainty is correlated or depends on state, the rectangular set can be conservative or misleading.

The returned result distinguishes state containment and actuator feasibility. A failure means **this candidate box is not certified under this model and gain**; it need not mean every actual trajectory is unsafe. A success means only a mathematical implication conditional on all specified assumptions. Sensor bias, computational delay, state-estimation error, saturating or rate-limited actuators, quantization and unmodeled dynamics invalidate this exact certificate unless they are included in the model. The tool explicitly refuses use when true full-state feedback is not asserted.

A physical safety case still requires independently established model bounds, calibrated sensors, measured actuator dynamics, environmental and timing uncertainties, and a separately reviewed protective system. MIT's *Underactuated Robotics*, [Robust and Stochastic Control](https://underactuated.mit.edu/robust.html) and [Lyapunov Analysis](https://underactuated.mit.edu/lyapunov.html), discuss invariant regions and bounded disturbances. These selected HTML sections, not the whole book, support this scientific distinction; no hardware experiment was performed here.


---

# 42. A mathematically stable feedback law can be physically inadmissible

Control analyses frequently begin with a nominal linear system and a feedback gain. Poles of the unsaturated closed-loop matrix inside the unit disk establish asymptotic stability for that exact finite-dimensional, autonomous, discrete-time linear model. They do not establish safe operating conditions of a plant. A physical input has voltage, torque, flow, heat, ramp-rate, dead-zone, delayed-command and shutdown constraints. A software algorithm may also have jitter, asynchronous samples or stale measurements. Stability under ideal inputs does not imply those inputs can be executed.

The new boxed-state certificate makes this issue explicit by reporting both `state_box_invariant_for_every_assumed_model` and `actuator_unsaturated_for_every_state_in_box`. A simple constructed example has a valid state-containment calculation but fails when the actuator limit shrinks from 0.25 to 0.12. A program that checks only the first Boolean would issue an overconfident conclusion. In this release the combined status is refused. This choice is deliberate: no computed status means an operator can deploy or bypass a safety interlock.

Hard constraints may include not only input magnitude but **rate of change**. An actuator that can produce ±1 unit eventually may still be incapable of changing by one unit within a sample. The v0.5 box model does not include slew limits. Such a limit can introduce a dynamic actuator state, requiring a new augmented plant and a different invariant-set computation. The same applies to set-point changes, integral windup, and safety PLC feedback that has its own sampling and failure modes. A conditional certificate tied to an exact controller cannot be silently transferred to another implementation.

Robust invariant boxes themselves can be too conservative. A rotated elliptical safe region or polytope might be invariant even where an axis-aligned box fails. A candidate failure does not prove that **no** robust invariant set exists. Numerical iteration of one trajectory cannot prove a universal property, either: an apparently benign disturbance sequence may omit the corner of the disturbance set that causes a violation. These are different logical statements and must be labeled independently.

For a real controller, record the state and input units, available sensor/actuator ranges, interlock hierarchy, sample and hold timing, computational deadlines, identification uncertainty, disturbance bounds, plant version, and operator authority. Independent engineering review is necessary for commissioning or safety-critical decisions. The methods in this Atlas are explicit offline research tools, not deployable protective functions.

**Sources:** MIT *Underactuated Robotics* [Robust and Stochastic Control](https://underactuated.mit.edu/robust.html); NIST [SP 800-82 Revision 3 final](https://csrc.nist.gov/pubs/sp/800/82/r3/final) describes OT safety and reliability considerations, but does not certify a particular feedback model.


---

# 43. Measured state, estimated state, and hidden sensor bias

The certificate `x'= (A-BK)x+w` assumes exact access to the physical state x. Most controllers actually apply feedback to an observation `y=Cx+v`, or to a state estimate derived from a history of observations. The resulting closed-loop dynamics are different: `x'=A x-BK xhat+w`, and the difference `e=xhat-x` contributes an additional term `-BK e` to the state transition. One cannot use the original invariant-state certificate without bounding the estimation error and incorporating its effect.

A single measurement can hide multiple physical causes. For example `y=10` could mean true process state 10 and zero sensor bias, or true state 8 with a +2 sensor bias. A residual monitor can flag disagreement between a model and observation, but identifying which state or sensor is wrong often requires independent evidence, additional measurements, fault isolation or an experiment. `NIS` values computed from normalized innovation covariance rely on justified sensor and noise models and do not by themselves certify a fault cause. A low residual also does not prove an uncompromised sensor if the model is biased in the same way.

The v0.5 casebook introduces two synthetic trajectories from the same two-state plant: one with exact state measurements, another with a time-varying sensor bias. Both apply the same feedback rule to the *measured* state and use an actuator clamp. The difference in resulting commands demonstrates why a proof that assumes perfect state feedback cannot be inherited by an estimated-state implementation. No real process data, sensor failure event, cyberattack or causally diagnosed equipment malfunction is provided.

For a defensible study, specify each sensor's physical quantity and calibration, time stamp provenance and latency, fault model, cross-channel dependencies, measurement covariance, observability, estimator initialization, state-error bounds, and how state/control estimates are used by the supervisory system. A permitted fallback command may differ from a universally safe physical action; safe-state design must be established by a qualified process-specific hazard analysis, not from the algebraic choice of output 0.

Source context: Stanford Engineering Everywhere [EE263](https://ee263.stanford.edu/archive/) includes observability and least-squares state estimation; MIT's [Underactuated Robotics state-estimation resources](https://underactuated.mit.edu/) distinguish known-state control and estimation. NIST's [OT guide](https://csrc.nist.gov/pubs/sp/800/82/r3/final) addresses operational safety and integrity. These are scoped source topics, not original experiments in this package.


---

# 44. A disturbance envelope needs physical evidence and timing assumptions

Robust models are often expressed as `w[k]∈W`, but the scientific issue is whether the specified W actually encloses disturbances in the target environment. A finite history of observed disturbances does not logically guarantee that all future disturbances lie within its observed minimum and maximum. Industrial disturbances may be correlated, time-varying, seasonal, process-dependent or caused by rare faults and abrupt maintenance changes. The selection of the envelope therefore needs an evidence basis and a specified confidence/operating domain.

For a state box, a one-step worst-case estimate adds the absolute disturbance radius to the feedback transition bound. It assumes that the disturbance component can take either sign independently of current state and other disturbances. Time correlation might reduce some reachable behaviors and enlarge others when the plant has memory or delayed responses; a conservative box may be computationally convenient but still depend on valid amplitude bounds. Nothing here discovers those bounds automatically.

A discrete-time controller also depends on correct timing. Sampling a continuous signal at an interval that misses its dynamics can produce aliasing, while a command delayed by one sample may change the closed-loop characteristic equation and destroy nominal stability. These are addressed in previous Control chapters but matter here because the robust-box certificate assumes the supplied matrices exactly describe the **actual sampled plant**. If a controller updates based on stale data, its effective model may be of higher order and cannot inherit the same certificate.

A synthetic trajectory is useful for falsification: if it violates the state box under an allowed disturbance, a candidate certificate or implementation is wrong. However, 100,000 successful synthetic steps do not prove the universal statement that a set is invariant over all allowed states and disturbances. Conversely, exact parameter-box vertex inequalities prove a mathematical implication for an assumed model without sampling the physical tails. We must retain this distinction in every AI context package.

A real empirical workflow would collect synchronized raw state and input histories, disturbance events, operating modes, instrument calibration and uncertainty, sampling jitter, actuator response, and observed fault conditions. Confidence that a disturbance set is conservative is external to the array-manipulation code. The next stage after domain-content construction can integrate these methods with authentic datasets, but not assume such datasets exist today.

Source context: [MIT Robust and Stochastic Control](https://underactuated.mit.edu/robust.html) discusses disturbance sets, uncertainty propagation and robust MPC. It explicitly distinguishes robust guarantees for a modeled disturbance family from conventional deterministic planning; no source files are mirrored.


---

# 45. Separate numerical verification, mathematical certification, and physical validity

There are at least five different evidence stages for a control result. First, a derived identity can be checked algebraically. Second, a numerical implementation can be compared against a separate algorithm and against adversarial inputs. Third, a mathematical certificate can be proved to hold under a declared set of assumptions. Fourth, the physical plant model and disturbance bounds need independent empirical support. Fifth, system-level performance and safety must be established with hardware tests, operator review, and applicable governing requirements. Higher test counts at earlier stages cannot substitute for missing later stages.

Our robust box model is precise enough to demonstrate this ladder. The vertex enumeration implements an exact worst-case statement under independent interval parameter assumptions. We cross-check the algorithm with direct enumeration of state-box corner signs and parameter vertices. This supports the formula, not the truth of the parameter bounds. If a physical model is omitted, the program should refuse a physical guarantee despite flawless numerical tests.

In controller development, the uncertainty register should distinguish *parameter estimation error*, *unmodeled states*, *numerical discretization*, *sampling jitter*, *actuator limits*, *sensor faults*, *disturbance envelope error*, and *physical operating mode*. Each has different observable evidence and may require a different remediation. A single scalar 'confidence' can hide these categories; a clear, versioned status ledger is more useful.

A scientifically responsible release note states exactly which cases were synthetic, which published results were numerically reproduced, and which independent experiments or peer review did not occur. It preserves source URLs and inspected scopes and avoids relabeling a NIST draft as final. NIST SP 800-82 Rev. 3 remained the relevant final OT guide as of November 13, 2026; Revision 4 was an Initial Public Draft published September 21, 2026, with public comments due November 30. This version status is evidence metadata and can change in a later release.

No tool in the Control Atlas actuates hardware, modifies a PLC, invokes a real industrial safety interlock, or grants operator authority. Retrieved documents are data, not executable instructions. The shared Forge context assembler preserves mathematical assumptions and source qualifiers with the claim. The future Bitwork routing layer should be assessed independently for answer quality and reliability after all 30 domain contents have been built, as the owner has directed.

**Primary source:** NIST [SP 800-82r3 Final](https://csrc.nist.gov/pubs/sp/800/82/r3/final), [SP 800-82r4 Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd), and MIT's [Robust Control](https://underactuated.mit.edu/robust.html).


---

# 46. What a scoped Control content release means

A scoped Control Atlas content edition is a research and learning reference. It should be internally consistent, executable where the formulas are bounded, linked to trustworthy identified sources, explicit about missing science, and compatible with the shared Forge record contract. It should not imply certified control of arbitrary industrial systems, a general robust MPC solver, or professional approval of safety-critical actions.

The current edition covers scalar continuous and sampled dynamics; 2×2 state space and reachability; PID and saturation; scalar LQR/Kalman; finite-horizon unconstrained LQR; input-grid planning; NIS and residual diagnostics; train/validation splits for simple ARX identification; nominal stability and delayed stability; bounded matrix Lyapunov candidates; static multivariable return differences; and new robust invariant state-box checks with explicit actuator and sensor assumptions. These are mathematically useful and source-linked but remain intentionally small model classes. A word such as 'general' in a document title does not authorize the code to solve a high-dimensional real control problem.

The remaining scientific gaps include verified robust invariant sets for nonlinear or hybrid plants, high-dimensional uncertainty sets, systematic input-delay and slew-rate constraints, full state-estimation error envelopes, dependent disturbances, stochastic reachability under empirically justified distributions, complex-frequency robust margins, identified real process records, and independently measured hardware performance. Formal numerical interval proofs would also be required before treating a floating-point inequality at equality as definitive for a safety-critical certificate.

For a future genuine Control v1 release, the scope must be frozen by what the content actually supports. The content can be substantial even when direct physical deployment is deferred. An engineering gate requiring a native Windows run, independent scientific review or real-world dataset must remain marked incomplete until observed evidence exists. The model's result status is neither a guarantee of plant safety nor a statement that a user can bypass protective controls.

The project-wide order is fixed: develop the planned 30 Atlas knowledge libraries, then design/evaluate the Bitwork-driven router over their exact versioned corpus, then integrate and test the system, and only then transfer it to the user's computer. Accordingly, Control remains the active knowledge domain. Agent Atlas stays queued. Routing is frozen, and no GitHub changes or desktop installation are authorized in this release.

**Reference framework:** MIT's [Underactuated Robotics](https://underactuated.mit.edu/), Stanford's [EE263 course](https://ee263.stanford.edu/archive/), NIST [OT security and safety context](https://csrc.nist.gov/pubs/sp/800/82/r3/final). These references ground the domain but are not substitute for physical validation.


---

# 47. Observer error bounds are conditional information, not sensor integrity

A feedback design that assumes the state is directly known may cease to satisfy its original theorem when the controller uses estimates. One response is to construct a model of the observer error and explicitly carry its uncertainty. A Luenberger observer is an example of a prediction plus measurement correction, not an oracle that discovers the physical truth from a single sensor. This chapter gives a bounded scalar, discrete-time error calculation. The fuller theory includes multivariable observers, observability, Kalman estimation, set-membership filters and unknown-input observers. None of those general problems is claimed solved here.

## Time-ordering matters

Let the physical state follow `x[k+1]=a x[k]+b u_applied[k]+w[k]`. The sensor reports `y[k]=x[k]+v[k]` at that same indexed time. An observer uses the **known applied input** and updates `h[k+1]=a h[k]+b u_applied[k]+L(y[k]-h[k])`. The estimation error `e[k]=x[k]-h[k]` then satisfies `e[k+1]=(a-L)e[k]+w[k]-L v[k]`. This exact identity follows from the declared equations and is independent of the chosen feedback gain K because plant and observer use the same applied input.

If `|e[0]|<=E0`, `|w[k]|<=W`, and `|v[k]|<=V`, an interval recurrence gives `E[k+1]=|a-L| E[k]+W+|L|V`. If `|a-L|<1`, the sufficient stationary bound is `(W+|L|V)/(1-|a-L|)`. These quantities are **deterministic bounds** conditional on true input noise limits, not probabilistic confidence intervals. Uniform probability distribution or Gaussian assumptions are unnecessary, but actual bounded disturbances and timing alignment must be established externally. A probability standard deviation is not an almost-sure maximum.

For stipulated a=0.8, L=0.6, W=0.02 and V=0.01, the limiting radius is 0.0325 model units. An observer that converges in the zero-noise model does not make this bound vanish when disturbance and sensor noise remain. If `|a-L|>=1`, a finite-horizon recurrence can still be calculated but no finite stationary certificate follows from this argument. The implementation reports that absence rather than substituting a favorable value.

## When the proof fails

The equation uses *applied* input, not an unsaturated command or an incorrect timestamp. Unknown actuator lag, delayed sensors, asynchronous packets, silent measurement changes and bias beyond the declared V alter the error dynamics. A measurement consistency check can reveal that some assumed bound fails, but that does not identify whether the sensor, plant model, parameter range or timing is responsible. The observation equation itself is a hypothesis requiring evidence.

**Source scope:** MIT *Underactuated Robotics*, Chapter 19 *State Estimation*, official online table of contents and selected section https://underactuated.csail.mit.edu/ ; Mayne et al. (2006) *Robust output feedback model predictive control of constrained linear systems*, publisher abstract https://www.sciencedirect.com/science/article/pii/S0005109806001221 . The scalar recurrence here is an original transparent derivation, not the complete methods of the papers.


---

# 48. The requested input is not the applied input

A controller computes a requested action. A physical actuator has amplitude limits, rate limits, energy constraints, latency, hysteresis, dead zones and possible failures. It may deliver something different. An infinite-horizon LQR design or PID gain that ignores these limits cannot directly inherit a guarantee when the actuator saturates. Actuation should be represented as a dynamical state and its behavior treated as an experimentally validated model before deployment.

## An explicit discrete teaching model

This edition implements three successive transformations of a scalar command. First the requested command `r[k]` is magnitude-clipped to the specified interval `[-U,U]`. Second the *target* is constrained to `u_applied[k] +/- D`, where D is a maximum allowed change in the sampled interval. Third a first-order response parameter `alpha` in `(0,1]` gives the next applied input: `u_applied[k+1]=u_applied[k]+alpha*(target-u_applied[k])`. This is an authored, causal discrete actuator model. It is not a source-supplied real actuator transfer function. The realized plant uses `u_applied[k]` for the present step, while the updated actuator state becomes available for the next step.

For a nominal requested input of 10 units, magnitude bound U=1, per-step D=0.2, previous applied input 0, and alpha=0.5, the magnitude-clipped target is 1, the slew-limited target is 0.2, and the next applied input is **0.1**. These are four distinct quantities. Replacing the applied input in the plant with the requested input of 10 is a model error, not a harmless optimization shortcut.

The model's update preserves `|u_applied|<=U` when its initial applied state satisfies the amplitude limit and alpha is between zero and one. It also preserves an applied per-step change no greater than D. These are properties of a mathematical recurrence, not of any motor, valve or PLC. If an actuator begins outside the declared bound, the function refuses the claimed premise instead of silently clipping its historical state. A zero D freezes the target. A hidden mechanical lag may differ from the chosen alpha; response fraction should be identified and validated.

## Why this matters for robust control

Actuator dynamics can increase phase lag, affect damping and invalidate a controller synthesized under an instantaneous-input assumption. A speed or saturation constraint can render a nominally reachable state unreachable under the real actuator. Rate limits can contribute to oscillatory behavior; the AIAA 2023 paper by Newton and Kroo discusses pilot-induced oscillation tendencies due to control-surface rate limits in a specific aerospace context. That is not experimental evidence for a factory valve.

**Source scope:** Newton and Kroo, *Model Reference Control for Reducing Pilot-Induced Oscillation Tendencies Due to Actuator Rate Limits*, AIAA 2023 published abstract https://doi.org/10.2514/6.2023-2512 ; Åström and Murray, *Feedback Systems* reference overview https://fbsbook.org/ . The local scalar lag and slew model is original synthetic teaching code and is not attributed as a published physical implementation.


---

# 49. Conservative reachable tubes around imperfect state estimates

A robust invariant set tells us which state values remain inside a boundary for all future time under stated feedback and disturbance assumptions. A finite-horizon *reachable tube* instead encloses possible states at selected future sampling instants from a specified initial set. Both require an accurate model and credible disturbance bounds. Neither should be presented as a real-hardware certification without plant measurements and independent engineering review.

## Augmented scalar state/observer/actuator dynamics

For the bounded scalar plant `x[k+1]=a x[k]+b u[k]+w[k]`, observer `h[k+1]=(a-L)h[k]+L x[k]+b u[k]+L v[k]`, and controller request `r[k]=-K h[k]`, we can propagate intervals for `x`, `h` and *applied* actuator input `u`. Magnitude saturation, a rate-limited target and first-order response produce `u[k+1]`. In this model, the true state and estimate are different variables; a static state-feedback theorem for `u=-Kx` cannot simply be reused for `u=-Kh`.

For an interval `[lo,hi]`, the image under a scalar multiplier c is `[min(c lo,c hi),max(c lo,c hi)]`. Sums of such images plus bounded noise provide a conservative interval hull. This independence relaxation **loses the correlation** between the physical state and estimate and can be much wider than the exact reachable set. If the resulting tube is within a specified state bound at each sampled instant of the requested horizon, the inequality holds for *all trajectories of the stated discrete model within its declared uncertainty envelopes*. It does not establish a state-invariant set, continuous-time intersample safety, safe response beyond the horizon, or physical model validity.

The implementation carries rate and magnitude bounds for the entire control path, assuming the previous applied input is inside its limit. Input effect is delayed one step under the stated actuator state order: the plant receives u[k], while a newly calculated action affects u[k+1]. Replacing u[k] with u[k+1] could produce falsely optimistic state trajectories. This distinction should be visible in data contracts for any eventual automation/AI consumer.

## Numerical and physical limitations

The finite horizon is deliberately capped at 100 intervals. Noise radii must be finite, nonnegative scalars. Initial state lies in `h[0]+[-E0,E0]`; the observer itself initially starts at the supplied estimated value. Coefficients are exact, not uncertainty intervals; uncertain plant matrices would require another model or an outer bound. States and commands have generic consistent units because no physical device is supplied. A physical sensor might have nonstationary bias or delayed measurements and violate V, so such cases must be recorded as model exclusions. A failed tube containment test is **not** proof of physical failure, and a passing one is **not** a safety sign-off.

**Related research:** Mayne et al. (2006) publisher abstract on bounded observer error, output feedback, invariant tubes and tightened constraints https://www.sciencedirect.com/science/article/pii/S0005109806001221 ; Sieber, Zanelli, Bennani and Zeilinger (2022) abstract on disturbance reachable sets and tube MPC https://www.sciencedirect.com/science/article/pii/S0947358022000723 ; MIT *Underactuated Robotics* Chapter 13 public section on robust MPC https://underactuated.csail.mit.edu/robust.html . The software here computes a *finite interval enclosure*, not a complete tube-MPC optimizer or an implementation of those authors' published algorithms.


---

# 50. Sensor inconsistency is evidence of a model contradiction, not a component verdict

A measured signal is a sample of a physical process, filtered by a sensor, acquisition system, timestamp, calibration and communication path. An unexpected reading may arise from a faulty sensor, unmodeled plant dynamics, material/process changes, a stale timestamp, an actuator not following commands, a unit conversion error, or a disturbance larger than assumed. A monitoring system must distinguish a *detected inconsistency* from a *diagnosed cause*.

## Scalar bounded-consistency gate

If the estimated state is h with a documented absolute error bound E, and sensor noise has a documented absolute limit V, the expected measurement interval is `[h-E-V, h+E+V]` for `y=x+v`. A reading outside this interval demonstrates that at least one assumed relation or bound is inconsistent with the observation, ignoring rounding and model arithmetic. It does **not** tell us which assumption failed. This holds regardless of whether a sensor defect is a likely hypothesis; statistical diagnosis requires a different study design and often redundant measurements.

For example, with h=0.1, E=0.04 and V=0.02, y=0.13 is inside the declared interval `[0.04,0.16]`. A reading y=0.30 is outside and lies 0.14 model units above the upper bound. The appropriate output is a scoped contradiction plus a list of unresolved causes, not “replace the sensor.” A nominal Kalman filter innovation covariance uses a probabilistic noise model; it cannot automatically substitute for a hard maximum noise envelope. Overconfidence about either uncertainty type can make a controller's risk assessment invalid.

## Practical fault-inquiry procedure

Define the physical quantity and units, time alignment, sampling rate and sensor location before computing a residual. Check sample freshness, calibration revision, data-handling path and process conditions. Validate the actuator's applied state separately from requested command logs. If a discrepancy persists, collect independent measurements or controlled tests to distinguish sensor failure, actuation failure and plant disturbance. A disagreement can be reproduced synthetically under more than one mechanism, and a controller should not escalate to physical intervention solely because a model consistency test failed.

For industrial operational technology, NIST SP 800-82 Revision 3 (final, September 2023) addresses the distinct performance, safety and security needs of systems that interact with the physical world. NIST Revision 4 was only an initial public draft as of November 2026. The Atlas should not describe a draft as the current final standard.

**Source scope:** NIST final SP 800-82r3 https://csrc.nist.gov/pubs/sp/800/82/r3/final and Revision 4 initial public draft https://csrc.nist.gov/pubs/sp/800/82/r4/ipd ; MIT *Underactuated Robotics* estimation chapter https://underactuated.csail.mit.edu/ . Official publisher overview and sections, not a certified system audit. No network/PLC device access in this package.


---

# 51. A credible bounded-feedback claim needs evidence for every envelope

Control proofs commonly begin with mathematical assumptions such as “process disturbance is bounded by W,” “measurement noise is bounded by V,” “actuator lag has response fraction alpha,” and “the plant dynamics are described by a,b.” These assumptions are not validated merely because the resulting inequality is true. The next verification layer must measure or justify the bounds, document drift and different operating modes, and establish what constitutes a failure to stay inside them.

## Minimum evidence packet

For the plant: identify the physical system, parameter sources, units, operating modes, sampling schedule, disturbance measurements, transient conditions, nonlinearities, hysteresis, and known delay. For the actuator: separate command, clamped target, measured applied position/force, magnitude limit, rate limit, dynamics, fault response and interlocks. For the sensor: physical quantity, calibration, drift, timestamp, freshness, quantization, noise and bias limits and missing data. For the estimator: update order, correct input-history representation, initial error distribution or set, observer gain, uncertainty propagation and mismatch monitoring. For constraints: distinguish process quality targets from physical protective limits and separate sampled constraints from intersample risks.

A statistical standard deviation does not provide a hard worst-case bound. Conversely, a worst-case interval does not assign a probability to its endpoints. If a source only gives 3σ under a Gaussian model, its finite bound status must remain unresolved: Gaussian tails are unbounded under the idealized model. Robust interval arithmetic may overapproximate reachability because state, estimate and past action are correlated. This is a conservative rejection hazard, not license to shrink the envelope without a valid derivation.

## Validation sequence

First check dimension and timing consistency. Then reproduce model calculations with a second numerical implementation and independent adversarial test cases. Check the smallest positive and largest allowed disturbances, gain changes, saturation and slew, initial state error, and measured-versus-predicted applied command. Compare estimator predictions against independent measurements. Test in a non-actuating replay/simulation environment and only under separately reviewed approval move toward bench validation. Safety-rated interlocks and failure recovery design are **not** provided by this Atlas.

The broader ATLAS FORGE sequence remains all thirty knowledge domains first, then the Bitwork/routing architecture, followed by integrated, independently authored retrieval/answer-quality studies and computer transfer. None of the mathematical models here establish that the routing system already works or improves AI performance.

**Sources:** MIT *Underactuated Robotics* state estimation and robust control notes; Mayne et al. 2006 output-feedback constrained-control abstract; NIST SP 800-82 Revision 3 final safety/security overview. This chapter is an authored evidence protocol, not a standards certification.


---

# 52. Control Atlas v0.6.0: new scope, falsification and next scientific requirements

This edition deliberately adds **finite-horizon bounded observer/actuator output-feedback** rather than claiming to have solved general robust output-feedback control. Existing v0.5 robust invariance assumes exact state feedback in a 2×2 independent parameter rectangle. The v0.6 scalar interval tube adds bounded measurement error, one-step applied-input timing, amplitude and slew limits, and actuator response lag, but only for a known scalar linear model with specified intervals and a finite number of sample instants. These do not compose into a general nonlinear or multivariable safety theorem. That distinction must remain explicit in every machine-readable record and exported context.

## Scope of executable methods

`scalar_observer_error_bound`: deterministic radius recurrence, with stationary bound only when |a−L|<1. `scalar_actuator_step`: magnitude clipping, rate limiting and first-order lag on a declared input. `scalar_output_feedback_tube`: conservative interval reachable sets for actual state, observer estimate and applied actuator over up to 100 discrete sample instants. `scalar_measurement_consistency`: checks whether a reading belongs to a bound-implied interval but never diagnoses a root cause. `output-feedback-casebook`: twelve authored test cases including two explicit refusal scenarios and a model-lag counterexample.

Independent NumPy and SciPy calculations validate numeric recurrence and interval-enclosure behavior on seeded synthetic inputs. Monte Carlo containment checks do not prove that actual process disturbances fit the assumed envelope; the mathematical interval argument does support model-conditional sampled containment when its inputs are accurate. The origin of any numerical result is *authored mathematical scenario*, not field data or a physical experiment.

## Content v1 roadmap for Control

A scoped v1 release should add deeper real-model parameter/uncertainty evidence, multivariable output-feedback uncertainty, rate-constrained robust sets, robust disturbance rejection and online identification limits, appropriate benchmark studies and a coherent source-inference matrix. Real hardware/OT safety validation, independent expert review, and later Bitwork/AI model benchmarking remain separate acceptance gates. The next increment should prioritize **measurement provenance for one authentic control trace** and a justified model mismatch study, rather than merely increasing the number of reference records.

## Release vetoes

Reject version promotion if earlier source records are silently rewritten, measurements are invented, the source scope is broadened beyond actually inspected portions, the observer uses the requested instead of applied input, the finite tube is labeled an infinite invariant certificate, bound conditions are silently replaced by probabilities, invalid input domains are accepted, code retrieval is treated as authority to actuate hardware, or the extracted release fails its checks.

**Policy:** complete all 30 Atlas domain knowledge libraries first; build and validate the shared Bitwork router only afterward; transfer the consolidated system to the computer last. Agent Atlas remains queued. Control remains active at v0.6, not scoped v1. No physical systems are operated.


---

# 53. Real control data: identify the recorded experiment before fitting

A real-data source is useful only when the variables actually record the intervention and observations required by the model. An experiment reporting elapsed time and motor RPM is not automatically a record of actuator inputs, even when its filename names a PWM setting. Conversely, a log containing both requested REF and actually applied PWM must not use REF as if it were the plant input. The mathematical relationship to be identified is conditioned on the physical actuation, measurement timestamps, transport delay, sensor quantization, and unobserved disturbances.

## OpenMCT laboratory data: publisher-grounded source scope

A 2026 open-access dataset by Alejandro Von Chong and Dorindo Cárdenas, deposited as **Mendeley Data v2, DOI 10.17632/5xvg43r9r8.2**, contains 14 acquired logs and more than 60,000 sample rows from a documented DC-motor educational platform. The version-2 description reports 10 columns: reference command (`REF`), measured speed (`MEAS`), measured loop interval (`DT_ms`), raw and averaged current-sense signals (`CURRENT_RAW`, `CURRENT_AVG`), applied PWM, and asynchronous digital-multimeter reading, time, age and ID. The article *Data in Brief* 69 (2026) 113274 provides the apparatus and analysis context and its authors. [Dataset publisher](https://data.mendeley.com/datasets/5xvg43r9r8/2). [Article DOI](https://doi.org/10.1016/j.dib.2026.113274).

The *published file descriptions and fields were inspected*, and the dataset page states **CC BY 4.0**. The original raw log bytes could not be retrieved through the available environment; accordingly **no v1 model fit, RMSE, current calibration or sampling statistic is presented as derived from OpenMCT's actual files**. The Atlas provides a strict local parser and chronological validation module ready to run on an explicitly supplied, authentic log. This is a reproducibility pipeline, not a performed empirical reproduction. The source list and checkout procedure record this distinction.

## Why metadata is a scientific prerequisite

A recorded error requires knowing when reference and observed speed were aligned. A plant could have fast dynamics at 2-ms sampling but a different effective response when a controller is deployed at 50 ms. Firmware filters can shift current measurements, and an asynchronous digital multimeter can repeat the same reading across many GUI rows. Counting repeated sample IDs as independent instrument measurements would artificially inflate apparent precision. `CURRENT_AVG` may contain provisional calibration; the original data article explicitly warns that final current calibration relied on the raw current data and the DMM.

The parser rebuilds acquisition times from the preceding recorded `DT_ms` values, refuses nonpositive intervals or malformed records, and counts unique digital-meter sample IDs. It does **not** invent absolute clock synchronization, replace missing DMM readings with zero, or infer that nominal PWM filename labels equal the applied time-series input. An observer model cannot be validated merely by possessing a CSV with thousands of rows.

## Future real-data gate

For any external data-based result, preserve upstream source UUID and release version, byte hash, acquisition method, raw log count, exact parser/fit version, sampled time axis, training/validation separation, potential closed-loop identification bias and all failed checks. Fit-performance numbers derived from the same identification record are not independent out-of-sample accuracy estimates. A successful numerical fit is not a physical safety certificate.


---

# 54. A small actual motor trace can support description but not a plant gain

A separate public educational GitHub project, [PID_Motor_Controlled](https://github.com/dilusha-c/PID_Motor_Controlled), includes three short CSV files labelled with PWM conditions 30, 50 and 70. The records each contain 49 timestamp/RPM pairs, between approximately 0.2 and 9.8 seconds. Their owner says the project's code and documentation remain the group's intellectual property; **the Atlas does not copy the raw CSV files, assume a permissive software license, or merge them with the Mendeley OpenMCT dataset**.

The Atlas's `evidence/v1_sources/public_motor_rpm_summary.json` records the original Git blob identifiers and the derived results. Under the file labels 30, 50 and 70, the overall measured-speed means are approximately **200.66**, **247.51**, and **265.93 RPM**. A descriptive last-10-record mean is approximately **196.96**, **249.96**, and **264.36 RPM**, respectively. Population standard deviations across the 49 logged points are approximately 16.34, 15.86, and 12.21 RPM. These are descriptive summaries made directly from the public raw text, **not** publisher-stated benchmarks, fitted dynamic models, precision estimates, or independently replicated trials.

These logs do not include per-timestep applied PWM, setpoint, current, load torque, mechanical conditions, or a synchronized controlled/uncontrolled comparison. The filename labels may indicate a nominal constant setting, but do not establish the sampled input actually applied at each time. Because the input within each trace is effectively unexcited and the trial conditions differ, the Atlas explicitly refuses to identify `y[k+1]=a*y[k]+b*u[k]+c` from these files. In particular, fitting an ARX model with a constant `u[k]` makes `b*u` indistinguishable from the intercept. Joining separate 49-point runs end to end creates artificial transitions between different experiments and is not a valid fix.

Even a visually stable speed over the final ten points is not a certified steady-state value, and the observed differences cannot be attributed solely to PWM without verifying the apparatus and protocol. This case demonstrates a valuable **evidence-preserving refusal**: real experimental numerical records can be described faithfully without manufacturing the missing identification information.

The primary dataset has no verified transfer license. The shared source cards link to its public origin but preserve the rights and state limitations. The independent OpenMCT 2026 paper supplies a better instrumented example for future empirical analysis once its explicitly licensed raw logs are retrieved and authenticated.


---

# 55. Acquisition intervals and asynchronous measurement alignment

Control algorithms are sensitive to the difference between sampling time, communication latency and the timestamp of a physical reading. The OpenMCT article records measured loop interval `DT_ms` and a separate asynchronous DMM timestamp, sample age and ID. Those fields are deliberately different. For a log with entries `0..N-1`, this Atlas constructs `t[0]=0` and `t[k+1]=t[k]+DT_ms[k]/1000`, preserving the experiment's interval recordings instead of imposing the nominal sampling period. The reconstruction establishes relative acquisition time **conditional on correct firmware logging**, not an absolute synchronized laboratory clock.

A multimeter may produce one reading every several control-loop iterations. Consecutive GUI records can repeat a single `DMM_SAMPLE_ID`, so repeated rows must not be interpreted as independent current samples. `parse_openmct` keeps explicit counts for absent, duplicate, stale and first-accepted DMM IDs; it refuses partial asynchronous records and does not interpolate missing values. A duplicate ID is not an independent replicate even if its sample age appears low. In the strict loader all required speed, timing and PWM fields must be finite; blank or NaN DMM records are permitted only as a whole missing group. These are software schema choices based on the published column description, **not yet verified against all raw v2 logs**.

For a discrete model `y[k+1]=a*y[k]+b*u[k]+c`, the input should be the **PWM recorded as applied** at sample k. Substituting `REF` would model the command rather than the actuator. Strong sample-interval jitter can invalidate one constant discrete coefficient matrix; this implementation rejects logs exceeding a chosen relative jitter tolerance. It does not resample automatically, infer time delays, identify sample-drop patterns, or align independent instrument clocks after the fact.

## Failure situations to retain

- Negative, zero or nonfinite acquisition interval: refuse, because time ordering is not physically defined.
- Repeated DMM ID: count once per unique meter reading, not once per GUI sample.
- Partial DMM fields: explicitly flag malformed/missing cross-channel data instead of treating them as a measurement of zero current.
- Large time jitter: a constant-sample ARX equation has an unverified premise; refuse or use an actual variable-step model.
- Reference command differs from applied PWM: log both, and identify which is an observed command versus physical actuation.

Preserve these statuses with any downstream record. NIST SP 800-82 Rev. 3's operational-technology guidance additionally emphasizes security, safety and operational reliability as distinct requirements for real equipment; the **September 2026 Rev. 4 is still a draft**, not a final replacement at this release date. [NIST final Rev3](https://csrc.nist.gov/pubs/sp/800/82/r3/final), [Rev4 initial draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd).


---

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


---

# 57. Two-state, two-sensor observer uncertainty without hidden safety claims

A model-based state estimate `xhat` is not the physical state `x`. For a linear sampled plant `x[k+1]=A x[k]+B u_applied[k]+w[k]`, observations `y[k]=C x[k]+v[k]`, and observer `xhat[k+1]=A xhat[k]+B u_applied[k]+L(y[k]-C xhat[k])`, the error `e=x-xhat` obeys

`e[k+1]=(A-LC)e[k]+w[k]-L v[k]`,

**but only** when the plant and observer use the same *known applied* input, identical time indices, and known A,C,L. The `u` term cancels exactly under that premise; if the actuator applies an unknown lagged value while the observer uses its requested command, this equation is wrong. This edition implements **2×2 A, C and L**, corresponding to two-dimensional state and two measured outputs.

Given componentwise **hard** bounds `|e0|≤E0`, `|w|≤W`, `|v|≤V`, the deterministic recurrence `E[k+1]=|A-LC| E[k]+W+|L|V` bounds each component for a requested finite horizon. An arbitrary Gaussian standard deviation is **not** a hard bound. The implementation checks every input matrix, refuses nonfinite/negative bounds, and returns the radius sequence, F=A−LC and qualifying assumptions. The algorithm operates on normalized/stated unit-compatible states; if states or output channels have different physical dimensions, the matrix entries and bounds must carry a dimensionally valid identification model.

## Distinguish finite bounds and sufficient long-term conditions

A finite sequence of radii proves **only** that the stipulated model's sampled observer error lies within the numerical envelope through the requested steps. The simple condition `max_i Σ_j |F_ij|<1` is a sufficient contraction criterion; when it passes, the code reports a conservative common infinity-norm radius `max_i(W+|L|V)_i/(1-max_row_sum)`. The condition is not necessary for asymptotic stability: certain rotations are stable while this particular interval norm test fails. Returning `stationary=None` is a refusal to *prove* it by this sufficient argument, not proof of physical instability.

## Consistency is not diagnosis

For measurement y and predicted C*xhat, the expected componentwise sensor envelope is `C*xhat ± (|C|E+V)`. Readings outside it contradict at least one declared assumption—sensor, timing, state, plant, applied input or noise bounds. They cannot identify a faulty sensor without independent redundancy and diagnostic evidence. Two apparently consistent readings also do not prove the sensors are authentic. No hardware or safety interlock is operated by this reference tool.

**Sources:** Stanford and MIT observer introductions on Luenberger error dynamics, and NIST's final OT guidance on separating integrity and operational safety. This chapter contains original finite interval derivations, not a third-party experiment.


---

# 58. Observer, actuator and control command form a coupled system

A feedback law can be mathematically well designed and still fail if the actuator differs from the commanded input or if its sensor estimate is stale. A useful implementation record therefore separates `requested_u`, `magnitude_clamped_target`, `slew_limited_target`, and `applied_u`. The previous Control editions provide scalar actuator lag, clipping and finite-horizon bounded output-feedback tools. Version 1 adds a separate two-state/two-sensor observer-error reference, but it **does not** automatically combine it with a multivariable physically certified actuator/controller.

This separation is intentional. A correct observer proof relies on the **same applied input** in the predictor and real plant. An experiment with only the command reference can support a setpoint-tracking description, not a strict proof that the actuator executed it. The 2026 OpenMCT logs retain PWM alongside the reference, precisely the information that can distinguish commands from applied actions. Those actual raw logs are not present in the current release; no empirical controller-model cross-check is claimed.

A source-aware Control Atlas should answer three different questions: *what was requested*, *what physically happened*, and *what does the model permit us to infer*. An input limit within an offline optimizer is not a safety-rated physical interlock. A finite-time reachable tube does not guarantee unmodeled intersample behavior or faults. A small observer covariance is conditional on the assumed noise model; it is not a measured bound unless a lab has validated one.

The next real integration work after all thirty domain libraries will use these typed relations to retrieve the correct conditional source and method, not to issue device commands. The existing Forge retrieval contract remains unchanged in this content phase.


---

# 59. A public control log is not permission to fabricate or redistribute evidence

The reference corpus contains three distinct source types: peer-reviewed and government guidance; a 2026 CC BY motor-control dataset described in an accessible open-access article; and public educational project files with an unspecified third-party redistribution license. These cannot be mixed under one licensing, reliability or scientific-validity label.

For the Mendeley OpenMCT version-2 dataset, the public metadata support its DOI, licensing, apparatus description, number of logs and column schema. **Direct raw-file bytes were not obtained through the current environment**. The Atlas therefore ships a parser and test fixtures, not publisher logs, and does not invent real-data fit metrics. Its parsed results must carry original file names, hashes, acquisition dates and dataset version when later executed. The article's analysis on the same identification run is not independent model-transfer validation.

For the public `dilusha-c/PID_Motor_Controlled` repository, three short source CSVs were read from GitHub to calculate *derived descriptive summaries*, but raw files are not bundled because the public README does not grant a clear distribution license for the group's data. The source identity, file-level Git blob SHA and derived metrics are recorded in a bounded summary. Each file has 49 time/RPM rows, but no measured per-row input; their differences cannot establish a plant gain, validate a PID controller, or certify repeatability. The source is also not a peer-reviewed replication of OpenMCT and is **not** merged into that dataset.

A cryptographic hash of a local normalized record confirms those bytes only. A Git blob ID identifies the source blob selected by the tool, not a measurement calibration certificate. Source URL stability, scientific review, measured uncertainty, instrument timestamps, physical specimen state and owner permission are independent axes of trust. The architecture must preserve each axis rather than reducing them to an attractive record score.

The collection's release schema explicitly separates `software_tested`, `numerically_reproduced`, `authentic_raw_data_evaluated`, `independent_engineer_reviewed`, `hardware_tested`, and `AI_performance_improved`. A model result that lacks any of those flags must not be represented as though the missing approval occurred.


---

# 60. Physical safety and operational technology are separate acceptance domains

Industrial control systems interact with equipment and the physical environment. The most relevant U.S. reference for this edition is **NIST SP 800-82 Rev. 3 (Final, 2023)**, which describes operational-technology reliability, safety and security as distinct requirements. **Rev. 4's September 2026 release is an initial public draft**, not a final replacement. A research control calculation is not an authority to operate a device or override its safety interlock.

An observed-model discrepancy could arise from a sensor fault, actuator delay, process disturbance, network timing, invalid plant linearization, changed process feedstock or a malicious data source. A single residual cannot identify which explanation is true. A proper diagnosis requires independent observations, verified time alignment, known limits and a test plan; the observation itself is not a command to modify a controller.

Before a physical deployment, a qualified engineering team needs hazards and constraints, equipment specifications, model structure, identification conditions, verified uncertainty envelopes, actuator characterization, fallbacks and safe-state logic, watchdog deadlines, interlock independence, change management, rollback and measured closed-loop tests. Where safety functions exist, their verification is independent of the AI knowledge layer. Merely checking that a simulated trajectory remains within a box says nothing about unmodeled faults or regulatory compliance.

The Atlas implementation does not expose hardware drivers, network endpoints, firmware update controls or device credentials. Its code computes mathematical reference values, parses external files supplied by an operator, and returns explicit refusal conditions. It must never interpret a retrieved source document as permission to execute code or control equipment. The future Bitwork navigation system, which will be built *only after all 30 domain knowledge libraries*, must preserve these constraints.


---

# 61. Scoped Control Atlas v1 content acceptance and remaining real-world validation

A scoped v1 reference content edition should be an honest collection milestone, not a claim to have solved the field of control engineering. This edition retains all earlier source and model revision IDs, with bounded sources, calculations, failure cases, example code, a real public trace description and a documented external-data ingestion path. It does **not** establish physical model robustness, guarantee stability, identify real faults, or prove improvement in AI output quality.

## Content included

- Classical sampled dynamics, stability, controllability, observability, PI/PID saturation, LQR/Kalman and small-gain references from earlier editions.
- Multivariable return-difference, Lyapunov certificates, constrained planning, residual diagnostics and model-mismatch counterexamples.
- Robust state/actuator tube examples that separate requested and applied commands, state estimates, hard bounds, and intersample limits.
- A bounded 2×2 two-sensor observer error and measurement-consistency reference.
- A ten-column OpenMCT log ingestion/chronological ARX validation workflow, with synthetic tests and clear **not-run-on-publisher-raw** status.
- Actual derived descriptive statistics from three public time/RPM traces, without treating nominal PWM filenames as measured per-row excitation or republishing unlicensed data.

## Scientific and platform gates open

1. Acquire rights-cleared original raw OpenMCT v2 files through a permitted channel, verify hashes against publisher's manifest, and perform an honest train/holdout reanalysis with failure traces.
2. Validate hard plant, actuator, disturbance, timing and sensor bounds from physically calibrated equipment; include hardware-in-the-loop and safety assessment where applicable.
3. Independently review source-critical control theory derivations, model assumptions, numerical conditioning, and the actual application domain. One simulator or synthetic oracle does not prove that an adopted model represents a plant.
4. Extend to general multivariable output-feedback and robust constrained control with realistic correlated uncertainties, nonlinear and delayed dynamics, and proper objective/feasibility checks. This edition is bounded rather than a universal controller.
5. After all 30 domain content libraries exist, develop and evaluate Bitwork routing against lexical/semantic baselines with held-out questions. Then perform real Windows host validation before transfer to the user's computer.

## Release vetoes

Stop an edition if schema closure fails, older record revisions change, links lose the scientific limitations, a numerical oracle disagrees with its declared target, an unavailable raw dataset is described as measured here, or the unpacked archive cannot reproduce its tests. The release label is a *scoped content* milestone only; external science and deployment acceptance remain false. Control belongs to the broader modular reference program, not to an autonomous equipment-control network.


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


# Worked investigations
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

# Investigation 19 — Nominal and interval robustness cannot be conflated

Given the *invented* scalar discrete plant `x[k+1]=a x[k]+b u[k]` with `u=-x`, compare two coefficient boxes. In the first, a∈[0.9,1.1] and b∈[0.25,0.45]. The four closed-loop poles range between 0.45 and 0.85 and the entire independent interval box satisfies |a-b|<1. The exact vertex argument works only because the scalar pole is affine and the set is a rectangle. In the second, a∈[1.35,1.8] and b∈[0.05,0.25], the worst case pole is 1.75. The model uncertainty set contains an unstable member.

A failed interval bound is not a physical failure report. The box boundaries must be justified independently: identification confidence intervals are not strict guaranteed parameter bounds, unknown actuator nonlinearities are not represented by a or b, and a larger unmodeled state can destabilize a nominally stable scalar projection. An engineer should design an experiment that measures the actual dynamics, actuator constraints, sensor timestamps and relevant operating regions.

**Run:** `python -m control_atlas robust-casebook`. **Result:** the node reports exact bounded mathematical classifications with assumptions and refusals; no equipment was controlled. Source scope: [Åström–Murray](https://fbswiki.org/) mathematical robustness topics.


---

# Investigation 20 — A one-sample delay reverses the stability result

A constructed discrete plant has a=1.5, b=1, K=1.2. Without feedback delay the characteristic pole is `1.5−1.2=0.3`, stable in the ideal linear scalar model. With feedback based on x[k−1], the characteristic equation is `z²−1.5z+1.2=0`. Its complex roots have magnitude `√1.2≈1.095445`, outside the unit circle.

The counterexample exposes a key architecture risk: assuming local-model decision time equals actual sensor-to-actuator response time. A model that passes without delay may fail even with one exact sample delay. It does **not** establish the stability of random, multiple-period, packet-loss or asynchronous delays. Record per-message timestamps, jitter, synchronized clocks, actuator timing and dropouts; select a model aligned to observed dynamics.

**Run:** `python -m control_atlas robust-casebook`. Published networked-delay research considers much broader structures than this algebraic example; [networked delay/dropout study](https://www.sciencedirect.com/science/article/pii/S0016003213001920) abstract is only background.


---

# Investigation 21 — Failure to certify with P=I does not mean unstable

For A=diag(0.7,0.9), a candidate P=I gives Q=diag(0.51,0.19), both positive definite, certifying strict decay of V=xᵀP x in the stipulated autonomous 2×2 discrete model. The calculation is a finite-precision diagnostic, not a machine-checked formal proof.

For the different matrix `A=[[0.5,4],[0,0.5]]`, the two eigenvalues equal 0.5, yet P=I does **not** satisfy the strict quadratic decrease test because the cross term causes large transient growth in the Euclidean norm. Saying “therefore A is unstable” would be a logical error: another P can certify it. A failed candidate is *not certified*, not a counterproof of all certificates.

This also illustrates why a nominal eigenvalue check is incomplete for a real controller with saturation or uncertain dynamics. The source-linked record must preserve what property was actually tested and which physical features were excluded. [MIT Lyapunov notes](https://underactuated.mit.edu/lyapunov.html).


---

# Investigation 22 — A frequency-domain identity that does not imply complete rejection

For the synthetic stable first-order plant `G(s)=2/(1+3s)` with proportional feedback Kp=1, evaluate at ω=0.5 rad/s. The loop transfer is `L=2/(1+1.5j)`. The program computes sensitivity `S=1/(1+L)`, complementary sensitivity `T=L/(1+L)`, and confirms the complex identity S+T=1. The magnitudes are approximately 0.53748 and 0.59628: they do **not** sum to one because complex magnitudes do not preserve addition.

This exercise does not show attenuation at every frequency, gain margin, disk margin, or stable behavior under unmodeled delay. The input disturbance, sensor noise and reference commands enter different parts of a block diagram. A controller engineer must request the correct transfer paths, physical noise spectrum, bandwidth and sampling. A diagram rather than a single gain number may be required. [Python Control margin docs](https://python-control.readthedocs.io/en/latest/generated/control.margin.html) support the distinct margin concepts.


---

# Investigation 23 — Perfect in-sample fitting is not validated identification

A synthetic alternating residual sequence `[1,-1,1,-1,...]` has mean zero and unit RMS, yet its lag-one correlation is strongly negative. A mean-zero residual is not evidence of white noise. A low lag-one correlation in another sequence would also be insufficient: a model may have lag-two correlation, correlation with past inputs, wrong disturbance variance or operating-regime shift.

The new function returns descriptive lag-one correlation but no p-value or significant-whiteness claim. It refuses constant residuals because the centered energy is zero and correlation undefined. It cannot infer sensor bias from one number, and it does not fit nuisance models, test the causal excitation design or identify a physical plant. [System Identification residual guidance](https://www.mathworks.com/help/ident/ug/what-is-residual-analysis.html) distinguishes residual autocorrelation and input-residual independence checks.


---

# Investigation 24 — Refusal of stale or invalid sensor input is not a safety certificate

A synthetic five-step trace asks an offline supervisor to evaluate commands. The first sensor reading is fresh, valid and consistent, so the requested output is retained. The next reading is stale; the third is flagged invalid; the fourth has an innovation larger than the caller's threshold; the fifth is fresh and passes. The program blocks exactly three of the five commands and substitutes a *caller-provided* fallback.

This deterministic calculation never actuates a device. A zero fallback can be dangerous on some real processes; the application must identify an actual safe state and independent physical interlocks. Sensor freshness does not prove accuracy, and a small innovation can result from shared model/sensor bias. No hazard analysis, safety-rated watchdog, emergency-stop function, timing deadline guarantee or industrial standard compliance is claimed. The only verified result is explicit software rejection under a declared policy.

A useful evidence packet would record sensor capture timestamps, input provenance, clock drift, innovation model, thresholds, fault rates, actuator commands versus observed actuation, safe-state feasibility and operator oversight. These data are not present in the synthetic trace.


---

# Investigation 25 — One harmless-looking gain matrix, one ill-conditioned direction

**Origin:** constructed 2×2 algebraic example. No real dynamic system or control hardware.

Supply G=[[1,−1.99],[−1.99,1]] and K=I. Then M=I+GK=[[2,−1.99],[−1.99,2]]. Its singular values are **3.99 and 0.01**, and condition number **399**. The program's S=(I+GK)⁻¹ and T=I−S satisfy S+T=I within floating-point tolerance.

The near-singular direction is a useful warning: looking at individual entries, or a single scalar “loop gain,” misses directional sensitivity. But this calculation contains no poles or frequency sweep; it cannot show whether a dynamic plant is internally stable or robustly stable. Singular values at one frequency cannot replace a system model, actuator saturation checks or a site-specific safety case.

**Reproduce:** `mimo_2x2_return_difference(G,K)` in `control_atlas.advanced`. An independent NumPy SVD and inverse agree on randomized 2×2 models in the release oracle. **Next evidence:** obtain transfer/state-space dynamics, operating point, calibrated units, bandwidth, latency and full-frequency uncertainty before making a physical stability claim.


---

# Investigation 26 — A common certificate is sufficient; a failed candidate is not an instability verdict

For a synthetic discrete-time family with A11∈[.5,.6], A12,A21∈[−.03,.03], A22∈[.3,.4], and P=I, the program checks all **16** matrix-box vertices and finds a strictly positive minimum eigenvalue of Q=P−AᵀPA. The worst is approximately **0.634697**. Under the exact linear model, the convexity argument supports a common quadratic decrease statement across the entire independent-entry box; this is not an interval-arithmetic verification of actual equipment.

Now replace the family with a single A=[[.8,1],[0,.8]]. Its eigenvalues are both .8, so it is asymptotically stable, yet P=I fails the sufficient test. The program correctly reports *candidate not certified*. Calling the plant unstable would be wrong. Another P may certify it. A real controller with saturation, delays or correlated uncertain coefficients is outside this test's scope.

**Adversarial question:** does numerical vertex checking prove robustness under every industrial disturbance? **Answer:** no. The guarantee is conditional on the exact bounded discrete-time matrix family, verified modeling assumptions, and numerical tolerance. Separate physical uncertainty identification, disturbance and interlock engineering remain necessary.


---

# Investigation 27 — The Riccati cost identity does not certify an actuator

A constructed two-state integrator uses A=[[1,1],[0,1]], B=[.5,1], Q=diag(10,1), R=.25, Qf=diag(10,1), x0=[2,0] and horizon eight. A backward Riccati recursion generates optimal feedback gains for this **unconstrained** finite-horizon linear model. Its predicted total quadratic cost equals x0ᵀP0x0 within numerical precision. Separate SciPy full-control-sequence minimizations agree on randomly generated models.

That identity verifies the optimization calculation. It does not indicate that the resulting input could be delivered by a physical actuator or that the state is safe. Motor torque, current limits, heat, actuator lag, encoder noise and sample clocks are absent. Nor does a finite-horizon nominal optimum prove global robust stability after the horizon.

An evidence-rich engineering study would compare physical input limits with the predicted first action, identify plant matrices and uncertainties, include timing and disturbances, and test admissibility with a qualified constrained controller. The Atlas exports a method result with limitations, not an actuator command.


---

# Investigation 28 — Finite-grid feasibility is a deliberately weaker claim than MPC

A toy scalar plant x+=x+u starts at x=1.5. With |x|≤2, |u|≤.75, horizon 4 and grid {−.75,−.5,0,.5,.75}, exhaustive search returns a low-cost admissible grid sequence. The result is optimal only among **the explicit finitely many grid candidates**; it is not necessarily optimal among all continuous admissible inputs. The method does not execute a receding-horizon loop.

Another toy plant has a=1.3, b=1, x0=1.9, |x|≤2, |u|≤.1 and grid {−.1,0,.1}. No grid candidate stays within the state bound at its first step. The program returns `no_feasible_candidate_on_grid`. It intentionally does not claim all conceivable continuous or redesigned control strategies are infeasible.

**Failure test:** treating an infeasible *grid* as proof of a globally infeasible physical plant is a category error. A real design needs independently verified bounds, disturbances, actuator dynamics, timing and terminal safety constraints; no physical safe state is known from this data.


---

# Investigation 29 — Innovation covariance and identical sensor readings with different causes

A constructed two-sensor innovation vector ν=[2,0] has covariance S=[[4,1],[1,1]]. The normalized squared innovation νᵀS⁻¹ν is **4/3**. If the off-diagonal covariance were falsely treated as zero, the result would instead be 1. Covariance structure is not a decorative metadata field; it changes the calculation.

This statistic is not a fault-class label. A single measurement y=10 can arise from actual state x=10 with zero bias or x=8 with bias 2. Both are perfectly consistent with the same reported sensor value. The library explicitly returns `not_identified_by_this_measurement` rather than guessing whether a machine changed or a sensor drifted.

A proper diagnostic investigation would compare an independently calibrated sensor, inspect actuator and timestamp evidence, incorporate a physically justified state observer and excitation, and account for communication or adversarial data issues. NIST's OT integrity guidance treats anomaly monitoring and system assurance as additional engineering layers, not proof of a root cause.


---

# Investigation 30 — Perfect training fit, worse later prediction

A constructed 32-step scalar ARX history starts with dynamics x+=.8x+.2u for its first 24 samples. The later eight steps instead use x+=.95x+.2u. The training model fits the first segment to near machine precision; its later one-step prediction RMS is about **0.129** because the true synthetic system changed. This is mathematical evidence that training fit alone cannot establish future prediction quality.

The implementation uses a chronological hold-later segment, not an external trial. The validation residuals use the **observed** prior state at each step. It therefore does not test multi-step model rollout accuracy, closed-loop stability, or real machine drift. It also refuses a constant-state/zero-input history with insufficient excitation rather than presenting arbitrary fit coefficients.

This example suggests a data-collection protocol: define a target operating envelope, record independent process disturbances and times, reserve later data by regime/shift, log actual vs commanded actuator values, and compare residuals under alternative models. In a real closed-loop process, ordinary least squares may still be biased by feedback; held-out time does not identify causation by itself.


---

# Investigation 31 — A monitor that says “normal” is not a physical safety interlock

An anomaly monitor is supplied sensor values, timestamp ages, model residuals and conditional covariance. It produces an alarm or model-consistency statistic. The result may be correct as a mathematical calculation while the underlying sensor data are false, delayed, manipulated or not representative of an actual hazard. A narrow NIS value cannot certify the plant's safe state; a large NIS cannot automatically name a failed part.

**Research response:** a decision record distinguishes (a) expected data within model assumptions, (b) model departure, (c) unknown cause, (d) unverified source integrity, and (e) independent operational safety status. Escalation to trained operators, site-defined physical interlocks and hazard analysis are separate from research software. The library has no PLC driver or network connection.

**Source maturity:** NIST SP 800-82 Rev 3 is a final OT security guide; the 2026 Revision 4 is an **initial public draft** at this checkpoint, not an adopted replacement. That distinction is part of the source card and must travel with any AI response. The user requested that all thirty domains be built first, then routing/Bitwork last, then desktop transfer. No further installation is performed here.


---

# Investigation 32 — An invariant box under bounded disturbance

**Question:** Can a fixed two-state feedback law keep every state within a chosen box under stipulated plant and disturbance uncertainty? In the authored example, the state radii are `[1,1]`, disturbances are bounded by `[0.05,0.05]`, and feedback is `K=[0.1,0.1]`. The six independent plant intervals provide 64 vertices. For each vertex, the tool bounds `|x'_i|≤Σ_j |A_ij-B_i K_j|r_j+d_i` and compares with the chosen state radii. It separately checks `|u|≤|K0|r0+|K1|r1≤0.25`.

The construction produces a conditional mathematical certificate under an exact sampled LTI model and true full-state feedback. It uses no plant data, actuator device or physical sensor. The maximum bounds are not confidence intervals learned from measurements; they result from stipulated input intervals. If those intervals are false, the certificate does not apply.

An independent test enumerates all 64 parameter corners and four state-box corner signs across seeded synthetic models. It compares the worst observed one-step bound to the original algorithm, without pretending the random tests are a physical experiment. An invariance result can be used to organize a test plan, but only a qualified process-specific review can establish applicability and operational risk.

**Reproduce:** `python -m control_atlas invariance-casebook`. **Source:** MIT [Robust and Stochastic Control](https://underactuated.mit.edu/robust.html), invariant-set discussion.


---

# Investigation 33 — Stable state bound, insufficient actuator authority

The same authored model from Investigation 32 remains state-box invariant according to the ideal closed-loop equation. Shrink the allowable actuator from ±0.25 to ±0.12 while keeping feedback `K=[0.1,0.1]` and state radii `[1,1]`. The worst requested input is `|K0|r0+|K1|r1=0.2`, exceeding 0.12. The tool therefore returns `state_box_invariant_for_every_assumed_model=true`, `actuator_unsaturated_for_every_state_in_box=false`, and `conditional_invariance_and_input_feasibility=false`.

This is an explicit **veto** on the combined certificate. If the hardware saturates, the modeled feedback `u=-Kx` cannot always be implemented. A different nonlinear saturated control law requires new analysis. A low-order optimizer reporting an unconstrained optimal command is not evidence that the actuator can execute that command in time.

No device is driven. The result does not tell an operator what the physical fallback should be; even an output of zero may be hazardous for some processes. NIST SP 800-82r3 stresses integrity and safety in OT operation, but this method is a teaching tool, not a safety instrumented system.


---

# Investigation 34 — A proof for x is not a proof for x-hat

The mathematical invariant-set certificate assumes exact state feedback. In a constructed simulator, the state evolves as `x'=A x+B u+w`, but the command uses `u=-K(x+bias)` subject to a clamp. A second run with identical underlying plant and disturbance sequence adds an artificial sensor bias after the sixth sample; the commands and state trajectories differ.

These series are not physical data. The simulator cannot determine whether a real anomalous reading comes from a physical state shift, sensor offset, numerical drift or a malicious manipulation. It only demonstrates that an unmodeled estimation error can alter feedback. The robust-box method refuses to return a proof when full state feedback is not affirmed; a robust observer-controller proof would need to model estimation error, clock delay and disturbance coupling.

**Evidence request for a real investigation:** independent reference sensors, sensor calibration, time stamps, actuator response, control-law version, sensor fusion assumptions and safety-logic responsibility. NIST SP 800-82r3 provides an operational integrity context. No fault diagnosis or security incident is inferred from this synthetic case.


---

# Investigation 35 — One-dimensional interval certificate and its limits

For `x[k+1]=g x[k]+w[k]`, assume `|x|≤r`, `|w|≤d`, and ideal feedback command magnitude `|u|=|k x|` capped at U. The interval is robust invariant under the supplied scalar model exactly when `|g|r+d≤r`, and requested inputs remain admissible exactly when `|k|r≤U`. These are worst-case inequalities over independent closed intervals, not statistical probabilities.

With stipulated `g=0.7`, `r=1`, `d=0.2`, `k=0.2`, `U=0.3`, the worst successor magnitude is 0.9 and the actuator command bound 0.2. The model condition passes. Change `g` to 1.1 without updating the interval and the invariant candidate fails. This does not establish safety or failure for any real machine. The actual plant may have an unmodeled state, delay or different disturbance bound, and physical units of the state matter for interpretation.

Use this as a falsifiable mathematical worked example: demand source and derivation for g, k and d before treating its status as more than a calculation. The higher-dimensional certificate generalizes the same philosophy, not every possible control system.


---

# Investigation 36 — Why a hundred successful rollouts do not certify a bounded set

An experimenter simulates an original two-state model with disturbances alternating among `[+0.05,0]`, `[−0.05,0]`, `[0,+0.05]`, `[0,−0.05]`. The trajectories stay finite. This is useful to test that the implementation does not numerically explode on those cases. It does not check every initial state, disturbance sequence, interval-parameter combination, sensor-bias pattern or actuator condition.

A universal invariant-set certificate requires inequalities covering **all** modeled states and disturbances in the set. The exact corner-based method can prove this conditional mathematical statement for a rectangular 2×2 class. But it cannot prove its own uncertainty bounds were measured correctly. Conversely, a single synthetic violation under assumptions can falsify an overly broad numerical claim, even though it does not show that actual equipment will fail.

The study should label distinct evidence: code tests, separate numerical algorithms, model-specific mathematical proof, experimental system identification, operator safety review and deployed behavior. None can be replaced with a number of rendered charts or agent-generated explanations. **No actual process was controlled** in this work.


---

# Investigation 37 — A stable observer still has a nonzero error envelope

**Origin:** synthetic scalar discrete-time model. Let a=0.8, observer gain L=0.6, initial error radius E0=0.1, bounded process disturbance W=0.02, and bounded sensor error V=0.01. Under the same known applied actuator input in the plant and observer, the error dynamics are `e[k+1]=(a-L)e[k]+w[k]-L v[k]`. The absolute error radius therefore updates as `E[k+1]=0.2 E[k]+0.026`, giving a limiting sufficient radius of **0.0325** model units.

The error begins at 0.1 and approaches 0.0325, not zero. A nominal observer pole of 0.2 is compatible with residual error caused by bounded disturbances and sensor error. If a-L becomes 1.2, the recurrence remains numerically defined over a short interval but does not admit a finite stationary bound under the same argument. The `scalar_observer_error_bound` program explicitly reports `None` for that stationary certificate.

**What was not measured:** no physical sensor noise maximum, process disturbance envelope, time synchronization or applied actuator log. If V were a Gaussian standard deviation rather than a hard bound, this deterministic certificate would not follow. A downstream AI must carry those assumptions with the 0.0325 result.

**Sources:** MIT *Underactuated Robotics* state-estimation reference; Mayne et al. 2006 output-feedback constrained-control abstract. The recurrence and synthetic values are authored, not source-reported measurements.


---

# Investigation 38 — The difference between an issued command and an actuator state

**Origin:** original actuator model, no hardware, motor or valve test. Suppose the controller requests input 10 in a generic unit. The actuator can accept magnitude at most 1, change by at most 0.2 per sample, and its modeled discrete response fraction is alpha=0.5. At the current sample the applied input equals zero.

The intended command is 10. The magnitude target becomes 1. The slew target becomes 0.2. The *applied next-sample input* becomes **0.1**. All four values are different. The plant consumes the *previous applied input* during this present step, not the new applied target unless the timing equation is changed. An LQR or PI regulator optimized under u=10 immediately applied would be predicting an entirely different plant.

If the slew limit is zero, the actuator state remains unchanged regardless of the requested command. If alpha equals one, the next applied state reaches the already limited target. These are arithmetic results of the assumed actuator model; they do not identify actual lag, friction, backlash, deadband or mechanical failure.

**Failure mode:** report that the controller “acted” merely because a command was logged. The relevant evidence is actual actuator position/force/flow with timestamp and uncertainty. Without it the control loop's input remains unverified. The final control record explicitly refuses physical actuation approval.

**Source:** Newton and Kroo, AIAA 2023 published abstract on actuator rate-limit effects; MIT/Åström feedback references. The specific scalar model and example are newly authored.


---

# Investigation 39 — A safe-looking sampled tube does not prove safe operation

**Origin:** authored 12-step interval simulation and overapproximate bound. Model `x[k+1]=0.6 x[k]+0.2 u_applied[k]+w[k]`, controller `requested=-0.4 h[k]`, observer gain L=0.55, initial estimate h[0]=0.1 and error radius 0.05. Disturbances satisfy |w|<=0.01 and |v|<=0.01 by stipulation. The actuator magnitude limit is 0.4, slew limit 0.1 per sample, lag alpha=0.6, with initial applied input zero. The state limit is |x|<=1.

The interval tube propagates physical state, observer state and actuator separately, rather than substituting h for x. Over the twelve sampled steps, all returned physical intervals lie inside the model's state bound. This does **not** make the tube invariant beyond twelve steps, show what happens between samples, prove that actual w and v satisfy the stipulated limits, or establish a physical hardware safety function. The model omits parametric variation, state-dependent sensor degradation and unmodeled dynamics.

Under a deliberately tightened state limit of 0.04, the returned interval fails containment; the correct status is insufficient mathematical evidence under that model, **not** a demonstration of physical equipment failure. When actuator response fraction is changed from 0.6 to 0.01, the state tube changes. Ignoring this actuator dynamic can invalidate predicted behavior.

Independent NumPy-generated trajectories drawn inside the stipulated bounds remain inside the conservative computed intervals for the tested seeds; this is an implementation regression test, not a proof of real-world validity. The interval hull loses correlations between physical state and estimate, so it can reject some systems that would actually satisfy tighter constraints. That conservatism must be reported without silently changing the envelope.

**Sources:** Mayne et al. 2006, robust output feedback with invariant tubes; MIT underactuated notes on reachable sets and robust MPC. The local method is a finite scalar interval calculation, not an implementation of their complete robust MPC algorithms.


---

# Investigation 40 — A residual contradiction does not isolate a failed sensor

**Origin:** authored scalar consistency test, no real process log. Assume the estimated state h=0.1, absolute error radius E=0.04 and sensor noise absolute maximum V=0.02. The predicted measurement lies within **[0.04,0.16]**. A reported y=0.13 is consistent with those assumptions. A reported y=0.30 lies 0.14 model units above the interval and is inconsistent.

This evidence does **not** establish whether a sensor broke. The process may have experienced a disturbance outside W, the actuator may not have followed the command, the plant model might be wrong, or the timestamp may be stale. A sensor bias could also explain the residual. Each possibility requires a distinct observation or controlled study to discriminate.

A useful diagnostic next step is to inspect independent actuator feedback and a calibrated secondary measurement, verify time alignment, check software data handling, and review process changes against the model's parameter range. Those steps are a research protocol, not instructions for unattended shutdown, bypass, override or repair. No physical action is performed in this reference system.

**Sources:** NIST OT Security Guide SP 800-82 Revision 3 (final, September 2023), on unique reliability and safety requirements of OT; MIT state-estimation notes. NIST Revision 4 remained a draft in November 2026. Bound equations are original and system-specific validity is untested.


---

# Investigation 41 — Probabilistic noise and hard limits are different evidence classes

**Question:** A sensor datasheet reports a standard deviation of 0.01 units. Can we use that as `V=0.01` in a deterministic observer error certificate?

**Answer:** Not without a justified physical bound. If the model assumes Gaussian noise with standard deviation 0.01, samples can exceed any finite multiple of the standard deviation with nonzero probability. A 1σ envelope is not a strict maximum. The error recurrence `E_next=|a-L|E+W+|L|V` provides deterministic containment only when W and V are actual hard bounds (or conservative engineering bounds established by other evidence) and their time/order assumptions are true.

For a=0.8, L=0.6, W=0.02 and hard V=0.01 the calculated limiting radius is 0.0325. If V=0.01 is *only* a standard deviation, the same algebra may compute a number but a deterministic worst-case certificate is not justified. The proper output is an unvalidated model condition, and the system should request a qualified noise model and application-specific uncertainty statement. Intermittent sensor bias, saturation or stale measurements introduce separate faults not covered by the Gaussian/noise distinction.

The Atlas stores the difference between a confidence interval, a standard deviation and a hard uncertainty set, rather than compressing all three into one confidence badge. This complements Measurement Atlas, whose accepted method outputs carry their own degrees of freedom and assumptions.

**Source:** MIT *Underactuated Robotics*, State Estimation/Filtering coverage; original deterministic set-membership derivation. No sensor has been calibrated here.


---

# Investigation 42 — What would move Control toward content v1?

**Question:** Our mathematical observer, actuator and tube algorithms pass thousands of tests. Does that qualify a real machine or even complete the control reference domain?

**Answer:** No. The tests concern authored models, not observed equipment. A scoped Control content v1 should cover experimentally identified plant dynamics with an authentic, rights-cleared time series; parameter uncertainty and sensor calibration; multivariable output feedback; known actuator rate/lag data; independent validation/held-out replay; and an explicit match from the physical model to any control-theory claim. The present v0.6 adds a significant missing interface—state estimate and applied actuator dynamics—but only in a bounded scalar setting.

**Research plan:** obtain permissioned genuine plant data, define safe sampling and audit requirements, estimate a model with train/validation splits, measure actual actuator response and timestamp error, specify state/noise bounds with independent evidence, compare plausible models, and evaluate finite envelopes against genuine unseen traces. Any future hardware experiment requires qualified authorization, safe interlocks, supervised procedures and independent review. None of those actions is implemented by this reference.

**Project-wide sequencing:** build all 30 Atlas domain content libraries first. Preserve each node's source closure and immutable historical revisions. Only after domain content development should the separate Bitwork-driven routing system be built and tested on independent benchmark questions with actual models. After final integration and PC-side verification, transfer the collection as a complete versioned release. Never silently treat the routing design as an already deployed system.

**Outcome:** a defensible v0.6 research milestone with sharply defined future gates, not a falsely labeled scientific v1 or engineering safety certificate.


---

# Investigation 43 — Real RPM observations with unidentifiable actuator dynamics

Three public 2026 educational motor CSVs named `data_pwm_30.csv`, `data_pwm_50.csv` and `data_pwm_70.csv` contain 49 `(time,rpm)` rows each. We derived simple descriptive statistics from the source text as retrieved through GitHub, recording original file URLs and blob IDs in `evidence/v1_sources/public_motor_rpm_summary.json`. No raw third-party CSV is bundled because redistribution terms were not established. These are authentic *source-reported* measurements, not synthetic motor values and not independently reviewed experimental records.

The overall observed RPM means are about 200.66, 247.51 and 265.93 respectively; the last-ten-row means are 196.96, 249.96 and 264.36. They are not certified steady-state values and cannot establish a causal PWM-speed law because the records contain no row-wise actually applied PWM, load history, motor calibration or interleaving of input steps. The filename labels indicate nominal settings only. Each individual experiment has insufficient excitation to separate a dynamic input gain from an intercept, and concatenating experiments would insert false transitions.

**Negative control:** The parser for the ten-column OpenMCT design must not fabricate a PWM channel for these two-column traces. The safe result is `descriptive_rpm_summary_only`, not an identified plant or verified controller. This example demonstrates that an authentic data source can be more epistemically limited than a synthetic model whose assumptions are known exactly. The missing physical metadata is an evidence gap, not a software bug.


---

# Investigation 44 — OpenMCT v2 raw-log replay, pending source-file acquisition

The publisher's version-2 OpenMCT dataset, DOI `10.17632/5xvg43r9r8.2`, is licensed CC BY 4.0 and contains more than 60,000 rows across 14 acquisition logs. The data article describes 10 CSV columns and two metadata lines preceding the header. This investigation is a **reproducibility protocol**, not a completed reanalysis. Dataset metadata and article were checked, but direct raw download was blocked in the execution environment, so no real OpenMCT model coefficients or RMSE are reported.

Once an authorized copy is available, preserve all original file bytes and publisher SHA-256 where supplied; record dataset version, hardware and firmware metadata, file path, checksums and licence. Run `parse_openmct` on a locally supplied acquisition log, inspect the reported sample count, `DT_ms` distribution, and DMM duplicate/stale IDs, and validate that the measured PWM—not REF—was used as the plant input. A chronological split then estimates a bounded ARX one-step model, compares against persistence and computes free-run error.

The program refuses a non-monotone or unsupported sample interval, missing required fields, too few records, constant or collinear PWM excitation, and high sample-period jitter. An actual controller validation should also compare *across* acquisition runs and physical regimes rather than only within one log. A winning one-step RMSE does not establish transfer, independence of residual noise, safe actuation or instrument calibration.

**Status:** source available publicly, data acquisition not completed here; original-byte hash and real-data metrics remain `null`. Synthetic parser and numeric-oracle tests are reported separately and cannot be relabeled as experiments.


---

# Investigation 45 — A commanded signal is not an applied input

Consider a controller that commands an input of 10 arbitrary units, but the actuator magnitude, slew and response rate allow only 0.1 at the next sampled instant. Existing Control v0.6 formulas distinguish requested, clipped, slew-limited and applied values. The experiment is *synthetic*, but its central error mode is grounded in how real actuator limits affect dynamic control.

The new OpenMCT parser uses the explicitly logged `PWM` column for an input-output model and retains `REF` as the reference. The data-paper description confirms both appear in the physical log. If a regression instead uses REF while the actuator has lag or saturation, it is estimating a different relationship from the one assumed by the underlying plant equation. An observer can only cancel the input term in its error dynamics if it uses the same **known applied input** as the plant.

For real validation, compare the controller command, physical PWM, measured speed, sample time, actuator model and load changes. A channel label is not independent proof that a driver performed its action. A safety-rated independent interlock is a distinct system, not supplied by a Python clamp. No hardware was commanded during this release.


---

# Investigation 46 — Two-state observer under hard bounded sensor noise

Build a *synthetic* two-state plant with `A=[[.9,.05],[0,.8]]`, observation `C=I2`, observer gain `L=diag(.45,.40)`, initial absolute estimation radii `[.4,.25]`, process disturbance radii `[.03,.05]` and per-sensor measurement noise radii `[.10,.12]`. The error recurrence is `e+= (A-LC)e+w-Lv`, and the bound is `E+=|A-LC|E+W+|L|V`.

The implementation returns a componentwise radius at each sampled step. A separate NumPy implementation reproduces the recurrence for hundreds of random systems. Thousands of randomly selected trajectories consistent with the declared box bounds remained within the intervals; those tests support code correctness, not physical hard-bound evidence. For this example, the infinity row-sum of `|A-LC|` is below one, supplying a simple sufficient stationary error envelope.

Adversarial counterexample: a stable rotating error system can fail the **sufficient** absolute-value row-sum criterion. The code must then return no stationary certificate under that test, not claim that the actual plant is unstable. Another negative case uses an inconsistent measured output: the reading may contradict a bound, but sensor fault, model error and timing remain alternative explanations.

**Unmet conditions:** measured sensor noise floors, calibration, transport delays, actuator applied-input alignment, state normalization and unmodeled dynamics. A calculated observer bound is not a physical safety function.


---

# Investigation 47 — Synthetic ARX: one-step accuracy, free-run drift and leakage

A seeded simulation produces a discrete scalar plant `y[k+1]=0.6 y[k]+0.35 PWM[k]+3+w[k]` with random bounded-amplitude commands and additive noise. We feed a synthetic ten-column OpenMCT-style log into the strict parser, then reserve the final 30% of transitions as a chronological validation set. The fitted coefficients agree with the known generating coefficients within the test tolerance. A separate NumPy least-squares oracle reproduces the model coefficients and held-out one-step RMSE; free-run RMSE is measured separately.

Why chronological separation matters: randomly splitting adjacent time samples leaks autocorrelated state information across train and test. An apparent low one-step error can also exploit knowing the preceding *measured* true speed, while a free-run forecast must use its own previous predictions. A correct report retains both metrics and a simple persistence baseline. It must not convert an autoregressive prediction into a causal plant gain when the input is closed-loop correlated with disturbances.

The study is intentionally **not empirical OpenMCT validation**. An actual model comparison awaits authenticated publisher logs and experiments across sample periods, sensor noise conditions, actuator regimes and independent motor runs. The synthetic test does not establish physical uncertainty bounds or plant safety.


---

# Investigation 48 — Repeated digital-meter readings are not replicates

In a constructed ten-column motor log, a multimeter produces one physical current sample for every four control-loop rows. Each of the four GUI records carries the same `DMM_SAMPLE_ID`. A careless analyst computes standard error as though there are four times as many independent current measurements, overstating precision. The correct parser reports 45 distinct DMM readings and 135 repeated IDs across 180 synthetic rows; it does not count all 180 as independent current observations.

The real OpenMCT article describes asynchronous DMM measurements and explicitly provides `DMM_TIME_s`, `DMM_AGE_ms` and `DMM_SAMPLE_ID` to support synchronization. The actual v2 raw data have not been downloaded, so no source-specific repeated-ID count is claimed. A stale DMM sample is not repaired by averaging, and a blank current field is not zero current. The new parser rejects partial meter records and records missing/stale cases.

A rigorous current calibration must reconstruct paired acquisitions from independent multimeter timestamps, account for repeated IDs and age thresholds, track the provisional versus final current calibration, and retain uncertainty at the level of independent DMM readings. The software checks establish only that the parser follows its declared policy on synthetic rows.


---

# Investigation 49 — The observer says “inconsistent”; the engineer must ask why

A two-state observer predicts a sensor value within componentwise intervals based on a declared state estimate and absolute noise bounds. A measured value outside that envelope is **evidence that at least one assumption was violated**. It does not isolate a sensor failure. The actual cause could be an actuator delivering a different input, timing drift, out-of-distribution process disturbance, changed plant dynamics, sensor bias or untrusted telemetry.

Run `two_sensor_consistency` with an expected state `[1,2]`, identity C, error radius `[.1,.1]`, measurement noise radius `[.1,.1]`, and sensor values `[10,2]`. The first channel is incompatible; the second may be compatible. The output sets `root_cause_identified=false`. The interface has no network or device-control side effects.

A proper field investigation would request independent calibrated sensors, actuator feedback, waveform history, network timing, firmware changes, environment and model confidence. It would preserve a contradiction without automatically correcting or overriding a real controller. NIST's final operational-technology guidance explicitly separates performance, reliability, and safety requirements. This Atlas is a research reference; it is neither a safety-rated controller nor a hardware fault classifier.


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


# Source register and open gates
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



## v0.3.0 new bounded source-navigation cards

**FBS-ROBUST:** [Åström and Murray, Feedback Systems wiki](https://fbswiki.org/), author wiki; chapters on stability and robustness, overview only. No book reproduction.

**MIT-LYAP-V03:** [MIT Underactuated Robotics, Lyapunov Analysis](https://underactuated.mit.edu/lyapunov.html), selected online sections on quadratic Lyapunov functions. The example calculations in this Atlas were authored, not copied from source code.

**PY-CT-MARGINS-V03:** [Python Control `margin` documentation](https://python-control.readthedocs.io/en/latest/generated/control.margin.html) and [stability margins](https://python-control.readthedocs.io/en/stable/generated/control.stability_margins.html), public API descriptions of gain/phase/stability margins. These APIs are not executed in the pure-Python runtime.

**MATLAB-RESID-V03:** [MathWorks, What Is Residual Analysis?](https://www.mathworks.com/help/ident/ug/what-is-residual-analysis.html), public R2026b documentation sections on residual whiteness and independence. The Atlas only calculates a descriptive lag-one statistic, not the vendor tests.

**NETWORK-DELAY-2013:** [Qiu et al., Stability and stabilization of networked control systems with random time delays and packet dropouts](https://www.sciencedirect.com/science/article/pii/S0016003213001920), published abstract only. This Atlas does not reproduce its Markov-delay control design or results.

**Publisher-rights boundary:** Source titles/URLs and newly authored, bounded paraphrases only. No restricted textbook, proprietary vendor software, or journal text is mirrored. No independent control engineer review.


## New scoped sources checked for Control 0.4.0

### MIT-LQR-DISCRETE: MIT Underactuated Robotics LQR discrete Riccati and constrained policy

- [Public source](https://underactuated.mit.edu/lqr.html)
- Inspected scope: Discrete-time Riccati and discussion of hard input/state constraints; public HTML, current revision not pinned
- Original bytes: not archived. Independent scientific reviewer: no.
- Content: link and bounded original summary, not redistributed full publisher text.

### MIT-LYAPUNOV-COMMON: MIT Underactuated Robotics Lyapunov with common certificates

- [Public source](https://underactuated.mit.edu/lyapunov.html)
- Inspected scope: Section on common Lyapunov functions for uncertain systems and its sufficiency interpretation; public HTML
- Original bytes: not archived. Independent scientific reviewer: no.
- Content: link and bounded original summary, not redistributed full publisher text.

### STANFORD-EE363: Stanford EE363 linear-system and control lecture archive

- [Public source](https://ee363.stanford.edu/archive/lectures.html)
- Inspected scope: Lecture index identifies LQR, filtering, Lyapunov topics. Only index, not all slide PDFs, inspected
- Original bytes: not archived. Independent scientific reviewer: no.
- Content: link and bounded original summary, not redistributed full publisher text.

### NIST-OT-R3-FINAL: NIST SP 800-82 Rev 3 final OT security guide, September 2023

- [Public source](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
- Inspected scope: Official publication metadata and abstract: performance, reliability, safety and control-system scope. Final document not read in full
- Original bytes: not archived. Independent scientific reviewer: no.
- Content: link and bounded original summary, not redistributed full publisher text.

### NIST-OT-R4-DRAFT: NIST SP 800-82 Rev 4 initial public draft, September 21, 2026

- [Public source](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd)
- Inspected scope: Official *Initial Public Draft* metadata and comments due November 30, 2026; not a final standard
- Original bytes: not archived. Independent scientific reviewer: no.
- Content: link and bounded original summary, not redistributed full publisher text.

### NIST-PHYSICS-MONITOR: NIST survey physics-based attack detection in cyber-physical systems

- [Public source](https://csrc.nist.gov/pubs/journal/2018/07/a-survey-of-physicsbased-attack-detection-in-cps/final)
- Inspected scope: Official abstract on sensor/command anomaly detection and limitations; paper not fully audited
- Original bytes: not archived. Independent scientific reviewer: no.
- Content: link and bounded original summary, not redistributed full publisher text.

### KALMAN-NIS-SECONDARY: NIS educational explanation with chi-square assumption

- [Public source](https://kalman-filter.com/normalized-innovation-squared/)
- Inspected scope: Public educational explanation of nu^T S^-1 nu and Gaussian model assumptions; not a national standard
- Original bytes: not archived. Independent scientific reviewer: no.
- Content: link and bounded original summary, not redistributed full publisher text.



## v0.5 source additions (public scoped portions only)

### MIT-ROBUST-SET — MIT Underactuated Robotics, Robust and Stochastic Control

- [Source](https://underactuated.mit.edu/robust.html)
- Inspected: Common Lyapunov/invariant sets and bounded disturbance/MPC discussion.
- Evidence: bounded public HTML/index only, no complete paper or hardware study; independent engineering review absent.
- Rights: bibliography and original paraphrase only; source bytes not mirrored.

### MIT-FUNNELS — MIT Underactuated Robotics, Feedback Motion Planning

- [Source](https://underactuated.mit.edu/feedback_motion_planning.html)
- Inspected: Parameterized controllers, regions of attraction and robust funnel composition.
- Evidence: bounded public HTML/index only, no complete paper or hardware study; independent engineering review absent.
- Rights: bibliography and original paraphrase only; source bytes not mirrored.

### STANFORD-EE263-STATE — Stanford EE263 archive

- [Source](https://ee263.stanford.edu/archive/)
- Inspected: Course index on observability, estimation, reachability.
- Evidence: bounded public HTML/index only, no complete paper or hardware study; independent engineering review absent.
- Rights: bibliography and original paraphrase only; source bytes not mirrored.



## Edition 0.6.0 — additional bounded publisher records

### source:MAYNE-OF-MPC-2006 — Robust output feedback model predictive control of constrained linear systems

[Publisher reference](https://www.sciencedirect.com/science/article/pii/S0005109806001221)  
Inspected: Publisher abstract and introduction: bounded state/output disturbances, observer error and robust invariant tube; the full method and proofs not reviewed.  
Only the published abstract/identified scope was checked. No full-text, source-code, hardware or independent scientific review was claimed.

### source:SIEBER-TUBE-2022 — System level disturbance reachable sets and their application to tube-based MPC

[Publisher reference](https://www.sciencedirect.com/science/article/pii/S0947358022000723)  
Inspected: Publisher abstract: finite impulse response disturbance reachable sets and nominal tube formulation; source paper details not reproduced.  
Only the published abstract/identified scope was checked. No full-text, source-code, hardware or independent scientific review was claimed.

### source:AIAA-RATE-2023 — Model Reference Control for Reducing Pilot-Induced Oscillation Tendencies Due to Actuator Rate Limits

[Publisher reference](https://doi.org/10.2514/6.2023-2512)  
Inspected: Publisher abstract only: actuator rate limits, induced phase lag and pilot-induced oscillation tendencies; aerospace case is not data about an industrial valve.  
Only the published abstract/identified scope was checked. No full-text, source-code, hardware or independent scientific review was claimed.


## Scoped Control v1.0 — externally inspected data sources

### source:OPENMCT-MENDELEY-V2 — OpenMCT DC-motor experimental control dataset, Mendeley Data version 2

[Published record](https://data.mendeley.com/datasets/5xvg43r9r8/2). Inspected scope: Dataset landing HTML; CC BY 4.0, 14 acquisition logs, >60,000 samples, 10-column apparatus and processing file inventory; raw file API inaccessible, no raw bytes downloaded. No independent engineering review, no actual raw dataset archived, and no third-party raw file redistribution claimed.

### source:OPENMCT-DIB-2026 — Experimental data from an open-source DC motor control educational kit

[Published record](https://doi.org/10.1016/j.dib.2026.113274). Inspected scope: Open-access abstract/accessible article excerpt listing hardware, 10 log columns, exact field meanings, asynchronous DMM readings, APRBS sampling conditions and interpretation limits. No independent engineering review, no actual raw dataset archived, and no third-party raw file redistribution claimed.

### source:GITHUB-MOTOR-EDU-2026 — Educational PID Motor Controlled project, repository-level provenance

[Published record](https://github.com/dilusha-c/PID_Motor_Controlled). Inspected scope: Public README: 12V brushed DC motor, encoder, Raspberry Pi, cited CSV step logs and ownership statement; permissive redistribution of raw CSV not established. No independent engineering review, no actual raw dataset archived, and no third-party raw file redistribution claimed.

### source:GITHUB-MOTOR-PWM30 — Public educational motor RPM CSV, nominal file label PWM 30

[Published record](https://github.com/dilusha-c/PID_Motor_Controlled/blob/main/Mode/mode1/data_pwm_30.csv). Inspected scope: Public raw text read through GitHub interface, 49 (time,rpm) observations and source Git blob; only derived descriptive metrics retained, original raw not bundled. No independent engineering review, no actual raw dataset archived, and no third-party raw file redistribution claimed.

### source:GITHUB-MOTOR-PWM50 — Public educational motor RPM CSV, nominal file label PWM 50

[Published record](https://github.com/dilusha-c/PID_Motor_Controlled/blob/main/Mode/mode1/data_pwm_50.csv). Inspected scope: Public raw text read through GitHub interface, 49 (time,rpm) observations and source Git blob; only derived descriptive metrics retained, original raw not bundled. No independent engineering review, no actual raw dataset archived, and no third-party raw file redistribution claimed.

### source:GITHUB-MOTOR-PWM70 — Public educational motor RPM CSV, nominal file label PWM 70

[Published record](https://github.com/dilusha-c/PID_Motor_Controlled/blob/main/Mode/mode1/data_pwm_70.csv). Inspected scope: Public raw text read through GitHub interface, 49 (time,rpm) observations and source Git blob; only derived descriptive metrics retained, original raw not bundled. No independent engineering review, no actual raw dataset archived, and no third-party raw file redistribution claimed.

