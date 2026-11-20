# Offline reconstruction

Python 3.10+ only. No internet required for locally authored material.

1. Read `README.md`, `docs/SOURCE_REGISTER.md`, `docs/SCOPED_V1_GATES.md`.
2. Run `python -m unittest discover -s tests -v` and `python -m electronics_atlas` from package root.
3. Verify the shared `common/registry.json` and `common/registry.lock.json` through `AtlasStore`; never bypass record/relation revision hashes.
4. Check source tree manifests, qualified graph relationships and 13-node federation.
5. Restore from canonical predecessor full archive and signed-by-hash incremental patch; do not replace original 12-node release files.

Model-fidelity evidence is separate from implementation or archival integrity.
