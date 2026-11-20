# First-order uncertainty propagation

**Record:** `linear-propagation` · **Type:** equation · **Origin:** source_reported

Combine input variances and covariances using local sensitivities.

## Declared relation

```text
u_c^2 = c^T Sigma c
```

## Source and inspected portion

[Law of propagation of uncertainty](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) · A.3, equation A-3

## Assumptions

- First-order Taylor approximation; sensitivities evaluated at input estimates.

## Limitations

- Nonlinearity may require another method.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
