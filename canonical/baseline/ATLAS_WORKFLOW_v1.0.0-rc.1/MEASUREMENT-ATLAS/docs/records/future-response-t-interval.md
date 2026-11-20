# A future response includes residual variation

**ID:** `future-response-t-interval` · **Origin:** `source_reported` · Assistant source-portion check, not independent review.

A prediction interval for one independent future response adds residual variance to fitted-mean variance before applying the t factor.

## Equation

```text
fhat(x) ± t_(1-alpha/2,n-p) sqrt(s_residual^2 + h^T Cov(beta) h)
```

## Assumptions

- Independent normally distributed errors with constant variance; applicability is supplied by the caller, not inferred from a passing calculation.
- The future response follows the same variance model as the calibration.

## Limitations

- No multiple-use coverage guarantee or complete metrological uncertainty budget is implied.

## Evidence

[Mean response and single-response prediction uncertainty](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd512.htm) · §4.5.1.2 Coverage Factor and Prediction Interval Formula. Inspected 12 November 2026. Original paraphrase or declared local derivation.
