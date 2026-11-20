# 31. Proof-carrying learning: what may an agent retain?

Agent adaptation ought to produce a claim with evidence, not merely accumulate fluent feedback. An agent can propose “calling tool X before tool Y increases accuracy,” but a new memory is scientifically meaningful only after the task, method, evaluator, software version, and observed outcomes have been documented. A reflective model's verbal explanation is a hypothesis. A worker's claim that a patch succeeded is not an independently verified effect. A model-generated summary cannot increase its own authority by being placed in a persistent database.

## A testable claim

Represent each proposed learning record as `(hypothesis_id, scope, source identifiers, candidate revision, evaluator revision, trial results, validity conditions, contradictions, expiry, provenance)`. Separate four phases: **proposed**, **tested**, **eligible for review**, and **admitted by a trusted external process**. This Atlas implements only the first three, with the last intentionally absent. Eligibility requires a tested revision, at least one supporting source, caller-reported passing evaluation, current freshness, and no unresolved contradictory source. This is a conservative *review gate*, not a proof that the source is genuine or the evaluation unbiased.

Different evidence may disagree legitimately. Two published studies can refer to different systems or selection mechanisms. A memory should not silently choose the most recent fluent statement. Keep the original claims, exact source identifiers, and a typed contradiction until a review determines whether the disagreement is scope-specific, measurement bias, stale provenance, or real conflict. If a source is withdrawn or an environment changes, an earlier memory may require expiry even when its original test once passed.

## Why an immutable reference matters

Suppose a self-improving agent uses a prompt patch in a coding benchmark and reports fewer failures. If the evaluator evolved during the same experiment, or previously failed tasks were used as training examples, the measured gain can reflect an unfair comparison. A source-linked learning record must include **both** the candidate's version and the method by which its benefit was assessed. The record must not drop caveats when compacted into an answer context.

The pure `memory_candidate_review` method checks bounded IDs, revision hashes, source-group separation, reported evaluation state, proposed/tested/superseded status, and current/expired/unknown freshness. It never writes to PEGASUS, SYMBIOTE, a database, an LLM context, or a retrieval router. A record marked `eligible_for_external_review` is an invitation to independent assessment, not a successful learning event. Even multiple source IDs may originate from the same primary observation; independence cannot be inferred from identifier count.

## Failure test and next evidence

An illustrative learned rule has one supporting receipt and one contradicting receipt. A naive system overwrites the contradiction. Our gate instead returns `review_conflicting_evidence`, preserving both references. A second synthetic rule has a positive reported test but expired provenance; it is held. An untested proposal requires tests before promotion.

A future empirical experiment should use real tasks withheld from the learning process, explicit outcome checks and rollback ability. The relevant design concepts are supported by Dwork et al.'s reusable-holdout abstract (2015) and the behavioral testing methodology of Ribeiro et al. (ACL 2020), but neither paper validates this particular implementation. This reference is an original research protocol, not independent proof of improved agent capability.
