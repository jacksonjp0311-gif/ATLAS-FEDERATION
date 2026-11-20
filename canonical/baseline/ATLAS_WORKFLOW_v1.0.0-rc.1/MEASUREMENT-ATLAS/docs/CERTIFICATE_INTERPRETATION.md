# Interpret calibration information without inventing certification

The new `review_certificate` utility accepts manually transcribed fields. It does not parse a PDF, verify a laboratory, authenticate a signature, establish accreditation, or reconstruct a traceability chain.

Required context includes the certificate identifier, source locator, instrument identity, calibration date, quantity kind, unit, reported value, uncertainty convention, conditions, traceability references and data origin. Missing or contradictory fields produce `incomplete`. A structurally complete input produces `structured_for_review`, never `certified`.

## Standard uncertainty

A reported expanded uncertainty can be divided by its explicitly stated factor. The importer requires that factor and will not guess it from an unexplained confidence percentage. This arithmetic follows [NIST TN 1297 section 4.2](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-4-type-b-evaluation-standard-uncertainty); choosing a distribution remains a separate scientific task.

The supplied `as_of` date makes date checking reproducible. No universal calibration expiry is invented. An optional operator due date is checked only as a declared scheduling constraint, not as a standard mandated interval. An expired operator date or a future calibration date blocks the structured component from being offered for use.

## Conditions and later use

NIST's policy limits its reported results to the specified item and test time unless otherwise stated. Its uncertainty guidance explains that transport, drift and different later-use conditions may need further assessment. See [calibration policies](https://www.nist.gov/calibrations/policies) and [TN 1297 sections 7.5–7.6](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty).

Completing this checklist does not make an actual result fit for a particular use. The software returns `authenticity_verified: false`, `traceability_established: false` and an unknown fitness-for-use result. Full evidence and competent review are still required.

## Explicit specification model

`specification_component` implements only a caller-justified additive model: percent of reading plus percent of full scale plus counts times resolution. It then requires a declared uniform or triangular distribution. It does not infer the intended combination from a manufacturer's prose, and it does not assume independent terms or a complete uncertainty budget.

Both files in `examples/` labeled synthetic are invented teaching inputs, not realistic-looking issued certificates. Run:

```powershell
py -3 -m measurement_atlas certificate-review --input examples/synthetic_certificate.json
py -3 -m measurement_atlas certificate-review --input examples/missing_factor_certificate.json
```

The second invocation computes an `incomplete` review. A successful process exit means the review ran, not that the submitted report is acceptable.
