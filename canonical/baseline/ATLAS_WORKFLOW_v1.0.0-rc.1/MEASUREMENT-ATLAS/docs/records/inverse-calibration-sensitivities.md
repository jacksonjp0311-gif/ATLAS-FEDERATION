# Sensitivities of inverse linear calibration

**Record:** `inverse-calibration-sensitivities` · **Type:** equation · **Origin:** formal_derivation

Differentiating the linear inverse gives sensitivities to the indication, intercept and slope; propagate their complete covariance matrix.

## Declared relation

```text
dx/dy=1/b; dx/da=-1/b; dx/db=-(y-a)/b**2
```

## Source and inspected portion

[Inverse calibration of future measurements](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc366.htm) · §2.3.6.6 linear inverse; Atlas differentiation

## Assumptions

- First-order propagation is adequate; parameter/input units are consistent.

## Limitations

- These are locally derived derivatives, not extra measurements from the source.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
