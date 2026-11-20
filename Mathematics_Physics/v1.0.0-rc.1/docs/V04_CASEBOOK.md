# v0.4 six constructed numerical investigations

These authored experiments probe finite computational behavior; none is a laboratory measurement or peer review.

| Investigation | Status | Metric | Scope |
|---|---|---:|---|
| manufactured_sine_O_h2 | PASS | 4.0057913 | Constructed exact sine solution; tests a truncation-order prediction, not field data |
| affine_boundary_laplace | PASS | 4.823375e-11 | Homogeneous charge with linear Dirichlet boundary; constant dielectric |
| piecewise_linear_dielectric_gauss | PASS | -1.7376071e-21 | Discontinuous linear dielectric and prescribed boundary; no calibrated interface model |
| signed_volume_charge_flux | PASS | -6.2172489e-15 | Discrete Gauss law for signed authored charges, 2D per unit depth |
| bounded_nonconvergence_refusal | PASS | 102.93181 | Underiterated solve is not represented as a converged physical prediction |
| SPD_symmetry_energy | PASS | 1.1368684e-13 | Algebraic symmetry and positivity on one finite Dirichlet grid |

Reproduce with `python -m math_physics_atlas` or `from math_physics_atlas.v04_cases import casebook_v04`. Inspect `v04_models.py` for solver stopping criteria and input contracts.
