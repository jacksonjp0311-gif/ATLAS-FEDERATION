# Atlas Federation — deterministic offline restoration

Original program: ATLAS FORGE. Public display name: Atlas Federation.

## Canonical checkpoints

- Compiler Design v0.1.0 full base SHA-256: `cfd36e91dd1a093bf1edbd8a752f1fd6505e66123c577d167ed0f687c1381ebd`.
- Compiler Design v0.2.0 delta: 3,233,432 bytes; SHA-256 `4cbe54fe29729c8895670f1efa31628d1501a848593a677798424dd03e46b3ed`.
- Compiler Design v0.2.0 complete deterministic ZIP: 735,193,042 bytes; SHA-256 `0ca19d26cda186a43ed994b9a2c9bb87b38d90d65a07f4ba4edde3a8ccfafae7`.

## Reconstruct from authenticated original predecessor and delta

Obtain the **exact** original v0.1.0 complete archive and v0.2.0 delta (not merely files from this GitHub import). The published restoration script and patch manifest live in `Releases/Compiler_Design_v0.2.0_incremental/`. Run:

```sh
python Releases/Compiler_Design_v0.2.0_incremental/RESTORE_ATLAS_FORGE_COMPILER_V02.py \
  /path/to/Compiler_Design_v0.1.0.zip \
  /path/to/ATLAS_COLLECTION_Compiler_Design_v0.2.0_DELTA_from_Compiler_Design_v0.1.0.zip \
  ./ATLAS_COLLECTION_Compiler_Design_v0.2.0.zip
```

Verify the resulting SHA-256 before extraction:

```sh
python -c "import hashlib,sys; p=sys.argv[1]; print(hashlib.sha256(open(p,'rb').read()).hexdigest())" ATLAS_COLLECTION_Compiler_Design_v0.2.0.zip
```

In a fresh extracted directory, run the historical verification entry points (when present):

```sh
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /new/empty/directory
```

Historical receipts report 3,405 tests and identical source/fresh replay reports, but those results are not a substitute for a new reproducible run.

**Note:** Browsable GitHub source and checksums alone cannot reconstruct the complete federation without its original full predecessor ZIP and delta.
