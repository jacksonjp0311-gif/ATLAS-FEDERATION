# 16. Mediation: direct and indirect contrasts require their own interventions

An exposure may change an intermediate variable, which may then affect the outcome. Calling the observed treatment association a “direct effect” after controlling for that mediator can be incorrect: the mediator may be affected by exposure, share causes with the outcome, or be related to post-exposure variables that are also affected by exposure. What causal contrast is desired must be stated precisely.

## Stochastic-intervention definition

For a binary exposure A and mediator M, suppose q_a(m) describes a proposed **mediator distribution under exposure a**, and μ(a,m) is an outcome risk under interventions on A and M. Define R(a,q_b)=Σ_m μ(a,m) q_b(m). Then a particularly simple decomposition is:

```
Total   = R(1,q1) − R(0,q0)
Direct  = R(1,q0) − R(0,q0)
Indirect= R(1,q1) − R(1,q0)
Total = Direct + Indirect
```

These are **interventional distribution contrasts** and not individual-level natural direct or indirect effects. Other equally valid mediation decompositions choose different reference distributions and need different interpretations. The local `mediation` tool computes the above identity from supplied mediator probabilities and outcome means; it cannot infer q or μ from observational records or check the cross-world assumptions sometimes required for natural effects.

In the synthetic example, exposure changes P(M=1) from 1/5 to 3/5. Four stated outcome risks generate a total contrast of 6/25, split into a 3/25 direct component and a 3/25 indirect component under the declared decomposition. These numbers are mathematical consequences of supplied probabilities. A statistically stable mediator regression would not, on its own, establish these as mechanisms in the physical system.

## Identification and timing hazards

Even interventional mediation contrasts require conditional exchangeability or other identification conditions for outcome and mediator models in a particular study. Post-treatment mediator-outcome confounders affected by exposure require careful definitions and methods; this two-variable tool has no such confounder. Distinguish exposure-induced intermediate causes, baseline confounders, competing pathways, multiple mediators, measurement error and downstream selection. Natural effects can require conditions involving combinations of counterfactuals; they are not automatically identified when an interventional contrast is calculable.

A practical mediation protocol should state the exposure strategy, mediator measurement time, feasible mediator intervention, outcome window, baseline covariates, exposure-induced confounders, choice of direct/indirect definition and what intervention on the mediator would actually mean. If the mediator is only a proxy, label it a proxy. If intervening on a mediator would change other downstream variables, make that restriction explicit.

**Source scope:** [Nguyen et al., *Clarifying causal mediation analysis for the applied researcher*](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496983/), interventional-effect definitions; [Díaz et al., stochastic interventions](https://pmc.ncbi.nlm.nih.gov/articles/PMC10345989/), overview. This chapter paraphrases the accessible discussions rather than mirroring their papers. The tool addresses a narrow static binary model only.
