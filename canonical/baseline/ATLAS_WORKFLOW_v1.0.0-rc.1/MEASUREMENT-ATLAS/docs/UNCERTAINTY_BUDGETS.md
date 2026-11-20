# Uncertainty budgets (v0.3)

A budget is a set of named contributions with standard uncertainties, sensitivity coefficients, correlations, and an explicit common output unit. `uncertainty_budget` returns `u_c=sqrt(J C J^T)` and signed contributions to variance. Signed contributions may be negative with correlated inputs; they are **not** percentage shares of an always-positive pie. Input uncertainty and output units must already be compatible; this module rejects mismatches rather than converting silently.

Type B half-width conversions assume *specified* symmetric distributions: uniform `a/sqrt(3)` and triangular `a/sqrt(6)`; neither distribution can be inferred from a manufacturer spec without interpretation. Coverage factor and statistical coverage probability are not interchangeable.

The code computes first-order linearized uncertainty. Large nonlinearities, asymmetries, non-Gaussian tails, drift, and calibration validity require domain-appropriate treatment beyond this model. Numerical checks do not make a real physical measurement independently validated.
