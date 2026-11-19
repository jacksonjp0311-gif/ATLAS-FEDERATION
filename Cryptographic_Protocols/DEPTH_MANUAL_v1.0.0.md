# ATLAS FORGE — Cryptographic Protocols: Offline Technical Depth Manual v1.0.0

Original domain #14 of the unchanged 30-domain queue. One node inside the original federation, not an alternate Atlas. The educational models do **not** provide confidentiality, public-key signatures, certificate validation or production TLS.

## Navigation

- [Security goals and adversarial capabilities](chapters/01_security_goals.md)
- [Canonical binary encoding and transcript ambiguity](chapters/02_canonical_framing.md)
- [Entropy, randomness, identifiers and nonces](chapters/03_entropy_and_nonce.md)
- [HMAC-SHA-256 and message authentication](chapters/04_hmac_and_integrity.md)
- [Extract-and-expand key derivation with HKDF](chapters/05_hkdf.md)
- [Key schedule and role/domain separation](chapters/06_key_schedule.md)
- [Authenticated encryption and nonce requirements](chapters/07_aead.md)
- [Anti-replay windows and authenticated sequence numbers](chapters/08_anti_replay.md)
- [Authenticated handshakes, identity binding and key confirmation](chapters/09_handshake.md)
- [Digital signatures, identity anchors and certificate validation](chapters/10_digital_signatures.md)
- [Elliptic-curve key agreement and forward secrecy](chapters/11_key_agreement.md)
- [TLS 1.3 transcript, record layer and revision control](chapters/12_tls13.md)
- [Hybrid Public Key Encryption and context separation](chapters/13_hpke.md)
- [Key lifecycle, epochs, rotation and compromise response](chapters/14_key_lifecycle.md)
- [Merkle inclusion proofs and append-only evidence](chapters/15_merkle_inclusion.md)
- [Authenticated software updates, rollback and threshold policy](chapters/16_signed_updates.md)
- [Offline source provenance, deterministic archives and trust handoffs](chapters/17_offline_provenance.md)
- [Independent vectors, negative controls and scientific acceptance](chapters/18_verification_limits.md)


---

# 01 — Security goals and adversarial capabilities

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

What exactly does a cryptographic construction promise and under what adversary capabilities?

## Threat model, prerequisites and assumptions

Specify roles, protected assets, adversary visibility, key exposure conditions, and what counts as an accepted event. Distinguish passive eavesdropping, active forgery, rollback, concurrency, and a compromised endpoint. Do not use "encrypted" as a synonym for authenticated or authorized.

## Governing formalism

`Pr[forge success] <= Adv_EUF-CMA(A); Pr[distinguish] - 1/2 is confidentiality advantage; an integrity verdict alone establishes neither availability nor identity ownership.`

## Derivation and interpretation

EUF-CMA allows chosen-message MAC queries but the adversary must output an accepted new message/tag pair. IND-CPA compares ciphertexts for two equal-length challenge messages, while authenticated encryption additionally requires ciphertext integrity. Each metric assumes an explicitly modeled key distribution and oracle.

## Worked constructed investigation

Consider a signed archive with SHA-256 only: an adversary who can replace both data and hash can forge matching hashes. The same archive with a verified MAC uses a secret but cannot verify publicly; a signature adds a public verification key but only if that key is independently trusted.

## Offline reconstruction and verification method

Write a five-column threat table: attacker control, secret exposure, protected operation, acceptance predicate, evidence of failure. Classify each reference implementation as primitive arithmetic, authentication-only protocol model, or conceptual overview.

## Negative control and known failure

A MAC verification can pass even when a client lacks authorization to read the material. Treat authentication success and role authorization as separate predicates.

## Applicability, uncertainty and acceptance boundaries

The federation does not claim computational hardness proofs, penetration tests, side-channel resistance, or defense against malicious authorized administrators.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC2104, RFC5116, NIST80057. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: agent-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

# 02 — Canonical binary encoding and transcript ambiguity

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How does a protocol prevent two logically different messages from sharing the same authenticated byte string?

## Threat model, prerequisites and assumptions

All fields are byte strings; lengths are unsigned big-endian integers, number of fields is bounded, and trailing bytes are rejected. Semantic validation still happens above the framing layer.

## Governing formalism

