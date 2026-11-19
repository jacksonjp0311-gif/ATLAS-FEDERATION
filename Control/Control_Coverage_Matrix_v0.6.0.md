# Control Atlas v0.5.0 — scientific content coverage and open gates

**Scientific status:** substantive bounded reference development, **not** full content v1, field validation, control-system commissioning, or product certification. Old source and model records are preserved.

| Question family | What v0.4 adds | What remains unverified / unimplemented |
|---|---|---|
| Multivariable frequency sensitivity | 2x2 real static return difference, singular values and S,T matrix identity | Complex full-frequency MIMO dynamics, robust margin computation, nonminimum-phase and hidden internal modes |
| Robust interval stability | Common P at all 16 corners of independent-entry A box, sufficient conditional convexity explanation | Physical parameter identification, numerical interval proof, nonlinear region of attraction, correlated uncertainties and actuator limits |
| Finite-horizon optimal control | Two-state one-input time-varying unconstrained LQR with Q,Qf PSD and R>0 | General MIMO/multivariable QP, hard state/input limits in LQR, nonlinear and disturbed plants |
| Constraints and feasibility | Bounded scalar finite-input-grid offline exhaustive planning, distinguish no-grid-candidate | Continuous MPC solver, recursive feasibility, terminal controller/invariant sets, real-time deadlines and fallback authority |
| Sensor model residuals | Two-sensor covariance-aware NIS; identical state+bias measurement counterexample | Real sensor covariance, clock and calibration, statistical significance, independent isolation of cause |
| System identification validity | Chronological train and later one-step ARX error, excitation guard | Multi-step and closed-loop bias correction, measured plant data, independent realistic changes and sensor fault isolation |
| OT integrity / safe operations | Separate final NIST SP800-82r3 from 2026 Rev4 initial public draft; monitor versus interlock distinction | Actual hazard analysis, approved safety PLC, human operations, field acceptance, secure system commissioning |
| Mathematical methods / provenance | Original code/tests, bounded source locator and immutable shared Atlas records | Expert source review, authentic system experiments, domain-general formal verification and practical control performance |
| Routing / final deployment | Frozen shared retrieval kernel reused | **User-mandated last stage:** build all 30 domain libraries first, then Bitwork routing, then integrated acceptance and desktop transfer |

**Release decision:** Control v0.4 is an engineering-evidence checkpoint. No content-v1 or scientific acceptance flags set true. Agent Atlas stays queued.


## v0.5 model-and-evidence increment

| Family | New scoped reference and executable method | Open physical/scientific scope |
|---|---|---|
| Bounded robust invariance | Independent-entry 2×2 A/B interval box, exact vertex computation (64 corners), conservative axis-aligned state-box and actuator inequality | Independent model bounds/parameter correlation, actual state measurement, nonlinearities, slew rates, delays, physical safety testing |
| Scalar robust interval | One-step invariant interval for exact scalar linear feedback with bounded disturbance and input | Sampled-plant identification, physical units and operational limits |
| Measurement ambiguity | Offline 2×2 true-state/bias trajectory comparison, no hardware connections | Sensor error bounds, observers with reliable time stamps, actual fault discrimination |
| Mathematical confidence | Separate brute corner/state-sign NumPy oracle; positive/saturation/refusal cases | Formal roundoff proof, independent scientific audit and physical commissioning |
| Full robust control | Source-linked guidance only | Nonlinear, constrained stochastic systems, MIMO frequency robust stability, real hardware and independent datasets |

**Status:** v0.5 scientific reference checkpoint; not scoped v1 content or qualified control. Build all 30 domain contents before routing and only transfer after integration/testing.


## v0.6 output-feedback and actuator-model increment

| Area | Implemented and explained | Outstanding evidence and scope |
|---|---|---|
| Scalar bounded observer | Finite error-radius recurrence and conditional limiting radius when |a-L|<1 | Actual sensor hard noise/bias bounds, time synchronization and calibrated plant input |
| Actuator dynamics | Scalar magnitude clamp, slew target and first-order lag with discrete timing | Real actuator position/time-response characterization, nonlinear faults, deadband and interlocks |
| Finite output-feedback reachable tube | Conservative scalar plant/observer/actuator interval propagation for up to 100 sampled steps | MIMO output feedback, joint uncertainty/correlation tightening, intersample and infinite-horizon safety |
| Model–measurement contradiction | Deterministic bound consistency interval with explicit no-root-cause status | Independent calibrated sensor redundancy, actual field faults, causality of discrepancies |
| Numerical verification | Separate NumPy/SciPy recurrence, LP corner and 57,600 sampled-state/estimate/action containments | Physically calibrated uncertainty, hardware-in-the-loop, nonlinear model and independent expert acceptance |

**Content status:** Control v0.6.0 development milestone, not scoped v1. Agent Atlas stays queued. All 30 domain content libraries precede routing and desktop transfer.
