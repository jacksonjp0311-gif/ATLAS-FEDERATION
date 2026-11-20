# 24. Method-selection directory and minimum evidence requirements

The first method to select is often **a better design**, not a more complicated estimator. This directory gives an investigator questions to ask before invoking any numeric tool. It does not substitute for a domain expert, formal protocol or independent review.

| Question | Possible analytic route | Required design evidence | Common failure |
|---|---|---|---|
| Well-defined randomized point intervention | Randomization-aware comparison; attrition and compliance audit | Assignment, eligibility, protocol, outcomes, follow-up, sample units | Excluding early failures or ignoring cluster assignment |
| Observational point exposure, baseline confounders | Standardization, weighting, outcome regression, AIPW | Measured sufficient confounders, overlap, correct time order | Unmeasured causes or misspecified nuisance models |
| Sustained treatment with affected time-varying covariates | Longitudinal g-formula, IPW MSM, appropriate g-estimation | Treatment/measurement histories, sequential assumptions, positivity | Conditioning on exposure-induced confounders naïvely |
| Policy adopted at different times | Group-time DiD / event-study designs | Cohorts, pretreatment periods, credible comparisons, no anticipation | Previously treated groups used as controls under heterogeneity |
| Threshold assignment | Sharp/fuzzy RD designs | Exact running variable, cutoff, no sorting/cointerventions, support | Confusing a local jump with a global causal effect |
| Offer influences uptake | Instrumental variables/local effect | Relevant instrument, exclusion, independence, monotonicity, first stage | Weak instrument, direct effect, wrong target |
| Explain a pathway | Interventional mediation with explicit target | Exposure, mediator, outcome timing, mediator-outcome confounders | Naïve mediator adjustment |
| Neighbor/cluster effects | Interference-aware design | Cluster or network boundaries, assignment mechanism, exposure map | Assuming no interference |
| Transfer to new population | Stratum standardization or formal transportability analysis | Source causal effects, target modifiers and positive support | Ignoring effect modification or new intervention version |
| Missing outcomes | Bounds or censoring/selection model | Full eligible count, missingness mechanism and data origin | Complete-case or missing-as-zero bias |
| Descriptive historical table | Stratified rates and standardization | Authentic counted data, documented target weights | Calling observed disparity a causal intervention effect |

## One-question interrogation sequence

1. Define the intervention, comparison, outcomes, target population and baseline time.
2. Sketch variables and their timing; list plausible confounders, mediators, colliders, and measurement channels.
3. Ask whether a randomized or natural experiment is feasible or whether the existing data justify a specified identification strategy.
4. Inspect treatment support and missingness. If an estimand is not identified, record why before fitting models.
5. Choose an estimator and its sampling-inference procedure under the *actual* data structure. Keep estimation precision separate from identification.
6. Compare alternative assumptions and negative controls where defensible.
7. Write a result with sources, data version, population, uncertainty, limitations and a falsification agenda.

A result cannot be upgraded from descriptive to causal by improving the fit or adding decimal places. The reference must allow a final answer of “the available data do not identify this effect.”

**Source navigation:** Hernán and Robins, [*Causal Inference: What If*](https://miguelhernan.org/whatifbook); Callaway and Sant'Anna, [staggered DiD journal record](https://doi.org/10.1016/j.jeconom.2020.12.001); Hudgens/Halloran, [interference](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/); Bareinboim/Pearl, [transportability](https://proceedings.mlr.press/v31/bareinboim13a.html); Bickel et al. via [R UCBAdmissions documentation](https://cloud.r-project.org/doc/manuals/r-release/packages/datasets/refman/datasets.html).
