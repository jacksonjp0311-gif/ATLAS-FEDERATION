# ATLAS FORGE — Cryptographic Protocols v1.0.0 original federation

**ONE original 20-node canonical federation**. This scoped v1.0.0 content increment extends the exact Neural Architectures v1.0.0 predecessor (not a second project). It contains **3,689 exact-revision records, 2,875 qualified relationships, 601 bibliographic source cards**, and preserves the original 30-domain queue byte-identically. Of the original candidates, **14/30 are represented** and **16 are unregistered**.

## Original scientific content — domain priority #14

18 authored technical chapters and their exact-revision scientific records; 15 source cards, 87 new records and 108 exact-revision relationships. Topics include threat models, canonical message framing, entropy and nonces, HMAC-SHA-256, HKDF-SHA-256, TLS 1.3 key schedule arithmetic, AEAD design constraints, anti-replay windows, handshake transcript concepts, digital signatures, key agreement, hybrid public-key encryption, key lifecycle, Merkle proofs, signed updates, offline provenance, and verification limitations.

Software is **standard-library-only educational reference implementation**, not a real TLS stack or deployable cryptographic solution. The demo is MAC-only and **does not encrypt**. Source edition RFC 9846 (July 2026) obsoletes RFC 8446; historical sources are retained with explicit edition qualifiers.

## Verified engineering evidence

- **3,119 source-tree federation tests and 3,119 fresh-restored tests**, 45 suites, 261 validated source-linked contexts; test reports byte-identical, SHA-256 `8d2d02ed5ac52c25644e6d12efeff72c8a138dbfe5880b2d1ce85b6d85011943`.
- **75 local unit tests**, **30,555 independent finite oracle comparisons**, RFC 4231 HMAC and RFC 5869 HKDF published vectors plus independent finite models and failure controls.
- Full reconstructed archive **721,723,439 bytes**, SHA-256 `6801f779b9f50ab8318ff13a71608548f124ed9eb84fea95f0a7d7a41fbb8090`; incremental delta **2,863,472 bytes**, SHA-256 `645d766c12a7276a9b1ce2a27c04e67906e56a45e31c8d5d36cc29880ae6a6dd`.
- **10,379 source-file SHA-256 values**, 242 changed-member hashes and exact reconstructed ZIP verified. **10,138 prior files byte-identical**, 7 authorized integration changes, 234 new files, zero deletions. Previously registered 19 scientific nodes preserved.

## Where everything lives

- `/ATLAS FORGE/Cryptographic_Protocols/`: versioned original chapters, complete manual, source register, scientific HOLD document, corpus JSONL collections, Python source, tests and independent oracle.
- `/ATLAS FORGE/Releases/Cryptographic_Protocols_v1.0.0_incremental/`: direct deterministic delta, restoration script, precursor snapshots and fresh/source validation receipts.
- `/ATLAS FORGE/CURRENT_CHECKPOINT.json` and `/ATLAS FORGE/Roadmaps/ATLAS_FORGE_CURRENT_ACTIVE_PRIORITY.json`: updated **only after** verified Library publication and readback.

### Offline reproduction

Restore the exact Neural Architectures v1.0.0 ZIP, then use `RESTORE_ATLAS_FORGE_CRYPTO_V1.py --base <predecessor> --delta <patch> --output <new full ZIP>`.

Inside extracted `CRYPTOGRAPHIC-PROTOCOLS-ATLAS`, execute `python -m unittest discover -s tests -q` and **`python -m evidence.independent_oracle`**. The latter is the supported direct-module command; use `PYTHONPATH=. python evidence/independent_oracle.py` if running as a script on Unix.

## Open scientific and operational gates

Published test vectors and finite reference-model tests do **not** prove implementation security, constant-time behavior, real-network confidentiality, cryptanalytic resistance, key management, physical power-loss recovery, authenticated publisher originals, or independent expert audit. Those evidence gates are **HOLD**. No Bitwork routing or desktop transfer.

**Next original priority: OS Internals #15.**
