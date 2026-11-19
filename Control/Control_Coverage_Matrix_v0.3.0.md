# Control Atlas 0.2 — unified evidence and coverage matrix

The work has a **bounded, source-linked technical foundation**, not content v1 or scientific/hardware acceptance. The existing 0.1 release, its 60 record revisions, 36 relationships and methods remain immutable in this 0.2 release; 57 complementary records and 28 relationships are integrated with provenance and two collision-safe source IDs.

| Domain family | Models and documents present | Outstanding validity |
|---|---|---|
| Continuous and sampled dynamics | Continuous first-order step, exact ZOH, state rollout, aliasing | Real plant identification, delays, nonlinearities, disturbances and measured uncertainty |
| Stability and control | Discrete scalar pole tests, two-state eigenvalues, conditional small-gain sufficiency | Robust MIMO stability, saturation, uncertainty sets and plant validation |
| State-space | Two-state controllability and observability with scale guards | Higher-dimensional numerically robust ranks, real sensor/actuator data |
| PI/PID | Simulated PI loop and conditional antiwindup; separate PID actuator traces | Derivative noise filtering, actuator dynamics, industrial tuning/safety checks |
| System identification | Scalar ARX supplied input-output linear fit | Model structure selection, closed-loop biases, noise models, validation splits |
| Optimal control | Finite and infinite-horizon scalar LQR; limitations | Constraints, nonlinear plants, general Riccati/MPC and robust tuning |
| State estimation | Kalman scalar one-step and sequential observation updates | Wrong noise covariance, bias drift, multi-sensor and real calibration |
| Verification | Source closure, rejected inputs, synthetic counterexamples | Independent engineering peer review, licensed standards, hardware HIL/field tests |
| Atlas routing | Existing common-node retrieval unchanged | Bitwork, live AI model, held-out query accuracy, energy/cost measurements |

**Scope v0.2:** two complementary 0.1 research branches merged as one versioned scientific-reference node. Source cards and citations require original-provider verification for any real engineering use. No active hardware or network control, field-proven stability, safety or certification.


## v0.3.0 expanded scope and remaining scientific gates

| Family | Verified content and bounded calculation | Unmet empirical or generality requirements |
|---|---|---|
| Scalar robust pole | Four corners of independent a,b parameter rectangle; strict | Real parameter-range validation, correlated uncertainty, hidden dynamics |
| Sampled measurement delay | Exact one-sample characteristic quadratic; nominal vs delayed counterexample | Variable latency, network dropouts, hybrid systems and full stability analysis |
| Lyapunov candidate | Supplied positive-definite P and nominal strict 2x2 Q; failed candidate is not proof of instability | Certificate search, numerical interval proof, nonlinear/uncertain region of attraction |
| Frequency-domain S and T | First-order proportional loop pointwise complex identity | Full margins, delay, high-order plant, noise spectra, robust performance |
| Identification diagnostics | Residual mean, RMS and lag-one statistic; no statistical test | Independent experiments, whiteness significance, closed-loop bias and model validation |
| Sensor watchdog policy | Offline stale/invalid/innovation refusal trace | Physical interlocks, hazard assessment, independent safe state and actual timing |

**Status:** Control v0.3.0 substantive reference checkpoint, NOT Control scientific/content v1. Agent remains queued. No control hardware or tool router was operated. All thirty content libraries precede routing and desktop transfer.
