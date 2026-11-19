# 07 — Crash-fault quorums, overlap and availability

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Quorum intersection is a combinatorial prerequisite for transferring knowledge between rounds, but not a complete consensus protocol.

## System model, assumptions and derivation

Two sets of sizes q1 and q2 drawn from n nodes have intersection at least max(0,q1+q2-n). Hence every pair intersects iff q1+q2>n. Strict majority q=floor(n/2)+1 satisfies self-intersection.

**Formal invariant / expression:** `min_overlap=max(0,q1+q2-n); majority=floor(n/2)+1.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For n=5, q=3; any two quorums overlap at >=1 node. Failure of 2 replicas leaves 3 responsive and permits quorum; failure of 3 leaves at most 2 and forces abstention. For n=6, q=3 can select disjoint sets: overlap is not guaranteed.

## Repeatable numerical or code method

Enumerate combinations for n<=8 and compare against the independent arithmetic prediction. Track unavailable nodes and the logical availability predicate.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Intersecting quorums do not guarantee safety when nodes forget accepted ballots after restart, or proposers ignore prior accepted values.

**Evidence boundary:** A quorum is not evidence that an acknowledged write was physically flushed or that Byzantine faults were handled. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `PAXOS1998` — The Part-Time Parliament — Leslie Lamport (1998); https://www.microsoft.com/en-us/research/publication/part-time-parliament/. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
