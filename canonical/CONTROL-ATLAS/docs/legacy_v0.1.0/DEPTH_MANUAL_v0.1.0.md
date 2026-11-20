# CONTROL ATLAS — Scientific Reference Manual v0.1.0

**Original source-linked synthesis, not independent review or machinery testing.**

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
