# v0.3.0 independent reconstruction and numerical oracle protocol

**Prerequisite:** verified exact Mathematics & Physics v0.2.0 original archive. This edition must be reconstructed from that byte-identified baseline plus the incremental patch, not inferred from a conversation transcript.

1. Verify original v0.2 full archive SHA-256 against the v0.2.0 preserved checkpoint.
2. Apply `RESTORE_MATHEMATICS_PHYSICS_V03_COLLECTION.py` with the new delta; validate old archive SHA, all delta member SHA, every reconstructed file SHA, final full ZIP SHA, and deterministic source-tree member inventory.
3. In the fresh extraction, run `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, and `python tools/check_collection.py --out /separate/new/report-dir`. Keep its output outside the manifest-tracked tree.
4. Run `python -m math_physics_atlas` and v0.3 tests; optional NumPy oracle uses a different linear-algebra implementation and dense solves for finite cases.
5. Verify historical v0.2 files and record/relation revisions separately; the old v0.1 tests and v0.2 test suite must run unchanged on their own exact snapshots.

**Do not label** NumPy checks as peer review, measured electrical fields, semiconductor validation, physical scientific truth, authenticated publisher files or AI improvement. Source anchors are bibliographic. For physical claims, plan separately for measurement calibration, data rights, uncertainty, boundary verification, independent expert replication and named reviewer receipts.

**Numerical boundaries:** dense real 32x32 singular-value computation; a truncated rank-ratio cutoff, unpivoted tridiagonal Thomas elimination, constant-epsilon 1D Poisson, constant-diffusivity 1D heat. Cases beyond these limits must refuse or require a new scoped model with validated input contracts. Bitwork is not included.
