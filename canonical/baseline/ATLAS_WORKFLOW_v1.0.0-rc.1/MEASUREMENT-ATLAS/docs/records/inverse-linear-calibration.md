# Invert a fitted response model in its valid range

**Record:** `inverse-linear-calibration` · **Type:** equation · **Origin:** source_reported

For a response model y=a+b*x with nonzero b, the corresponding input estimate is (y-a)/b.

## Declared relation

```text
x = (y-a)/b
```

## Source and inspected portion

[Inverse calibration of future measurements](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc366.htm) · §2.3.6.6, Linear calibration line

## Assumptions

- The fitted linear response is applicable at the new indication; b is nonzero.

## Limitations

- This arithmetic does not justify extrapolation, stability or neglected calibration uncertainty.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
