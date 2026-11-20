# 18 — Independent vectors, negative controls and scientific acceptance

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

Which tests support a bounded software-content release and which scientific claims remain unproven?

## Threat model, prerequisites and assumptions

A known-answer vector constrains arithmetic for a specific input. A finite property test increases exercised coverage but does not establish cryptographic security, statistical randomness or an implementation-independent formal proof. No live attackers or hardware tests are in the observed evidence.

## Governing formalism

`Evidence = {normative vector agreement, alternate implementation agreement, invariant and negative-control tests, federation regression, source provenance}; no single term implies certified deployment security.`

## Derivation and interpretation

The HMAC alternate oracle explicitly constructs RFC 2104 pads without calling `hmac.digest`, while both share standard-library SHA-256. HKDF is checked against RFC 5869 external published vectors. Anti-replay is compared against a set-model; Merkle trees use a separate recursive implementation; role-separated authentication is attacked with altered frames and wrong keys.

## Worked constructed investigation

The offline oracle includes RFC 4231 cases 1–3, RFC 5869 A.1/A.3, thousands of randomized comparisons and rejected tampering and replay. All randomness here is deterministic test sampling and provides no operational entropy.

## Offline reconstruction and verification method

Run tests in a newly extracted archive and compare byte-identical JSON receipts from source and restored trees. List every omitted primitive (AEAD, Ed25519, X25519, certificate validation, secure boot) rather than counting conceptual prose as an implementation.

## Negative control and known failure

A test suite that verifies only an encryption/decryption round trip can pass for a broken cipher. Cross-implementation and known-answer vectors are distinct evidence classes.

## Applicability, uncertainty and acceptance boundaries

Scoped v1 acceptance means offline content/reference-model readiness only. No security certification, FIPS validation, independent expert peer review or hardware-backed trust is claimed.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC4231, RFC5869, RFC9846, NIST80057. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: measurement-atlas, neural-architectures-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
