# Investigation 5: the jump is real in the table, but what caused it?

## Define a boundary investigation

Imagine a program assigned at a prespecified score threshold. The question concerns the effect at that threshold, not a global average for all cases. This investigation constructs a score cutoff of zero and two outcome functions: `1+2x` below the cutoff and `6-x` at or above it. The slopes differ, but the right and left boundary values are 6 and 1. The jump is exactly five.

Use scores −3, −2, −1, 0, 1, 2 and 3. Their outcomes are −5, −3, −1, 6, 5, 4 and 3. These are arbitrary continuous response units, not binary outcomes or measurements. A triangular window of width four includes all rows with positive kernel weights. Separate local weighted lines recover the boundary intercepts exactly. The zero residual in this construction is a property of the stipulated piecewise-linear functions.

## Compare indistinguishable explanations

World A attributes the outcome jump to the intervention of interest. World B gives that intervention zero effect but applies an additional policy at exactly the same threshold; the additional policy causes the jump. The same observations, score, cutoff and intervention-assignment indicator appear in both worlds.

The local-line estimator returns five in both worlds because it receives the same data. That is not a software defect. It demonstrates why evidence excluding coincident changes belongs to the causal design rather than the curve-fitting routine. Infinite precision in the fit cannot distinguish observationally identical mechanisms.

For a real maintenance policy, collect operating procedures, rollout dates, threshold exceptions, changes in equipment allocation and outcome-recording rules. The relevant check is not “the curve looks smooth”; it is whether the alternative outcome pathway is excluded or explicitly part of the target intervention. A bundled-policy effect can be a legitimate target, but it should be named as such rather than assigned entirely to one component.

## Allow imperfect receipt

The fuzzy case places ten synthetic units at each score. Two take the intervention below the cutoff and seven take it above. Their response is defined as `2+x/10+3d`. The fitted outcome jump is 1.5 and the fitted uptake jump is 0.5. The ratio is three, matching the specified receipt effect.

If uptake is changed to two of ten on both sides, the denominator vanishes and the ratio remains unresolved. The program does not choose another outcome, bandwidth or threshold to recover a finite answer. It preserves the first-stage failure and the original inputs.

## Read the diagnostic output

The point calculator reports intercepts, side-specific slopes, row counts, distinct score counts, omitted IDs, nearest-score gaps and equivalent weights. These allow another implementation to reproduce the arithmetic. It does not produce confidence intervals, select an optimal window, test density manipulation, discover a causal graph, or certify the policy assignment.

Run `python -m causal_atlas rd examples/sharp_rd.json` and `python -m causal_atlas fuzzy-rd examples/fuzzy_rd.json`. Read the unchanged common reference runtime's context alongside the numerical output; neither replaces the other. The [threshold review template](../templates/RD_DESIGN_REVIEW.md) prompts the missing design evidence, and [Chapter 11](../chapters/11_regression_discontinuity.md) derives the exact estimator. The result is useful computational groundwork, not an empirical effect estimate.
