![Approved Atlas Forge identity](CAUSAL-ATLAS/assets/atlas_forge_knowledge_hub.png)

# Atlas collection content edition 0.2.0

**Causal depth build · common contract 1.0 · James Paul Jackson**

Causal is the active reference build. This edition develops the investigation path from question and identification to weighting, augmented estimation, missingness, sensitivity and reporting. It does not move to Materials, ask for a desktop transfer, or mark deferred scientific/system acceptance complete.

## Read the knowledge

[Eight-chapter Causal guide](CAUSAL-ATLAS/docs/REFERENCE_GUIDE.md) · [Worked investigation](CAUSAL-ATLAS/docs/investigations/01_process_change.md) · [Coverage and gaps](CAUSAL-ATLAS/docs/COVERAGE_MATRIX.md) · [Source register](CAUSAL-ATLAS/docs/SOURCE_REGISTER.md)

The Causal node contains 73 records: 38 bounded literature capsules, 19 authored method/example/protocol records and 16 source cards. Three expanded investigations and 12 computed synthetic checks supplement the five retained cases. Four blank templates turn the material into an investigation workflow. Counts are inventory, not scientific completeness.

## Preserved collection

| Location | Purpose |
|---|---|
| [CAUSAL-ATLAS](CAUSAL-ATLAS/README.md) | Active 0.2.0 reference and explicit mathematical teaching tools |
| [common](common/registry.json) | Four common-contract nodes, 578 records |
| [baseline](baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/START_HERE.md) | All 771 original rc1 files unchanged, including Forge/Measurement and their acceptance limitations |
| [Build policy](BUILD_POLICY.json) | Content readiness separate from final scientific/deployment acceptance |
| [Domain queue](DOMAIN_QUEUE.json) | Original domains; Causal active and Materials still queued |
| [Execution report](RELEASE_CHECKS.json) | Actual source test and numerical comparison results |
| [Release history](history/0.1.0) | Prior collection receipts and inventories |

The preserved baseline runtime is Forge 1.0.0rc1, not a silently merged rc2 branch. The build input is the latest delivered `ATLAS_COLLECTION_v0.1.0.zip`; its exact digest is recorded. The earlier Library rc2 workspace remains a separate retained artifact. This resolves the prior differing collection inventories without changing historical reports.

## Reproduce

`python tools/check_collection.py --out output/check-local` runs all suites with the correct shared import paths. Use a fresh output directory. Optional algorithm checks: `python CAUSAL-ATLAS/tools/estimation_oracle.py` (NumPy) and `python CAUSAL-ATLAS/tools/graph_oracle.py` (NetworkX). Runtime tools need neither optional dependency.

No new real observations, independently reviewed causal findings, live Bitwork/AI execution, Windows run, GitHub publication or desktop installation is claimed. The final archive/extraction receipt is distributed separately as `ATLAS_COLLECTION_RELEASE_v0.2.0.json` so it can bind the completed archive hash without a circular self-reference.
