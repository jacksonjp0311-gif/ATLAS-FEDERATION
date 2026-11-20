# Unobserved binary outcomes bound a cohort risk

**Record:** `causal-atlas:binary-missing-bounds`  
**Kind:** equation  
**Evidence:** authored_mathematical_teaching_material

With N counted units, O observed outcomes and S observed successes, risk lies between S/N and (S+N-O)/N without a missingness model. Difference bounds subtract the opposite endpoints of the two arms. These are finite-cohort arithmetic bounds, not confidence intervals or confounding adjustment.

## Formula

```text
L=S/N; H=(S+N-O)/N; RD in [L1-H0,H1-L0]
```

## Assumptions

- The example’s stated mechanism or the protocol’s declared scope.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- Not independent empirical validation or a general identification result.

## Provenance

Local derivation or workflow: `docs/chapters/05_missingness_and_sensitivity.md`.

Immutable record revision: `dc778870b92c6d0a2e12c24185c2c650855d57f62e857b46a5f6c233e4e17e15`.
