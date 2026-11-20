# Chapter 49 — Cryptographic assumptions and post-quantum agility

**Area:** Security. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Cryptographic integrity, authenticity, confidentiality and key agreement are different properties. Hashing verifies consistency relative to a trusted expected digest; a digital signature binds a message to a signing key under a security assumption; encryption hides content subject to a threat model; a key-encapsulation mechanism allows two parties to derive a shared secret via a public channel. Standards and algorithms require exact versions, parameter choices, key custody, interoperability tests and consideration of future cryptanalytic developments. Modern post-quantum designs respond to quantum threats but are not a promise of unconditional security.

## Mathematical contract

A KEM has KeyGen→(pk,sk), Encaps(pk)→(ciphertext,shared_secret), Decaps(sk,ciphertext)→shared_secret or a defined failure behavior. Security depends on the scheme, parameters, adversary model and implementation.

## Derivation and reasoning

NIST FIPS 203 specifies ML-KEM and parameter sets 512, 768 and 1024. Published documentation includes a November 2025 errata planning note, which is a reminder that a standards citation is versioned rather than timeless. Strong algorithm design does not prevent side-channel, random-number, key-reuse or API misuse vulnerabilities. This Atlas does not implement ML-KEM or invent a new quantum-resistant scheme; it preserves the distinctions and standards locators for future authorized implementers.

## Worked reconstruction and independent check

Create a conceptual table of hash digest, signature, encryption and KEM: what property each claims and what it does not. Verify a file hash against a separately stored trusted digest, then explain why the digest alone does not prove the publisher identity. Inspect FIPS 203 edition and recorded errata before any security claim.

## Limitations, falsification, and invalid use

Do not use the small teaching code for cryptographic deployment. Do not infer authenticity from matching SHA-256 fields or equate a KEM with digital signatures. Standards can be revised, and compliance is a system-level question.

## Cross-domain meaning

Future preservation may rely on signatures and key custody, but the current archive is not an authenticated global storage network.

## Source orientation and recoverability

- [NIST FIPS 180-4 Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — original publisher bytes unavailable in this package.
- [NIST FIPS 203 ML-KEM key encapsulation standard](https://csrc.nist.gov/pubs/fips/203/final) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
