# ATLAS FORGE — Recover Computer Architecture v0.1.0 offline

## Recover the one original federation

Restore the **exact** predecessor `ATLAS_COLLECTION_Manufacturing_v0.2.0_MERGED.zip` (SHA-256 `018dda14277a1980748c2a4fbaa95d73dc0b3a7680d4008ef754db796a56f894`) from its verified earlier release chain. Apply the `Computer_Architecture_v0.1.0` incremental patch with its own `PATCH_MANIFEST.json` and `RESTORE_ATLAS_FORGE_COMPUTER_V01.py`. The restorer must verify predecessor SHA-256, each patched member, all resulting source-file hashes, and the exact reconstructed full ZIP digest. Extract to an empty directory.

## Validate the federation

```sh
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /independent/fresh/results
```

## Run the standalone software example

From `COMPUTER-ARCHITECTURE-ATLAS` (Python 3.10+):

```sh
python -m unittest discover -s tests -q
python -m computer_atlas
python evidence/independent_oracle.py
```

`python evidence/continuity_challenge.py` also imports the existing Manufacturing and Electronics nodes from the same federation root. It must pass the AT8 software trace while reporting **12 missing physical evidence types**, not certify a fabricated CPU. The normal AT8 reference uses only the Python standard library; no model API or network is required.

## Evidence limits

This edition reconstructs a software instruction set, not a transistor fab, hardware computer, compiler, OS, or AI accelerator. Primary publisher-original files, independent reviewer signoff and calibrated hardware remain HOLD.
