# Materials Atlas v0.3.0 — release audit

**Status: passed local engineering checks; scientific content v1 remains open.** Date: 12 November 2026. Python 3.13.5 on Linux.

## Executed checks

| Stage | Result |
|---|---|
| Forge tests | 188 passed |
| Measurement tests | 218 passed |
| Causal tests | 233 passed |
| Materials tests | 104 passed |
| Total tests | **743 passed, zero skipped** |
| Basic numerical oracle | 1,200 comparisons passed |
| v0.2 advanced numerical oracle | 1,440 comparisons passed |
| v0.3 phase/diffraction/Hahn oracle | 90 phase cases, 960 diffraction scalar checks, eight Hahn1 residual bins passed |
| NIST Hahn1 regression replay | Passed, separate SciPy fit algorithms |
| Generic five-node conformance | 760 records, 156 relations; JSON schema passed |
| Three new source-closed context queries | Exact expected roots and validation passed |
| Clean installed Python wheels | Forge, Measurement, Causal and Materials 0.3.0; five nodes, 760 records |
| Original rc1 baseline | 771 original members unchanged |
| Other node snapshots | Signal, Cymatics, Measurement and Causal unchanged |

The exact JSON receipts are in `receipts/materials_v03/`. These checks establish software behavior and agreement between numerical algorithms, not physical scientific validation. The newly authored examples are not independent held-out evidence.

## New methods and evidence boundaries

- Symmetric constant-omega regular solution: explicit Gibbs energy, binodal, spinodal, metastability and equilibrium lever fractions. No real measured phase diagram or CALPHAD assessment.
- Indexed cubic Bragg peak calculation: shared wavelength uncertainty is not divided by the number of peaks. No automatic indexing, instrument correction or sample identification.
- NIST Hahn1 residual diagnostics: 236 checked published observations; RSS matches certified numerical benchmark. The original upstream data transport bytes and physical response multiplier are not established. Temperature-sorted residual correlation is not a time-series statistic.

## Outstanding content and acceptance

Rights-cleared measured diffraction and mechanical datasets, independent source/physical review, comprehensive phase and degradation evidence, qualified specimen provenance, actual Windows execution, live Bitwork routing and independent AI evaluation remain open. The user has explicitly deferred routing and desktop transfer until **all 30 domains** have been built. Materials stays active and Control remains queued.
