# A useful algebraic regression test

**Record:** `causal-atlas:constant-outcome-test`  
**Kind:** method  
**Evidence:** authored_mathematical_teaching_material

Set Y=m0=m1=c for every unit. Residuals vanish and AIPW must return zero. A test that fails this condition has an implementation or formula error; passing it alone does not prove complete correctness.

## Assumptions

- The example’s stated mechanism or the protocol’s declared scope.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- Not independent empirical validation or a general identification result.

## Provenance

Local derivation or workflow: `tests/test_estimation.py::test_same_constant_outcome_aipw_zero`.

Immutable record revision: `d18444f9bb7d6cafe6ad696a5a30a39a778b04959d3a792e1c5645bc8cf0d644`.
