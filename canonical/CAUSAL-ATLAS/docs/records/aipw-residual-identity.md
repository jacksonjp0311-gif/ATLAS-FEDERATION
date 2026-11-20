# Residual form keeps the control sign explicit

**Record:** `causal-atlas:aipw-residual-identity`  
**Kind:** equation  
**Evidence:** authored_mathematical_teaching_material

For treatment a, add the outcome prediction to an inverse-probability residual correction. Subtract the complete control quantity from the treatment quantity. If both predictions and every observed outcome equal the same constant, every unit’s contrast is zero, whatever its interior propensity.

## Formula

```text
phi=m1-m0+A/e*(Y-m1)-(1-A)/(1-e)*(Y-m0)
```

## Assumptions

- The example’s stated mechanism or the protocol’s declared scope.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- Not independent empirical validation or a general identification result.

## Provenance

Local derivation or workflow: `docs/chapters/04_augmented_estimation.md`.

Immutable record revision: `5c7ed4cdf26dca07ff69f3081a6fbfa0a7d131ee541a9b0284107809578aae15`.
