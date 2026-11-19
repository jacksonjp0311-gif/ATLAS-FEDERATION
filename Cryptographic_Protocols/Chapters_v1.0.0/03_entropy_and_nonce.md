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
