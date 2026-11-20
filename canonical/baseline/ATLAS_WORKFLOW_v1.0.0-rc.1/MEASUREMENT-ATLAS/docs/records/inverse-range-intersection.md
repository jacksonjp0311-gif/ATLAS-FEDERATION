# Clipping an inverse interval does not validate extrapolation

**ID:** `inverse-range-intersection` · **Origin:** `formal_derivation` · Assistant source-portion check, not independent review.

The computed inverse confidence set may extend beyond the calibrated range. Restricting it to that range must be marked as clipping rather than reported as a complete unrestricted interval.

## Equation

```text
reported_set = inverse_set ∩ calibrated_range
```

## Assumptions

- The calibration is supported only on its declared predictor interval.

## Limitations

- The default toolkit call refuses out-of-range endpoints; opt-in clipping is labeled and preserves the limitation.

## Evidence

[Load-cell inverse calibration example](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd61a.htm) · §4.6.1.10 admissible load range; local intersection rule. Inspected 12 November 2026. Original paraphrase or declared local derivation.
