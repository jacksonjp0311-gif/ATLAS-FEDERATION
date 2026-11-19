# Control Atlas v1.0.0-rc.1 scope and evidence gates

**Status:** substantive candidate for a scoped v1 scientific reference; content acceptance remains incomplete until the authentic OpenMCT experimental analysis can be run and reviewed. External scientific, physical and host acceptance is NOT claimed. The previous 214 records and 124 relations remain unchanged.

| Scientific domain | Reference and executable coverage | What remains open |
|---|---|---|
| Classical feedback and sampled systems | First-order, PI/PID, antiwindup, sampling, poles, controllability, observability | Real system commissioning and hardware validation |
| Robust control / uncertainty | Interval stability, common Lyapunov, finite robust invariant boxes, scalar output-feedback tubes | Physical hard-bound measurements, nonlinear/inter-sample and broad multivariable certification |
| Two-state/two-sensor output feedback | 2×2 observer error radius and consistency check, sufficient row-sum envelope | Applied-input and timestamp validation, actual 2×2 plant, correlated uncertainty and closed-loop physical test |
| Constrained control | Finite-horizon LQR and bounded grid examples, commanded vs applied actuator | General real-time MPC, verified state constraints, safety interlocks |
| System identification | Strict ten-field OpenMCT parser and chronological descriptive ARX fit/one-step/free-run metrics | Publisher v2 raw logs inaccessible here; no actual OpenMCT fit, motor parameter confidence or independent cross-run transfer |
| Actual external motor observations | Source-attributed small descriptive statistics from 3×49 public time/RPM CSVs, with source Git blobs | No observed rowwise PWM, no plant gain identification, no source rights to mirror raw data, no independent peer review |
| Data quality and measurement integrity | Sample-time reconstruction, asynchronous DMM unique reading count, missing/stale IDs and refusals | Physical clock sync, calibrations, original bytes, quantization/noise covariance and error bars |
| Safety and operational context | NIST SP 800-82r3 final vs r4 initial draft, hardware-action refusal | Hazard analysis, certified interlocks, physical failure investigation, operational release |
| AI integration and routing | Evidence-preserving shared Forge context tested | All 30 domain libraries before router; no Bitwork, held-out AI model, real Windows host, desktop transfer |

**Content v1 gate:** source-raw experimental replay and scientific review remain outstanding. This release is `v1.0.0-rc.1` to make that distinction visible. Control remains active, Agent Atlas queued.
