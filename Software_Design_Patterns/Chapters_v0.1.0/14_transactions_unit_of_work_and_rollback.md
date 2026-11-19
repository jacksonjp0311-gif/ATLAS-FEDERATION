# 14. Unit of Work, SQLite transactions and rollback boundaries

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

The Unit of Work pattern coordinates related changes as a single logical transaction. An offline SQLite database offers an explicit transaction boundary with BEGIN IMMEDIATE, protected uniqueness constraints, a deterministic reducer and COMMIT or ROLLBACK. The journal chooses WAL mode with synchronous FULL to improve software durability under supported filesystem semantics. It is important to describe the database boundary precisely: separate filesystem snapshots and external machines do not automatically join this transaction. A crash after the database commits but before another action can leave derived state stale.

## Formal contract and executable reference

**Invariant:** `BEGIN IMMEDIATE; validate->reduce->insert->COMMIT or ROLLBACK`.

**Implementation:** `ledger.CommandJournal`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Make a reducer raise after a transaction has begun. The database must roll back and contain zero committed commands for that ID. Submit a valid command afterward; the sequence must begin at one. In a separate test mutate a stored result directly using SQLite and verify the journal's independent hash-chain audit reports corruption. Read SQLite's official WAL and atomic-commit documentation for host/storage caveats.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

SQLite durability depends on the operating system, filesystem, disk controller, flush implementation and power conditions. A passing unit test on a desktop cannot substitute for controlled power-cut experiments. Do not claim transactional consistency between SQLite and a printer, actuator, or independently committed external database.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
