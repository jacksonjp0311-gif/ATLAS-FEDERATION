# ATLAS FORGE — Scoped v1 release candidate investigations

This casebook is executable with standard-library Python 3.10+ through `python -m math_physics_atlas` and `math_physics_atlas.v1_cases.casebook_v1`. The eleven new investigations are **constructed verification fixtures**, not physical experiments.

1. Five exact discrete equilibria on 4/8/16/32/64 interior cells with positive exponential electron/hole ratios and synthetic neutrality-enforcing doping.
2. Three biased two-carrier Poisson/continuity cases on 4/12/32 interior cells with independently inspectable Poisson, particle-continuity and Gauss errors.
3. Two thermal-voltage and Debye-scaling unit examples at different geometry lengths; verify one-over-length-squared dependence.
4. One deliberate under-iteration that must return a typed nonconvergence error.

**Separate software oracle:** SciPy's dense multivariate nonlinear root algorithm independently assembles the full 3m equation residual on 60 deterministic small synthetic systems. It compares all potential/electron/hole components. See `tools/independent_oracle_v1.py` and `evidence/independent_oracle_v1.json` for the result. An exact solution to the finite discrete equations is not a proof that a semiconductor device obeys the modeling assumptions.

**Limits:** No generation, recombination, traps, contact-state models, crystallographic defects, mobility characterization, real current-voltage data, or independent expert review.
