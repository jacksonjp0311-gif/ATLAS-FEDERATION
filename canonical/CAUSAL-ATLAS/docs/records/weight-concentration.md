# Weights can leave little effective representation

**Record:** `causal-atlas:weight-concentration`  
**Kind:** equation  
**Evidence:** authored_mathematical_teaching_material

For nonnegative weights define ESS=(sum w)^2/sum(w^2). By Cauchy–Schwarz it cannot exceed the row count. For weights 1000,2,2 it is 126002/125001, approximately 1.008, despite three rows. This measures concentration only, not the number of independent observations.

## Formula

```text
ESS=(sum w)^2/sum(w^2)
```

## Assumptions

- The example’s stated mechanism or the protocol’s declared scope.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- Not independent empirical validation or a general identification result.

## Provenance

Local derivation or workflow: `docs/chapters/03_weighting_and_diagnostics.md`.

Immutable record revision: `16e8bcac6c4643ecd365e96b774b73a7574e6088c6b9e3ebb50a12d739476b00`.
