# 10 — Digital signatures, identity anchors and certificate validation

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

Which authenticity claims can a signature establish, and how is the verification key trusted?

## Threat model, prerequisites and assumptions

Signature verification assumes a correct public key and algorithm-specific encoding. Certificates additionally require a trust path, purpose constraints, name validation, validity and revocation policy. Verification of a self-supplied key alone does not authenticate a real entity.

## Governing formalism

`Verify(pk,m,Sign(sk,m))=true (correctness); unforgeability is a separate adversarial claim, not an equation established by one known-answer test.`

## Derivation and interpretation

Ed25519 signature algorithms require careful point validation, key handling and context rules. A proof of key possession is not proof of authorization. An offline system must pin or otherwise authenticate the verifying key from a trusted acquisition channel.

## Worked constructed investigation

Assume an artifact A and two candidate public keys P_known and P_attacker. A signature by P_attacker verifies under P_attacker, but fails the trust-anchor test if only P_known is authorized. Thus a green cryptographic verification result can coexist with a failed provenance policy.

## Offline reconstruction and verification method

The reader records RFC 8032 Ed25519 as a normative design reference and a test-vector acquisition target. It intentionally does not implement Ed25519 or X.509 validation in the standard-library model.

## Negative control and known failure

Accepting any embedded self-signed certificate as a trust anchor collapses authenticity into attacker-controlled metadata.

## Applicability, uncertainty and acceptance boundaries

External signature implementations, certificate chain validation and hardware-backed trust anchors are not part of scoped software acceptance.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC8032, NIST80057, RFC9846. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computer-architecture-digital-hardware-atlas, measurement-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
