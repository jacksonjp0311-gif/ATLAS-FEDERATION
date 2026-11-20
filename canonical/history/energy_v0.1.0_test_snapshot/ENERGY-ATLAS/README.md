![ATLAS FORGE knowledge hub](assets/atlas_forge_knowledge_hub.png)

# ENERGY ATLAS v0.1.0 — Knowledge-Survival Research Reference

**Thirty domain libraries first. Bitwork routing last.**

A source-linked offline reference for first-principles energy physics, thermodynamics, heat transfer, electrical power, renewables, nuclear and fusion foundations, storage, grids, cost and scientific metrology. **This is not a live energy system, control platform, reactor or safety-certified design.**

## Explore

- [36-chapter original research manual](docs/DEPTH_MANUAL_v0.1.0.md), reconstructed mathematics and model assumptions
- [25 reproducible investigations](docs/CASEBOOK.md), constructed rather than empirically measured
- [20 publisher source cards](docs/SOURCE_REGISTER.md) with rights notes and missing-original-byte flags
- [Research coverage](docs/COVERAGE_MATRIX.md) and [validation](docs/VALIDATION_v0.1.0.md)
- [Versioned machine records](data/) under the immutable Atlas Common 1.0 contract
- [Pure-Python models](energy_atlas/models.py) and [tests](tests/)

## Offline computations

```sh
python -m energy_atlas
python -m unittest discover -s tests -q
python tools/check_manifest.py verify .
```

**Scope:** 176 source-linked records, 144 standalone relationships and 149 full-collection relationships. Five cross-domain links are intentionally kept ONLY in the full collection because their target records reside in the earlier nine nodes. Both exports remain internally source-closed.

No local original source files were obtained; publisher websites and compiled datasets may disappear. The source acquisition ledger treats this as a critical survival gap, while the original derivations and executable examples remain offline-readable. Safety and physical plant claims need real measurements and independent qualified review.
