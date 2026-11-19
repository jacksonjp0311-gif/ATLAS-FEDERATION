# 16. Event sourcing with immutable blobs and a versioned head pointer

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Event sourcing records successive state-changing facts rather than only the newest current state. A content-addressed event graph allows replay from a head pointer to earlier immutable event blobs. Each event includes its sequence number and predecessor digest; the head identifies the newest entry, so a new blob created but not published can remain an orphan without becoming visible history. The reader verifies every referenced blob hash and contiguous sequence numbers. A missing or altered head must not silently reset the chain to empty.

## Formal contract and executable reference

**Invariant:** `entry_i={event_i,prev:H_(i-1),sequence:i}; head points to last hash`.

**Implementation:** `events.EventChain, atomicfiles.ContentStore`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Append events {n:1} and {n:2}, close the process and construct a new reader from the same directory. Replay must return both in order with the same head hash. Corrupt the head pointer to an unknown digest: the next append and replay must refuse. Limit replay length to a declared bound and test rejection when the event chain exceeds it.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The sample is single-writer only; two concurrent writers can race on the same head and one update may be lost. A hash chain whose pointer is not independently anchored does not resist an attacker rewriting all content. Event sourcing can also expose sensitive information unless retention and access controls are engineered separately.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-PUBSUB` — Microsoft Learn, Publisher-Subscriber Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
