# Changing weights changes the calculation

**Record:** `causal-atlas:truncation-tradeoff`  
**Kind:** concept  
**Evidence:** primary_portion_checked_by_assistant

Truncating extreme weights can exchange variance reduction for bias. Report the modification and resulting estimand/model implications instead of treating clipping as invisible numerical housekeeping.

## Assumptions



## Applicability

- Declared target and data-generating conditions only.

## Limitations

- No automatic clipping or truncation rule is implemented.

## Provenance

[CH2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2732954/), Weight truncation as a means to tradeoff bias and variance. Inspected 2026-11-12.

Immutable record revision: `ad16e5ad5bc9dcd39aeeebb820f8ecd242edb50dddb96717f1f35dadd2ff704d`.
