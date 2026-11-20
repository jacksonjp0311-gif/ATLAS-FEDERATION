# Chapter 10 — Deterministic compiler artifacts, provenance and restoration

Reproducibility requires identifying the *input source*, compiler edition, declared semantics, normalization, validation policy and output serialization. This reference's bytecode encoder produces sorted-key, compact UTF-8 JSON with an explicit language identity `atlas-compiler-tiny-i32/1`; the same source and flags produce the same bytes. Its SHA-256 digest is suitable for integrity checks only when the expected digest is anchored independently.

A correct federation release involves more than serializing new code. Source documents and corpus data have exact file hashes, record revisions and source relationships. The incremental patch is from the **specific Database Optimization v1.0.0** canonical predecessor, whose archive SHA-256 is `13d8f5d19ed98d052dad9c424b22295599722b82a2938ec6f94f2a95122fe8c2`.

The release process must verify that no old science data or original 30-domain queue entry was deleted, changed outside the authorized integration files, or silently reassigned a different revision. The deterministic patch is applied to the exact prior archive, a new whole-federation ZIP is reconstructed and compared byte-for-byte to the development ZIP, then the full test suite runs again in the restored source tree.

**Failure controls:** Wrong predecessor digest, missing patch member, extra member, path traversal, duplicate ZIP member, wrong uncompressed file SHA, wrong full archive SHA, malformed source-linked record revision and mismatched source/fresh test receipts. These produce `FAIL_CLOSED`; no authoritative checkpoint advances.

**External limit:** SHA-256 on its own does not authenticate the person or organization who created the archive. Cryptographic signatures, trusted keys, reproducible toolchains across different machines and physical storage reliability require separately validated components.
