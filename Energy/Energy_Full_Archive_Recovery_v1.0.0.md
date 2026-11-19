# Energy Atlas v1.0.0 — Complete 10-node archive recovery

The original, verified ten-node ZIP is **594,686,370 bytes**. The ChatGPT Library cannot store it as a single file, so the full archive is preserved in nine non-overlapping parts in:

`/ATLAS FORGE/Releases/Energy_v1.0.0_full_archive_parts`

Download every `ATLAS_COLLECTION_Energy_v1.0.0.zip.part001` through `.part009` together with `MULTIPART_MANIFEST.json` and `RESTORE_FULL_COLLECTION.py` into a single directory. On a machine with Python 3.10+ run:

```sh
python RESTORE_FULL_COLLECTION.py --dir .
```

The script validates every part's SHA-256, reconstructs exactly `ATLAS_COLLECTION_Energy_v1.0.0.zip`, verifies the full archive SHA-256 **`cb896893ee984ebc0d7b92af8c921e1ce4da75891a90101c052e109029e462f2`**, and then checks ZIP content integrity.

After extraction, run `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, and `python tools/check_collection.py --out /external/output`. A release-success result means the package is structurally sound; it does **not** certify real equipment or all science.

**Version preservation:** all ten prior nodes remain unchanged except the active Energy node's append-only new records and the top-level release registry. The v0.2 full archive remains separately recoverable in its earlier Library folder.
