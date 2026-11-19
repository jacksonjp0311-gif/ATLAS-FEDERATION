# Fully offline ATLAS recovery and preservation

## If you have the full ZIP or its split parts

1. Copy all `ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip.partNNN` files, `FULL_ARCHIVE_PARTS_MANIFEST.json`, and `RESTORE_FULL_ATLAS.py` into a single folder.
2. On a Python 3.10+ interpreter, run `python RESTORE_FULL_ATLAS.py --parts-dir . --output ./ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip`.
3. The restore script verifies each volume SHA-256, verifies part order and total length, and matches the complete archive SHA-256. **It refuses to overwrite an existing output** and rejects unsafe names or missing parts.
4. Inspect the restored ZIP before extraction and ensure it has exactly one declared collection root; the restore script checks that too.
5. Extract the archive to a clean, empty directory. Never extract a third-party ZIP blindly with a script that allows `../` or absolute file paths.
6. From the extracted collection root run the following. All three use the Python standard library:

```sh
python tools/atlas_offline.py catalog
python tools/atlas_offline.py audit
python tools/atlas_offline.py challenge
```

`audit` checks the complete file inventory, each file SHA-256, all node registry/manifests/collections, each record/relation revision and the exact endpoints of every relationship. The fixed `challenge` checks the source-to-machine software reconstruction. Neither proves original-source authenticity or physical engineering.

## If you have only the incremental patch

You **must** possess the exact verified `ATLAS_COLLECTION_Computer_Architecture_v0.4.0.zip` predecessor. Apply `RESTORE_ATLAS_FORGE_CONTINUITY_V01.py` using its declared base digest and target digest, and then perform the same offline audit.

If the predecessor is missing, recover the original historical nine-part Energy archive and its verified incremental chain, with the exact hashes preserved in `SURVIVAL/RELEASE_LINEAGE_VERIFICATION.json` and the previous Library release folders. The separate original patch chain is not included inside the full current ZIP.

## Disaster-recovery copies

Maintain multiple copies on independent physical media and in distinct geographic or administrative failure domains. Keep the recovery script, manifest and a printed `READ_ME_FIRST.txt` alongside each set. Test restoration on a disconnected system periodically, record scrub dates, replace failing media, and compare independently retained SHA-256 digests. Do not rely on any one cloud account as the sole store.

The archive contains historical research and possibly third-party material whose redistribution rights require review. A user-owned private recovery copy should not be described as a rights-cleared public redistribution pack without a separate rights audit.
