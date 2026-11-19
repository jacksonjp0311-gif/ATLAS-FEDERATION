# CRYPTOGRAPHIC PROTOCOLS ATLAS — priority 14 · scoped v1.0.0

A technical reference **inside the one canonical ATLAS FORGE federation**, not a second Atlas or a deployable encryption stack.

- 18 authored scientific chapters, 15 official bibliographic links, explicit negative controls and cross-domain exact-revision dependencies.
- Pure-Python standard-library educational models of HMAC-SHA-256, HKDF-SHA-256, TLS 1.3 label/nonce arithmetic, canonical binary framing, a MAC-only authenticated-session simulation, anti-replay window and Merkle inclusion proofs.
- Independent oracle uses published HMAC/HKDF test vectors plus alternate algorithms and finite counterexamples.
- Current TLS authority is **RFC 9846 (July 2026)**; older RFC 8446 is superseded.

```bash
python -m unittest discover -s tests -q
python evidence/independent_oracle.py
python -m crypto_atlas
```

**Security warning:** The authenticated-session simulation provides no encryption, public-key authentication, forward secrecy, protection of persistent nonces, secure randomness, safe key storage or robustness to concurrent real-world delivery. It must not be deployed. Read `docs/SCIENTIFIC_AND_OPERATIONAL_HOLD_v1.0.0.md` before reuse.

See `docs/DEPTH_MANUAL_v1.0.0.md` for the complete human-readable reference, and `data/` for exact-revision AI retrieval.
