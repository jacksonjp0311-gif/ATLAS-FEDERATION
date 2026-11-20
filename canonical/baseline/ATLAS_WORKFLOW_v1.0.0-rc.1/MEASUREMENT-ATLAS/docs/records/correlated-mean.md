# Variance of a mean with correlated inputs

**Record:** `correlated-mean` · **Type:** equation · **Origin:** formal_derivation

For the arithmetic mean, propagation with sensitivities 1/n gives the sum of all covariance entries divided by n squared.

## Declared relation

```text
Var(mean) = sum_ij(Sigma_ij)/n**2
```

## Source and inspected portion

[Law of propagation of uncertainty](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) · A.3; local substitution c_i=1/n

## Assumptions

- The supplied covariance describes the readings; averaging is a linear model.

## Limitations

- The familiar variance/n reduction follows only with the appropriate zero-covariance and equal-variance conditions.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
