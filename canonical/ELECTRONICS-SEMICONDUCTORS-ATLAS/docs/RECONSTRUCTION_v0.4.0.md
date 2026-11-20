# ATLAS FORGE — Electronics v0.4.0 reconstruction and test instructions

This is the **same original ATLAS FORGE federation** with an Electronics node content increment. Never reinterpret the standalone wheel as the entire collection.

## Offline model usage

From the source checkout, Python 3.10+ and no network:

```sh
python -m unittest discover -s tests -q
PYTHONPATH=. python evidence/independent_oracle_v04.py
```

No hardware-validation claim follows from these numerical results. The full federation uses the inherited `tools/check_collection.py --out /path/out` and `tools/check_manifest.py verify .` with unchanged shared schema.

## Exact preservation and restoring the federation

The increment must be built against the verified `ATLAS_COLLECTION_Electronics_Semiconductors_v0.3.0.zip`, whose recorded SHA-256 is `2e6e896386154d3c5e17e650606ae22576719812d55b6af46c2034765c70af60`. The earlier 12 scientific nodes, versioned records and 30-domain roadmap remain byte-identical. Apply only a direct incremental patch after validating both baseline and patch checksums. Exact per-file hash verification and extracted release test replay are required; do not silently accept a ZIP compression mismatch as exact full-archive equality.

## Physical science and manufacturing requirements

To leave the software-only reference stage, retain raw measured voltage transfer curves, loading/temperature/clock-corner timing, contact resistance, deposition/doping parameters, instrument calibration chain, chip/wafer identification, and experiment uncertainty. Independently verify source-to-equation mappings from original publisher bytes and arrange qualified engineering review. Nothing in this Python edition is a fabricated integrated circuit.
