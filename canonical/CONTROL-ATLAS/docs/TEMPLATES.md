# Control Atlas experiment templates

## Plant and safety record
- Physical system, exact model, units and state limits:
- Operating point, expected disturbances and validated domain:
- Sensor/actuator identity, calibration, delay, rate/saturation, safety interlocks:
- Data-acquisition clock and control computation jitter:
- Operator approval, test plan, rollback, monitoring and stop conditions:

## Control algorithm record
- Design objective, target, performance metric, state-space/transfer model:
- Parameters and identification/uncertainty provenance:
- Continuous/discrete hold convention, sample time, gain limits:
- Test cases for disturbances, reference changes, noise, saturation and failures:
- Formal sufficient conditions versus observed traces; unexplored failure modes:
- Independent reviewer, source revisions and bounded decision:

## State estimation record
- Sensor model, bias, noise covariance, process noise and origin:
- Filter structure and measurement ordering:
- Residual/innovation statistics, missing values, outlier policy:
- Estimation uncertainty model versus actual calibration evidence:
- Response to sensor failure, fallback mode, and operator review:

## Evidence/revision ledger
- Record ID and revision, source URL and inspected scope, model/software release:
- Inputs and state conditions, physical units, certified versus synthetic origin:
- Alternate explanation, source contradiction, missing evidence:
- Updated corpus dependencies and context invalidation:


## v0.2 extension material

# Control Atlas blank study templates

## Plant and model specification

- Physical plant and operating context:
- States and measurement channels, units and calibration:
- Actuators and limits (range, rate, delay):
- Baseline time and sample clock:
- Disturbances, hazards, safety interlocks and protected fallback:
- Model class, fit algorithm, parameters and covariance:
- Validity conditions, source and exact revision:
- Independent test data and unresolved model gaps:

## Controller evidence ledger

- Setpoint and tracking objective:
- Control law, convention and time discretization:
- Gain/weight values and their provenance:
- Actuator limits and saturation/antiwindup implementation:
- Measurement noise and derivative filtering:
- Open- and closed-loop tests, disturbances and safe fallback:
- Robustness uncertainty family and worst cases:
- Correctness, performance, and excluded claims:

## System ID validation report

- Input excitation and consent to experiment:
- Sample times, missing/jitter traces:
- Training/validation splits and exclusion policy:
- Competing model structures and residual diagnostics:
- Nuisance disturbances, closed-loop feedback bias:
- Source raw data, license and provenance:
- Uncertainty and reproducible comparison:
- Failed hypotheses and alternative explanations:


## v0.3.0 robustness/monitoring assessment record

- Plant, sampling, state and actuator definitions and model revision:
- Source of parameter bounds and guaranteed versus statistical meaning:
- Nominal and uncertain poles with valid domain and excluded dynamics:
- Sensor, command, receipt and actual actuator timestamps and jitter:
- Actuator saturation, hysteresis, delay and communication faults:
- Candidate Lyapunov function, numerical margin and model assumptions:
- Residual validation dataset and autocorrelation/cross-correlation protocol:
- Actual safe state, interlocks and independent hazard-review requirements:
- Source IDs, checked sections, rights, reviewers and remaining gaps:
- Explicit result category: conditional calculation / field evidence / not established:


## v0.4 model assurance packet

- System name, operating envelope, state/input/output units and sample interval:
- Full or reduced plant representation, physical parameter interval sources and correlation assumptions:
- Input/actuator bounds, state constraints, transport/processing delays, fallback and safe-state authority:
- Candidate P, numerical eigenvalue margins, matrix box and uncertainty kind:
- LQR/MPC objective with Q,R,Qf and terminal set; grid or continuous solver nature:
- Numerical algorithm result versus physical observations, independence and reviewer:
- Source and code revision IDs, static model and uncertainty domains:
- Conclusions explicitly unsupported (safety approval, commissioning, transfer or component replacement):

## v0.4 sensor and fault evidence packet

- Sensor type, primary calibration, units, uncertainty covariance, timestamp integrity and dropout behavior:
- Observer/model identification source, fault hypotheses, innovation definition and acceptable thresholds:
- Measurements that discriminate state deviations from sensor biases, including independent data source:
- NIS assumptions and false-alert policy, detector validation vs physical interlocks:
- Training/test dataset boundaries, excitation and process regime, error metric and uncertainty:
- Human operational approval and incident response route; no automatic actuation from knowledge retrieval:


## v0.5 invariant-box evidence ledger

- Physical plant identity, units, operating regime and model source:
- State vector, observation model, sensor latency, calibration and error bounds:
- A/B interval model: data, parameter correlations, confidence and revision:
- Feedback K, controller implementation, sample clock, computation deadline:
- Disturbance set, evidence basis, rare events, excluded modes:
- State-safe region and its relation to actual hazard analysis:
- Actuator amplitude, rate constraints, saturation and interface behavior:
- Mathematical certificate status and numerical tolerance:
- Alternative Lyapunov/invariant set candidates if current box fails:
- Site hazard approval and independently tested safety system:
- Final evidence verdict: model-only / experimentally supported / not established:


## v0.6 output-feedback evidence packet

- Physical plant identity and operating conditions; source for a,b and model version:
- Units and exact sample time; known, *applied* input u[k] and timestamp alignment:
- Sensor y[k] location, calibration, update order, quantization, bound V evidence:
- Estimated initial state h[0], error set E0 and validation against independent measurement:
- Process disturbance envelope W; measured range, exclusions, nonstationarity:
- Actuator amplitude U, slew D, lag alpha; supporting real step tests and model mismatch:
- Feedback K, observer L, saturation/antiwindup logic, controlled/deployed code revision:
- Finite-horizon tube, sampled-state constraints, intersample risks and contingency design:
- Failure-mode alternatives if an observation is inconsistent with bounds; no automatic blame:
- Human engineering and OT safety review, rollback/interlock/authorization status:
- Explicit `unknown`, `modeled`, `numerically_checked`, `experimentally_validated` evidence labels:


## v1 real-control-source ingestion ledger

- Dataset owner, DOI/repo, licence and exact version/commit:
- Verified original file SHA-256 or Git blob ID (source byte authenticity category distinct):
- Experimental apparatus, motor/controller, sensor and firmware versions:
- Acquisition conditions, control mode, requested command vs applied PWM:
- Raw field names, units and measured sample-period/clock alignment:
- DMM repeated IDs, age distribution and independent reading count:
- Training and held-out time ranges, excitation/rank diagnostics and exclusion reasons:
- One-step/free-run/persistence RMSE and separate prediction uncertainty:
- Model's intended physical interpretation, source of disturbance bounds and unverified assumptions:
- Source rights and exclusion of unlicensed raw files:
- Independent replication/cross-run and qualified engineering review:
- Final status: descriptive / numerically reproduced / physically validated / refused:

## v1 2×2 observer hard-bound audit

- Defined state vector, output sensors, sample period, physical units:
- A,C,L (and plant B/u applied input) basis, identification and precision:
- Verified or merely stipulated hard bounds W,V,E0 (sigma alone is insufficient):
- Condition checked: finite tube, simple row-sum sufficient stationary envelope, or alternate certificate:
- Sensor and actuator timestamps, lag and bias restrictions:
- Explicit non-conclusions: no independent fault cause, actuator feasibility or safety guarantee:
