# Control Atlas v0.1 — scope and missing evidence

**Status:** domain reference foundation, not Control v1 content readiness or physical controller certification.

| Content | Source-linked explanation | Executable support | Still missing |
|---|---|---|---|
| Plant and experiment scope | Plant/actuator/sensor/objective and uncertainty | First-order exact step | Real identified process data and credible operating region |
| Sampled plants | ZOH assumptions, sample timing | Exact first-order hold coefficients | Delay, jitter, multi-state ZOH, discretization uncertainty |
| Stability | Scalar continuous/discrete limitations, nonlinear caveat | Scalar pole test | Full Nyquist/root-locus/Lyapunov numerical certification |
| Reachability & observation | General controllability/observability overview | Restricted 2x2 determinants | Numerically robust arbitrary-dimension rank/Gramian with real sensors |
| PI/PID | Integral action and saturation | Discretized PI clamping/none on synthetic plant | Derivative filtering, tuning, constraints, delay/industrial safety |
| Identification | Excitation, holdout, source conditions | No fitting by design | Actual time-series data, uncertainty and validation |
| Estimation | Scalar Kalman model, covariance limits | Scalar Joseph filter | Multi-state, bias estimation, correlations, real instruments |
| Optimal control | Finite LQR, constraints warning | Scalar finite-horizon Riccati | MPC feasibility, physical constraints, robust uncertainty |
| Robustness | Small gain sufficient bound | Product of supplied norms | H-infinity, quantified uncertainty models and physical robustness tests |
| Agent/Bitwork interoperability | Common Atlas records, evidence closure | Read-only standard contract | Actual live routing and independent held-out evaluation deferred until all 30 domain libraries |

**Use of this reference does not authorize control of hardware.** Evidence and real-world safety approvals remain separate from math test suites. Earlier five nodes and common routing code are frozen.
