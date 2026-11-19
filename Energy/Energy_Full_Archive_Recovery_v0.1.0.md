# ATLAS FORGE Energy v0.1.0 — complete-archive Library recovery

The **Energy Atlas v0.1.0 complete ten-node ZIP** has passed its final extracted 1,656-test replay and integrity check, but the persistent Library rejected the **585,118,030-byte ZIP** as a single upload (`file_too_large`). This is a storage limitation, not a scientific or engineering test failure.

To preserve every historical byte without altering the sealed ZIP, the complete archive is stored in the Library folder:

`/ATLAS FORGE/Releases/Energy_v0.1.0_full_archive_parts/`

This folder contains **nine byte-ordered parts**, `ATLAS_COLLECTION_Energy_v0.1.0.zip.part001` through `part009`, a `MULTIPART_MANIFEST.json` with the SHA-256 of every part, a dependency-free `RESTORE_FULL_COLLECTION.py`, and `START_HERE.txt`.

## Recover the original complete archive

1. Download the entire folder, keeping the original filenames.
2. In a local terminal, run `python RESTORE_FULL_COLLECTION.py .` from the downloaded folder. Requires only Python standard library.
3. The script refuses to overwrite an existing ZIP, verifies all nine part sizes and hashes, joins the bytes in documented order, validates the complete archive SHA-256 and opens the ZIP to check members.
4. The resulting ZIP is **exactly** `ATLAS_COLLECTION_Energy_v0.1.0.zip` and must have SHA-256:

`14f3ed75e27ac0c6649d4e7ea6dc8cb5fa8557d11e3257c06c3195806c9dd173`

This procedure has been **executed and passed** using the actual nine parts from the sealed delivery; the reconstructed ZIP hash and ZIP integrity both matched. The un-split original remains available as a ChatGPT conversation artifact. The smaller `ENERGY-ATLAS_v0.1.0.zip` standalone archive is stored normally under `/ATLAS FORGE/Releases/`.

## Other facts

The full federation contains 10 nodes, 1,927 records and 1,133 relationships. Software tests: 1,656 passed from source and extraction, zero skipped. This does not establish physical energy-system certification. The 455 bibliography/source cards do not currently have authenticated original publisher-byte copies under the strict source survival audit. Those are still essential future preservation work. No Bitwork routing or desktop transfer has been performed.

**Checkpoint decision:** Energy v0.1.0 is verified and stored, with its full ZIP retrievable via this explicit multipart restoration process. Earlier editions and the historical source snapshots remain unchanged.
