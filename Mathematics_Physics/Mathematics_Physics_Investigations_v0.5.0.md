# Mathematics & Physics v0.5.0 — investigation catalog

**44 original finite constructed investigations across five editions; no laboratory measurements.**

- v0.1.0: 22 cases in prior `CASEBOOK.md`, unchanged and retained in the standalone archive.
- v0.2.0: 6 cases in prior `V02_CASEBOOK.md`, retained.
- v0.3.0: 4 cases in prior `V03_CASEBOOK.md`, retained.
- v0.4.0: 6 cases in prior `V04_CASEBOOK.md`, retained.
- v0.5.0: 6 additional cases, detailed below.

# ATLAS FORGE — v0.5.0 finite constructed investigations

**All six cases are authored arithmetic fixtures; none are laboratory measurements.**

| Case | Passed | Metric | Qualification |
|---|:---:|---:|---|
| zero_boundary_equilibrium | Yes | 0 | A manufactured zero state only |
| constant_equilibrium | Yes | 0 | Requires matching source and boundary |
| nonlinear_manufactured_second_order | Yes | 4.00505768451 | Analytic continuous function, not experimental dielectric data |
| exponential_equilibrium_edge_flux | Yes | 0 | Constant field, Boltzmann ratio; no contacts or recombination |
| zero_field_Fick | Yes | 0.8 | A single edge Fick law is not a full transient transport model |
| Bernoulli_extreme_reciprocity | Yes | 120 | Stable mathematical identity |

Run `python -m math_physics_atlas` and `python tools/independent_oracle_v05.py` (optional NumPy and SciPy).
