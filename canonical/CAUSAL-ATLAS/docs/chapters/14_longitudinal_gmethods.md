# 14. Longitudinal g-methods and treatment-confounder feedback

At two or more decision times, a variable may predict future treatment and outcome while itself being changed by earlier treatment. A baseline-only model can leave confounding, but naïvely conditioning on the post-treatment variable can block parts of the earlier treatment effect or create collider bias. Longitudinal g-methods address this structure under explicit assumptions. They do not eliminate the need for information about the treatment-assignment mechanism or the outcome process.

## Two-decision mathematical reference

Let L0 be baseline, A0 the first treatment, L1 the intermediate state, A1 the second treatment, and Y the outcome. For a **static strategy** (a0,a1), a finite longitudinal g-formula is:

```
R(a0,a1) = Σ_l0 P(l0) Σ_l1 P(l1 | l0,a0) E[Y | l0,a0,l1,a1]
```

As an *identification formula from observational data*, this requires sequential exchangeability at both decisions, consistency, positivity, and adequate models or nonparametric empirical support. The local `longitudinal` command does not fit these ingredients. Instead, it accepts them as fully stipulated probabilities, enumerates binary L1, and reports the resulting four strategy risks and requested contrast.

In the synthetic worked example, early treatment changes the probability of an intermediate high-risk state from 1/5 to 3/5, while both treatment decisions also change the outcome probabilities. The computed (1,1) versus (0,0) risk difference is 17/50. This is a property of the declared model, not an estimate from factory or patient data.

## Weighting and g-estimation

Marginal structural models may use inverse probabilities of observed treatment histories, multiplying appropriate treatment and censoring factors across time. Those weights require models and positivity for each history. Rare treatment sequences can produce extreme weights, reducing precision. Report support, distribution of weights, rules for truncation, and sensitivity of results to those rules. Clustering and repeated measurement require suitable uncertainty estimates. Longitudinal g-estimation can target structural nested models, but it has a different parameterization and is not interchangeable with a simple weighted average.

## Common failures

Do not adjust for every post-treatment measurement just because it predicts outcome. Conversely, do not assume two treatment decisions are independent merely because the first was assigned. No procedure should manufacture data for an unobserved treatment sequence: missing positivity makes that strategy comparison nonidentified in relevant strata without external assumptions. Time-varying censoring may be informative. A stable fitted model is not evidence that all relevant history was captured.

For a real project, preserve the complete measurement timeline, time stamps, strategy definitions, adherence status, censoring reasons, treatment mechanisms, supported histories, and code/version for outcome estimation. Then test whether the assumptions are plausible and whether a negative control or alternative design disagrees.

**Sources:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook), especially the authors' description of Part III and their chapter on treatment-confounder feedback; [Hernán and Robins target-trial article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/), per-protocol and postbaseline sections. The code here implements a bounded finite formula, not a full longitudinal estimator.
