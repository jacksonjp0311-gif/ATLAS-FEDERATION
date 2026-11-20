# Investigation 09. Is improvement carried through an intermediate variable?

**Question:** If a change affects an intermediate diagnostic and then the outcome, how should “through the mediator” be defined?

A synthetic system assigns exposure A, measures an intermediate M, and later records a binary outcome Y. The mediator probability changes from P(M=1|A=0)=1/5 to P(M=1|A=1)=3/5. The outcome risk under an *intervention* on A and M is stipulated as 0.1, 0.3, 0.2, 0.5 for (A,M)=(0,0),(0,1),(1,0),(1,1).

**Run:** `python -m causal_atlas mediation examples/mediation.json`.

The exact standardization produces a total contrast 6/25, an interventional direct component 3/25 under the baseline mediator distribution, and an interventional indirect component 3/25 at A=1. The decomposition is an algebraic property of the declared probability model, not proof that a measured mediator transmitted a real effect.

For actual evidence, measure the mediator at an appropriate time, identify baseline and exposure-induced mediator–outcome confounders, state a feasible stochastic intervention on its distribution, and determine how shifting that distribution would alter other variables. Distinguish stochastic interventional effects from individual-level natural direct/indirect effects; the latter can impose additional counterfactual independence requirements.

Two plausible causal models can reproduce the same regression but imply different mechanistic interpretations. Data that track only A, M and Y cannot resolve every hidden variable or mediator measurement error. A regulator or engineer should not infer an actionable mechanism simply because the mediator coefficient is nonzero.

**References:** [interventional mediation definitions](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496983/); [chapter 16](../chapters/16_interventional_mediation.md).


## Investigation stopping conditions

Do not attribute the output to a mediator if there is no credible intervention that would alter the mediator as modeled, or if the mediator was recorded after the outcome. Ask whether the exposure itself affects how the mediator is measured, and whether shared hidden factors could affect both mediator and outcome. Prespecify the mediator target distribution before comparing outcomes. If two plausible mechanisms fit the records equally well, report ambiguity and propose an experiment aimed at distinguishing the mechanisms rather than declaring the “indirect effect” a physical pathway.
