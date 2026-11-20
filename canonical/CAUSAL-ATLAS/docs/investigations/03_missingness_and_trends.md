# Investigation C The same observations permit opposite conclusions

**Data origin: original counts and four-mean scenarios; neither is a real study.**

## Part one Missing inspection outcomes

The treated arm has100 total units,60 observed outcomes and48 observed passes. Control has100 total,90 observed and54 passes. The observed-only difference is0.80−0.60=0.20. Without assumptions about unobserved binary outcomes, full-arm differences range from−0.16 to+0.34.

```sh
python -m causal_atlas missing-bounds examples/missing_outcomes.json
```

The algorithm computes these endpoints from successes and missing counts. It is not a95% confidence interval and does not decide that missingness is random. The uncertainty is about unseen outcomes in the supplied counted set. Causal identification, measurement validity and sampling uncertainty remain separate.

The sign becomes positive only under restrictions strong enough to make `-0.06+0.40*r1-0.10*r0 > 0`, where r1 and r0 describe the missing treated and control outcomes. Those probabilities are not estimated here. A reviewer should examine why the allowed range is plausible, not merely select a favorable pair.

## Part two Before–after production comparison

The treated line rises from0.80 to0.90 and control from0.70 to0.75. The four-mean contrast is+0.05. The function `two_period_contrast` accepts an explicit sensitivity value delta for the untreated trend difference. Delta0 gives+0.05; delta0.08 gives−0.03. No observed mean changes between scenarios.

This is a controlled demonstration of an identification assumption. It does not show that delta0.08 is plausible for any actual line. The function has no regression, panel clustering, pretrend test, staggered-adoption method or interval estimator.

## Build a better data request

For the missingness problem, request outcome accounting by arm, time, reason for missingness and baseline strata, plus any independently recovered outcomes. For the trend problem, request assignment rationale, preintervention series, changes in product mix, contemporaneous shocks, inspection revisions and possible spillovers. Each item should be tied to a proposed alternative explanation rather than collected indiscriminately.

More information may narrow the analysis but need not settle it. A source-backed reference must be able to return “not determined under the supplied information.” That is a useful outcome when the alternative is a falsely precise recommendation.

## Deliverable

Use the result-report template to record both the primary descriptive contrast and all declared sensitivity scenarios. Keep unknowns visible. Do not label the bounds as experimental uncertainty, the adjusted DiD scenario as an observed effect, or a successful JSON response as scientific approval.
