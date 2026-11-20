# Residual error separates into pure error and lack of fit

**Record:** `lack-of-fit-partition` · **Type:** equation · **Origin:** source_reported

For least squares with replicated predictor levels, residual sum of squares separates into within-level pure error and weighted deviations of replicate means from the fitted function. Their mean-square ratio gives the lack-of-fit statistic.

## Declared relation

```text
SS_RES = SS_PE + SS_LOF; F_LOF = [SS_LOF/(m-p)]/[SS_PE/(n-m)]
```

## Source and inspected portion

[Replicate-based lack-of-fit assessment](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd446.htm) · §4.4.4.6 pure error, model error and F-ratio definitions

## Assumptions

- p is the number of fitted coefficients.
- n is the number of readings and m the number of distinct settings.
- Both n-m and m-p must be positive, and the pure-error variance nonzero.

## Limitations

- A zero denominator or missing degrees of freedom is reported explicitly, not replaced by a passing verdict.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
