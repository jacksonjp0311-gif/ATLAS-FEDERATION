# Two normalizations of inverse weighting

**Record:** `causal-atlas:ipw-estimator-choices`  
**Kind:** method  
**Evidence:** primary_portion_checked_by_assistant

With supplied treatment probabilities, inverse weights enter either a total divided by sample size or separate normalized arm means. These are distinct finite-sample estimators and should be named rather than silently interchanged.

## Assumptions

- Binary point exposure; causal identification and probability specification justified externally.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- No fitted-propensity uncertainty or confidence intervals implemented.

## Provenance

[AS2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4626409/), §2.2, two ATE estimator equations. Inspected 2026-11-12.

Immutable record revision: `7207eab5bf5bab13e063b2bab1437f99ca463d5d435cea4a4e2c4a8b0495b3aa`.
