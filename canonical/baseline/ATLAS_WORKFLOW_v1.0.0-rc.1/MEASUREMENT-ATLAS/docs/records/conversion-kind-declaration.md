# Unit conversion requires an explicit quantity kind

**Record:** `conversion-kind-declaration` · **Type:** method · **Origin:** formal_derivation

Matching dimensions do not identify the quantity kind. The converter requires a caller-declared kind and refuses frequency-to-activity substitutions.

## Source and inspected portion

[SI quantities, dimensions and units](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) · Section 2: quantity kinds and dimensions; local conversion policy

## Assumptions

- The caller supplies the intended physical quantity.

## Limitations

- A finite parser is not a universal units ontology.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical certification.
