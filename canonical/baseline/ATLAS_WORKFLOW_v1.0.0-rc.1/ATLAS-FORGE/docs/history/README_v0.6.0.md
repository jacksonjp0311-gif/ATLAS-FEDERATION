![Atlas Forge knowledge network artwork](assets/atlas_forge_knowledge_hub.png)

# ATLAS FORGE

**Different knowledge. One evidence contract.**

**Content checkpoint 0.6.0 · Measurement-first workflow · Scientific v1 acceptance pending**

Forge is the common access layer for James Paul Jackson's scientific reference Atlases. It preserves the research behind a claim, makes exact records discoverable, and assembles task-specific context for a consuming AI. The domain knowledge changes between nodes; the storage, retrieval, citation and context contracts do not.

**Measurement remains the active Atlas until its v1 gates pass.** Causal Atlas and the other proposed domains are a roadmap, not parallel releases. The supporting Forge and Bitwork bridge work belongs to this milestone.

[Start the workflow](docs/WORKFLOW_GUIDE.md) · [Common contract](docs/COMMON_CONTRACT.md) · [Current audit](docs/RELEASE_AUDIT_v0.6.0.md) · [Bitwork boundary](docs/BITWORK_BRIDGE.md) · [Agent instructions](AGENTS.md)

## Content first, navigation later

The owner has deferred navigation development. The common/search/router/HTTP code is byte-identical to v0.4.0; hashes are recorded in `workflow/deferred_navigation.json`. This edition deepens Measurement science and documentation, not navigation. The earlier Bitwork and AI evaluation gates remain open.

[Ordered domain roadmap](DOMAIN_ROADMAP.md) · [Measurement guide](../MEASUREMENT-ATLAS/docs/REFERENCE_GUIDE.md)

## What this checkpoint delivers

A generic, data-only kernel reads all three nodes through one contract. It supports discovery, BM25 candidate retrieval, exact revision fetch, bounded relationship traversal, evidence-preserving context assembly, context replay validation and correction invalidation. Search does not import node code, run calculators, call a language model or access the network.

| Node | Software edition in the common view | Records | Evidence boundary |
| --- | --- | ---: | --- |
| Signal Atlas | 1.0 | 232 | 82 scoped claims and 150 source records; original labels retained |
| Cymatics Atlas | 1.0.0 | 132 | Concepts, citations, audits, publisher checks and external dataset listings; not replicated experiments |
| Measurement Atlas | 0.6.0 | 103 | 62 bounded reference records, 36 source cards and five preserved navigation records |
| **Total** | | **467** | Record counts include bibliographic cards; not independently verified scientific findings |

All 370 prior reference records remain preserved with their original IDs, evidence labels and raw normalized envelopes. The common view adds 97 records to the frozen legacy view: 62 Measurement reference records and 35 source pages. This edition adds 21 records relative to v0.5.x. The original Signal/Cymatics repositories are unchanged.

The old v0.3 federation export and `/api/search` remain available as a frozen compatibility view of 370 records. **Use `acs` or `/api/common/` for the new common contract.** The Measurement numerical toolkit is the companion package; context retrieval never silently executes it.

## Quick start

Python 3.10 or newer. From the source checkout:

```powershell
$env:PYTHONPATH = "$PWD\src"
py -3 -m atlas_forge acs discover
py -3 -m atlas_forge acs conform
py -3 -m atlas_forge acs context "expanded uncertainty" --node measurement-atlas --max-bytes 32768
py -3 -m atlas_forge serve --port 8766
```

Open `http://127.0.0.1:8766`, or use `START_FORGE.cmd`. The local page browses all three common nodes and saves full context packages. `/legacy` opens the preserved historical portal. The approved header artwork remains artwork, not measured evidence.

From the combined delivery workspace, install both local wheels with the command in `START_HERE.md`; no runtime third-party packages are required. Optional developer checks use `jsonschema`, `numpy`, and a browser automation tool. They are not required to query the library.

## One task-specific context package

```powershell
py -3 -m atlas_forge acs context "uncertainty of a difference" --node measurement-atlas --max-bytes 32768 > context.json
py -3 -m atlas_forge acs validate-context context.json
py -3 -m atlas_forge acs changes-since context.json
```

A package contains exact records, source references, assumptions, applicability, units, limitations, evidence gaps, conflicts, versions, dependencies, selection exclusions and a replayable checksum. Qualifying and contradictory records travel with their claim. An inclusion unit either fits in the declared budget or is excluded intact.

The budget is **UTF-8 bytes of `context_text`**, not model tokens or the complete JSON envelope. The envelope intentionally includes structured data and the rendered view. Pass only `context_text` as retrieved data to a consuming model, or use `--render`. The model's answer still requires evaluation.

`context_available` means context was assembled. It does not mean the question is answered correctly, sufficiently or completely. Scores measure retrieval relevance, not scientific confidence. A byte checksum detects changed bytes; it is not a signature or proof of truth.

## Five reusable agent skills

The repository includes project-local Agent Skills under [`.agents/skills/`](.agents/skills/):

