# 04 — HMAC-SHA-256 and message authentication

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can offline software authenticate a message while retaining deterministic published conformance evidence?

## Threat model, prerequisites and assumptions

The key is already securely provisioned; SHA-256 is supplied by the Python standard library; reference vectors come from RFC 4231. Constant-time comparison helps avoid direct timing leaks in tag equality but is not a complete side-channel guarantee.

## Governing formalism

`HMAC_K(m)=H((K′⊕opad)||H((K′⊕ipad)||m)); for SHA-256 B=64, output 32 bytes.`

## Derivation and interpretation

If key length exceeds 64 bytes, first hash the key; pad to 64 bytes; XOR with 0x36 and 0x5c for inner and outer compression layers. The construction uses two independent-looking keyed domains rather than plain H(K||m). The outer hash binds the inner digest without requiring secrecy of the hash function.

## Worked constructed investigation

RFC 4231 case 1: K=0b repeated 20 bytes, m="Hi There", HMAC-SHA-256=b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7. Case 2 with key "Jefe" provides an independent short-key vector.

## Offline reconstruction and verification method

Compute using `primitives.hmac_sha256`, compare RFC 4231 cases 1–4 and the separate independent oracle that manually builds ipad/opad with `hashlib`. Reject a changed message and a changed key. Never log the key in test evidence.

## Negative control and known failure

HMAC does not encrypt contents, prove who originally generated a shared secret, or establish public nonrepudiation; a copied key enables impersonation.

## Applicability, uncertainty and acceptance boundaries

No FIPS 140 cryptographic-module validation or private-key protections are claimed.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC2104, RFC4231. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computation-atlas, mathematics-physics-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
