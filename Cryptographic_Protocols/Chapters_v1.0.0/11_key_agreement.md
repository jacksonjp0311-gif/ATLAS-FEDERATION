# 11 — Elliptic-curve key agreement and forward secrecy

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

What does ephemeral Diffie–Hellman contribute and what does it not solve?

## Threat model, prerequisites and assumptions

Public-key curves and coordinate encodings must follow a specified standard; ephemeral secret randomness and key erasure are required. Authentication of the peer remains a separate problem.

## Governing formalism

`DH symmetry: scalar_mult(a, B)=scalar_mult(b,A), with A=aG and B=bG; forward secrecy requires later compromise not to reveal erased ephemeral secrets.`

## Derivation and interpretation

The raw shared secret is not generally used directly as an application encryption key; it is passed to an appropriate KDF with transcript context. A handshake binding a wrong peer identity can derive matching keys but still be vulnerable to active impersonation.

## Worked constructed investigation

Two test parties create ephemeral public keys A and B and compute a shared secret S. If a middle party replaces A or B and no signature/MAC binds the exchange, the endpoints can complete different exchanges with the middle party rather than each other.

## Offline reconstruction and verification method

Use published X25519 vectors in RFC 7748 for an externally maintained implementation; assess identity binding, low-order handling and all-zero shared-secret rules under the chosen protocol. No curve arithmetic is implemented here.

## Negative control and known failure

The existence of an ephemeral key pair in a test does not prove erasure, hardware security, side-channel resistance or forward secrecy.

## Applicability, uncertainty and acceptance boundaries

No original DH implementation or post-quantum migration readiness is certified by these models.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC7748, RFC9846, RFC9180. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: mathematics-physics-atlas, computer-architecture-digital-hardware-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