| Skill | Job |
| --- | --- |
| `atlas-build` | Keep the active milestone, follow the shared layout and run the build sequence |
| `atlas-source-curation` | Admit bounded records with primary locators, rights notes and explicit review scope |
| `atlas-node-conformance` | Check generic records, node versions, exact links and migration preservation |
| `atlas-context-audit` | Check whole-claim evidence closure, budgets, hostile text and correction invalidation |
| `atlas-release-gate` | Require evidence for G1–G8; block advancing while Measurement v1 is incomplete |

These are real instruction files packaged with the tools. They have been used for this build's checks. They have **not** been installed into your desktop agent, account Memory or a global plugin store. Hosts that do not auto-discover `.agents/skills` can read the files through `AGENTS.md`.

## Executable workflow

```powershell
py -3 tools/run_workflow.py --measurement ..\MEASUREMENT-ATLAS --out output\check-001
py -3 tools/workflow.py status
py -3 tools/workflow.py advance --node causal-atlas
```

The last command currently exits 2 because Measurement is not v1-ready. That is an intended guard, not a failed release. The workflow runner checks that this guard works. It does not grant scientific review, auto-approve gates, publish code or install host tools.

[`tools/new_node.py`](tools/new_node.py) is the shared scaffold generator. It uses the same kernel and respects the milestone guard. The older `init` command is retained only for legacy consumers, is also guarded, and is not the new common-standard builder.

## Bitwork integration status

The published Perci implementation was inspected at commit `0811f45a5c7322f77a17c75856eabc9a7a620870`. Its documented `route` interface classifies requests; the observed interface is not a prototype-to-Atlas-record resolver.

This release provides a version-bound **route-request and candidate-receipt bridge**, validating exact node IDs, record revisions, request/corpus hashes, score kinds, encoder/index versions, and fallback behavior. Invalid or abstaining receipts fall back explicitly to BM25. Test fixtures are marked as fixtures. **A live Bitwork-to-Atlas-to-model run has not occurred.** G6 remains blocked.

## Build and evidence directory

| Path | Purpose |
| --- | --- |
| [src/atlas_forge/common.py](src/atlas_forge/common.py) | One data-only common runtime, no domain-specific dispatch |
| [src/atlas_forge/routing.py](src/atlas_forge/routing.py) | External candidate receipt contract and fallback |
| [src/atlas_forge/workflow.py](src/atlas_forge/workflow.py) | Evidence-bound release gates |
| [src/atlas_forge/resources/common/](src/atlas_forge/resources/common/) | Three versioned normalized nodes and registry lock |
| [schemas/common/](schemas/common/) | JSON Schemas for records, nodes, relations and contexts |
| [tools/build_common.py](tools/build_common.py) | Offline migration; legacy-specific mapping belongs here |
| [tools/run_workflow.py](tools/run_workflow.py) | One command to run local build checks and retain receipts |
| [workflow/](workflow/) | Active milestone, candidate criteria, scope and decisions |
| [evaluations/](evaluations/) | Authored diagnostic, not independent held-out evidence |
| [docs/receipts/](docs/receipts/) | Actual test, migration, browser, install and evaluation receipts |
| [docs/history/](docs/history/) | Earlier landing documentation preserved |

## Reproducibility and limits

Run `python -m unittest discover -s tests -v`, `python tools/workflow.py conform`, and `python scripts/check_release.py verify`. Optional schema validation: `python tools/schema_check.py` with `jsonschema` installed. Run the companion Measurement tests and its synthetic casebook separately, or use the workflow runner.

The small authored retrieval set is a regression diagnostic. It is not a blind evaluation, and it does not measure model answer improvement. Primary-source checks are assistant checks of the named public portions, not independent replication. Units must still be harmonized by the caller for numerical tools. No automatic live publisher monitoring, authenticated remote service, native Forge MCP server, or deployed Bitwork mapping is provided.

Source rights remain attached to records; linked publications and external datasets are not mirrored. Project-local hashes are not an authenticated supply chain. Third-party and earlier project license boundaries are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [LICENSE_DECISIONS.md](LICENSE_DECISIONS.md).

**Next work stays inside Measurement v1:** deepen the scoped reference, inspect the remaining source passages, expand worked cases, and review the documented coverage gaps. Navigation, live Bitwork integration and downstream model evaluation are deferred until the content pass is ready; their acceptance gates are not waived. No next domain is opened by this checkpoint.

## Published calibration case in 0.6.0

The Measurement companion now includes a provenance-documented transcription of 40 NIST Pontius observations and a deterministic OLS reproduction. It agrees with 11 StRD certified numerical reference targets at their displayed precision and preserves six stricter handbook-rounding mismatches rather than hiding them. The original transport bytes were not acquired. No independent laboratory replication, instrument certification or AI answer-quality result is claimed.

See [the case study](../MEASUREMENT-ATLAS/docs/PUBLISHED_CALIBRATION_CASE.md) and [source discrepancy record](../MEASUREMENT-ATLAS/docs/SOURCE_DISCREPANCIES.md). The inherited navigation engine is unchanged. The 30-domain queue is recorded separately from completed nodes.
