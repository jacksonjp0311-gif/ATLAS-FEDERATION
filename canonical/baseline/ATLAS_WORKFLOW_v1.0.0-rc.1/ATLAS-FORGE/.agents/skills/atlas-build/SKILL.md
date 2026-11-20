---
name: atlas-build
description: Build or update an Atlas node through the common contract while enforcing the active-domain v1 milestone.
compatibility: Requires Python 3.10 or newer and access to the Atlas Forge checkout.
---

# Atlas build workflow

Read `AGENTS.md`, `workflow/state.json`, and `docs/COMMON_CONTRACT.md` first.

1. Run `python tools/workflow.py status` and `python tools/workflow.py conform`.
2. Keep Measurement as the active domain. Infrastructure, adapter and evidence work are part of that milestone. Do not start the next domain while any v1 gate is incomplete.
3. Inspect existing source and preserve the historical federation snapshots. Use the shared kernel in `src/atlas_forge/common.py`; do not fork a per-domain kernel.
4. Use `atlas-source-curation` for scientific additions, `atlas-node-conformance` for migration, `atlas-context-audit` for retrieval, and `atlas-release-gate` before packaging.
5. Record runtime checks under a fresh `output/` folder; promote reviewed build receipts to `docs/receipts/current/` before sealing a release. Keep software success distinct from evidence maturity.

Output: updated source, regression receipts, a gate report, and explicit remaining work. Do not publish, install on another device, or claim automatic account Memory changes without actual tool confirmation.