`Enc(x1,...,xn) = u16(n) || Σ[u32(|xi|)||xi]; Enc(a,bc) != Enc(ab,c).`

## Derivation and interpretation

Naive concatenation maps the pairs ("ab","c") and ("a","bc") to the same bytes. Prefix lengths before each field so decoding determines a unique segmentation; enforce upper bounds before allocation and reject noncanonical trailing data. A unique serialization is necessary but not sufficient: Unicode normalization and semantic aliases still need a policy.

## Worked constructed investigation

Enc([0x61,0x6263]) begins 00 02 | 00 00 00 01 61 | 00 00 00 02 62 63. Its one-field alternative Enc([0x616263]) begins 00 01 and cannot collide. Verify both through `crypto_atlas.framing`.

## Offline reconstruction and verification method

Run `encode_fields`/`decode_fields` on empty, multi-field, null-byte and one-megabyte inputs; compare output with a second parser using a byte cursor. Check truncation at each boundary and rejected surplus bytes.

## Negative control and known failure

Concatenating a role string directly with a variable-length identity allows ambiguous messages; hashing ambiguous bytes does not restore the missing boundary.

## Applicability, uncertainty and acceptance boundaries

The framing format is original educational notation, not an interoperable TLS, COSE, ASN.1 or canonical CBOR encoding.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9846, RFC9180. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: language-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

# 03 — Entropy, randomness, identifiers and nonces

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

Which protocol values must be unpredictable, which only unique, and what happens after restart?

## Threat model, prerequisites and assumptions

Cryptographic secrets require a validated operating-system cryptographic random source and safe provisioning. Sequence numbers used as nonce inputs may be deterministic if unique within the key epoch, but only when a specified construction allows it. No entropy rate is measured here.

## Governing formalism

`For n independent uniformly sampled b-bit values, approximate collision probability p ≈ 1-exp[-n(n-1)/(2·2^b)] under the birthday model.`

## Derivation and interpretation

The birthday bound follows from no-collision product ∏(1-i/2^b), approximated by exp(-Σi/2^b). It does not apply to adversarially biased randomness and is not the same as a per-key security guarantee. A counter avoids random collisions but demands a durable, non-rollbackable state or a fresh key epoch.

## Worked constructed investigation

For uniformly random 32-bit identifiers after n=100,000 samples, n(n-1)/(2·2^32) ≈ 1.164; the exponential approximation suggests more than 68% collision risk. A 96-bit nonce can still be catastrophic if reused due to a crash or cloned VM.

## Offline reconstruction and verification method

Document key epoch, nonce width, counter size, storage atomicity and wrap limit; for TLS 1.3 record construction check `tls13_record_nonce` on 0,1,2 and 2^64 boundary. Separate deterministic test-vector seeds from operational entropy.

## Negative control and known failure

A restored VM snapshot reuses a counter and key, causing nonce reuse even if the random number generator was originally strong. This model does not test real hypervisor rollback.

## Applicability, uncertainty and acceptance boundaries

No DRBG, key generation or entropy collector is implemented or evaluated. Do not use Python `random.Random` for cryptographic keys.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC4086, NIST80090A, RFC9846. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: measurement-atlas, computer-architecture-digital-hardware-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

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


---

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


---

# 06 — Key schedule and role/domain separation

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How are key purposes, protocol editions, endpoints and directions distinguished in derived material?

## Threat model, prerequisites and assumptions

Both peers agree on a context identifier, protocol edition and endpoint identity labels before deriving keys. Domain-separated labels are unambiguous framed bytes. A transcript hash is not an authenticated identity by itself.

## Governing formalism

`K_c2s=HKDF-Expand(PRK,Enc(domain,"client-to-server",transcript),32); K_s2c=HKDF-Expand(PRK,Enc(domain,"server-to-client",transcript),32).`

## Derivation and interpretation

The same PRK expands into different output bytes when labels change. This is computational key separation under HKDF assumptions, not a substitute for negotiating authentication. TLS 1.3 uses `HKDF-Expand-Label` with `tls13 ` prefix and a structured `HkdfLabel`, so raw generic HKDF info cannot be swapped in.

## Worked constructed investigation

A 32-byte fixed test secret and transcript context "mission-1" produce two distinct 32-byte keys. Change the context to "mission-2" and both outputs change. The model refuses identical client/server labels.

