# 02. Canonical data, strict schemas, and versioned contracts

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A recoverable exchange format must be decodable after its generating software changes. A versioned envelope explicitly identifies a kind, integer version, stable record ID and payload, with a deterministic SHA-256 of canonical JSON. Sorting object keys and refusing nonfinite numbers eliminates many accidental differences between processes; restricting sizes and nesting bounds prevents unbounded parsing. The parser must reject extra fields rather than silently assigning new semantics. A content digest checks equivalence to an expected value, but an attacker who controls the document and hash can change both. Real authentication requires separately trusted signing or attestation, which is absent here.

## Formal contract and executable reference

**Invariant:** `H=SHA256(canonical(kind,version,id,payload)); digest equality ≠ authentication`.

**Implementation:** `contracts.envelope, contracts.parse_envelope`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Create the mapping {b:2,a:1}, wrap it as a version-one command, serialize and decode it. Reverse the order of input keys: the payload digest must not change. Modify a value without recomputing SHA-256: decoding must refuse. Supply a NaN, an unexpected schema field, an invalid ID, and excessive nesting: reject each. Record exact byte-length bounds and the trusted provenance of any external envelope.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

JSON key ordering alone is not a complete cross-language canonical-JSON standard: numeric formatting, Unicode normalization and large integers must be specified before interoperability can be certified outside this Python reference. No signed origin or network protocol is provided.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `NIST-SSDF` — NIST SP 800-218 Secure Software Development Framework (https://csrc.nist.gov/pubs/sp/800/218/final). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
