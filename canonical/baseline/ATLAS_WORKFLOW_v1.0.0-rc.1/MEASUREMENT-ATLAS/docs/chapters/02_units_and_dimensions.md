# Units and quantity meaning

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## Carry the unit and quantity kind

Use the quantity value together with its unit, and distinguish quantity kinds even when dimensions match. Treat intervals separately from offset scales and distinguish Hz from rad/s. [SI330: 2.1 and 2.3.1–2.3.4](https://www.nist.gov/pml/special-publication-330/sp-330-section-2)

## Worked arithmetic

These are invented teaching inputs. A length estimate of 25 mm with standard uncertainty 0.2 mm becomes 0.025 m with standard uncertainty 0.0002 m. Both numbers scale by 0.001. Applying the conversion to the estimate alone would change the represented uncertainty.

An invented Celsius estimate of 20.0 °C with standard uncertainty 0.3 °C becomes 293.15 K with standard uncertainty 0.3 K. A rise of 5 °C is a rise of 5 K, not 278.15 K. The exact offset does not get added to the uncertainty. For an invented 10 Hz oscillation, angular frequency is 20π rad/s.

These examples are explicit arithmetic, not a general units parser. The existing numerical library expects the caller to harmonize units. It cannot infer from the bare number 10 whether the quantity is length, temperature or frequency.

## Record design

Store quantity kind, numerical value, unit, absolute uncertainty unit, scale/interval flag, and reference conditions separately. This is an Atlas documentation convention; it is not evidence that an input was measured correctly. A column heading may express a quantity divided by its unit, such as length/mm. [SI811: 7.1–7.2](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-7-rules-and-style-conventions-expressing-values)

**Stop condition:** units or quantity kind are ambiguous. Do not use numerical coincidence as a substitute for identification.


## Exact reference records

- [A quantity value includes its unit](../records/quantity-value-unit.md)
- [Dimensions alone do not identify a quantity](../records/dimensions-not-kind.md)
- [Absolute Celsius conversion differs from an interval](../records/celsius-temperature-interval.md)
- [Cyclic and angular frequency are different quantities](../records/angular-frequency-unit.md)
- [Dimension one does not remove quantity meaning](../records/dimensionless-meaning.md)
- [Write values and units without ambiguity](../records/quantity-notation.md)
