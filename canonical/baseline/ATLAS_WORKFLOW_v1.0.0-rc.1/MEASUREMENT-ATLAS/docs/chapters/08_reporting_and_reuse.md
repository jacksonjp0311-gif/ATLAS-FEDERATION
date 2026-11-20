# Report enough context for a later investigator

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## A reusable measurement record

Historical TN 1297 reporting guidance asks for the uncertainty form, component evaluations, coverage factor where used and the basis of a probability interpretation. Its section 7 page is marked no longer updated; use it as the named historical reference, not a current compliance certificate. [TN7: 7.1–7.2 and page warning](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty)

The proposed Atlas report template separates the intended quantity, object and conditions, raw-input references, measurement model, correction terms, numerical output and units, uncertainty budget, coverage assumptions, unresolved effects, and reviewer status. It also identifies the exact data and code revisions used.

## Worked reporting pattern

For a synthetic length calculation, a useful result might say: “Model estimate 10.000 mm; combined standard uncertainty 0.224 mm under the stated independent-component budget. Inputs are invented teaching values. No conformity decision and no coverage probability is assigned.” The purpose is to make the provenance and interpretation difficult to lose during reuse.

This wording is an example, not an actual measurement. For genuine data, retain instrument identifiers, original files and acquisition context instead of editing the example into a purported certificate.

## Correction workflow

When new evidence changes an input, do not silently replace the previous calculation. Record the changed assumption or input, preserve the earlier result, recalculate, and mark dependent reports for review. This is an Atlas record-management convention rather than an assertion about any external quality standard.

**Release boundary:** a source locator, reproducible calculation and successful software test are distinct evidence. This edition adds reference depth and authored teaching checks; it does not add independent review, real experimental reproduction or measured AI improvement.


## Exact reference records

- [Report uncertainty with its basis](../records/uncertainty-reporting.md)
- [Traceability is not fitness for purpose](../records/fitness-for-purpose.md)
- [Write values and units without ambiguity](../records/quantity-notation.md)
- [Error is not uncertainty](../records/error-not-uncertainty.md)
