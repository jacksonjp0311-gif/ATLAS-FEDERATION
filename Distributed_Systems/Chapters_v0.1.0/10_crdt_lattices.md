# 10 — Semilattice CRDT merge and eventual convergence

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A state-based CRDT converges when updates inflate replica state in a join-semilattice and repeated deliveries merge by the associative, commutative and idempotent join.

## System model, assumptions and derivation

A grow-only counter stores a nonnegative per-node integer map and merges pointwise maximum; readout sums components. An observed-remove set stores unique add dots and a tombstone set; a removal only removes dots observed at that replica, allowing concurrent add wins.

**Formal invariant / expression:** `join(a,b)=join(b,a); join(join(a,b),c)=join(a,join(b,c)); join(a,a)=a.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Replica A counts {A:2}, B counts {B:3}; merge yields total 5 regardless of message order. For OR-Set, A removes dot A:1 while B concurrently adds B:1; after merge the item remains present due to B:1.

## Repeatable numerical or code method

Run GCounter/ORSet with repeated and reordered merges; compare with independent maxima over finite vectors, test dot uniqueness and removal semantics.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Unique event dots and stable replica identifiers are prerequisites. Tombstone cleanup without a causal stability protocol can resurrect removed values.

**Evidence boundary:** CRDT convergence does not imply serializable transactions or general conflict-free business semantics. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `CRDT2011` — A Comprehensive Study of Convergent and Commutative Replicated Data Types — Marc Shapiro; Nuno Preguiça; Carlos Baquero; Marek Zawirski (2011); https://asc.di.fct.unl.pt/~nmp/pubs/tr-inria-2011.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
