# Causal Atlas v1.0.0 — content release validation

**Status:** Scoped reference/content release; platform-wide scientific acceptance remains pending. Date: 2026-11-12.

The common Forge runtime is unchanged. The new Causal node contains 149 records, including 34 bibliographic source cards, and 65 typed relationships. All 105 prior Causal record revisions and the entire preserved 771-file baseline remain unchanged. The four-node Forge view contains 654 records; entries include editorial summaries, references and constructed methods, **not** 654 validated scientific discoveries.

## Scope and numerical validation

- 24 substantive chapters, 13 worked investigations (one attributed real historical descriptive case), six blank study templates.
- Unit tests cover prior graph, weighting, RD and IV methods, seven additional methods, invalid inputs, CLI, source closure, versioned records and budgeted context validation.
- `python tools/v1_numerical_oracle.py` cross-checks seeded synthetic model values against an independently written NumPy calculation and historic-count aggregation. This evaluates arithmetic, not the real-world correctness of model assumptions.
- Berkeley application counts reproduce the published tabulation at the level of 1973 six-department aggregate counts; the male/female comparisons and pooled-department standardization are **descriptive**. Neither intervention effect nor discrimination cause has been inferred. Underlying dataset redistribution terms are not established; original raw files are linked, not bundled.
- In the collection, Forge and Measurement remain pinned to their existing wheels. They are not rebranded or declared final v1 by this Causal release.

## Release commands

```sh
PYTHONPATH="baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src:baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS:CAUSAL-ATLAS" python tools/check_collection.py --out receipts/local-check
PYTHONPATH=CAUSAL-ATLAS python CAUSAL-ATLAS/tools/v1_numerical_oracle.py
python CAUSAL-ATLAS/tools/check_manifest.py verify CAUSAL-ATLAS
```

The live command requires a fresh receipt folder. Windows should use platform-appropriate environment and path separators; the source archive has not been tested natively on a Windows host.

## Limitations and acceptance

The verified numbers, platform and independent-implementation comparisons are in the adjacent release audit. Independent human scientific review, authentic causal experiment replication, general statistical estimators, unrestricted identification, Bitwork/AI agent integration, independent held-out tests and Windows verification are **not completed**. No source content from an untrusted page is executed. No claims of lower GPU cost, improved AI accuracy or unprecedented discovery are made.
