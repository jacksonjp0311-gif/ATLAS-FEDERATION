# 13. Command identity and database-local idempotent effects

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A command is a request to perform a specific change; an event is a record that something occurred. Their distinction is fundamental to recovery after an interrupted response. A stable command ID and exact canonical payload digest allow a local journal to identify duplicate submissions. Within one serialized SQLite transaction, the first submission computes a result and stores it; an identical later submission reads that result without invoking the reducer again. The uniqueness constraint belongs in the database, not only in application memory, otherwise restarting could forget it.

## Formal contract and executable reference

**Invariant:** `same ID + same payload -> same committed row; same ID + different payload -> error`.

**Implementation:** `ledger.CommandJournal.execute`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Insert command ID c1 with {a:5,b:7}, using a pure reducer that returns {sum:12}. Submit the same command again and assert the reducer ran once; the replay returns the exact stored result with new_commit=False. Now reuse c1 with {a:5,b:8}: refuse. Close SQLite, reopen the database and verify c1 persists with a valid hash chain.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The reducer must be pure and deterministic. If it sends a command to a printer before database COMMIT, a later retry can send it again after a crash. A local unique ID does not establish exactly-once actuation, distributed exactly-once effects, or physical safety.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-RETRY` — Microsoft Learn, Retry Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/retry). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
