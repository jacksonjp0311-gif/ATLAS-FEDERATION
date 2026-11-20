# Agent Atlas v1.0.0 — content release audit

**Edition:** scoped educational/scientific content v1.0.0. **Not:** independent scientific certification, actual general intelligence, verified agent learning, an operational tool broker, completed global science archive, or live Bitwork router.

## What was exercised

- 6 node test suites: **1256 passed, zero failed/skipped** (Forge 188, Measurement 218, Causal 233, Materials 122, Control 244, Agent 251).
- Source records and all shared context schemas validate: 1241 records, 451 relations, seven nodes and 22 representative contexts. Reference context closure checks all passed. Draft 2020-12 was spot-checked; exhaustive full-size contexts were checked with compiled schema and AtlasStore, not exhaustively by the slower Draft202012 validator.
- **2340 NumPy/NetworkX comparisons** on author-generated finite belief models, MDPs, graphs and importance weights, max absolute discrepancy 3.553e-15. These verify numerical implementations, not measured agent performance.
- Clean offline wheel install: Agent 1.0.0 and all previously preserved distributions; 190 Agent records and 122 relations queryable from the installed package; v1 casebook and source closure pass.
- 158 Agent record revisions and 101 relation revisions preserved, plus 1424 protected baseline/previous-node files byte-identical to v0.4.

## Archive survival audit

- **1241 records** across **7** existing nodes, including **375 source cards**. The strict audit recognizes **0 authenticated original primary-source files**; this is a *preservation shortfall*, not a claim that the original educational text is absent.
- Original primary publication bytes for the new four source cards are not archived, and scholarly copyrights remain with their sources. A source URL is not an offline archive.
- Only 3 of 30 domain candidates are currently marked scoped content ready in the roadmap; Measurement/Control retain external science gates, and Signal/Cymatics are companion nodes outside that queue.
- The audit verifies file/record and source-reference consistency; no independent confirmation of factual scientific truth, legal rights, author identity or geographically redundant backups is asserted.

## Open science and execution gates

No original MAST trace rows, no live provider calls, no independent agent model improvements, no authenticated external host receipts, no independent expert review, no verified Windows deployment, no completed multi-location disaster recovery and no Bitwork retrieval evaluation. These are explicitly uncompleted, not hidden test skips.

## Reproduce

```sh
python tools/survival_audit.py --root . --check-files
python tools/check_manifest.py verify .
python tools/check_collection.py --out output/new-unique-check
python -m agent_atlas v1-casebook
python AGENT-ATLAS/tools/v1_numeric_oracle.py
```

The final archive's manifest, extraction and replay are checked separately in the external release receipt so it cannot claim they passed before those operations occur.
