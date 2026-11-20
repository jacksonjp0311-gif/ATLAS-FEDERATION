# Direct-path sensitivity is a scenario, not a confidence interval

Vary a caller-supplied direct contribution gamma under an explicit additive equation; return ordered effect bounds only when the declared first-stage guard permits division.

**Record:** `causal-atlas:iv-exclusion-sensitivity`  
**Exact revision:** `26718112f500a20e2b80269b859be73f16c4326628f13c2e81336eb21439e5e4`  
**Origin:** `authored_derivation`

## Equation

`theta(gamma) = (DeltaY-gamma)/DeltaD`

## Assumptions and limits

- Not a generic bound on all violations or a sampled confidence interval.

## Source and locator

Original derivation/example; see the local locator.

docs/chapters/10_iv_failures_and_sensitivity.md; causal_atlas/quasi.py:exclusion_sensitivity

No independent scientific review or empirical validation is claimed.
