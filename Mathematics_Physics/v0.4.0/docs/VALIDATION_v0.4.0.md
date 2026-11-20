# Mathematics & Physics Atlas v0.4.0 — verification and limits

This edition supplies original 2D linear electrostatics, matrix-free Jacobi-PCG, discrete Gauss flux, finite-grid boundary cases and independent small dense NumPy solver comparisons. The source-tree and extracted-archive test receipts are separate files in the v0.4 incremental release. Tests of numerical finite cases are not laboratory experiments, rights authentication or general theorem proofs.

- Deterministic NumPy dense 2D system oracle: 144 random well-posed systems, 3,356 independently compared nodal voltages, independent operator residuals and boundary-charge balance; maximum observed absolute potential difference ~1.21052e-11 V.
- Manufactured analytic sine continuum test: 7,15,31,63 interior nodes per axis; ratios ~4.0233,4.0058,4.0014 when h halves, consistent with second-order spatial error for this smooth test.
- Core Python 3.10+ implementation requires only the standard library. NumPy is optional for the separate oracle.
- No physical measurements, measured semiconductor carrier dynamics, authenticated publisher transport files, independent expert review or real-model AI performance benchmark.

See `SCOPED_V1_GATES.md` and the release receipt for final cross-federation tests, historical byte-preservation, exact archive restoration, and source-audit status.
