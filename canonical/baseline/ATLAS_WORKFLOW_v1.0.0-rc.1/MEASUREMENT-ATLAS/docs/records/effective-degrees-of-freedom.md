# Welch–Satterthwaite effective degrees of freedom

**Record:** `effective-degrees-of-freedom` · **Type:** equation · **Origin:** source_reported

The conventional effective-degree calculation combines independent uncertainty contributions and their degrees of freedom.

## Declared relation

```text
nu_eff = u_c**4 / sum((c_i*u_i)**4/nu_i)
```

## Source and inspected portion

[Coverage factors and effective degrees of freedom](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-b-coverage-factors) · B.3, equation B-1 and following independence condition

## Assumptions

- The component uncertainty estimates meet the stated statistical-independence and approximation conditions.

## Limitations

- Do not apply this formula unmodified to a correlated-component budget; it does not by itself choose k.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
