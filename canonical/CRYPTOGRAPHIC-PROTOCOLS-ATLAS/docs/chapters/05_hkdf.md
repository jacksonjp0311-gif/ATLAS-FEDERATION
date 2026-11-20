# 05 — Extract-and-expand key derivation with HKDF

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can one high-entropy input derive purpose-separated cryptographic keys reproducibly?

## Threat model, prerequisites and assumptions

Use HMAC-SHA-256, HashLen=32 bytes; an arbitrary IKM is not thereby guaranteed strong. Salt is preferably independent random input and may be a public transcript hash only when the protocol specifies that use.

## Governing formalism

`PRK=HMAC(salt,IKM); T(0)=empty; T(i)=HMAC(PRK,T(i−1)||info||octet(i)); OKM=T(1)||... truncated to L, 0≤L≤255·32.`

## Derivation and interpretation

Extraction compresses input keying material to a pseudorandom key under suitable assumptions. Expansion constructs independently labeled output blocks; changing info changes the derived sequence. The 255-block bound comes from the one-octet counter; it is a format constraint rather than an estimate of key entropy.

## Worked constructed investigation

RFC 5869 Appendix A.1: IKM=22 bytes of 0b, salt=000102...0c, info=f0f1...f9, L=42. PRK starts 07770936 and OKM starts 3cb25f25. A.3 has empty salt and info and a different published digest.

## Offline reconstruction and verification method

Verify `hkdf_extract`, `hkdf_expand` and `hkdf_sha256` against RFC vectors A.1 and A.3; compare against a separate explicit ipad/opad oracle and reject L>8160. Do not use HKDF as a password-hardening function.

## Negative control and known failure

Reusing identical HKDF info labels for a traffic key and exporter can permit unwanted cross-protocol coupling. The code requires distinct domain labels for its educational channel.

## Applicability, uncertainty and acceptance boundaries

No proof is made that the particular input IKM has sufficient entropy, nor that side-channel leaks are absent.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC5869, RFC2104. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: mathematics-physics-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
