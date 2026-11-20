# A sufficient monotonicity check prevents ambiguous inverse bounds

**ID:** `inverse-band-slope-condition` · **Origin:** `formal_derivation` · Assistant source-portion check, not independent review.

For the supported degree-one/two models, a lower bound on mean slope can exceed the largest slope contribution of prediction uncertainty. This is a sufficient condition for monotone interval boundaries.

## Equation

```text
min|fprime(z)| > k max sqrt(hprime(z)^T Cov(beta) hprime(z))
```

## Assumptions

- Coefficient covariance is positive semidefinite and the calibration curve is monotone on the stated range.

## Limitations

- Failure of this conservative test means the limited solver refuses; it does not prove that an inverse confidence set cannot exist.

## Evidence

[Mean response and single-response prediction uncertainty](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd512.htm) · §4.5.1.2 variance formula; original derivative-bound derivation in docs/COVERAGE_METHODS.md. Inspected 12 November 2026. Original paraphrase or declared local derivation.
