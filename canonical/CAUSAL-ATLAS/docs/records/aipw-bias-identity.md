# An exact misspecification identity

**Record:** `causal-atlas:aipw-bias-identity`  
**Kind:** equation  
**Evidence:** authored_mathematical_teaching_material

For one stratum with true propensity e, working propensity g, true means mu0,mu1 and working means m0,m1, the expected AIPW bias is (e-g)*[(mu1-m1)/g+(mu0-m0)/(1-g)]. Its target-weighted sum vanishes if g=e or both working means are correct. This is an original worked derivation of a standard property.

## Formula

```text
bias(z)=(e-g)*((mu1-m1)/g+(mu0-m0)/(1-g))
```

## Assumptions

- The example’s stated mechanism or the protocol’s declared scope.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- Not independent empirical validation or a general identification result.

## Provenance

Local derivation or workflow: `docs/chapters/04_augmented_estimation.md`.

Immutable record revision: `671031235dbb2327e97f5a147f097cad83e0ab7a8a35a67cfc0aca278f7502e4`.
