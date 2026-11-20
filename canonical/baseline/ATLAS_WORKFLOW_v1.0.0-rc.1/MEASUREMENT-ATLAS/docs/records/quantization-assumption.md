# Quantization uncertainty needs an explicit model

**Record:** `quantization-assumption` · **Type:** equation · **Origin:** formal_derivation

Assuming a uniform rounding error within half a display step gives standard uncertainty step/sqrt(12).

## Declared relation

```text
u_round = step/sqrt(12)
```

## Source and inspected portion

[Law of propagation of uncertainty](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) · A.5, equation A-7; local a=step/2 substitution

## Assumptions

- Rounding, not truncation; the uniform model is justified independently of the display specification.

## Limitations

- Resolution alone does not establish this distribution; avoid counting the same effect twice.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
