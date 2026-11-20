# Reconstruct Electronics v0.3.0 offline

1. Restore the exact v0.2.0 full federation ZIP from the existing ATLAS FORGE historical recovery chain. Verify its SHA-256.
2. Apply the v0.3.0 direct delta with `RESTORE_ATLAS_FORGE_ELECTRONICS_V03.py`; validate all member and full ZIP digests before extracting into a new directory.
3. From the extracted federation root run `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, and `python tools/check_collection.py --out /new/unique/output`.
4. From `ELECTRONICS-SEMICONDUCTORS-ATLAS`, run `python -m unittest discover -s tests -q`; optionally run `PYTHONPATH=. python evidence/independent_oracle_v03.py` with NumPy available.
5. Review negative cases, RC time-step error, and unknown-state behavior before consuming any result in a real instrument or hardware design.

No cloud service, model inference, routing framework or experimental hardware is required to reproduce the **software** evidence.
