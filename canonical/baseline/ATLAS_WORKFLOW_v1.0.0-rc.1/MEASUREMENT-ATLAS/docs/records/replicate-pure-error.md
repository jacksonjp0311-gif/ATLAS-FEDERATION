# Replicate measurements estimate pure error

**Record:** `replicate-pure-error` · **Type:** method · **Origin:** source_reported

Within-level squared deviations from replicate means provide a model-independent pure-error estimate. They supply the comparison denominator for a replicate-based lack-of-fit test.

## Declared relation

```text
SS_PE = sum_i sum_j (y_ij - mean_i)^2; df_PE = n - number_of_distinct_levels
```

## Source and inspected portion

[Replicate-based lack-of-fit assessment](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd446.htm) · §4.4.4.6 Testing Model Adequacy Requires Replicate Measurements; estimating sigma from replicates

## Assumptions

- Replicates represent the same predictor settings and experimental conditions.
- Classical F interpretation needs its error assumptions.

## Limitations

- Replicates differing in unmodeled conditions do not automatically meet those assumptions.
- No replicates means this pure-error comparison is unavailable.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
