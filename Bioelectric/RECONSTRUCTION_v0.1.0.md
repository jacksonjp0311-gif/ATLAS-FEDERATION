# ATLAS FORGE — Bioelectric Atlas offline reconstruction

**This is the 16th node in the ONE original ATLAS FORGE federation.** Its priority is #9 in the immutable thirty-domain queue. It does not create a second Atlas or reorder the roadmap.

## Software-only reproduction (Python 3.10+ standard library)

From `BIOELECTRIC-ATLAS`:

```bash
python -m unittest discover -s tests -q
PYTHONPATH=. python evidence/independent_oracle.py
PYTHONPATH=. python evidence/reconstruction_challenge.py
```

From the restored federation root:

```bash
python tools/check_manifest.py verify .
python tools/check_manifest.py verify BIOELECTRIC-ATLAS
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /outside/a/new/result/folder
python tools/verify_bioelectric_v01_preservation.py --base-archive /path/to/ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip --target . --out /outside/federation_historical.json
```

The new node is only an additive scientific-content release; all prior fifteen node manifests and old revision bytes remain unchanged. Preserve the original queue in `DOMAIN_QUEUE.json`. Next unregistered original domain after registered Manufacturing priority #10 is Software Design Patterns priority #11.

## Caution

No body-connected hardware, tissue stimulation, medical experimentation, clinical inference, calibration or independent peer review is present. The 18 worked investigations are entirely constructed computational examples.
