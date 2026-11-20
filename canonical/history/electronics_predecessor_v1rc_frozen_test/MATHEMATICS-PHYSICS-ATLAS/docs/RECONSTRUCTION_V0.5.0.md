# Mathematics & Physics v0.5.0 — Cold-start scientific reconstruction

This is a **scientific software reference**, not a finished semiconductor device simulator.

## From the compact release

Start with the exactly verified v0.4 federation full ZIP (archive SHA specified in the v0.5 release manifest). Apply the v0.5 incremental patch using `RESTORE_MATHEMATICS_PHYSICS_V05_COLLECTION.py`. This verifies the baseline ZIP digest, delta member digests, every final source file and the exact reconstructed ZIP SHA. No Bitwork routing and no online resources are required for restoration.

## Standalone implementation

1. Read Chapters 53–56 after the frozen earlier chapters; keep `u=V/U_T` dimensionless.
2. Recreate the tridiagonal Jacobian of `-alpha u''+beta sinh(u)=f` and check the discrete flux identity.
3. Recreate `B(z)=z/expm1(z)` with `expm1` and small/large-argument branches; verify `B(-z)=B(z)+z`.
4. Implement the single-edge exponential-fitting formula with stated particle-flux sign and units. Verify both Fick diffusion and exact local Boltzmann equilibrium.
5. Run `python -m unittest discover -s tests -p 'test_v05_*.py' -q` and `python -m math_physics_atlas`.
6. Optionally run `python tools/independent_oracle_v05.py` with NumPy/SciPy; the ordinary models use the Python standard library alone.
7. Record residual versus manufactured continuum error; never treat software performance as device measurements.

**Unavailable evidence:** no experimental material parameter calibration, no electron-hole continuity coupling, no independent expert reviewer, and no locally authenticated original publisher transport document. Preserve original research explanations with bibliographic source links rather than asserting copyrighted publisher files are mirrored.