## Offline reconstruction and verification method

Run `derive_directional_keys` and `hkdf_expand_label` across roles, contexts, lengths and empty labels. Record both the label encoding and the derived output hash (never a production secret).

## Negative control and known failure

Deriving an identical key for both send/receive directions can permit message reflection if the protocol checks neither roles nor direction headers.

## Applicability, uncertainty and acceptance boundaries

The educational shared-secret construction is not a TLS handshake, does not authenticate public keys, and does not provide forward secrecy.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC5869, RFC9846, RFC9180. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: software-design-patterns-atlas, distributed-systems-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

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


---

# 08 — Anti-replay windows and authenticated sequence numbers

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How does a receiver accept bounded out-of-order authentic traffic while rejecting duplicates and stale records?

## Threat model, prerequisites and assumptions

A receiver tracks high watermark h and a width-w bitmap. Authenticate the complete message before changing replay state; state can roll back after a crash unless durably persisted. A replay window is not meaningful without authenticating the sequence number.

## Governing formalism

`On seq s>h: bitmap←((bitmap << (s-h)) OR 1) mod 2^w, h←s; otherwise k=h-s, accept iff 0≤k<w and bit_k=0.`

## Derivation and interpretation

For a new maximum s, shift the bitmap and set the least-significant bit. For an older accepted s in the window, set its offset bit without moving h. Values below h-w+1 are stale. This is the same logic as a finite set of recent accepted identifiers under bounded arithmetic.

## Worked constructed investigation

For width 8, accept 7, then 5 and 6; reject a second 5 and any 0 after high reaches 20. A forged far-future sequence must fail authentication without advancing the high watermark.

## Offline reconstruction and verification method

Use `ReplayWindow` with an independent set-based oracle across thousands of random sequence permutations, and `AuthenticatedSession.receive` to show that invalid tags never mutate state.

## Negative control and known failure

A process that forgets its high watermark may accept an old authenticated frame again; restart survival is a separate persistence and identity-epoch problem.

## Applicability, uncertainty and acceptance boundaries

No real network clock, packet loss distribution, persistent anti-replay database, or concurrency interlock is tested.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9846, RFC5116. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: distributed-systems-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

# 09 — Authenticated handshakes, identity binding and key confirmation

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can a key agreement be linked to participant identities and a specific session transcript?

## Threat model, prerequisites and assumptions

A secure handshake requires anti-downgrade negotiation, identity authentication and transcript binding under its own protocol semantics. A shared-secret MAC-only educational demonstration does not establish secure public-key negotiation.

## Governing formalism

`transcript_hash=SHA256(Enc(version,suite,client_id,server_id,messages)); Finished=MAC(K_finished,transcript_hash).`

## Derivation and interpretation

If an attacker changes a version, handshake parameter, or an endpoint label, a properly constructed Finished or signature verification over the transcript should fail. Key confirmation also requires matching role-specific keys, not simply receipt of an unverified welcome message.

## Worked constructed investigation

Construct two peers under context `mission-1`, IDs `reader` and `archive`, and a fixed test PSK; verify the authenticated record in both directions and reject a peer using a different context or key.

## Offline reconstruction and verification method

Use the `AuthenticatedSession` MAC-only model as a finite demonstration of role-separated authenticated messages. For a real handshake use a maintained, standards-conforming TLS library; do not adapt this demo into a custom network security protocol.

## Negative control and known failure

A shared PSK distributed to two organizations does not prove which holder sent a particular message, and key compromise invalidates the model’s identity interpretation.

## Applicability, uncertainty and acceptance boundaries

No PKI, ephemeral key exchange, real mutual authentication or full TLS handshake is implemented or certified.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9846, RFC5869, RFC7748. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: distributed-systems-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

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


---

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


---

# 12 — TLS 1.3 transcript, record layer and revision control

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How should an offline reference preserve the current authoritative TLS standard without silently treating older editions as current?

## Threat model, prerequisites and assumptions

RFC 9846 (July 2026) obsoletes RFC 8446. The standard defines a complete handshake and record protocol; this chapter only models selected HKDF labeling and record nonce arithmetic.

## Governing formalism

`TLS-1.3-Nonce = write_iv XOR (0x00000000 || uint64_be(seq)) for a 96-bit IV; HKDF-Expand-Label(secret,label,context,L) uses an encoded HkdfLabel with `tls13 ` prefix.`

