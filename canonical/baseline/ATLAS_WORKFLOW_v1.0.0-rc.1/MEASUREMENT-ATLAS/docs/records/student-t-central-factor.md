# A two-sided coverage level needs a central t quantile

**ID:** `student-t-central-factor` · **Origin:** `formal_derivation` · Assistant source-portion check, not independent review.

For a symmetric Student t model, central probability p selects the quantile at (1+p)/2. The numerical factor depends on the degrees of freedom.

## Equation

```text
k = F_t,nu^(-1)((1+p)/2)
```

## Assumptions

- Independent normally distributed errors with constant variance; applicability is supplied by the caller, not inferred from a passing calculation.

## Limitations

- The distribution must be justified. This implementation supports finite 1≤nu≤10000 and 0.5≤p≤0.9999; infinity is an explicit normal-limit choice.

## Evidence

[Student t density and numerical quantiles](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3664.htm) · §1.3.6.6.4 density and Percent Point Function; equal-tail substitution. Inspected 12 November 2026. Original paraphrase or declared local derivation.
