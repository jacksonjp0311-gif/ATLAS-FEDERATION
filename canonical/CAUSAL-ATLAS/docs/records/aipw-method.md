# Augmented weighting under identification assumptions

**Record:** `causal-atlas:aipw-method`  
**Kind:** method  
**Evidence:** primary_portion_checked_by_assistant

AIPW combines an outcome contrast with propensity-weighted residual corrections. The local implementation uses the residual expression derived in the guide and supplied nuisance values; it does not fit or validate them.

## Formula

```text
mean(m1-m0 + A/e*(Y-m1) - (1-A)/(1-e)*(Y-m0))
```

## Assumptions

- Consistency; sufficient adjustment; positivity; appropriate sampling.

## Applicability

- Declared target and data-generating conditions only.

## Limitations

- See the correction notice and local algebra, not a verbatim transcription of displayed publisher equations.

## Provenance

[KURZ2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8793316/), AIPW Estimator section. Inspected 2026-11-12.

Immutable record revision: `2df7876759403fe2dbf59618d17d3810e0b98284ed04d65079b959bec1399f17`.
