# Chemistry Atlas v0.2.0 — executed software verification and science limits

**Content:** substantive technology-continuity research v0.2, not final scientific-content v1 and not independent laboratory review.

## Source-tree engineering checks

- **1,871 tests passed, zero failures/errors/skips**, across 14 release-specific suites. Original 68 Chemistry v0.1 tests run against their unmodified 11-node historical snapshot; the current v0.2 node passes **60 new tests**.
- **7,790 independent mathematical comparisons passed** using separately written NumPy arithmetic and constructed species/data. Maximum normalized discrepancy 1.38e-13. A large absolute difference in values with molar-carrier units can reflect scale: use the normalized bound, not misleading unit-free precision claims.
- Shared Common Contract: eleven nodes, **2,289 records**, **1,455 typed exact-revision relationships**, **484 source cards**. All 78 source-linked context packages and fast-compiled JSON schemas pass, plus bounded Draft 2020-12 samples. Exhaustive full Draft validation of every assembled context not claimed.
- **3,085 previous protected files byte-identical** to Chemistry v0.1 as verified by its old SHA256 file manifest. Every one of the **2,220 previous record revisions** and **1,391 previous relation revisions** remains unchanged, including all ten earlier scientific nodes and chemistry itself.
- Clean offline wheel installation of Chemistry v0.2 loads **237 records and 204 locally closed relationships**. Six cross-domain Chemistry edges remain exclusively in the full eleven-node federation.
- The domain contains 51 original scientific chapters and 39 constructed worked investigations, all with limits and source context.

## Scientific limits

- NIST Chemistry WebBook, NIST Kinetics, IUPAC terminology, PubChem and Materials Project are referenced as scoped publisher pages, **not locally authenticated original publication/dataset transport bytes**. Strict survival audit: 484 source cards, **zero authenticated original files**.
- The new exact atom-and-charge balance does not establish a reaction's feasibility, yield, safe handling or actual species identity.
- Gibbs/enthalpy, ion activity and equilibrium examples require compatible standard states, temperature, phase and measured properties; those values are invented in the test fixtures.
- Diffusion, semiconductor carriers and optical absorption use deliberately idealized models with bounded validity. No semiconductor fabrication, laboratory calibration or live model training was performed.
- IUPAC online Gold Book v5 (2025) individual terms have CC BY-SA context and the collection may have different licensing. The source register does not claim unrestricted redistribution of the entire work.

## Offline commands

```sh
cd CHEMISTRY-ATLAS
python -m chemistry_atlas advanced
python -m unittest discover -s tests -q
python tools/numerical_oracle_v02.py # optional NumPy
cd ..
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /unique/outside/directory
```

The external release audit records the full **extracted ZIP replay** and patch reconstruction after those operations actually complete.
