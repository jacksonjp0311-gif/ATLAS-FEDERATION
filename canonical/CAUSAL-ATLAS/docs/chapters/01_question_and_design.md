# 1 Define the question before choosing an estimator

A causal question is a comparison between specified interventions in a specified population over a specified time. A column named `treatment` is not that specification. In a factory example, “use the new process” might mean changing a machine setting, retraining operators, or assigning work to a different machine. Those are different interventions even when a database records them under one label. This chapter supplies an original investigation workflow; it does not certify any actual process.

## The object we want to learn

Let A be a binary intervention and Y a pass indicator measured after a fixed follow-up. Write Y(1) and Y(0) for the outcomes under the two interventions. An average treatment effect in target population T is

`ATE_T = E_T[Y(1) - Y(0)]`.

The target population is part of the definition. It is not a cosmetic label appended after fitting a model. The observed treated group, the entire study sample, and a future production mix can have different distributions of relevant conditions. They need not have the same average effect.

Our original heterogeneous-effect example makes this explicit. Suppose the benefit is +0.10 for easy jobs and +0.40 for difficult jobs. A target containing 80% easy jobs has effect `0.8*0.10 + 0.2*0.40 = 0.16`. A target containing 80% difficult jobs has effect `0.2*0.10 + 0.8*0.40 = 0.34`. No estimator failed and no measurement changed. The question changed. These calculations are reproduced by `python -m causal_atlas investigations`.

## Design a comparison people can interpret

For an actual investigation, record eligibility, each intervention, assignment, time zero, follow-up, outcome measurement, target contrast, and analysis plan before inspecting which analysis gives a preferred result. The target-trial literature supplies a source anchor for organizing these decisions: [Hernán and Robins 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/), named portions recorded in the source register. Our blank [study specification](../templates/TARGET_STUDY.md) turns these decisions into fields without filling them with fictitious observations.

An implementable production question might be: “Among eligible batches entering one specified machine family during a declared period, what would the difference in final pass probability be if every batch were assigned the new validated setting rather than the existing setting, with the same inspection definition and a fixed follow-up?” That wording still needs domain review. It is much better defined than “did quality improve?” because an analyst can now identify excluded jobs, incompatible outcomes, and changes in intervention version.

## Keep time zero coherent

Consider this original timeline. A batch becomes eligible at entry; process assignment occurs at entry; inspection follows. If the analyst instead calls a batch ‘treated’ only when it remains in production for three more shifts, membership now depends on future survival or continuation. Comparing that selected group with all control batches does not answer the entry-time assignment question. The fix is not a special coefficient: first repair the group definitions and timeline.

The source-level principle is that eligibility, assignment and follow-up start must be aligned; future information used to define treatment can introduce selection. See [Hernán and colleagues 2016, §2 and §3](https://pmc.ncbi.nlm.nih.gov/articles/PMC5124536/). This Atlas does not implement trial emulation, censoring weights or adherence-effect estimation. It supplies the design questions and a boundary check.

## Separate assignment from receipt

An assignment effect asks about the policy of assigning the process, including nonadherence as it occurs. An effect of actually following the process asks a different question. Replacing assignment with receipt in an analysis can require additional assumptions because receipt may depend on information collected after assignment. Record which question is intended; do not silently switch when compliance is disappointing.

Likewise, interference and multiple intervention versions must be considered rather than buried in a generic consistency label. One machine's treatment may affect a shared line or operator schedule. This node has no interference estimator. A genuine spillover problem must remain a design limitation or be routed to a future explicitly defined method, not forced into the binary point-treatment calculator.

## Completion check

Before estimating, an investigator should be able to name the unit, interventions, outcome window, target mix, and comparison. Unknown answers belong in the assumption ledger. A precise question does not establish identification, but it prevents a precise calculation from answering the wrong question.

**Related records:** `estimand`, `target-population-example`, `coherent-entry`, `survivor-restriction`, `time-labelled-variables`.
