# 20. CQRS-style separation of command authority and read projections

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Command Query Responsibility Segregation separates the authoritative mutation path from a potentially cached or delayed read model. In an offline recovery workflow, the SQLite command journal is authoritative for accepted local operations. A content-addressed JSON snapshot is only a derived projection that can be reconstructed at any time. This simplifies restart logic: before relying on a read view, compare its source head to the journal's verified head. A stale projection is not evidence that a command failed; it may mean the secondary update was interrupted. A corrupted projection is an integrity failure that should be made visible.

## Formal contract and executable reference

**Invariant:** `read_view = f(verified_committed_journal); commands do not trust stale projections`.

**Implementation:** `workflow.RecoveryWorkflow`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit two journal entries while intentionally interrupting publication after the second. The old snapshot contains one entry, while the verified authoritative ledger contains two. Calling recover reconstructs the projection; repeat without new commands to verify idempotent read results. The projection should not cause a second execution of the reducer or any physical device output.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A read-projection pattern does not guarantee freshness without a defined synchronization protocol. This reference is single-host and local; distributed replicas, interleaved writers and conflict resolution belong to the Distributed Systems Atlas, not to an unproven local transaction claim.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
