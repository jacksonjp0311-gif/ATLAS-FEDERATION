# Unit-aware measurement calculations

This release candidate provides a bounded unit parser and a conversion API. It is not a universal units system. Numerical functions remain dependency-free and require explicit invocation; retrieving an Atlas record never executes a calculator.

## Contract

Call `convert_quantity(value, from_unit, to_unit, quantity_kind=..., uncertainty=..., interval=...)`. The value and optional standard uncertainty must be finite JSON numbers. Uncertainty cannot be negative. The quantity kind is mandatory, preserved, and not inferred from dimensions.

Expressions use known atoms joined by `*` and `/`, optionally raised to a signed integer exponent such as `kg*m/s^2`. Whitespace around operators is accepted; implicit products, parentheses, fractional powers, logarithmic units, unknown atoms and arbitrary code are rejected. Unit expressions are limited to 128 characters, 16 factors and exponents of magnitude at most 12. Numeric conversions use binary floating point.

The catalog includes SI base units and common derived units, grams, litres, minutes, hours, percentages, Celsius, radians and steradians. A finite list of common prefixes is supported. Unsupported prefixes or compound forms fail explicitly; the catalog is not advertised as the complete current SI. `parse_unit` returns the supported dimensional and scale representation.

## Examples

```python
from measurement_atlas.units import convert_quantity

convert_quantity(36, "km/h", "m/s", quantity_kind="velocity")
# value: 10.0

convert_quantity(20, "degC", "K", quantity_kind="temperature", uncertainty=0.2)
# value: 293.15; standard_uncertainty: 0.2

convert_quantity(20, "degC", "K", quantity_kind="temperature", interval=True)
# value: 20.0
```

The absolute Celsius conversion has an offset; an interval or uncertainty does not. See [NIST SP 811 section 8.5](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8). This implements the stated relation, not a sensor-calibration procedure.

## Quantity kinds

Dimensions alone do not distinguish every scientific quantity. Frequency-to-activity conversion (`Hz` to `Bq`) is refused, as is silently replacing `Hz` with `rad/s`. An angular-velocity conversion requires an explicit radian unit. Converting a bare dimensionless ratio to an angle is also refused. These checks are conservative software policies; they are not a full ontology or a general physical-relation solver.

The caller's declaration of energy versus torque or another same-dimensional kind still needs scientific justification. A compatible unit does not establish the intended measurand. Unsupported quantity kinds require a reviewed extension rather than a guessed conversion.
