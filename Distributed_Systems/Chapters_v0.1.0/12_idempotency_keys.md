# 12 — Idempotent command journals and scope of exactly-once

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A unique transaction key with an atomic state update can prevent duplicate local database mutations, but cannot guarantee exactly-once remote or physical effects.

## System model, assumptions and derivation

Within a single SQLite transaction, insert a unique key and change local materialized state. On retry, first query the key; equal payload returns prior effect without reapplying. A conflicting payload with the same key must be rejected. Commit configuration, file system and backup policy matter.

**Formal invariant / expression:** `apply_once(key,delta) = prior_state if key already in journal and delta equal; otherwise prior_state+delta on first insert.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Submit k=repair-7, delta=+3 twice; tally rises by 3 once. Submit the same k with delta=+4; reject. After process restart, a fresh connection reports committed local tally.

## Repeatable numerical or code method

Use the sqlite3 standard library, WAL and synchronous FULL as a software setting; independently reopen DB and validate state. Never call external actuator within the same transaction and infer exactly-once.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** If a remote printer starts a motor after a successful RPC but before acknowledgment, retrying may start it twice, regardless of the SQLite key.

**Evidence boundary:** No measured disk cache honesty, power-cut tests, external delivery reconciliation or production concurrency races. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `LINEAR1990` — Linearizability: A Correctness Condition for Concurrent Objects — Maurice Herlihy; Jeannette Wing (1990); https://www.cs.columbia.edu/~wing/publications/HerlihyWing90.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
