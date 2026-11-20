# ATLAS FORGE — Computer Architecture v0.3.0 offline reconstruction

This edition extends the **original canonical 15-node federation** from exact Computer Architecture v0.2.0. It must not become an independent Atlas.

## Source-layer reconstruction

Use Python 3.10+ with no cloud API. From `COMPUTER-ARCHITECTURE-ATLAS`:

```sh
python -m unittest discover -s tests -p 'test_v03_*.py' -q
PYTHONPATH=. python evidence/independent_oracle_v03.py
PYTHONPATH=. python evidence/reconstruction_challenge_v03.py
```

The complete 15-node federation includes a version-aware runner preserving the original v0.1 86 tests, the v0.2 56 tests, and current v0.3 tests. Do not rewrite historical counts or edit the old test fixtures to fit new node counts.

## Boot and execution acceptance

1. Decode AT8R/3 header using fixed 44-byte layout and check exact ROM size, CRC, SHA and ISA syntax.
2. Simulate A/B slots; interrupted staging cannot supplant a known valid committed image.
3. Recover bounded single-bit ECC corruption; reject detected double errors and reconstructed hash mismatches.
4. Run the independent source evaluator, architectural interpreter and microcycle interpreter with identical finite input tapes.
5. Verify full observable RAM, register R0, output tape, input-consumption counters, HALT or explicit failure state.
6. Create canonical JSON receipts; reproduce hashes in an independent process and store negative cases.
7. Check the existing Manufacturing physical-evidence gate. It must remain HOLD on missing calibrated hardware evidence.

## Federated historical recovery

Restore the exact verified predecessor `ATLAS_COLLECTION_Computer_Architecture_v0.2.0.zip` (SHA-256 `ed06f0d2d22ebb9c6f5016e94ccff285b90eb4139ecc2dfc2cc9a324ce7674f3`) from prior releases. Apply the v0.3 direct incremental patch and independently check its manifest, exact full-ZIP SHA, all target file hashes and the full federation suite from a fresh extraction. The previous scientific nodes and original 30-domain roadmap must be byte-identical; no Bitwork router work.

**Limit:** No actual boot ROM, authenticated firmware signer, hardware flash, OS process scheduler, physical cache, silicon CPU or calibrated device test is present. The new version is a reproducible educational/software foundation.
