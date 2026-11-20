# Group-time staggered DiD contrast

Compare cohort changes to eligible untreated comparison changes, recording cohort, period, baseline and comparison groups.

**Record:** `causal-atlas:staggered-cohort-time`  
**Revision:** `aa8e18ed464e0aee205a21ab5633b53202d81bb3407c9e8198149a5e5801f932`  
**Evidence type:** original_arithmetic_with_source_context

## Conditions

- No anticipation and conditional counterfactual parallel trends for causal interpretation

## Limitations

- Local tool computes mean changes only, not the original complete estimator or its confidence bands

## Primary source scope

[Difference-in-Differences with Multiple Time Periods](https://doi.org/10.1016/j.jeconom.2020.12.001) — Publisher abstract, varied treatment timing

**Equation:** `D(g,t)=(Y_g,t-Y_g,g-1)-(Y_C,t-Y_C,g-1)`

This source-linked record is not independently scientifically reviewed.
