# Reconstruct Electronics v0.2 inside the original ATLAS FORGE federation

1. Verify the exact predecessor Electronics v0.1 full-federation ZIP by SHA-256 and compare historical roots; never overwrite the old archive.
2. Apply the new direct v0.2 delta through its restore utility, checking every member and file hash.
3. Extract to a clean directory and run `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, `python tools/check_collection.py --out /fresh/output_dir`.
4. Within `ELECTRONICS-SEMICONDUCTORS-ATLAS`, run `python -m unittest discover -s tests -v`; with NumPy/SciPy/mpmath locally installed, run `python evidence/independent_oracle_v02.py`.
5. Read 18 original chapters, the machine-readable records and their source/gap statuses. Use `electronics_atlas/v02_models.py` independently of cloud computation.

No Bitwork routing, new query schema, or desktop transfer is part of this edition.
