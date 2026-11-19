# Electronics & Semiconductor Devices Atlas — scoped v1 release candidate

**Part of the single canonical ATLAS FORGE federation, not a new project.**

52 original reconstruction chapters, built on the 34 historical originals, 48 constructed cases across editions (34 historical + 14 new) in `docs/CASEBOOK_v1.0.0-rc.1.md`, immutable JSONL records, source-gap ledger, unit-aware Python reference kernels, distinct historical test snapshots, and finite independent numerical oracle.

Start with the complete [`DEPTH_MANUAL_v1.0.0-rc.1.md`](docs/DEPTH_MANUAL_v1.0.0-rc.1.md), the [`RECONSTRUCTION_v1.0.0-rc.1.md`](docs/RECONSTRUCTION_v1.0.0-rc.1.md) chain and the [`SCOPED_V1_GATES_v1.0.0-rc.1.md`](docs/SCOPED_V1_GATES_v1.0.0-rc.1.md) acceptance matrix.

Run:

```
python -m unittest discover -s tests -q
PYTHONPATH=. python evidence/independent_oracle_v1rc.py
```

The reference package requires only Python 3.10+ for normal model operation; independent oracles additionally use NumPy/mpmath. **No authenticated original publisher PDF, peer-reviewed scientific review, calibrated silicon data, functioning CPU or physical fabrication is claimed.** Archive integrity and mathematical verification are not hardware verification. The 30-domain roadmap and deferred Bitwork rule are preserved.
