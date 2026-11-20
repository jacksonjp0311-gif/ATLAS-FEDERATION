# 18. Atomic same-filesystem pointer replacement and rollback design

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A recoverable system should not leave readers observing a partially written pointer. The reference creates a temporary file in the same directory as the target, writes its full digest and flushes it, then uses os.replace to make the head switch visible in one supported local operation. It retains old content-addressed blobs so an operator can inspect historical versions after a head update. The reference attempts parent-directory fsync where supported, but the physical durability of a filesystem operation depends on platform semantics and storage behavior.

## Formal contract and executable reference

**Invariant:** `write temp->fsync(file)->os.replace(temp,head)->best_effort_fsync(parent)`.

**Implementation:** `atomicfiles.ContentStore.publish`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Publish an initial head pointing at blob A, then update it to blob B. A fresh reader must see the complete digest for B, while blob A remains retrievable by hash. Attempt a path traversal tag or symlink head: the operation must fail. A power interruption simulation can test the software's handling of stale/missing pointers, but cannot certify actual Windows or Linux storage devices under a power cut.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

os.replace provides atomic rename semantics on appropriate platforms and filesystems; it does not by itself guarantee power-loss atomicity or synchronous commit across SQLite and filesystem storage. Not all filesystems safely support directory fsync or network shares. Test on the actual device before a blackout-readiness claim.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `PY-OS` — Python Software Foundation, os.replace Documentation (https://docs.python.org/3/library/os.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
