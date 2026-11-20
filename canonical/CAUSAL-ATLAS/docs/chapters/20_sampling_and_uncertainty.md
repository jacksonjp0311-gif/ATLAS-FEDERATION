# 20. Estimation uncertainty is not causal identification

Statistical precision and causal identification answer different questions. A confidence interval describes variability of an estimator under a sampling and model framework; it does not establish that its target is a causal contrast, that an intervention is well defined, or that confounding has been removed. Conversely, a validly randomized intervention can still have a very imprecise estimate when samples are small or outcomes are noisy.

## Independent binary samples

For independent samples with binary outcomes, a basic descriptive risk difference is p1−p0. An introductory large-sample estimated variance is p1(1−p1)/n1+p0(1−p0)/n0. The tool `binomial-interval` applies a named normal quantile to this standard error. It requires two integer count groups, at least 30 observations per arm and non-extreme proportions; even with these guards, Wald intervals can have poor coverage, particularly near boundaries or when the independence assumptions fail. The package does not claim this method is universally recommended.

For a constructed case with 60 successes in 100 control observations and 75 in 100 treated observations, the observed difference is 0.15 and an approximate nominal 95% interval is about [0.0219, 0.2781]. This is a **descriptive independent-binomial calculation**, not a randomized experiment or causal effect. It also is not an interval for any of the observational Berkeley effects, which require an appropriate data and design analysis.

## Why generic standard errors fail

A matched-pair design, a cluster-randomized trial, a repeated-measures panel and an event study have different dependence structures. Treating all observations as independent under cluster assignment may substantially understate uncertainty. Estimators with nuisance models can require influence-function or resampling methods; nonregular settings such as weak instruments or cutoff discontinuities may need specialized inference. Large sample size does not fix bad measurement, missing outcomes, flawed identification or model extrapolation.

In difference-in-differences, standard errors must respect the level of treatment assignment and serial correlation. In longitudinal IPW, rare histories generate volatile weights. In regression discontinuity, bandwidth choice and model bias matter. In IV, a denominator close to zero can make conventional ratio intervals behave badly. These are *distinct* failures and should not be papered over by one generic “95% CI” command.

## What a citation-ready result requires

For each reported effect and uncertainty estimate, record: target population, treatment contrast, sample selection, design, target estimand, estimator, analytic or bootstrap method, clustering/repeated-measures structure, uncertainty level, degrees of freedom where relevant, multiple testing policy, and unresolved identification assumptions. If these inputs cannot be justified, report the numerical contrast with limitations rather than calling its interval decision-ready.

**References:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook) for separate treatment of random variation and causal assumptions; [Callaway and Sant’Anna 2021](https://doi.org/10.1016/j.jeconom.2020.12.001) for staggered-DiD inference scope. This chapter does not implement their full inference procedures.
