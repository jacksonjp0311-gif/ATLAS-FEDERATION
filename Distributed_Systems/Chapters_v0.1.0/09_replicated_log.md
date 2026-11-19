# 09 — Replicated logs and leader-election invariants

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A replicated state machine needs an agreed ordered command history, not just agreement on isolated values.

## System model, assumptions and derivation

Raft separates leader election, log replication and safety. Terms and per-index log metadata guard against inconsistent leaders, while the committed prefix cannot be overwritten by future elected leaders if election and commit rules are respected.

**Formal invariant / expression:** `For committed prefix length c: apply_i(log[1:c]) must be deterministic and equal across correct replicas of same membership/epoch.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

If a follower has entries (1:A,2:B), a new leader may reconcile an uncommitted suffix but may not erase a committed entry 1:A. The reference compares this narrative with single-decree Paxos; it does not claim to implement Raft.

## Repeatable numerical or code method

Write adversarial histories: stale leader, conflicting log suffix, crash after append before commit, and restart with persisted term. Require an explicit invariant checker and model checker before claiming agreement.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Electing a leader by largest wall-clock timestamp instead of log term and committed-entry rules risks electing stale replicas.

**Evidence boundary:** No multi-decree Raft service, election scheduler, snapshot installation or membership reconfiguration implementation in this edition. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `RAFT2014` — In Search of an Understandable Consensus Algorithm — Diego Ongaro; John Ousterhout (2014); https://web.stanford.edu/~ouster/cgi-bin/papers/raft-atc14.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
