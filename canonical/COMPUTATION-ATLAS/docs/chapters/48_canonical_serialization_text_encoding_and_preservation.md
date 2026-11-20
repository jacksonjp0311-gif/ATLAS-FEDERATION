# Chapter 48 — Canonical serialization, text encoding and preservation

**Area:** Information. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Knowledge preservation requires deterministic interchange formats and explicit text encoding. A computer stores bytes, not abstract characters. Unicode code points, normalization, grapheme clusters and UTF-8 sequences must be distinguished before claiming that two text strings are equal. Canonical serialization aims to give one deterministic byte representation for a specified data model, making content hashes comparable across software versions. Sorting JSON keys is helpful but is not a complete standard for every number, Unicode or floating-point edge case. The exact canonicalization specification must be named and preserved.

## Mathematical contract

Digest = SHA256(canonical_bytes(record)). Byte equality under the same canonicalization implies equal digest; digest equality does not prove source authenticity or semantic truth. For UTF-8, one Unicode scalar may occupy multiple bytes.

## Derivation and reasoning

A content-addressed record can preserve revision identity only when canonicalization rules are stable and the expected hash is trusted. A file and its listed hash can both be replaced; cryptographic hashing alone does not authenticate its original publisher. Unicode normalization can change byte sequences while preserving some user-visible text. Differences may be important for search, source citations and author names; the archive should preserve original bytes and separately record normalized views.

## Worked reconstruction and independent check

Serialize {"b":2,"a":1} and {"a":1,"b":2} under the exact sorted-key subset and confirm the same digest. Then serialize a NaN and confirm the implementation refuses non-JSON values rather than silently using implementation-specific tokens. Compare composed and decomposed accented letters as UTF-8 bytes.

## Limitations, falsification, and invalid use

The `canonical_json_digest` reference is intentionally not a full RFC 8785 implementation and should never be labeled interoperable JCS. Signing and archival authorization need separate issuer identity and key lifecycle.

## Cross-domain meaning

This is essential for ATLAS FORGE source closure and future Bitwork context packets, but it does not change the current router.

## Source orientation and recoverability

- [Python decimal module: rounding, context and arithmetic](https://docs.python.org/3/library/decimal.html) — original publisher bytes unavailable in this package.
- [NIST FIPS 180-4 Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
