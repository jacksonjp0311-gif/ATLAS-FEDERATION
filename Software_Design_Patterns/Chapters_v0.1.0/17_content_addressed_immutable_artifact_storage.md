# 17. Content-addressed immutable artifacts and integrity checks

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A content-addressed store names an artifact by a digest of its bytes. Identical inputs have identical names, and accidental byte changes should be detected during retrieval. This is useful for technical continuity because recovery depends on exact binaries, test data, CAD source files and manifests, not just human-readable filenames. The reference restricts individual blobs to one MiB to keep tests finite. It writes a temporary file and atomically replaces the digest-named leaf within a controlled local directory, then verifies content hashes on every read.

## Formal contract and executable reference

**Invariant:** `blob_name=SHA256(blob_bytes); retrieval recomputes the digest`.

**Implementation:** `atomicfiles.ContentStore.put/get`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Store the bytes of a small offline instruction file. The returned name must equal SHA-256 of those bytes. Store the same bytes again and verify the name is unchanged. Corrupt the stored blob through a separate test tool and require the next retrieval to fail. Submit a malformed hash or too-large file: reject it before writing.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Content-addressed naming is not secure provenance without a separately trusted digest. One local copy is also vulnerable to physical media failure. Multi-disk backups, verified redundancy and lawful redistribution are required for meaningful long-term survival.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `PY-OS` — Python Software Foundation, os.replace Documentation (https://docs.python.org/3/library/os.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
