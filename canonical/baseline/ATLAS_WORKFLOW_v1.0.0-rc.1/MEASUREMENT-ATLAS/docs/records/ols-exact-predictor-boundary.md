# Ordinary least squares reproduction omits predictor uncertainty

**Record:** `ols-exact-predictor-boundary` · **Type:** claim · **Origin:** formal_derivation

This reproduction fits response variation conditional on supplied load values. It contains no model or uncertainty term for errors in those reference loads.

## Source and inspected portion

[Pontius numerical certification methodology](https://www.itl.nist.gov/div898/strd/lls/data/LINKS/c-Pontius.shtml) · Ordinary least squares definition; local statement of the fitted model boundary

## Assumptions

- Predictor values are treated as fixed and exact for the calculation.

## Limitations

- Treating x as exact computationally does not establish uncertainty-free reference loads physically.
- An errors-in-variables analysis or a complete calibration budget would require more information.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
