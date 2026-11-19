# Causal Atlas reference guide 0.3.0

A practical reference for moving from a causal question to an explicit design, calculation and appropriately limited conclusion. The twelve chapters below contain original explanations and worked reasoning; bounded literature capsules retain exact inspected source portions. The standalone tools do not fit nuisance models, authenticate a causal design or calculate sampling confidence intervals. New local linear fits estimate boundary points only, with an explicit bandwidth and kernel.

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
| [9 Instrumental variables](chapters/09_instrumental_variables.md) | What effect can a randomized offer identify when receipt differs from assignment? |
| [10 IV failure and sensitivity](chapters/10_iv_failures_and_sensitivity.md) | How do exclusion failures, defiers and small treatment changes alter the ratio? |
| [11 Regression discontinuity](chapters/11_regression_discontinuity.md) | What does a cutoff identify, and what do separate local lines calculate? |
| [12 RD design and reuse](chapters/12_rd_validation_and_reuse.md) | How should support, bandwidth sensitivity, co-interventions and inference limits travel with a result? |

## Investigations, not just definitions

[Process change and job mix](investigations/01_process_change.md) · [Deliberate model failure](investigations/02_model_failure.md) · [Missing outcomes and trend assumptions](investigations/03_missingness_and_trends.md).

[Training offer and local effects](investigations/04_training_offer.md) · [Threshold policy and alternative explanations](investigations/05_threshold_policy.md) · [Support and sensitivity audit](investigations/06_support_and_sensitivity.md).

Run `python -m causal_atlas quasi-casebook` for twelve new exact IV/RD checks. Run `python -m causal_atlas investigations` for 12 computed development checks. They supplement, not replace, the [five original synthetic cases](CASEBOOK.md). All numerical examples in this edition are constructed. None is the user's actual workplace data.

## Build a defensible study record

[Target study](templates/TARGET_STUDY.md) · [Assumption ledger](templates/ASSUMPTION_LEDGER.md) · [Analysis plan](templates/ANALYSIS_PLAN.md) · [Result report](templates/RESULT_REPORT.md).

[IV design review](templates/IV_DESIGN_REVIEW.md) · [RD design review](templates/RD_DESIGN_REVIEW.md).

These forms are blank by design. They do not simulate a review or invent missing observations.

## Evidence and scope

[Source register](SOURCE_REGISTER.md) · [Coverage matrix](COVERAGE_MATRIX.md) · [Estimator contract](ESTIMATOR_CONTRACT.md) · [Authored review questions](../evaluations/depth_review_v0.2.0.json) · [Validation](VALIDATION.md).

The node contains **105 records**: 52 bounded literature capsules, 30 authored derivation/example/protocol records and 23 source cards. All 73 prior record revisions remain intact. The 16 new [IV/RD review questions](../evaluations/quasi_review_v0.3.0.json) supplement the earlier 32, for 48 visible development questions. No unseen or independent model evaluation is claimed.

Seven new source cards distinguish selected PDF portions from indexed abstracts. Access failures and inspection limits are retained in [the source inspection receipt](../evidence/source_inspection_v0.3.0.json). They are not represented as complete-paper audits. No whole publication or new participant dataset is mirrored.
