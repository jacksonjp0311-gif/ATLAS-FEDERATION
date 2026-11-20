# 12 Threshold design validation: preserve competing explanations

## Start from the mechanism, then examine the data

A discontinuity in an outcome is evidence of a discontinuity in the observed regression function. Deciding what caused it requires a defensible assignment design. Maintain a dated record of the threshold rule, the scoring procedure, who could influence it, when the score was recorded, and whether another policy changed at the same value. A familiar estimator cannot repair an undocumented intervention.

A density discontinuity can provide evidence relevant to sorting of the running variable; McCrary's primary paper develops such a test. Only its publisher abstract and bibliographic description were inspected for this release, not its full proof or implementation. See [MC2007](../SOURCE_REGISTER.md#mc2007). We implement no density test. Counting observations in arbitrary bins should not be relabeled as the McCrary procedure.

The practical guide by Imbens and Lemieux is recorded as an implementation reference, with an abstract-only inspection limit for the newly added card. See [IL2007](../SOURCE_REGISTER.md#il2007). The stronger evidence for detailed statements in this module comes from the specifically inspected full-text source portions and our original derivations, not from claiming that an entire guide was reviewed.

## A perfectly fitted jump can still answer the wrong question

Construct observed curves `Y=1+2X` below zero and `Y=6-X` at or above zero. World A assigns the jump to training. World B gives training zero effect but assigns a second intervention at exactly the same threshold and attributes the jump to it. Both worlds produce the same observed `X,Y,D` table when `D` labels training eligibility. The numerical jump is five in either world.

This is an identification counterexample, not a diagnostic failure in line fitting. Another design, separately changing assignment, or substantive evidence excluding the competing pathway is needed to distinguish the explanations. A perfect residual fit and stable estimates across bandwidths cannot supply that missing information.

A data package should therefore contain an explicit coincident-interventions field, with “unknown” allowed. Do not convert an empty checklist into “none exist.” Unresolved mechanisms should appear next to the numerical estimate, not in a footnote dropped during AI context assembly.

## Bandwidth sensitivity is informative but not a proof

Our curved example has a true limiting jump of five. The left untreated curve uses a small quadratic term and the right treated curve a larger one. Fitting separate local lines with triangular weights gives 4.925 at bandwidth 1, 4.775 at bandwidth 2, and approximately 4.3901 at bandwidth 4. The deterministic curvature bias changes with the fitting window. There is no sampling noise in this construction, so none of these deviations can be called a standard error.

The example does not establish that smaller bandwidth is always preferable. In a real sample a smaller window can have fewer independent units, less support, greater sampling variability or no estimable slope. `bandwidth_sensitivity` reports every requested window, including unsupported ones, and never selects the result closest to a preferred answer.

High-order global polynomial fits are criticized by Gelman and Imbens for sensitivity and inferential behavior; the inspected record here is their primary indexed abstract, not a replication of their simulations. See [GI2014](../SOURCE_REGISTER.md#gi2014). Our implementation deliberately remains a local linear calculator rather than growing a generic polynomial-fitting system. That is a bounded engineering choice, not a claim that all possible alternatives are invalid.

## Distinct support and score precision matter

Three rows at score −1 and three at score +1 do not identify two independent intercept-and-slope regressions. More copies at those same values do not resolve that rank deficiency. The tool requires at least three positive-weight rows and two distinct score values on each side. That minimum permits arithmetic; it is not a recommended statistical sample size.

If an instrument rounds scores to whole units, report the gap around the cutoff and how many distinct values exist. Exact rational arithmetic preserves reported values, not the latent unrounded scores. Do not infer density continuity or a shrinking-bandwidth argument merely because the output is numerically exact. The reference explicitly defers dedicated discrete-running-variable methods and clustered inference.

## Falsification asks where a design could fail

Useful checks should be motivated before seeing the preferred outcome result: prespecified baseline covariates, outcomes the intervention should not affect, known administrative breaks, score-generation records and alternative windows. Their interpretation depends on power, multiple testing, measurement quality and the substantive mechanism. A nonsignificant check is not a certification of all assumptions. The validation discussion in [CT2022](../SOURCE_REGISTER.md#ct2022), §4, treats these as indirect checks.

Separate design validity from estimator precision. A narrow sampling interval cannot rule out a second treatment at the cutoff. Conversely, a well-justified design can be too imprecise for a useful conclusion. The current tools leave uncertainty uncomputed rather than reuse ordinary line-fit standard errors as if they were robust RD inference.

## Human and AI handoff

A reusable package must retain the question, cutoff, treatment definition, local target, selected window, omitted rows, method, assumptions, negative findings and missing information. Include a statement that the generated numerical examples are constructed, not measurements. Source passages remain linked to immutable records; our software derivations and test fixtures have a different origin label.

Use the [threshold review template](../templates/RD_DESIGN_REVIEW.md). The next substantive step is a rights-cleared empirical reanalysis with a separately checked assignment story and appropriate inference. No such empirical study is claimed by this edition, and Materials remains queued.
