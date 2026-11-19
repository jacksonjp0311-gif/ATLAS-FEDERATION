# Control Atlas v0.4.0 — scientific content coverage and open gates

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
