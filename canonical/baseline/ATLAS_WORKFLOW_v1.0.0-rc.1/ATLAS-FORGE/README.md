![Atlas Forge knowledge network artwork](assets/atlas_forge_knowledge_hub.png)

# ATLAS FORGE

**Build research once. Preserve the evidence. Reuse it across compatible systems.**

## Version 1.0.0 release candidate 1

This is a tested engineering and reference candidate, not accepted final Measurement v1.0. The final gate remains closed, the 30-domain roadmap is preserved, and Measurement is the only active new Atlas. Signal and Cymatics keep their own versioned nodes.

The same runtime discovers, searches, fetches exact records, follows typed relationships and assembles bounded context across every enabled node. An exact reference record, not its search score, remains the evidence-bearing object. A record carries its sources, assumptions, limitations, original status and revisions.

| Node | Included common records | Boundary |
|---|---:|---|
| Signal Atlas | 232 | Pinned source/claim reference subset; original status preserved |
| Cymatics Atlas | 132 | Pinned concepts, sources and audits; no new laboratory validation |
| Measurement Atlas | 141 | 92 bounded records, 44 source cards and five starter records |

Counts include bibliographic and editorial material. They do not indicate complete scientific coverage. The former 370-record federation remains frozen for compatibility.

## Start here

| Path | Purpose |
|---|---|
| [Agent instructions](AGENTS.md) | The consistent build process and Measurement-first rule |
| [Common contract](docs/COMMON_CONTRACT.md) | Exact records, relations, versioning and context invariants |
| [Integration guide](docs/NODE_INTEGRATION.md) | Existing Python, CLI and local HTTP use |
| [Workflow criteria](workflow/acceptance.json) | All eight required v1 gates, unchanged |
| [Project-local skills](.agents/skills/) | Build, source curation, conformance, context audit and release discipline |
| [Release audit](docs/RELEASE_AUDIT_v1.0.0-rc.1.md) | Actual execution evidence and remaining blockers |

The full workspace includes `MEASUREMENT-ATLAS`, both Python wheels and `START_HERE.md`. Run `RUN_CHECKS.cmd` or `RUN_V1_ACCEPTANCE.cmd` there. The second launcher checks final readiness and intentionally refuses acceptance while evidence is missing.

## Reference and domain tools

```powershell
py -3 -m atlas_forge acs context "normal conformance probability" --node measurement-atlas --max-bytes 32768
py -3 -m atlas_forge serve --port 8766
```

The new numerical operations live in Measurement, not in search. Retrieval never executes certificate text or source instructions. The context budget counts UTF-8 bytes, not model tokens. The local server is not an authenticated internet service.

## Release boundary

The navigation runtime, original nodes and approved image are unchanged. Live Bitwork, downstream model execution, independently held-out comparisons and native Windows evidence remain open. The stored criteria also require review/freeze. The package cannot certify its own scientific truth or advance to another domain.

No GitHub publication, desktop installation, sharing change or account Memory update is performed by unpacking the source. See [rights decisions](LICENSE_DECISIONS.md) and retained source-level notices.
