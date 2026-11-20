# Investigation 13. A narrow confidence interval does not prove a cause

**Question:** What extra information is required to turn two independently observed binary outcome proportions into a causal effect claim?

A constructed case reports 60 successes out of 100 observations in one group and 75 out of 100 in another. The difference is +0.15. The large-sample normal interval from the tool is about [0.02185, 0.27815] at a nominal 95% confidence level under **independent binomial sampling** assumptions. The program can compute this accurately even if the treatment assignment process is entirely unknown.

**Run:** `python -m causal_atlas binomial-interval examples/binomial_interval.json`.

An identification analysis asks whether treatment status is exchangeable with unobserved potential outcomes, whether the outcome was measured comparably, and whether the groups are drawn from the intended target. A perfect interval for an observational difference remains an interval for the *association*, not an intervention effect, if confounding or selection cannot be ruled out.

The method also is not a universal confidence interval. It uses a Wald approximation which can have inadequate coverage near 0 or 1 and ignores clustering and pairing. The tool rejects extreme proportions and small groups, but this does not guarantee coverage under arbitrary real data. A factory trial randomized by machine would need an analysis that respects machine-level assignment; 10,000 individual parts from two machines are not 10,000 independent randomization units.

Record which uncertainty sources are counted and which causal uncertainties remain unquantified. An evidence-preserving context package must carry both; it should not flatten a standard error and a causal verdict into one confidence number.

**Reference:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook), treatment of random variability and causal identification; [chapter 20](../chapters/20_sampling_and_uncertainty.md).


## What the interval cannot establish

Even a nominal interval that excludes zero can coexist with severe unmeasured confounding. An observational association can become statistically “significant” with enough data despite being a poor estimate of a causal effect. Conversely, a randomized small experiment with an inconclusive interval does not prove the intervention has no effect. Ask for the original assignment mechanism, baseline comparability, outcome definition, missingness, clustering and chosen sampling units before interpreting the contrast. If key design information is absent, the result should be labeled a descriptive difference with an approximate interval, not a verified treatment effect.
