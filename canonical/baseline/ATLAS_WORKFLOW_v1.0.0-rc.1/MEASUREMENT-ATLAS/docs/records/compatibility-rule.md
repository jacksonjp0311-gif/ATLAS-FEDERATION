# Compatibility of results needs a chosen multiplier

**Record:** `compatibility-rule` · **Type:** method · **Origin:** source_reported

Comparing a difference with a chosen multiple of its standard uncertainty requires a specified measurand and covariance-aware difference uncertainty.

## Declared relation

```text
abs(x1-x2) < k * u(x1-x2)
```

## Source and inspected portion

[Metrological compatibility](https://jcgm.bipm.org/vim/en/2.47.html) · 2.47, definition and note 2

## Assumptions

- A multiplier and its intended interpretation are declared.

## Limitations

- Compatibility is not proof of equality or an automatic product-conformity decision.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
