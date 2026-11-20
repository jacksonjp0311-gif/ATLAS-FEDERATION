# Stratum-standardized target effect

Reweight source conditional causal effects using target population covariate distribution when effects are transportable within strata.

**Record:** `causal-atlas:transport-by-standardization`  
**Revision:** `98503709fb8564cf07fae596e6ba4656009e1ee2a872ee6e939529b0c164a433`  
**Evidence type:** original_arithmetic_with_source_context

## Conditions

- Source response functions causal
- Target conditional invariance
- Source support for target strata

## Limitations

- Stratum reweighting is not a general graphical transportability algorithm

## Primary source scope

[Transportability of Causal Effects: Completeness Results](https://ojs.aaai.org/index.php/AAAI/article/view/8232) — Abstract defining transportability of causal information

**Equation:** `ATE_target=sum_z p_target(z) (mu1,src(z)-mu0,src(z))`

This source-linked record is not independently scientifically reviewed.
