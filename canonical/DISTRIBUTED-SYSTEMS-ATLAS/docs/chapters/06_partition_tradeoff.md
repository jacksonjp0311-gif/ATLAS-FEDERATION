# 06 — Consistency, availability and network partitions

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

During a partition, an implementation that provides every reachable client a response may have to relax single-copy consistency; one must state exact definitions.

## System model, assumptions and derivation

Linearizability requires operations to appear atomic while respecting nonoverlapping real-time precedence. Partition tolerance means the system continues to obey its specification despite arbitrary message loss between components. The familiar CAP impossibility is about these formal definitions under partitions.

**Formal invariant / expression:** `P and A (every request eventually responds) and strict linearizable C cannot all be guaranteed in the asynchronous partition model.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

With a disconnected two-replica store, side A writes x=1 and returns success; side B, unable to talk to A, must choose to block, return stale data, or violate linearizable reads if it answers x=0.

## Repeatable numerical or code method

State the consistency model and availability liveness predicate; simulate a partition and assert the precise expected failure or abstention, not a slogan about arbitrary tradeoffs.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Classifying a system as CP or AP for all conditions obscures its normal-operation consistency, latency and stale-read behaviors.

**Evidence boundary:** Model assumes the paper’s formal availability definition, not a user satisfaction or SLA measurement. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `CAP2002` — Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services — Seth Gilbert; Nancy Lynch (2002); https://doi.org/10.1145/564585.564601. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
