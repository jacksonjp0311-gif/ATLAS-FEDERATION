# Offline reconstruction and scientific custody

1. Restore the exact 13-node Electronics & Semiconductors v0.4.0 release from its verified historical chain.
2. Apply the direct Manufacturing v0.1.0 delta using the release restore script and ensure exact full-archive SHA-256 equality.
3. Extract into a new directory, run `python tools/check_manifest.py verify .` and `python tools/survival_audit.py --root . --check-files`.
4. Run `python tools/check_collection.py --out /new/external/output` and `python -m unittest discover -s tests -q` inside `MANUFACTURING-ATLAS`.
5. Read the generated manifest, source register and evidence limits; keep every prior release immutable.

Before physical reconstruction, separately qualify calibration chain, environmental controls, dimensional accuracy, materials, machine guarding, structural loads, electrical isolation, responsible operations and process hazards. Nothing in this package authorizes unsafe operation.
