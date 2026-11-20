# 18. Transportability: what changes when the target population changes?

An average effect estimated in a trial population need not be the average effect in the population facing the decision. If effects vary with age, baseline condition, machine type or environment and these characteristics occur with different frequencies in the target population, averages will differ. The central task is to determine which conditional causal response functions can be carried across populations and which selection mechanisms make that transfer invalid.

## A narrow stratum-standardization identity

Suppose Z is a pre-intervention categorical effect modifier. Under a justified transfer assumption for conditional causal risks μ_a(z), the target effect is:

```
ATE_target = Σ_z P_target(z) [ μ_1,source(z) − μ_0,source(z) ]
```

Every stratum with positive target weight requires source support or an explicit extrapolation model. The local `transport` command requires strictly positive source mass for any positive target-mass stratum, checks both mass distributions sum to one, and computes the source and target contrasts separately. It does not test that source outcome response functions are causal or invariant across settings.

In the constructed example, a source population is three quarters low-risk and one quarter high-risk; the target reverses those proportions. The stratum effects are 0.10 and 0.30. The source average is 0.15; the target average is 0.25. Both numbers can be arithmetically correct. Neither can be applied to an actual institution unless effect modifiers, study conditions, outcomes and intervention versions are comparable.

## Reasons transfer fails

Different intervention versions, outcome measurement, follow-up, exposure support, calendar conditions and unmeasured effect modifiers can make source estimates unsuitable. A selection diagram may formalize which processes differ across settings; a general graphical transportability algorithm is not implemented here. Sampling weights estimated from available covariates do not eliminate unmeasured differences. The presence of a source stratum with observations does not guarantee enough precision or valid conditional causal identification.

Document the source inclusion criteria, target inclusion criteria, calendar and geographic scope, measured effect modifiers, outcome definitions, intervention versions, support overlaps and uncertainty in the source contrasts. If a target subgroup is absent from the source and the needed response is unknown, the comparison should be marked `unsupported`, not assigned a convenient estimate.

**Source scope:** Bareinboim and Pearl, [*Transportability of Causal Effects: Completeness Results*](https://ojs.aaai.org/index.php/AAAI/article/view/8232), publisher abstract; [*Meta-Transportability of Causal Effects*](https://proceedings.mlr.press/v31/bareinboim13a.html), conference overview. The code computes only a finite weighted average conditional on supplied response functions; it is not the published complete selection-diagram algorithm.
