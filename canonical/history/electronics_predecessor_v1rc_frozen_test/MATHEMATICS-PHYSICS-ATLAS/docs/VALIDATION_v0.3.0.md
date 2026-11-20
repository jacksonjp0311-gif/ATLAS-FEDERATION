# Mathematics & Fundamental Physics v0.3.0 — software validation and scientific boundaries

This document records the SOURCE-TREE test results and scientific limits. The independent sealed-release replay is recorded in the later v0.3.0 release receipt outside the archive; it was **not yet performed when these source bytes were sealed**.

- Full-federation source-tree runner: **2,085 tests passed**, 0 failures, 0 errors, 0 skips across 18 separately versioned suites. The historical Math v0.1.0 64-test and v0.2.0 72-test suites were run from their exact frozen snapshots; current v0.3.0 tests passed 26 cases. These are software tests, not 2,085 independent physical experiments.
- **12 federated nodes, 2,564 records, 1,719 relationships, 500 bibliographic cards.** All 98 source-linked contexts passed closure/replay; complete compiled-schema validation passed for 2,564 records and 1,719 relations, with bounded Draft 2020-12 samples rather than full exhaustive Draft validation.
- New NumPy/analytic oracle: **1,300 deterministic finite comparisons plus 120 invalid-input refusals**, zero failed checks; floating-point comparison only, not independent scientific peer review.
- Four authored chapters, four constructed cases and new standard-library kernels for bounded real Jacobi SVD, truncated pseudoinverse, constant-epsilon 1D electrostatics, backward Euler and Crank–Nicolson diffusion.
- **Zero** authenticated locally archived publisher originals, experimental data, independently accepted physics results or demonstrated AI accuracy/performance improvements.

## Acceptance boundaries

The SVD uses a finite 32x32 real reference algorithm with chosen relative-rank cutoff and explicit nonconvergence rejection; it is not a production-grade large-scale SVD. The Poisson example assumes known constant dielectric and 1D boundary data; semiconductor physics is not implied. The heat models assume constant diffusivity and fixed boundaries, with Crank–Nicolson potentially sign-oscillating under large Fourier numbers. Neither source pointers nor numerical tests establish empirical truth.

## Offline checks

`python -m math_physics_atlas` validates constructed teaching cases. `python -m unittest discover -s tests -q` tests current package behavior; the full collection's version-aware runner includes the original historical suites. NumPy is only needed for optional `python tools/independent_oracle_v03.py`. Fresh archive recreation, integrity and historical preservation must be independently rerun from published v0.2 baseline before public promotion.
