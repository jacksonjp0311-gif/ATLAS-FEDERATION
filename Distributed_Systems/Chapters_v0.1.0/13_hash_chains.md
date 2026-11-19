# 13 — Content-addressed integrity and restart reconstruction

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A SHA-256 hash chain detects many accidental or unsophisticated modifications under an intact, trusted head; it does not authenticate data against an attacker who can rewrite the whole chain.

## System model, assumptions and derivation

Canonicalize each event into UTF-8 sorted-key JSON. Let H_0 be fixed genesis, H_{i+1}=SHA256(bytes(H_i)||canonical(event_i)). Recompute after restart and reject any mismatch before rebuilding projections.

**Formal invariant / expression:** `H_(i+1) = SHA256(H_i || encode_canonical(event_i)).`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For events {a:1},{b:2}, compute two heads. Change the first event to {a:2} without changing the published head and the chain verification fails. But attacker can recompute both if no trusted anchor is externalized.

## Repeatable numerical or code method

Use journal.extend_chain/verify_chain; require event schema validation, canonical encoding, checksum and independent head copy for long-term archival.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Bit rot, truncation and malicious re-signing require different mitigations. A trusted external anchor and immutable backups are not implemented.

**Evidence boundary:** Cryptographic integrity is not physical storage reliability, authenticity without protected key or scientific source verification. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `LINEAR1990` — Linearizability: A Correctness Condition for Concurrent Objects — Maurice Herlihy; Jeannette Wing (1990); https://www.cs.columbia.edu/~wing/publications/HerlihyWing90.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
