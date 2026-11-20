# Measurement Atlas 0.5.0 content audit

**12 November 2026 · Content-first checkpoint, not v1 acceptance**

The node now contains 50 bounded reference records, 27 bibliographic source cards and five preserved starter navigation records. Thirty bounded records and seventeen source pages were added in this edition. Earlier source content and evidence labels remain preserved; old snapshots are retained in `history/`.

## Reader-facing deliverables

Eight chapters cover the measurand and terminology, units, repeated readings, Type B information, budgets and nonlinear models, calibration and traceability, comparisons, and reporting. Fifty individual pages retain statement, exact locator, assumptions, applicability and limitations. Four blank templates guide a measurement plan, uncertainty budget, calibration review and result report. Twenty-four authored questions have explicit rubrics and evidence targets; these are not a model benchmark result.

[Read the guide](REFERENCE_GUIDE.md) · [Source register](PRIMARY_SOURCE_REGISTER.md) · [Worked cases](CASEBOOK_v0.5.0.md) · [Coverage matrix](COVERAGE_MATRIX.md)

## Actual checks

**75 Measurement tests passed**; the companion Forge suite passed **170 tests**. Twelve new original synthetic examples and five retained examples reproduce. The NumPy numerical oracle passed 600 seeded valid covariance cases and rejected five invalid cases. Current-content Markdown links, reference/source IDs, chapter targets, rubric references and required qualifiers passed the content audit. Historical documents are retained in their original context and excluded from the current-content link audit.

The numerical core modules are unchanged from 0.4.0. The version 0.5.0 wheel installed in a clean environment and its common reference has 82 records. The wheel includes portable records and numerical methods; the eight chapters, per-record documentation and templates are delivered in the source workspace/ZIP rather than installed as Python package data.

## Evidence and release limits

Source checks are assistant inspection of identified portions, not independent review or source-author endorsement. Locally derived formula records are identified as derivations. Teaching examples use invented numbers. No new raw measurements, authentic calibration certificates, laboratory replication, model-answer evaluation or Windows test was performed. The library is not a calibration service and contains no universal pass/fail decision rule. A compatible Atlas Forge installation is needed for the `reference` command; numeric functions remain standalone.

The common contract remains stable. G4/G5 software checks have current receipts in Forge. Measurement v1 is not accepted; the remaining eight-family coverage gaps are listed explicitly. Navigation is deferred, not waived. Do not advance to a new domain based on this version number.
