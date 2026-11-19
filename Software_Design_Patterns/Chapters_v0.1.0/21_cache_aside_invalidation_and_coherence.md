# 21. Cache-aside, invalidation and the limits of stale knowledge

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A cache increases read speed by retaining previously computed values, but its content may become stale when the underlying source changes. The Cache-Aside pattern makes the source authoritative and loads cached values on demand. In the Atlas, a version hash or exact record revision offers a concrete invalidation key; an old context assembled from earlier records should not silently replace new evidence. The Computer Architecture node includes a separate direct-mapped write-through cache at the byte level. The Software Design Patterns domain focuses instead on application-level reconstruction of derived results.

## Formal contract and executable reference

**Invariant:** `cache_valid iff cache_revision == authoritative_revision`.

**Implementation:** `workflow snapshot revision comparison; Computer Architecture cache reference`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit a new journal entry and deliberately leave the derived snapshot stale. The read-side recovery compares hashes, detects revision mismatch, and reconstructs a fresh projection. A second read returns the same digest without rebuilding. Contrast that with deliberately modifying a cached byte without its source update: retrieval must detect corruption or refuse inconsistent evidence rather than returning it as authoritative.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Cache coherence across multiple machines is not solved by local SHA-256 comparisons alone. Read stale values can be dangerous for control systems and medicine; real service deadlines, network partitions and consistency models require explicit designs and external validation.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
