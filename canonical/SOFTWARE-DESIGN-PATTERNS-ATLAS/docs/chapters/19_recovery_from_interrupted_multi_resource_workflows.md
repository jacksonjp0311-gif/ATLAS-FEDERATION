# 19. Recovering a derived snapshot after a committed journal update

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

An application often updates more than one storage resource: a primary database and a derived file snapshot, for example. They cannot simply be described as one transaction. A safer design identifies the authoritative source and treats the secondary artifact as rebuildable. The Atlas recovery workflow commits a bounded pure command to SQLite and then publishes a derived content-addressed snapshot of all committed results. If an interruption occurs between these steps, a restarted process compares the journal head with the snapshot head, rebuilds the derived view if necessary, and records the new digest.

## Formal contract and executable reference

**Invariant:** `authoritative_journal_head != snapshot_head -> reconstruct derived view`.

**Implementation:** `workflow.RecoveryWorkflow.apply/recover`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit command A normally. Commit command B but deliberately raise a simulated interruption before publishing its snapshot. Close the process. Reopen the journal, validate every hash-chain link, and call recover(): it should detect that the snapshot head is stale and reconstruct a two-command view. A second recover should return recovered=False because the views now agree. Corrupt the existing snapshot pointer: refuse silent repair and require an operator to establish a trusted recovery basis.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A real controller can have other nonrebuildable state, including motor movements, heat, physical stock or remote financial transactions. Such effects are not rolled back by rebuilding a database view. The demonstration only certifies deterministic software-level derived state under its explicit model.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `SQLITE-WAL` — SQLite, Write-Ahead Logging (https://www.sqlite.org/wal.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
