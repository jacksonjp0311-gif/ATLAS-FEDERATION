# Why inverse weighting works in a specified population

**Record:** `causal-atlas:ipw-expectation-identity`  
**Kind:** equation  
**Evidence:** authored_mathematical_teaching_material

Conditional on Z, E[A*Y/e(Z)|Z]=mu1(Z) when e is the true treatment probability. The corresponding control expectation equals mu0(Z). This algebra requires support and does not prove the measured variables suffice for causal identification.

## Formula

```text
E[A Y/e | Z]=e*mu1/e=mu1
```

## Assumptions

- The example’s stated mechanism or the protocol’s declared scope.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- Not independent empirical validation or a general identification result.

## Provenance

Local derivation or workflow: `docs/chapters/03_weighting_and_diagnostics.md`.

Immutable record revision: `93d4ad520900670911be5f257116347401905b02aea33162e529e62dc6ca584c`.
