# Investigation 11. Transfer a result to a different population

**Question:** A process appears beneficial in a demonstration facility. Does the same average benefit apply across a different machine fleet?

Two synthetic strata have different response contrasts: the easy stratum improves by 0.10 and the difficult stratum by 0.30. The source is 75% easy and 25% difficult; the target is 25% easy and 75% difficult. Both stratum response functions are stipulated and held fixed between settings. The source average contrast is 0.15, and the target contrast is 0.25.

**Run:** `python -m causal_atlas transport examples/transport.json`.

The tool requires source support for every positive target stratum, reports both averages and refuses unsupported target mass. It is a finite weighted average and cannot demonstrate that response functions are invariant. The result is not evidence that a change actually produces either response in real machines.

Before transporting a real effect, list effect modifiers and how they were measured, source/target eligibility, outcome calibration, intervention versions, machine and material differences, follow-up windows, and selection into the source. Some factors may be unmeasured and matter precisely because the two settings differ. If the target contains a machine class never studied in the source, no amount of weighting can supply its unknown response without extrapolation.

A valid external-validity argument can be stronger than one dataset, but it requires a scientific model of what changes across settings. Preserve the target distribution, source strata, missing support and differences in the mechanism as part of any exported context.

**Reference:** [Bareinboim and Pearl, transportability framework](https://proceedings.mlr.press/v31/bareinboim13a.html); [chapter 18](../chapters/18_transporting_effects.md).


## Investigative evidence packet

For an actual fleet deployment, preserve machine model, maintenance age, production mix, operator mix, climate, load range, intervention dose and measurement system as candidate effect modifiers. Retain both source and target population counts, including missing categories. Identify which variables were measured only after assignment, because treating them as baseline modifiers can change the target. If a source and target use distinct definitions of a defect, a weighted average cannot repair that mismatch. Report assumptions needed to transport the effect separately from those needed to identify it in the source.
