# Define the measurement before using a formula

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## Start with the intended quantity

The measurand is the target quantity, including relevant object and state conditions. An instrument may perturb what it observes. Specify the target before choosing a correction or comparing results. [VMEAS: 2.3, notes 1 and 3](https://jcgm.bipm.org/vim/en/2.3.html)

**Atlas working example, not measured data:** “plate length” is too vague for a reproducible task. A useful proposed specification is “distance between the identified reference faces of specimen P, at a stated reference temperature, using procedure R.” Record the material, orientation, load and temperature information when the model needs them. This is an intake pattern, not a universal dimensional-inspection procedure.

## Keep the terms separate

Use *accuracy* qualitatively; use dispersion statistics to describe *precision* under specified conditions. Neither a small standard deviation nor a calibration label supplies a complete uncertainty budget. [VACC: 2.13 notes 1–2](https://jcgm.bipm.org/vim/en/2.13.html) [VPREC: 2.15 notes 1–4](https://jcgm.bipm.org/vim/en/2.15.html)

Uncertainty describes the spread of values assigned using the information available, potentially including systematic-effect and reference-value components. [VUNC: 2.26 definition and notes](https://jcgm.bipm.org/vim/en/2.26.html)

## Before proceeding

Write a short task statement with the quantity kind, object identifier, reference conditions, intended use, measurement procedure, and output unit. Mark missing values as unknown rather than substituting defaults. Decide whether temperature belongs to the target specification, the instrument-response model, or both in different roles. VIM3 and GUM do not use identical scopes for “influence quantity.” [VINFL: 2.52 example 3 and note 2](https://jcgm.bipm.org/vim/en/2.52.html)

**Stop condition:** the intended quantity cannot be distinguished from the instrument indication. Resolve the specification before publishing a corrected estimate.


## Exact reference records

- [Specify the measurand before calculating](../records/measurand-definition.md)
- [Measurement may disturb the target](../records/measurement-intervention.md)
- [Accuracy is not a numerical uncertainty specification](../records/accuracy-qualitative.md)
- [Precision requires stated measurement conditions](../records/precision-conditions.md)
- [Influence quantity depends on the measurement definition](../records/influence-quantity.md)
- [Uncertainty belongs to the result and information used](../records/uncertainty-information.md)
