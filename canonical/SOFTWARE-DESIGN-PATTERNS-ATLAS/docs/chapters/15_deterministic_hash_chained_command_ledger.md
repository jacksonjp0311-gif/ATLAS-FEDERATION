# 15. Hash-chained command history with independent replay checks

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

An ordered journal needs evidence that sequence gaps, payload mutation and result tampering are detectable relative to an independently trusted head. Each committed row stores a sequence number, command ID, canonical payload and result, previous row hash and current row hash. Replaying validates consecutive sequences, recalculates payload identity, checks canonical serialization and recomputes each link. A mutation of an early row should invalidate that row and subsequent chain verification. This protects against accidental corruption of locally stored entries; an adversary with control of every row and head may rewrite the chain consistently.

## Formal contract and executable reference

**Invariant:** `H_i=SHA256(seq,id,payload_sha,payload,result,prev=H_(i-1))`.

**Implementation:** `ledger.CommandJournal.verify_replay`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit two commands and capture the final head hash. Reopen SQLite and confirm the same head. Use a separate SQLite connection to alter result_json without updating the recorded hash: replay must fail. Test a changed payload and a broken previous-hash link. A recovered journal that fails a hash audit must enter a HOLD state instead of silently deriving new snapshots from untrusted history.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Hash chains are not digital signatures or tamper-proof logs when the attacker controls the entire file. Reliable audit needs separately anchored head values, trusted timestamps, key management or independent replicas, as appropriate. Crash durability also needs physical storage testing.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `SQLITE-WAL` — SQLite, Write-Ahead Logging (https://www.sqlite.org/wal.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
