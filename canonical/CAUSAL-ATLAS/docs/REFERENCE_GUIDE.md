# Causal Atlas Reference Guide

Version 1.0.0 content edition. Begin with the scientific question and target estimand. The chapter directory includes bounded source provenance and limitations; reading all headings alone is not scientific evidence.

## Core chapters

1. [1 Define the question before choosing an estimator](chapters/01_question_and_design.md)
2. [2 Identify an effect before estimating it](chapters/02_identification_and_graphs.md)
3. [3 Weighting, standardization and what diagnostics can establish](chapters/03_weighting_and_diagnostics.md)
4. [4 Augmented weighting with a derivation and falsification cases](chapters/04_augmented_estimation.md)
5. [5 Missing outcomes and honest sensitivity analysis](chapters/05_missingness_and_sensitivity.md)
6. [6 Before and after is not automatically a causal design](chapters/06_design_extensions.md)
7. [7 Report uncertainty without hiding identification assumptions](chapters/07_uncertainty_and_reporting.md)
8. [8 Build an investigation from evidence, not from an impressive method name](chapters/08_evidence_and_reuse.md)
9. [9 Instrumental variables: distinguish the invitation from the treatment](chapters/09_instrumental_variables.md)
10. [10 Instrumental variables: failures, sensitivity and identification limits](chapters/10_iv_failures_and_sensitivity.md)
11. [11 Regression discontinuity: learn at a boundary, not everywhere](chapters/11_regression_discontinuity.md)
12. [12 Threshold design validation: preserve competing explanations](chapters/12_rd_validation_and_reuse.md)
13. [13. Target trial emulation: define the experiment before analyzing records](chapters/13_target_trial_emulation.md)
14. [14. Longitudinal g-methods and treatment-confounder feedback](chapters/14_longitudinal_gmethods.md)
15. [15. Staggered-adoption difference-in-differences: group-time comparisons](chapters/15_staggered_adoption_did.md)
16. [16. Mediation: direct and indirect contrasts require their own interventions](chapters/16_interventional_mediation.md)
17. [17. Interference and spillovers: another unit's treatment can matter](chapters/17_interference_and_spillovers.md)
18. [18. Transportability: what changes when the target population changes?](chapters/18_transporting_effects.md)
19. [19. An authentic descriptive reproduction: Berkeley admissions in 1973](chapters/19_berkeley_observational_reproduction.md)
20. [20. Estimation uncertainty is not causal identification](chapters/20_sampling_and_uncertainty.md)
21. [21. Negative controls and sensitivity analyses: try to falsify your explanation](chapters/21_negative_controls_and_sensitivity.md)
22. [22. Missingness, measurement error and selection are part of the causal model](chapters/22_measurement_and_selection.md)
23. [23. Evidence-preserving causal knowledge for other AI systems](chapters/23_evidence_governance.md)
24. [24. Method-selection directory and minimum evidence requirements](chapters/24_method_selection_directory.md)

## Investigations

1. [Investigation A A process improves within groups but looks worse overall](investigations/01_process_change.md)
2. [Investigation B Deliberately break the working models](investigations/02_model_failure.md)
3. [Investigation C The same observations permit opposite conclusions](investigations/03_missingness_and_trends.md)
4. [Investigation 4: an offer changes attendance, but whose outcome effect is identified?](investigations/04_training_offer.md)
5. [Investigation 5: the jump is real in the table, but what caused it?](investigations/05_threshold_policy.md)
6. [Investigation 6: sensitivity and unsupported calculations are part of the result](investigations/06_support_and_sensitivity.md)
7. [Investigation 07. A treatment changes the next treatment decision](investigations/07_feedback_over_time.md)
8. [Investigation 08. Different groups adopt a change at different times](investigations/08_staggered_policy.md)
9. [Investigation 09. Is improvement carried through an intermediate variable?](investigations/09_mediation_pathways.md)
10. [Investigation 10. A treatment on one line affects the nominal control](investigations/10_shared_resource_spillovers.md)
11. [Investigation 11. Transfer a result to a different population](investigations/11_transport_to_new_population.md)
12. [Investigation 12. Real historical data can reverse after stratification](investigations/12_berkeley_admissions.md)
13. [Investigation 13. A narrow confidence interval does not prove a cause](investigations/13_sampling_vs_identification.md)

## Study templates

- [Analysis Plan](templates/ANALYSIS_PLAN.md)
- [Assumption Ledger](templates/ASSUMPTION_LEDGER.md)
- [Iv Design Review](templates/IV_DESIGN_REVIEW.md)
- [Rd Design Review](templates/RD_DESIGN_REVIEW.md)
- [Result Report](templates/RESULT_REPORT.md)
- [Target Study](templates/TARGET_STUDY.md)

## Retrieval and status

Each machine record has an immutable revision, bounded source locator or gap, assumptions and limitations. A source-linked passage is not independent human review. The local tools check declared mathematical models, not a real causal design. [Coverage and final release gates](COVERAGE_MATRIX.md).
