# Software Design Patterns — Offline reconstruction procedure

1. Restore the exact predecessor `ATLAS_COLLECTION_Bioelectric_v0.1.0.zip` (SHA-256 `685e9d8d610c1714eab4a1a11eef6006845be10982b5213184b1182ff6218ff5`) from the original historical releases.
2. Apply the new versioned incremental patch using its `RESTORE_ATLAS_FORGE_PATTERNS_V01.py`, embedded `PATCH_MANIFEST.json`, and per-file digests. Verify exact complete full-ZIP SHA-256 against the versioned release receipt before accepting it.
3. Extract into a clean directory; run full file manifest, common registry, schema, tests and historical preservation audit. Run `python -m patterns_atlas` and the independent oracle without internet access.
4. In the node's demo, commit one pure SQLite command, simulate interruption after another database commit but before the secondary snapshot, close all connections, then reopen and recover. Verify two commands and the new content-addressed snapshot.
5. Intentionally reuse a command ID with a different payload and damage a blob; both must be rejected. Demonstrate that the event-chain head cannot silently reset after corruption.
6. On a real Windows device, copy the complete package to two different storage media and test their read/restore hashes with a clean Python interpreter. This software-only exercise does not test actual battery or controlled power failure.

**Scientific and safety HOLD:** authenticated publisher originals, independent peer review, target hardware power-cut tests, filesystem durability characterization, secure key/trust origin, and any external actuator semantics.
