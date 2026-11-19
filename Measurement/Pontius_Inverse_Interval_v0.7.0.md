# Pontius inverse interval replay

**Checkpoint 0.7.0 · 12 November 2026**

The new calculation uses the same 40 checked decimal observations and the same hypothetical response 1.239722 as the retained v0.6 study. It adds no new laboratory observations and does not erase the six earlier publisher-display discrepancies.

## Model and source

The calculation uses the quadratic ordinary least squares fit, coefficient covariance, residual variance, 37 residual degrees of freedom and a computed two-sided 95% t factor of **2.0261924630291333**. It inverts pointwise future-response prediction bands, conditional on independent normal errors, equal response variance, exact predictor values and an adequate calibration model. These conditions have not been experimentally verified here.

The [NIST example](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd61a.htm) describes a single-use interval. Physical units remain unspecified source load units. Original upstream bytes remain unavailable, even after two download attempts in this checkpoint.

## Fixed comparison

Targets and half-integer tolerance were written before the first local interval computation. This is an authored prospective numerical check, not a blind or independently authored evaluation. The target digest is `c90495800126a1a524b0dbf5b30c4d363214f660bc71969ec9a43bd17eedca9c`.

| Quantity | Local calculation | Publisher display | Absolute difference | Within 0.5 source unit? |
|---|---:|---:|---:|---|
| estimate | 1705105.56885173 | 1705106 | 0.43114827 | Yes |
| lower | 1704513.37293746 | 1704513 | 0.37293746 | Yes |
| upper | 1705697.76361652 | 1705697 | 0.76361652 | No |

The estimate and lower endpoint match within that tolerance; the upper endpoint does not. The cause is unestablished. This report does not assign it to publisher error, a particular rounding rule, data changes or software defects. The comparison remains `computed_with_publisher_discrepancies`.

## Separate numerical algorithm

A NumPy least-squares fit and covariance, SciPy t quantile and SciPy Brent root solver give lower **1704513.37293746** and upper **1705697.76361652**. Endpoint agreement with the local implementation is within 4.66e-10 source unit. The predeclared cross-check tolerance is 1e-5 source unit.

This comparison reduces the chance of a shared implementation mistake but is not independent human review. It also cannot establish the physical validity of the statistical assumptions.

## Preserve the evidence

The publisher upper bound and recomputed upper bound are separate common-contract records joined by `contradicts`. The unchanged context assembler can retain them together. Old source records, thresholds and case bytes remain intact; the new target file is separately hashed.

```powershell
py -3 -m measurement_atlas inverse-interval
```

The command exits successfully when the computation succeeds, while its JSON explicitly reports publisher disagreement. Success of the program is not success of every scientific comparison. See [v0.6 source discrepancies](SOURCE_DISCREPANCIES.md) and [method assumptions](COVERAGE_METHODS.md).
