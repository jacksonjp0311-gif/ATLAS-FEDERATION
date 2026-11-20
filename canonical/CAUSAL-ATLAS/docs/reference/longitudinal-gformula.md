# Two-decision g-formula risk

A specified transition model and outcome model can be marginalized over an intermediate state to obtain a strategy risk.

**Record:** `causal-atlas:longitudinal-gformula`  
**Revision:** `5ace5bcbc3645fdbc8243b9f05379d10a7785a257024cc2e794457cceba37c66`  
**Evidence type:** original_arithmetic_with_source_context

## Conditions

- Sequential exchangeability
- Positivity for all compared histories
- Consistency and correct conditional models

## Limitations

- The bundled tool is exact finite enumeration of a stipulated model, not an observational fitted estimator

## Primary source scope

[Causal Inference What If author resource page](https://miguelhernan.org/whatifbook) — Part III broad topic description

**Equation:** `R(a0,a1)=sum_l0 p(l0) sum_l1 p(l1|l0,a0) E[Y|l0,a0,l1,a1]`

This source-linked record is not independently scientifically reviewed.
