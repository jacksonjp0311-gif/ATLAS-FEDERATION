# Investigation 08. Different groups adopt a change at different times

**Question:** Does a policy change cause better outcomes when adoption is staggered and the comparison group changes over time?

Consider three synthetic groups observed in periods 0, 1, and 2. One is never treated, one begins in period 1, and one begins in period 2. Observed group means are:

| Group | First treated | Period 0 | Period 1 | Period 2 |
|---|---:|---:|---:|---:|
| Never | — | 0 | 1 | 2 |
| Early | 1 | 0 | 3 | 5 |
| Late | 2 | 1 | 2 | 6 |

Assume in this constructed world that untreated outcomes would each rise by one per period. With `not_yet` controls, the early cohort at period 1 can compare with both the never and late groups; at period 2, late is already treated and must not be a control. The calculated change differences are +2, +3, and +3 for early t1, early t2 and late t2 respectively. These are not real policy effects; the assumptions were built into the example.

**Run:** `python -m causal_atlas staggered-did examples/staggered_did.json`.

The tool reports comparison IDs and baseline periods, not merely a pooled coefficient. If every available comparison group is already treated, it returns an unavailable result. An analyst cannot treat a group as an untreated comparison simply because it received treatment in a different year.

For real data, require first-treatment dates, eligible cohort definitions, preperiod outcomes, evidence about anticipation, missingness, differential shocks, and support for credible comparisons. Estimate uncertainty at the level of assignment; if groups are counties or factories, the number of independent assignment units may be much smaller than the number of individual records. A pretrend plot is diagnostic, not proof of future parallel trends.

**References:** [Callaway–Sant’Anna 2021](https://doi.org/10.1016/j.jeconom.2020.12.001) and the [`did` package control-group documentation](https://search.r-project.org/CRAN/refmans/did/help/att_gt.html); [chapter 15](../chapters/15_staggered_adoption_did.md).
