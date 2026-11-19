# 17 — Offline source provenance, deterministic archives and trust handoffs

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

What additional evidence is needed to convert an internal checksum into a trustworthy reconstruction record?

## Threat model, prerequisites and assumptions

The federation already preserves exact source-file hashes and release provenance, but local checksums only establish equality with a recorded value; the record itself must have a trusted origin. Do not treat a retrieved URL as an authenticated publisher source file.

## Governing formalism

`SHA256(restored_archive)==SHA256(expected_archive) ∧ VerifyManifest(files) is integrity agreement, not AuthenticatedOrigin(expected_digest).`

## Derivation and interpretation

A deterministic archive lets future systems reconstruct identical bytes from a known predecessor and a small patch. This provides reproducibility even without network access, but one must separately prove the initial trust anchor and authenticate each transfer across storage media.

## Worked constructed investigation

The previous Neural Architectures archive has recorded SHA-256 453746a04cd5b5b291a37e9c6bd39b513c6c53e21b7bf7f493fc71437887a97b. If restored bytes match that hash, the bytes are identical to the recorded digest; this alone does not prove that a third party authored the claim.

## Offline reconstruction and verification method

Use `tools/check_manifest.py verify`, `tools/check_collection.py`, and fresh restore receipts. Preserve old source and reviewer metadata. Record observed hashes and keep post-upload Library readback as an independent transport check.

## Negative control and known failure

An adversary who changes an unsigned digest alongside an artifact preserves apparent integrity. This is why offline origin and chain-of-custody remain open security gaps.

## Applicability, uncertainty and acceptance boundaries

No signed root-of-trust or hardware-verified provenance chain has been established for the full Atlas.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC8032, NIST80057, RFC6962. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: software-design-patterns-atlas, computation-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
