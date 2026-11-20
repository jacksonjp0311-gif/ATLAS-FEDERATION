# Mathematics & Fundamental Physics v0.2.0 — executed verification and limitations

This is an incremental mathematical and computational reference release, not scoped scientific v1.0.

## Executed evidence

- The complete twelve-node federation replay passed **2,059** unit tests across 17 groups, zero failures/errors/skips. The original v0.1.0 Math/Physics test files were replayed from a SHA-preserved frozen historical snapshot; historical Chemistry/Energy and other suites remain original.
- **94** source-linked context packages validated against exact current revisions, and the collection schema compilation passed.
- **1,320** new independent numerical comparison cases passed versus NumPy LAPACK/FFT and distinct analytic ODE/PDE solutions. **120** deliberate bad-domain inputs were rejected. Numeric tolerances, seeds and the largest observed errors are in `../evidence/independent_numeric_oracle_v0.2.0.json`.
- The new v0.2.0 wheel installed offline with `--no-index --no-deps` and executed the previous 22 and added 6 examples; its embedded exact-version common registry was present.
- **4,682** previous manifest-tracked files preserved byte-for-byte, **36** changed only within allowed new-edition Math/Physics, index, registry, roadmap pointer and runner metadata; no previous files deleted and original 164 Math records/152 Math relations had identical revision envelopes and unchanged JSONL prefixes.

## Scientific and archival boundaries

Householder QR here assumes an overdetermined full-rank matrix (no pivoting), singular values are analytic only for **2×2** matrices, FFT accepts power-of-two lengths, scalar step-doubling RK4 is not stiff-stable and has no general error theorem, and 1D heat/wave models depend on declared linear boundary conditions and discrete stability criteria. No 3D electromagnetism, real device, physical apparatus calibration, independently peer-reviewed scientific result, demonstrated AI benchmark improvement, general SVD or authenticated original publisher media is claimed. The code is designed to **refuse** unsupported input domains.

## Reproduction

In an extracted twelve-node release root:

```sh
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /tmp/atlas-fresh-validation-unique
```

For the local package:

```sh
cd MATHEMATICS-PHYSICS-ATLAS
python -m unittest discover -s tests -q
python tools/independent_oracle_v02.py
```

Full release restoration and extracted-root replay receipts are in the external incremental release folder. Historical verified v0.1 manifests remain independently retrievable from the Library.
