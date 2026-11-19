# ATLAS FORGE Compiler Design v0.2.0 — one original complete federation

Exact base archive Compiler Design v0.1.0 SHA-256 `cfd36e91dd1a093bf1edbd8a752f1fd6505e66123c577d167ed0f687c1381ebd`.

## Restore offline

```sh
python RESTORE_ATLAS_FORGE_COMPILER_V02.py /exact/Compiler_Design_v0.1.0.zip ./ATLAS_COLLECTION_Compiler_Design_v0.2.0_DELTA_from_Compiler_Design_v0.1.0.zip ./ATLAS_COLLECTION_Compiler_Design_v0.2.0.zip
```

That program checks exact predecessor SHA, each changed file hash, every final file hash and the full reconstructed deterministic ZIP. Extract to a fresh directory, then run:

```sh
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /new/empty/directory
```

The original 24-node Compiler v0.1 acceptance is preserved and run against `history/compiler_design_v0.1.0_acceptance_snapshot`. All Compiler v0.1 scientific records and relations retain exact revisions. The v0.2 source and tests are at `COMPILER-DESIGN-ATLAS/`. No hardware or independent expert acceptance implied.
