# Measurement Atlas reference guide

**Release candidate 1.0.0-rc.1 · James Paul Jackson · 12 November 2026**

A bounded scientific reference for specifying, calculating and reporting measurements. Sources, assumptions and limitations travel together. Start with the measurement definition rather than with a formula. The earlier synthetic casebooks remain explicitly invented teaching values. The separate Pontius case uses 40 source-reported observations.

## Eight chapters

| Chapter | Topic |
|---|---|
| [01](chapters/01_measurand_and_terms.md) | Define the measurement before using a formula |
| [02](chapters/02_units_and_dimensions.md) | Units and quantity meaning |
| [03](chapters/03_repeat_readings.md) | Repeat readings and shared effects |
| [04](chapters/04_type_b_and_resolution.md) | Type B information and resolution models |
| [05](chapters/05_budgets_and_nonlinearity.md) | Build the uncertainty model and budget |
| [06](chapters/06_calibration_and_traceability.md) | Calibration, uncertainty and continuing applicability |
| [07](chapters/07_comparison_and_coverage.md) | Compare results without inventing a verdict |
| [08](chapters/08_reporting_and_reuse.md) | Report enough context for a later investigator |

## Apply the reference

Read the [worked casebook](CASEBOOK_v0.5.0.md), [coverage matrix](COVERAGE_MATRIX.md), [source register](PRIMARY_SOURCE_REGISTER.md), and [answer review questions](../evaluations/content_review_questions.json). Templates are under `templates/`.

## What remains

The chapters cover the declared introductory scope, not all metrology. A checked decimal transcription of a published calibration dataset is now included; original file bytes and traceability documents are not. Universal unit parsing beyond the new bounded grammar, independent scientific review, validation of real measurement models, live Bitwork/AI execution and the final held-out study remain open. Navigation development is deliberately deferred; the existing shared engine remains intact.

## Published observation case

[Reproduce the Pontius calibration analysis](PUBLISHED_CALIBRATION_CASE.md) and inspect [the six source-display discrepancies](SOURCE_DISCREPANCIES.md). These extend the calibration family without claiming new laboratory replication.

## Coverage and inverse-interval supplement

[Conditional coverage methods](COVERAGE_METHODS.md) · [Inverse interval replay](INVERSE_INTERVAL_REPLAY.md) · [Synthetic coverage experiment](COVERAGE_SIMULATION.md) · [Independent review checklist](INDEPENDENT_REVIEW_CHECKLIST.md).

The node now contains 92 bounded reference records, 44 source cards and five preserved starter records. These counts include editorial/reference material, not independent measurements.

## Practical v1 candidate additions

[Unit conversions](UNIT_CONVERSIONS.md) · [Certificate interpretation](CERTIFICATE_INTERPRETATION.md) · [Decision models](CONFORMITY_DECISIONS.md) · [Declared v1 scope](V1_RELEASE_SCOPE.md) · [Final review handoff](V1_REVIEW_HANDOFF.md).

Final v1 acceptance remains blocked; none of these documents is a substitute for a required execution or reviewer receipt.
