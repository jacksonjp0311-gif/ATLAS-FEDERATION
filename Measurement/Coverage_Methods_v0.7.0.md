# Conditional uncertainty intervals

**Measurement Atlas 0.7.0 · 12 November 2026**

This supplement turns the previously documented coverage assumptions into separately invoked, testable calculations. It does not determine that a real instrument satisfies those assumptions. The scientific reference remains the primary product; search never executes a calculator.

## Choose the object before the multiplier

A mean interval estimates a fixed average. A future-response prediction interval also includes variation of a new reading. Both differ from a complete uncertainty budget and from a product-conformity decision. [NIST mean response](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd511.htm) and [single response](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd512.htm) identify this distinction.

The `coverage_factor(p, df)` function returns the equal-tail Student t factor for central probability p. Infinite df explicitly selects the normal limit. Finite support is 1–10000 df and 0.5–0.9999 central probability; outside values are refused. These are implementation limits, not limits of the mathematical distribution. [NIST t distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3664.htm).

## Independent-component budgets

The implemented Welch–Satterthwaite approximation uses contributions c_i u_i in a common output unit:

```text
u_c^2 = sum((c_i u_i)^2)
nu_eff = u_c^4 / sum((c_i u_i)^4 / nu_i)
```

Callers must declare independence. General correlated budgets are refused by this calculation; the older covariance-propagation tool remains available for variance calculation, not automatic df inference. Component df and infinite-df choices are explicit. NIST describes this as a conventional approximation with conditions, not a rigorous universal coverage guarantee. [TN 1297 Appendix B, B.1–B.3](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-b-coverage-factors).

For the original synthetic example, u_A=0.02 mm with 9 df and u_B=0.01 mm with explicitly justified infinite df give u_c=sqrt(0.0005) mm and nu_eff=14.0625. The t factor is then selected numerically. This assumes the output distribution supports that approximation; merely obtaining the number does not establish the model.

## Numerical method

For positive t, integrating the t density by the substitution x=nu/(nu+t^2) gives the survival function 0.5 I_x(nu/2,1/2). The code uses the regularized incomplete beta definition, symmetry and continued fraction, then brackets the inverse by bisection. These are original implementation steps from the public formulas, not a learned model. [NIST DLMF 8.17](https://dlmf.nist.gov/8.17).

Convergence, input limits and representability are checked. The runtime uses only Python's standard library. Optional developer comparisons use SciPy and NumPy, report their actual installed versions, and do not become runtime dependencies.

## Bounded inverse-calibration interval

The new `inverse_prediction_interval` inverts the two future-response bands. It does not replace them with a symmetric derivative approximation. In the normalized predictor z, write h=(1,z,z²) and q(z)=sqrt(s²+hᵀCh), where C is coefficient covariance and s² is residual variance. For positive semidefinite C, Cauchy–Schwarz implies:

```text
|q'(z)| = |h'(z)^T C h(z)| / q(z) <= sqrt(h'(z)^T C h'(z)).
```

For degree at most two, the squared bound is convex in z, so its maximum on a compact interval occurs at an endpoint. If f' has constant sign and min|f'| > k max sqrt(h'ᵀCh'), both bands are strictly monotone. This is our sufficient condition for unambiguous bisection. A small numerical margin is required. Failure means this limited solver refuses; it is not proof that a general confidence set is impossible.

This derivation is part of the local implementation and has not been independently peer reviewed. Its premise and inequality are covered by authored analytical/edge-case tests and a separate numerical comparison, not by physical measurements.

The default rejects endpoints outside the measured predictor range. Explicit clipping returns `range_limited_confidence_set`, labels the clipped endpoints, and never claims a full interval outside calibration support.

## Interpretation and reporting

All regression intervals require the explicit model label `iid_normal_equal_variance_exact_predictors`. This records caller intent; it does not run a normality or independence test. Shared errors, drift, model misspecification and uncertain reference inputs may need additional terms. A frequentist interval's level describes repeated use of the procedure, not a posterior probability for one realized interval. [NIST confidence limits](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm).

The coverage simulation is entirely synthetic. It is not a real calibration, an independent held-out trial, or a scientific admission receipt. Its intentionally omitted shared offset demonstrates a failure mode rather than a method to use on real measurements.

## Reproduce

```sh
python tools/coverage_casebook.py
python -m measurement_atlas inverse-interval
python tools/coverage_oracle.py       # optional NumPy + SciPy
python tools/coverage_simulation.py   # optional NumPy
```

See [inverse replay](INVERSE_INTERVAL_REPLAY.md), [coverage experiment](COVERAGE_SIMULATION.md) and [review checklist](INDEPENDENT_REVIEW_CHECKLIST.md).
