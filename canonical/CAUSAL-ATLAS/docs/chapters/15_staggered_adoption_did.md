# 15. Staggered-adoption difference-in-differences: group-time comparisons

A policy may reach different groups in different years. A single treated-versus-control line can conceal effects that vary with treatment timing or exposure duration. Two-way fixed-effects coefficients can become difficult to interpret under heterogeneous dynamic effects. A useful reference identifies cohort-specific effects for a cohort first treated in period g and an outcome observed at period t, then makes the comparison group explicit.

## Declare the target before aggregating

A group-time target ATT(g,t) is the average effect at period t for members whose first treatment was period g, normally for t ≥ g. A basic group-time difference in changes is:

```
D(g,t) = [Ybar_g,t − Ybar_g,g−1] − [Ybar_C,t − Ybar_C,g−1]
```

Interpretation as ATT(g,t) requires no anticipation, a defensible untreated counterfactual trend for group g represented by C, consistency, valid measurement and appropriate selection/censoring assumptions. The local `staggered-did` tool computes the arithmetic from user-supplied group-period means, **not** a causal ATT estimator with covariate adjustment or sampling inference.

Two comparison policies are exposed. `never` uses only never-treated groups. `not_yet` includes groups first treated after the comparison period (as well as never-treated groups), if they have appropriate untreated outcomes. Groups already treated by period t are excluded from the control set. If no eligible comparison exists, the result contains an explicit unavailable entry rather than a constructed effect.

## A fully specified teaching panel

Periods are 0, 1, and 2. Never-treated means are 0,1,2. The early cohort begins in period 1 and records 0,3,5. The late cohort begins in period 2 and records 1,2,6. Under no anticipation and a stipulated untreated +1 trend, the early period-1 contrast is +2, early period-2 is +3, and late period-2 is +3. The tool reports all three with their baseline period and comparison-group IDs. The assumptions were authored to fit the values; these are not observed effects.

## What makes applied estimation harder

A real study should verify who was exposed when, whether treatment is absorbing or reversible, the policy's eligibility rules, survey weights and attrition, repeated outcomes, cluster boundaries and common shocks. Parallel trends for an untreated outcome is not testable from a post-treatment trajectory alone. Preperiod checks can reveal certain contradictions but cannot prove future counterfactual trends. Cohort composition may change over time. Anticipatory effects require shifting eligibility and baseline definitions.

For uncertainty, account for sampling and cluster dependence; consider simultaneous confidence bands when many groups and horizons are compared. Preserve aggregation weights and do not compress heterogeneous cohort effects into one number without stating whose average it is. A policy result should carry sensitivity to trend differences, group selection, timing definitions and measurement units.

**Source scope:** Callaway and Sant'Anna (2021), *Difference-in-Differences with Multiple Time Periods*, [journal abstract](https://doi.org/10.1016/j.jeconom.2020.12.001); [official `did` package method documentation](https://search.r-project.org/CRAN/refmans/did/help/att_gt.html) for comparison-group options. This Atlas tool is a simpler descriptive teaching comparison, not a reproduction of their estimator.
