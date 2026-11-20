# Absolute Celsius conversion differs from an interval

**Record:** `celsius-temperature-interval` · **Type:** equation · **Origin:** source_reported

Celsius temperature and kelvin temperature differ by an offset; a temperature interval has the same numerical magnitude in °C and K.

## Declared relation

```text
T/K = t/degC + 273.15; deltaT/K = deltat/degC
```

## Source and inspected portion

[SI quantities, dimensions and units](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) · §2.3.1, kelvin and Celsius paragraphs

## Assumptions

- Values refer to the stated thermodynamic/Celsius scale relationship.

## Limitations

- Do not add 273.15 to a temperature difference or its absolute uncertainty.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
