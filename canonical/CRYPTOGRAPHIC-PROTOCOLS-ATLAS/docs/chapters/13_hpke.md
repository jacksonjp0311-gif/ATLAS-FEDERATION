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
