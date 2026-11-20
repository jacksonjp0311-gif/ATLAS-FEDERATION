# Temperature uncertainty uses scale not offset

**Record:** `temperature-uncertainty-scale` · **Type:** equation · **Origin:** formal_derivation

Temperature differences use the same scale in Celsius and kelvin. Uncertainty conversion uses the derivative, not the absolute-temperature offset.

## Declared relation

```text
T = t + 273.15; u(T) = u(t)
```

## Source and inspected portion

[NIST SI guide: temperature intervals and quantity meaning](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8) · §8.5; affine-map derivative

## Assumptions

- Same underlying temperature quantity and compatible uncertainty convention.

## Limitations

- Does not validate temperature realization or sensor calibration.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical certification.