## Derivation and interpretation

A separate 64-bit read/write sequence starts at zero under each traffic key. The nonce mask is padded to the IV length and XORed. If sequence exhaustion approaches, update keys or close; resetting the number without changing the key can reuse nonces. The transcript includes handshake fields that protect against downgrade.

## Worked constructed investigation

With IV=01 repeated twelve times, sequence 0 yields that IV; sequence 1 flips the final low bit and produces the last byte 00. Passing 2^64 is rejected before any record operation. HKDF label `key` is distinct from `iv`.

## Offline reconstruction and verification method

Use `tls13_record_nonce` and `hkdf_expand_label` in offline tests, then consult RFC 9846 for full interop semantics. The historical RFC 8446 may be retained as source history but is not the current authority.

## Negative control and known failure

Treating a passing HKDF/nonce test as proof that certificate validation, Finished verification, 0-RTT replay policy or AEAD encryption are implemented would be false.

## Applicability, uncertainty and acceptance boundaries

No full TLS 1.3 implementation, external network interoperability or side-channel security certification is claimed.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9846, RFC5869, RFC8439. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: distributed-systems-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

# 13 — Hybrid Public Key Encryption and context separation

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

What distinguishes HPKE key encapsulation, KDF and AEAD, and why do context labels matter?

## Threat model, prerequisites and assumptions

HPKE follows suite-specific KEM, KDF, AEAD and mode conventions. Key validation, PSK parameters, sender authentication modes and exporter context must be checked by a conforming library.

## Governing formalism

`shared_secret=KEM(...); (key,nonce,exporter_secret)=KeySchedule(shared_secret,info,psk,psk_id); context bound to suite/mode.`

## Derivation and interpretation

RFC 9180 separates domain strings used for DHKEM and HPKE key schedule (`KEM...` and `HPKE...`). Labels prevent one valid primitive output from being substituted as an input with different semantic meaning. Derivation of different keys does not itself authenticate the KEM public key.

## Worked constructed investigation

A context `archive-records` must not be silently reinterpreted as `software-update` when both derive bytes from a common setup. Change the info/suite and record a distinct context; enforce that a PSK and PSK identifier are either both present or both absent.

## Offline reconstruction and verification method

Use the source map to reconstruct HPKE’s inputs, KEM validation rules and reference vectors in an external conformant implementation. The package gives no HPKE encrypt/decrypt function.

## Negative control and known failure

An application that accepts an attacker-chosen recipient public key without authentication encrypts to the attacker, regardless of mathematical correctness.

## Applicability, uncertainty and acceptance boundaries

HPKE is documented as a dependency and design pattern, not a working local encryption implementation.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC9180, RFC5869, RFC5116. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: mathematics-physics-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

# 14 — Key lifecycle, epochs, rotation and compromise response

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

What operational metadata is necessary to know whether a valid tag was created under an authorized key?

## Threat model, prerequisites and assumptions

Trust decisions include key identifier, purpose, epoch, algorithm, creation/activation/retirement, revocation state, custodian and compromise response. Timing and policy cannot be inferred from cryptographic arithmetic.

## Governing formalism

`Accept(record)=VerifyTag(K_epoch,record) AND EpochAllowed(epoch,t) AND RoleAllowed(actor,action) AND NotRevoked(key_id).`

## Derivation and interpretation

Rotating keys requires moving from old to new encryption/authentication domains while preventing rollback. A key-change message itself needs authentication under an authorized root. Old secrets should be deleted when no longer necessary, subject to recovery and legal requirements.

## Worked constructed investigation

An archival reader may verify a 2025 signed receipt with a retired key if policy includes historical validation and a trusted timestamp, while refusing new data signed after revocation. Neither policy follows automatically from a SHA-256 digest.

## Offline reconstruction and verification method

Maintain a minimal offline key inventory and recovery checklist (identifier, source, allowed purpose, epoch, retirement, trusted anchors, revocation evidence, audit). Consult NIST SP 800-57 for actual lifecycle guidance.

## Negative control and known failure

A cryptographically valid replay under an expired or compromised key must be refused by an independent policy decision; MAC verification alone cannot make that decision.

