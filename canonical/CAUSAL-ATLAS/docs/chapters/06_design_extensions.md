# 6 Before and after is not automatically a causal design

The node's main implemented estimators concern a binary point exposure. This chapter adds a bounded two-period arithmetic investigation and distinguishes it from methods not implemented. It is not a replacement for a full panel-data, instrumental-variable or longitudinal analysis.

## A four-mean contrast

Suppose a treated production line changes from0.80 to0.90 pass probability, while a comparison line changes from0.70 to0.75. The before–after difference in the treated line is+0.10. Subtracting the comparison-line change produces

`D = (0.90-0.80) - (0.75-0.70) = 0.05`.

That arithmetic is observable from the four means. To interpret D as the treated line's causal effect, assumptions must connect the comparison line's change with what would have happened to the treated line without the intervention. The implemented function does not validate that connection.

## Put the unobserved trend into the equation

Define delta as the untreated treated-line trend minus the comparison line's untreated trend. Under the rest of the stipulated design, the causal contrast is `D-delta`. With delta0, it is+0.05. With delta+0.08, it is−0.03. Both scenarios have exactly the same four observed means. They disagree about the untreated counterfactual, which is not observed for the treated line after its intervention.

This original sensitivity calculation shows what the identifying assumption does. It does not estimate delta or give it a probability distribution. A plausible range needs substantive evidence about production mix, measurement changes, common shocks, spillovers, selection and timing. More preperiod observations may help examine a design, but a visually flat past difference does not logically determine future untreated differences.

The inspected multi-period difference-in-differences paper states distinct comparison-group, anticipation, overlap and parallel-trend conditions ([Callaway and Sant'Anna, version4, §2.3–2.4](https://arxiv.org/html/1803.09015v4)). The Atlas stores those bounded source claims; the local four-mean function does not reproduce that paper's estimators or inference.

## Why a staggered rollout needs another method

If lines adopt a setting at different times, a unit used as a comparison may already be treated. The treatment effect can also vary by adoption cohort or elapsed time. Collapsing every treated observation into one indicator can change what is being compared. This reference identifies the issue and keeps the multi-period source as an entry point. It does not label a two-period arithmetic result as a validated staggered-adoption analysis.

A future node increment should specify the cohort-time targets, admissible comparison observations, aggregation weights, anticipation window and uncertainty procedure before adding an estimator. The current coverage matrix lists this as limited reference depth, not an implemented capability.

## Time-varying treatment is not repeated point treatment

A variable measured after an initial treatment may affect both later treatment and outcome while itself being affected by the earlier treatment. Treating each row as a new independent person and applying the point-treatment function ignores the history. The inspected weighting source explicitly concerns such histories ([Cole and Hernán2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2732954/)). The present individual-row interface rejects duplicate IDs and makes no longitudinal inference claim.

## What remains deliberately unfinished

Instrumental variables, regression discontinuity, mediation, censoring/survival methods, interference and transportability require their own identification definitions, diagnostics, inference and source review. They are not inferred by a graph search failing to find a back-door set. They remain gaps rather than being represented by a method name and a false completion flag.

For an analyst, the immediate useful action is to describe why ordinary baseline adjustment is inadequate and identify what additional design information is available. The Atlas can preserve that unresolved question without pretending the problem has been solved.

**Related records:** `did-assumptions`, `staggered-comparison`, `did-trend-sensitivity`, `longitudinal-warning`, `scope-maturity`.
