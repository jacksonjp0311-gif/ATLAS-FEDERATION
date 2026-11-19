# ATLAS FORGE — Compiler Design v0.1.0 one canonical federation

Original predecessor: Database Optimization v1.0.0 full archive SHA-256 `13d8f5d19ed98d052dad9c424b22295599722b82a2938ec6f94f2a95122fe8c2`.

## Offline deterministic restoration

Place `RESTORE_ATLAS_FORGE_COMPILER_V01.py`, the direct incremental ZIP, and the exact predecessor ZIP in a local directory. Run:

```sh
python RESTORE_ATLAS_FORGE_COMPILER_V01.py /exact/Database_Optimization_v1.0.0.zip ./ATLAS_COLLECTION_Compiler_Design_v0.1.0_DELTA_from_Database_Optimization_v1.0.0.zip ./ATLAS_COLLECTION_Compiler_Design_v0.1.0.zip
```

The restore checks original predecessor SHA, patch member identities and hashes, all final source file hashes and full deterministic ZIP SHA. Extract into a new directory. Verify file inventory with `python tools/check_manifest.py verify .`, run the 24-node integrity audit and `python tools/check_collection.py --out /new/empty/directory`; compare results with source receipt.

Compiler source and documentation: `COMPILER-DESIGN-ATLAS/`. Library retains every prior historical release in its same original federation. Complete archive is reproducible from Library base volumes plus the successive signed-hash delta chain; do not create a separate Atlas.
