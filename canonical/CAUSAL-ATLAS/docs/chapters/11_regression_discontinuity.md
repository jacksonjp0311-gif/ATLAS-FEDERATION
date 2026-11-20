# 11 Regression discontinuity: learn at a boundary, not everywhere

## Identify an actual rule

A score threshold can create a useful comparison only when it belongs to the assignment mechanism. Suppose a maintenance program is assigned when an inspection score reaches 50. Define the score as it existed before assignment, the threshold, the eligible equipment, the intervention and a fixed outcome window. Retain any exceptions, rerating, rounding, overrides or other changes at the same cutoff. A visually convenient breakpoint chosen after seeing outcomes is not the documented rule in this proposal.

Cattaneo and Titiunik distinguish continuity-based and local-randomization interpretations, as well as sharp and fuzzy designs. The inspected source portions are §2.1–2.2, pp. 824–828. See [CT2022](../SOURCE_REGISTER.md#ct2022). This Atlas's implemented calculation is a local-line point estimate; it does not establish either identification framework from a dataset.

## Continuity gives a target at the cutoff

Let `X` be the running score and `c` the threshold. With sharp receipt `D=1[X>=c]`, the observed right-side limit concerns treated outcomes and the left-side limit concerns untreated outcomes. A continuity argument compares their limits at the same value `c`, not their means over the entire treated and untreated populations. Its target is a treatment effect at that boundary under the design's assumptions.

For an original example, take the untreated response near zero to be `1+2x` and the treated response to be `6-x`. The boundary values are 1 and 6, so the cutoff effect is 5. Farther away, their difference changes with `x`. Claiming a constant benefit of five everywhere would add an assumption not present in these curves.

The separate local-randomization framework treats assignment within a declared neighborhood as having a justified randomization structure. It is not obtained merely by using a small bandwidth. The source's finite-window assumptions and the limiting continuity assumptions answer related but different questions. This release does not implement randomization inference or window selection.

## The implemented weighted-line calculation

For each side use `u=(x-c)/h` with a caller-selected positive bandwidth `h`. Include rows satisfying `abs(x-c)<h`; assign `x=c` to the right. Choose either uniform weights or triangular weights `w=1-|u|`. Fit an intercept and slope separately on each side by minimizing the weighted sum of squared residuals.

Define `S0=sum(w)`, `S1=sum(w*u)`, `S2=sum(w*u*u)`, `T0=sum(w*y)` and `T1=sum(w*u*y)`. With `Delta=S0*S2-S1*S1`, the fitted boundary intercept is

`a=(S2*T0-S1*T1)/Delta`.

The scaled-coordinate slope is `(S0*T1-S1*T0)/Delta`; divide by `h` for the slope per score unit. The reported jump is `a_right-a_left`. This two-by-two weighted-line solution is an original explicit derivation of the implemented arithmetic. Fraction arithmetic avoids roundoff for the bounded input class; it does not eliminate scientific uncertainty.

The equivalent weight on observation `i` in the intercept is `w_i*(S2-S1*u_i)/Delta`. These weights sum to one and their weighted score sum is zero. Some can be negative because the boundary intercept is an extrapolated local-line value. The tool reports them rather than silently clipping them. Kernel-weight effective sample size is a concentration diagnostic, not the number of independent causal observations.

The local-polynomial construction and bandwidth/inference distinction are described in the primary [CCT2014](../SOURCE_REGISTER.md#cct2014) paper, pp. 2296–2297. Its bias-corrected uncertainty procedure is not implemented here. Returning a plausible line fit is not equivalent to delivering a defensible confidence interval.

## Fuzzy uptake changes the interpretation again

When crossing the threshold changes treatment receipt from a probability below one to another probability, compute both an outcome jump and a treatment-probability jump. Their ratio is a local Wald-type quantity. A local complier interpretation needs additional assumptions, including an appropriate exclusion condition and monotonicity, beyond calculating both jumps.

The authored case creates seven score levels and ten constructed records per level. Two of ten receive treatment below the threshold, and seven of ten above it. With `Y=2+x/10+3D`, the outcome jump is 1.5 and the treatment jump is 0.5, giving a ratio of 3. This is an exactly specified teaching population. It does not prove that an empirical discontinuity satisfies the mechanism.

`fuzzy_local_ratio` uses the same rows, bandwidth and kernel for both fits. It reports unsupported or tiny first stages according to an explicit guard. Local linear treatment-probability predictions can leave [0,1]; they are flagged, not clipped. The function never reports a confidence interval or automatically labels the ratio a validated local average effect.

## A complete output includes its boundary

Save cutoff units, score timing, bandwidth, kernel, counts, distinct score values, nearest observed score on each side, excluded row IDs and equivalent weights. State whether the target is assignment or receipt, and whether the result is a point summary or justified causal finding. Distinguish the observed data range from the exact boundary. Many repeated scores cannot replace missing score support.

Read the [threshold investigation](../investigations/05_threshold_policy.md) and [validation chapter](12_rd_validation_and_reuse.md) before making a substantive claim.
