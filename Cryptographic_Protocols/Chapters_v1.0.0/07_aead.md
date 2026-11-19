# 07 — Authenticated encryption and nonce requirements

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

Why is encrypting and then adding a checksum not equivalent to a secure authenticated encryption interface?

## Threat model, prerequisites and assumptions

AEAD simultaneously specifies a key, unique nonce, plaintext, and additional authenticated data; it returns ciphertext and an authentication tag or fails closed. Each algorithm has bounds on per-key data and nonce reuse.

## Governing formalism

`(C,T)=AEAD_Encrypt(K,N,P,A); Decrypt(K,N,C,A,T) ∈ {P,FAIL}. Security depends on nonce discipline and implementation.`

## Derivation and interpretation

AEAD binds external headers A without hiding them. Decrypt must not release unauthenticated plaintext before tag validation. ChaCha20-Poly1305 in RFC 8439 combines a stream cipher and a one-time authenticator with carefully formatted AAD and lengths; nonces must not repeat with the same key.

## Worked constructed investigation

Construct a record header A="archive-v1", plaintext P="scientific record" and an epoch-specific nonce N. Changing A must cause FAIL in a conforming AEAD implementation. No AEAD algorithm is written into this package: the model only documents required invariants.

## Offline reconstruction and verification method

Before deployment, use a mature AEAD library with published vectors (RFC 8439), test AAD modification, tag truncation, nonce reuse, empty messages, length caps, and power-loss sequence behavior.

## Negative control and known failure

XORing plaintext with a hash stream without authentication leaks malleability; even a correct AEAD becomes unsafe after nonce reuse for some algorithms.

## Applicability, uncertainty and acceptance boundaries

The package deliberately does not implement encryption or claim protection of secret data. Never confuse the MAC-only educational model with AEAD.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC5116, RFC8439, RFC9846. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: electronics-semiconductors-atlas, distributed-systems-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.
