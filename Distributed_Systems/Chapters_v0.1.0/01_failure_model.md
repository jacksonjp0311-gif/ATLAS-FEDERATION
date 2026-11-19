# 01 — System boundaries and failure semantics

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A distributed system consists of independent state machines that exchange messages; their visible behavior depends on fault and timing assumptions.

## System model, assumptions and derivation

Safety means bad output never occurs; liveness means desirable progress eventually occurs under a stated schedule. Model crash-stop, crash-recovery, network loss, duplication, reordering, delay, partitions, Byzantine deviation and disk corruption as distinct failure families.

**Formal invariant / expression:** `Safety = forall admitted traces t: not Bad(t). Liveness = forall fair traces t: eventually Good(t).`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For a three-node archive index, let A and B keep responding while C is disconnected. Quorum read/update can proceed on A,B only if their persisted state and protocol match. A simple local retry cannot establish whether C crashed or messages are delayed.

## Repeatable numerical or code method

Enumerate allowed fault events separately. Mark network delay unbounded unless timing is assumed, enforce one transition at a time for the finite model, record violated invariants and rejected counterexamples.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** A paused but healthy node may be falsely suspected; a power-loss disk that acknowledges data before persistence is not a crash-stop process.

**Evidence boundary:** No real scheduling fairness or end-to-end delivery guarantee is established by a finite simulator. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `FLP1985` — Impossibility of Distributed Consensus with One Faulty Process — Michael J. Fischer; Nancy A. Lynch; Michael S. Paterson (1985); https://doi.org/10.1145/3149.214121. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
