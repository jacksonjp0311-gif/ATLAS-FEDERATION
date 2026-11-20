# Calibration, uncertainty and continuing applicability

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## What calibration supplies

Calibration relates standards and indications with uncertainties, then supports deriving a result from an indication. Adjustment and verification are different operations. [VCAL: 2.39 definition and notes](https://jcgm.bipm.org/vim/en/2.39.html)

For a fitted response y=a+bx, the inverse is x=(y−a)/b when b≠0. The input indication, intercept and slope can all be uncertain. [CALINV: 2.3.6.6, linear calibration line](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc366.htm)

## Original synthetic calculation

Choose y=10, a=2 and b=4 in compatible abstract response/input units. Then x=2. The sensitivities to (y,a,b) are (0.25,−0.25,−0.5). Let their variances be (0.04,0.01,0.0025), covariance(a,b)=−0.002 and other covariance zero. Applying those sensitivities yields variance 0.00325 and standard uncertainty about 0.05701 input units. The code uses the supplied coefficient covariance rather than inferring independence.

## Evidence beyond the arithmetic

For a multi-input measurement, traceability can involve several branches. A valid chain does not guarantee suitability for a use case. [VTRACE: 2.41 notes 3–5](https://jcgm.bipm.org/vim/en/2.41.html)

Drift and day-to-day changes can invalidate a calibration; correction does not inherently reduce repeat scatter. [CALFAIL: 2.3.6.4, named inspected paragraphs](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm)

The cited NIST linear-control procedure checks low, middle and high parts of the range. Treat that as its stated design, not a universal three-point guarantee. [CALCHECK: 2.3.7](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc37.htm)

The certificate-review template asks for identity, applicable range, conditions, uncertainty interpretation, parameter covariance where relevant, reference chain and ongoing checks. This is an Atlas review aid, not an accreditation checklist or certification.


## Exact reference records

- [Calibration relates standards, indications and results](../records/calibration-two-stages.md)
- [Calibration is not adjustment or verification](../records/calibration-not-adjustment.md)
- [Invert a fitted response model in its valid range](../records/inverse-linear-calibration.md)
- [Sensitivities of inverse linear calibration](../records/inverse-calibration-sensitivities.md)
- [Traceability can involve several input chains](../records/traceability-network.md)
- [Calibration must remain applicable over time](../records/calibration-stability.md)
- [Calibration does not inherently improve precision](../records/calibration-not-precision-fix.md)
- [Monitor a linear calibration across its range](../records/check-standard-regime.md)

## Work a published calibration case

The [Pontius case study](../PUBLISHED_CALIBRATION_CASE.md) analyzes 40 published readings, compares a line with a quadratic, separates pure error from lack of fit, and constrains inverse calibration to the observed range. It also preserves a [numerical source disagreement](../SOURCE_DISCREPANCIES.md). The data do not establish a complete traceability chain or supply physical units.
