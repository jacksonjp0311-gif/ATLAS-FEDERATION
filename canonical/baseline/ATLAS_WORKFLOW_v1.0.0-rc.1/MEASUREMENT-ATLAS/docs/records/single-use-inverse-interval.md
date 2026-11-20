# Inverse calibration can invert prediction bounds

**ID:** `single-use-inverse-interval` · **Origin:** `source_reported` · Assistant source-portion check, not independent review.

A single-use load interval is obtained by solving the upper and lower response prediction equations for load. The example response is hypothetical, not an additional observed row.

## Equation

```text
y_new = fhat(x) ± t_(1-alpha/2,n-p) s_prediction(x)
```

## Assumptions

- Independent normally distributed errors with constant variance; applicability is supplied by the caller, not inferred from a passing calculation.
- The admissible calibration branch is identified.

## Limitations

- A point estimate and symmetric derivative shortcut are not automatically the same inverse confidence set.

## Evidence

[Load-cell inverse calibration example](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd61a.htm) · §4.6.1.10 +/- What? and the two endpoint equations. Inspected 12 November 2026. Original paraphrase or declared local derivation.
