# 15 — Transport, partitions and replica reconciliation

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Transport reliability and logical replication correctness are separate problems: TCP does not automatically imply transactional exactly-once processing at the application layer.

## System model, assumptions and derivation

Messages need stable IDs, schema versions, bounded sizes, sequence or causal metadata and explicit retry policy. During partition, local state may diverge within the specified consistency model. Reconciliation must guard against replay, loss, duplicate delivery, and stale membership.

**Formal invariant / expression:** `Safety envelope = validated_identity + accepted_schema + bounded_payload + durable_commit_rule + replay_policy.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Disconnect B, queue updates on A, reconnect and deliver the same update twice; a GCounter merge is idempotent but a naive integer increment is not. Distinguish eventual convergence from ordered log agreement.

## Repeatable numerical or code method

Simulate duplicates and reorder; verify a CRDT merge and compare to strict state-machine command replay. Add CRC/hash only for corruption detection, not identity trust.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** A stale node with a reused replica ID can violate unique-dot assumptions and a client can read stale data after partition heal while background anti-entropy is incomplete.

**Evidence boundary:** No actual network stack or authenticated wire protocol implemented; operational performance unknown. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `BAYOU1995` — Managing Update Conflicts in Bayou, a Weakly Connected Replicated Storage System — Douglas B. Terry and colleagues (1995); https://doi.org/10.1145/224056.224070. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
