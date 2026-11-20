# MEASUREMENT ATLAS

**A reusable scientific reference for meaningful measurements.**

**Content edition 0.5.0 · Active Atlas in Forge · Scientific v1 acceptance pending**

Measurement Atlas helps a person or compatible AI specify what is being measured, understand units and uncertainty, inspect calibration assumptions, and communicate results without losing their evidence. The reference comes first; calculators and retrieval support it.

**[Read the eight-chapter reference guide](docs/REFERENCE_GUIDE.md)** · [Worked cases](docs/CASEBOOK_v0.5.0.md) · [Coverage gaps](docs/COVERAGE_MATRIX.md) · [Sources](docs/PRIMARY_SOURCE_REGISTER.md)

## Current reference content

The common node has **82 records**: 50 bounded reference records, 26 inspected primary source-page cards, five preserved unreviewed starter-navigation records, and one original source card. The 50 records include conceptual explanations, methods and equations. Record counts include bibliographic metadata and are not counts of independently verified discoveries.

This edition adds **30 reference records and 17 source pages**, eight explanatory chapters, 50 individual reference pages, four blank review templates, 12 new synthetic worked cases and 24 authored review questions. Together with the retained five examples, there are 17 executable teaching cases.

The new sources are public JCGM/BIPM VIM3 entries and NIST SI/calibration/uncertainty pages. Each addition retains its exact inspected portion, edition, assumptions, limitations and rights. Assistant source inspection is not independent review. TN 1297 section 7 now carries the source's explicit no-longer-updated warning; it is not presented as a current accreditation requirement.

## Reference directory

| Topic | Entry point |
|---|---|
| Measurand, accuracy and precision | [Chapter 1](docs/chapters/01_measurand_and_terms.md) |
| Units, Celsius intervals and angular frequency | [Chapter 2](docs/chapters/02_units_and_dimensions.md) |
| Repeatability, averaging and correlation | [Chapter 3](docs/chapters/03_repeat_readings.md) |
| Type B information and resolution models | [Chapter 4](docs/chapters/04_type_b_and_resolution.md) |
| Budgets and nonlinear counterexamples | [Chapter 5](docs/chapters/05_budgets_and_nonlinearity.md) |
| Calibration and traceability | [Chapter 6](docs/chapters/06_calibration_and_traceability.md) |
| Comparisons and coverage | [Chapter 7](docs/chapters/07_comparison_and_coverage.md) |
| Reporting and reproducible reuse | [Chapter 8](docs/chapters/08_reporting_and_reuse.md) |

## Reproduce the examples

Python 3.10 or newer, from this source directory:

```powershell
py -3 tools/content_casebook.py
py -3 tools/casebook.py
py -3 tools/check_content.py
py -3 -m unittest discover -s tests -v
```

The optional `tools/numerical_oracle.py` uses NumPy for a separate numerical comparison. Shared-reference tests require the companion Forge wheel or its `src` directory on `PYTHONPATH`. Without Forge those tests explicitly skip; the complete workspace runner supplies it.

```powershell
py -3 -m measurement_atlas reference "inverse linear calibration" --max-bytes 32768
```

This command uses the retained Forge runtime. No new search or Bitwork implementation was added. The numerical core remains unchanged from v0.4.0, including its repaired covariance validator. It accepts caller-supplied units/models, not arbitrary automatic unit conversions or nonlinear solvers.

## Reusable records and tools

`atlas_manifest.json` and `data/` implement the common contract. `reference/` duplicates those record collections for inspection. `measurement_atlas/resources/common/` contains the portable single-node registry. Forge bundles identical current Measurement collections. `history/v0.4.0/` preserves the earlier corpus. Whole-record revisions change when the curated source package changes; older context must be rebuilt rather than silently retargeted.

`templates/` contains measurement-plan, uncertainty-budget, calibration-review and result-report aids. They are unfilled review documents, not certificates. `evaluations/content_review_questions.json` is an authored answer rubric; it has not been executed with an AI or used as an independent held-out benchmark.

## Current work order

**Deepen Measurement content before returning to navigation.** Finish scoped source review, challenging worked cases and real-data reproduction while keeping the common setup intact. Navigation, Bitwork/AI evaluation and platform gates remain open, not waived. Measurement remains active until meaningful v1 acceptance; no new scientific domain is started by this edition.

This is not a calibration laboratory, exhaustive encyclopedia, independently reviewed reference or certified measurement service. No experimental measurements were added and no improvement in AI answer quality or research cost was measured.
