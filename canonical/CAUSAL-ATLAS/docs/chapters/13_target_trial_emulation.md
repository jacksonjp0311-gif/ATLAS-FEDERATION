# 13. Target trial emulation: define the experiment before analyzing records

A causal investigation begins with a decision question, not an estimator. An observational database contains a mixture of past decisions, measurements, censoring, and survival conditions. Before comparing outcomes, articulate the randomized trial whose result would matter, even if that trial cannot be conducted. This is the target-trial approach of Hernán and Robins (2016), not a procedure for converting arbitrary historical associations into randomized evidence.

## Specify the protocol

Name the eligibility criteria, time zero, strategies, assignment procedures, outcomes, follow-up duration, causal contrast, and analysis plan. Write a date- or event-specific rule for each field. Avoid criteria determined after assignment: selecting only units that completed treatment can exclude early failures and introduce selection bias. An exposure that is defined as “received treatment for at least six months” cannot be assigned at baseline unless one simultaneously specifies what happens to units who stop or die before six months. A treatment is a strategy over time; “ever treated” is usually not a precise intervention.

Consider an industrial intervention to replace a valve in one of two production lines. **Time zero** could be the timestamp when a machine becomes eligible for replacement, not the time of first completed good batch. Eligibility might require a scheduled maintenance interval and an eligible part number. Strategies could be replacement at that interval versus scheduled replacement at the next interval. Outcomes might be defects per 1,000 attempted parts over a prespecified follow-up, with machine shutdowns counted explicitly. The analysis should not eliminate a shutdown simply because it produced no acceptable units. This is a *design template*, not a claim about any observed plant.

## Assignment versus compliance

An intention-to-treat contrast concerns assignment to strategies; a per-protocol contrast concerns following them. In an observational emulation, assignment is not necessarily recorded and treatment initiation is not identical to randomized offer. Changing adherence can be associated with prognostic history. If those histories are affected by prior treatment, ordinary baseline-only adjustment can be inadequate; a suitable longitudinal g-method may be required.

Define both the eligible population and the population represented by observed records. Exclusions at time zero change the target. For a matched cohort, each unit's baseline window must be aligned with its comparison's baseline window. Explicitly specify the handling of repeated eligibility and follow-up until outcome, censoring, or a fixed horizon. State when a strategy could not have been implemented or when exposure information is missing.

## Validity checklist

- Could both strategies realistically have been assigned to each eligible unit at time zero?
- Does every outcome and covariate timestamp precede or follow assignment as required?
- Are baseline confounders distinguishable from postbaseline consequences?
- Do records contain sufficient support for the compared strategies in the target population?
- Were exclusions, censoring, competing events, and deviations from strategy handled consistently?
- Could the same question be answered by a stronger design, such as randomization, interrupted time-series with credible controls, or a prospective instrument?

Passing this checklist is not proof of exchangeability. Report unmeasured causes, measurement error, adherence definitions, and target population differences. A target-trial diagram is a discipline for identifying what to learn, not a certificate of causal identification.

**Source scope:** Hernán and Robins, *Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available*, 2016, [full published PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/), sections defining target-trial protocol and baseline alignment. The Atlas paraphrases selected passages and does not redistribute the paper. See also [BMJ target trial primer](https://www.bmj.com/content/378/bmj-2022-071108).
