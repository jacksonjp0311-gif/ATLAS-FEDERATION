# Numerical t tails retain an inspectable calculation path

**ID:** `incomplete-beta-t-calculation` · **Origin:** `formal_derivation` · Assistant source-portion check, not independent review.

The t survival function can be reduced to a regularized incomplete beta evaluation. The toolkit evaluates that representation and brackets the inverse numerically.

## Equation

```text
P(T>t)=0.5 I_(nu/(nu+t^2))(nu/2,1/2), for t>0
```

## Assumptions

- Finite positive degrees of freedom; documented numerical range and convergence checks.

## Limitations

- A numerical cross-check is not scientific review. Probabilities outside the tested interface range are refused.

## Evidence

[Incomplete beta function representations](https://dlmf.nist.gov/8.17) · §8.17 E1–E4 and §8.17(v); substitution into Student t density. Inspected 12 November 2026. Original paraphrase or declared local derivation.
