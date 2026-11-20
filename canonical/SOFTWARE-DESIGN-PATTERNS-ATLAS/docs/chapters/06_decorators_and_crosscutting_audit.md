# 06. Decorator pattern for explicit audit boundaries

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A decorator adds consistent behavior around an existing operation while preserving its primary interface. Logging and audit are common examples, but an audit event should not claim success if the wrapped operation throws an exception. A purely functional digest of the returned value can record which result was observed; it does not prove the operation caused or avoided any external side effect. Error states, retry attempts and interrupted outcomes should be represented in separate durable events when a production system needs them.

## Formal contract and executable reference

**Invariant:** `record(receipt)=digest(output) only AFTER successful invocation`.

**Implementation:** `composition.audited`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Wrap a function mapping x to {out:x+1} with an audit decorator and inspect the result SHA-256. Invoke the wrapper twice on the same input; the output digests should agree, although two audit entries exist. Wrap a function that raises: verify no false completed entry appears. Keep detailed failure information separately if the surrounding workflow requires it.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

An audit decorator does not make a distributed operation transactional. A crash after external action but before logging can leave missing evidence; a crash after logging but before completion can produce misleading partial records unless state transitions are separately modeled.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `NIST-SSDF` — NIST SP 800-218 Secure Software Development Framework (https://csrc.nist.gov/pubs/sp/800/218/final). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
