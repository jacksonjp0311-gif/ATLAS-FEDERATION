# 22. Software supply-chain evidence, rights, and untrusted inputs

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Rebuildable software needs more than a ZIP. Its source, build commands, interpreter/compiler version, dependencies, tests, expected outputs, licenses and security boundaries must be recorded. NIST's Secure Software Development Framework offers guidance on organizational practices, but the existence of this Atlas code does not establish conformance. Hashes show byte equivalence to a claimed value; they do not authenticate a publisher, prove the absence of vulnerabilities, or grant redistribution rights. The complete Atlas requires authenticated original files and independently reviewed claims before any domain can be considered scientifically accepted.

## Formal contract and executable reference

**Invariant:** `release_acceptance = artifact_integrity AND scoped_tests AND independent_provenance`.

**Implementation:** `contracts.parse_envelope, evidence receipts`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Build a compact release with a source manifest, test receipt and exact restore instructions. Modify a single source byte and verify that the file digest no longer matches. Feed an oversized JSON message and a nested malicious-looking path to the strict parser, which must reject them. Document each failure and its source revision. Ensure original third-party publications are only linked, not copied without rights clearance.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The reference parser is not a comprehensive hostile-data sandbox; pure Python strategies are not safe to execute from untrusted sources. Production threat modeling, independent code review, dependency scanning and patch management remain open work.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `NIST-SSDF` — NIST SP 800-218 Secure Software Development Framework (https://csrc.nist.gov/pubs/sp/800/218/final). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
