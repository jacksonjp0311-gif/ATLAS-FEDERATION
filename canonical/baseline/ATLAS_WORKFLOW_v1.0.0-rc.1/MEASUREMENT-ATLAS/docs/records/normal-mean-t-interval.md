# A normal-sample mean uses estimated standard error and n minus one degrees of freedom

**ID:** `normal-mean-t-interval` · **Origin:** `source_reported` · Assistant source-portion check, not independent review.

For independent normal readings, a mean interval uses sample standard deviation divided by the square root of sample size and a Student t factor.

## Equation

```text
mean ± t_(1-alpha/2,n-1) s/sqrt(n)
```

## Assumptions

- Independent normally distributed errors with constant variance; applicability is supplied by the caller, not inferred from a passing calculation.

## Limitations

- Shared offsets and unknown biases are not supplied by the within-sample standard error.

## Evidence

[Confidence limits for a mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) · §1.3.5.2 Definition: Confidence Interval. Inspected 12 November 2026. Original paraphrase or declared local derivation.
