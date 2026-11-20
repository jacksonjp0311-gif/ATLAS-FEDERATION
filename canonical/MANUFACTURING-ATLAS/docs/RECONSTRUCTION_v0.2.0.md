# Offline reconstruction — Manufacturing v0.2.0 merged canonical federation

1. Obtain exact Electronics & Semiconductors v1.0.0-rc.1 full federation ZIP with SHA-256 `2b24bd5a3fbb6e9b51887ce2bea68dd0b2a0b0c728521b4ac5b483d457d6ebb8`.
2. Apply Manufacturing v0.2.0 direct incremental ZIP, pinning its `PATCH_MANIFEST.json` and target full-archive checksum.
3. Extract to a fresh directory; run `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, `python tools/check_collection.py --out /separate/results`.
4. In `MANUFACTURING-ATLAS`: `python -m unittest discover -s tests -q`, `PYTHONPATH=. python evidence/independent_oracle_v02.py` (NumPy/SciPy optional for independent oracle; stdlib for models).
5. Run the cross-domain reconstruction challenge, retain missing physical evidence as HOLD. Do not relabel synthetic metadata as fabricated silicon.

The prior Manufacturing v0.1 fork is preserved in `/ATLAS FORGE/Releases/Manufacturing_v0.1.0_incremental/`, with its 18 chapters and 46 original tests; this release reconciles it with the later Electronics v1rc mainline. No historical source files are removed or altered.
