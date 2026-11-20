# 7 Report uncertainty without hiding identification assumptions

Every calculation in this checkpoint is reproducible, but reproducibility alone does not turn it into an empirical causal finding. A report should separate what was observed, what was assumed, what was computed, and which claim that supports.

## Three distinct uncertainty questions

First, sampling uncertainty concerns variability from observing a finite sample under a declared sampling or assignment design. Second, nuisance-model uncertainty concerns the fitted predictions or scores used by an estimator. Third, identification uncertainty concerns assumptions connecting an observed-data function to the causal target. A confidence interval for the first two does not automatically cover violations of the third.

The current sample calculator returns no confidence interval. This is intentional: the file does not establish independent sampling, clustering, prediction-training provenance or a justified variance estimator. Adding a familiar standard-error formula would conceal rather than resolve those missing design inputs. This release is useful as an exact calculation and review tool, not a complete inferential package.

## Use the exact output labels

`computed_conditional_on_inputs` means a computation was performed with the supplied rows. It does not mean treatment was randomized. `synthetic_stipulated_population` means the generating distribution was authored and known. `bounded_not_identified` means an interval of possible values follows from supplied counts, not that a repeated-sampling confidence level was calculated.

The old graph outputs also retain their boundaries: no back-door set found is scoped to the supplied graph and implemented criterion. A graph-validation pass is not an authentication of the causal graph. When preparing model context, preserve these labels rather than shortening them to “verified effect.”

## A report that can be challenged

An original study report should state the target population and intervention; eligibility and follow-up; data origin and exclusions; outcome definition and units; plausible causal structure; the precise identification argument; estimator and normalization; nuisance-model provenance; overlap and balance diagnostics; missingness handling; primary and sensitivity results; and unresolved alternatives. The blank [result report](../templates/RESULT_REPORT.md) makes these fields explicit.

Write the main conclusion at the strength supported by the record. “The standardized difference in the declared target is0.10 under the supplied strata and assumptions” is different from “the process improves every line by10%.” The first may be a computational description; the second adds causal transport and effect-homogeneity claims that the numbers do not establish. For binary probabilities, distinguish a0.10 difference, ten percentage points, a relative risk and a percent change. Do not interchange them.

## Preserve disagreements among analyses

In the synthetic process investigation, crude and adjusted results differ in sign for a documented reason: the job mix is deliberately unbalanced. In the model-failure investigation, two wrong working models produce an augmented result−0.26 even though the stipulated truth is+0.10. Neither disagreement should be discarded. The first illustrates a successful correction under assumptions; the second illustrates that method sophistication does not guarantee success.

An actual analyst does not have access to the true generating means. Agreement between estimators can reflect shared assumptions, while disagreement can reflect finite-sample noise, target changes, normalization, misspecification or bugs. A frozen analysis plan helps avoid choosing a result simply because it supports the desired narrative. Changing the plan is allowed, but it should create a dated exploratory branch rather than silently rewrite the primary question.

## What the test suite establishes

The exact-fraction tests check known answers, invalid inputs and invariances. The separate numerical comparison checks another arithmetic implementation on generated cases. The retained graph comparison checks algorithmic agreement. All are authored development evidence. None is an independently authored held-out AI benchmark, peer review, real-world intervention or calibration of causal confidence.

The proposed learning rubric asks a consumer to distinguish these objects, reconstruct calculations and request missing information. It is development material and can be inspected with the answers. It must not later be described as an unseen benchmark.

**Related records:** `sample-versus-population`, `uncertainty-ledger`, `frozen-analysis-plan`, `conflicting-method-results`, `scope-maturity`.