## Applicability, uncertainty and acceptance boundaries

No real production key-management system, HSM, secure erase or operator approval process has been exercised.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: NIST80057, NIST800193, RFC9846. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computer-architecture-digital-hardware-atlas, distributed-systems-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

# 15 — Merkle inclusion proofs and append-only evidence

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can a reader verify that a leaf belongs to an ordered commitment without downloading every other leaf?

## Threat model, prerequisites and assumptions

The model uses the historical RFC 6962 v1 domain prefixes and an ordered list; it does not claim current Certificate Transparency v2 protocol conformance. A trusted signed root is a separate requirement.

## Governing formalism

`LeafHash(m)=SHA256(0x00||m); NodeHash(L,R)=SHA256(0x01||L||R); EmptyRoot=SHA256(empty).`

## Derivation and interpretation

For n non-power-of-two leaves, split the tree at the largest power of two strictly below n; recursively hash left and right ranges. An inclusion proof contains the necessary sibling hashes. Verification rebuilds the root with the same leaf index and tree size.

## Worked constructed investigation

For leaves [a,b,c], root=NodeHash(NodeHash(LeafHash(a),LeafHash(b)),LeafHash(c)); a three-leaf tree is not the hash of LeafHash(a) and NodeHash(b,c). Reordering leaves changes the root.

## Offline reconstruction and verification method

Compute `tree_hash`, `inclusion_proof`, and `verify_inclusion` for every index of trees with 1..89 leaves; compare to an independently implemented recursive oracle. Refuse wrong leaves, wrong indices, forged siblings and excess proof elements.

## Negative control and known failure

An attacker who substitutes both the tree root and proof can still satisfy mathematical membership checks: obtain the expected root from a trusted signed checkpoint.

## Applicability, uncertainty and acceptance boundaries

No certificate issuance system, log consistency proof, independent witness signature or live gossip network is implemented.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: RFC6962, RFC9162, RFC8032. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computation-atlas, software-design-patterns-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

# 16 — Authenticated software updates, rollback and threshold policy

**ATLAS FORGE · Original 30-domain priority 14 · Scoped cryptographic-protocols technical reference v1.0.0**

## Scientific and engineering question

How can offline rebuild tooling reject a validly signed but obsolete or unauthorized update?

## Threat model, prerequisites and assumptions

A secure update workflow separates trusted root metadata, delegate roles, artifact hashes, version monotonicity and expiry. Clock trust is not assumed merely because an offline file has a date.

## Governing formalism

`AllowUpdate=SignatureThresholdOK ∧ HashMatch ∧ RoleAuthorized ∧ Version>=trusted_min ∧ NotExpired_as_policy_verified.`

## Derivation and interpretation

Threshold signatures are distinct from multiple copies of one shared key. A policy may require, for example, 2 signatures from 3 independently managed keys; the actual threshold and authorization must be stored outside attacker-modifiable update metadata. Rollback prevention requires protected local version state.

## Worked constructed investigation

An attacker presents legitimate signed release v4 after the system already accepted v6. Its signature may verify, but a reader with trusted minimum version v6 must refuse to install it. A changed archive hash must fail independently of the signature count.

## Offline reconstruction and verification method

Write a pencil-and-paper acceptance table with authorized signer sets, expected hashes, minimum versions, timestamps and unresolved clock trust. Use verified historical Atlas release receipts as data examples, not as proof of a complete signed-update system.

## Negative control and known failure

Replacing both the package and an unprotected version marker defeats a purely local rollback check. A signed file is not a synonym for a trustworthy source.

## Applicability, uncertainty and acceptance boundaries

No threshold signature implementation, secure boot, TUF client, trusted offline clock or tested update chain is supplied.

## Exact-source navigation and scholarly caveats

Bibliographic anchors: NIST80057, NIST800193, RFC8032. The source register contains direct issuing-organization links, not locally authenticated original publisher bytes. Cross-domain conceptual prerequisites: computer-architecture-digital-hardware-atlas, distributed-systems-atlas. Exact record revisions are captured in `data/relations.jsonl`. A `related_to` relation is navigation, not independently established evidentiary support.

**Units:** byte lengths, bit widths, abstract counts and dimensionless probabilities unless stated otherwise. **Measurements:** none. **Scientific peer review:** none commissioned.


---

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


---

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

