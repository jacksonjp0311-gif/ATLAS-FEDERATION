# Pointwise uncertainty in the fitted regression mean

**ID:** `regression-pointwise-mean-ci` · **Origin:** `formal_derivation` · Assistant source-portion check, not independent review.

A fitted mean interval uses coefficient covariance at the stated predictor, with the residual degrees of freedom. It is pointwise, not a simultaneous band.

## Equation

```text
fhat(x) ± t_(1-alpha/2,n-p) sqrt(h(x)^T Cov(beta) h(x))
```

## Assumptions

- Independent normally distributed errors with constant variance; applicability is supplied by the caller, not inferred from a passing calculation.
- Predictors are treated as exact; the declared regression form is adequate.

## Limitations

- Model error, uncertain reference inputs and drift need additional treatment.

## Evidence

[Confidence interval for a fitted mean response](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd511.htm) · §4.5.1.1 confidence interval construction; local polynomial-vector notation. Inspected 12 November 2026. Original paraphrase or declared local derivation.
