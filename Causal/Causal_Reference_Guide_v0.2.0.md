# Causal Atlas reference guide 0.2.0

A practical reference for moving from a causal question to an explicit design, calculation and appropriately limited conclusion. The eight chapters below contain original explanations and worked reasoning; bounded literature capsules retain exact inspected source portions. The standalone software does not fit nuisance models, authenticate a causal design or calculate sample confidence intervals.

## Read in investigation order

| Chapter | The question it helps answer |
|---|---|
| [1 Question and design](chapters/01_question_and_design.md) | What intervention, target population, outcome and timeline are we comparing? |
| [2 Identification and graphs](chapters/02_identification_and_graphs.md) | Under what assumptions could observed information answer that question? |
| [3 Weighting and diagnostics](chapters/03_weighting_and_diagnostics.md) | What do the weighting conventions calculate, and what can diagnostics establish? |
| [4 Augmented estimation](chapters/04_augmented_estimation.md) | Why can either correct working component remove a bias, and when does that fail? |
| [5 Missingness and sensitivity](chapters/05_missingness_and_sensitivity.md) | Can unobserved outcomes reverse the conclusion? |
| [6 Design extensions](chapters/06_design_extensions.md) | What assumptions are hidden in a before–after comparison, and where do current tools stop? |
| [7 Uncertainty and reporting](chapters/07_uncertainty_and_reporting.md) | How should calculations, assumptions and unresolved questions be communicated? |
| [8 Evidence and reuse](chapters/08_evidence_and_reuse.md) | How can a human or AI reuse this material without inflating its evidence status? |

## Investigations, not just definitions

[Process change and job mix](investigations/01_process_change.md) · [Deliberate model failure](investigations/02_model_failure.md) · [Missing outcomes and trend assumptions](investigations/03_missingness_and_trends.md).

Run `python -m causal_atlas investigations` for12 computed development checks. They supplement, not replace, the [five original synthetic cases](CASEBOOK.md). All numerical examples in this edition are constructed. None is the user's actual workplace data.

## Build a defensible study record

[Target study](templates/TARGET_STUDY.md) · [Assumption ledger](templates/ASSUMPTION_LEDGER.md) · [Analysis plan](templates/ANALYSIS_PLAN.md) · [Result report](templates/RESULT_REPORT.md).

These forms are blank by design. They do not simulate a review or invent missing observations.

## Evidence and scope

[Source register](SOURCE_REGISTER.md) · [Coverage matrix](COVERAGE_MATRIX.md) · [Estimator contract](ESTIMATOR_CONTRACT.md) · [Authored review questions](../evaluations/depth_review_v0.2.0.json) · [Validation](VALIDATION.md).

The node has38 bounded literature capsules,19 authored method/example/protocol records and16 source cards. Those73 objects are not73 independently validated findings. Every old record is preserved with its exact revision; new source checks are assistant checks of the named portions. No whole book or external dataset is represented as fully audited.
