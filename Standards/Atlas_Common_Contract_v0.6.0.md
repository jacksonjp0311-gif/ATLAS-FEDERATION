# Atlas Common Contract 1

This is the implemented v0.4 engineering contract. `contract_version: 1.0` names the wire format, not Measurement scientific v1 readiness. The original architectural draft remains in `ATLAS_COMMON_STANDARD_DRAFT_v01.md`.

## Persistent objects

Every node includes `atlas_manifest.json` and eight explicit JSONL collections: concepts, claims, sources, equations, methods, datasets, reviews and relations. Empty collections are valid. Registry entries bind each manifest SHA-256. Manifests bind each collection hash and count. `corpus_revision` is the digest of the collection manifest; `index_revision` names the deterministic ranker.

Record identity is node-qualified and stable. The immutable `revision` is SHA-256 over canonical JSON excluding that revision field. Original identity and the complete legacy envelope are retained during migration. Exact source references carry both `record_id` and `revision`. Scientific locators are separate from repository-record locators; missing primary evidence is recorded as a gap.

Content fields are text, tags, domain, equation, assumptions, applicability, limitations, units and uncertainty. Evidence retains origin, review status, exact inspected locators, original labels and gaps. Rights states are local_reference, restricted or unknown. Restricted/unknown records are excluded by default; this is a conservative local delivery policy, not a legal rights certification.

Relations declare an exact source and destination revision, a type and provenance. `related_to` is navigation, not support. `depends_on` is directional. `qualifies` and `contradicts` are symmetric inclusion requirements for context assembly: each travels with its other endpoint and source closure.

## Operations

All are on `AtlasStore`, with the CLI under `python -m atlas_forge acs`:

| Operation | Behavior |
| --- | --- |
| discover | Validate files and return scope, versions, counts and limits |
| search | Field-weighted BM25 candidates; no scientific confidence inference |
| fetch | Require exact record ID and revision; never silently resolve latest |
| neighbors | Typed connectivity with explicit depth and edge limits |
| assemble_context | Greedily include ranked whole evidence units within a byte budget |
| validate_context | Verify exact bytes/closure, dependencies, qualifiers, versions, budget and deterministic replay |
| changes_since | Conservatively invalidate old packages after dependency or registry changes |

The default renderer is canonical JSON, so Unicode has deterministic UTF-8 accounting. The documented budget limits `context_text`, not total JSON transport size. No tokenizer is invoked. No named token estimate is fabricated. Exclusions and gaps stay outside the retained payload as explicit diagnostics.

## Context status

`context_available`, `conflicting_context`, `budget_exhausted`, `evidence_unavailable`, and `no_match` are retrieval outcomes. `evidence_sufficiency` remains `not_assessed`. Failed integrity raises an explicit error; the HTTP API returns failure rather than a silent partial answer.

Validation preserves entire records and required relationships, rejects unknown envelope fields, then replays selection under the exact current registry and policy. This is not scientific verification, cryptographic authentication, guaranteed relevance, semantic completeness or a prompt-injection defense inside the consuming model. The consumer must treat all record strings as untrusted data.

## Migration and compatibility

Source-specific offline adapters produce one common view. The 370 legacy records remain intact in provenance, with no evidence promotion. The runtime itself has no Signal/Cymatics/Measurement branches. The generic loader is exercised on a synthetic fourth-node fixture; that fixture is only a test, not a new scientific Atlas.

The legacy federation remains frozen for compatibility; its interfaces are not silently redefined. Use `/api/common/*` and `acs` for current behavior. Changes to a corpus, ranker or mandatory schema require explicit regenerated revisions and new context. Historical release artifacts are not overwritten.

## Current constraints

Maximum record 256 KiB; collection 32 MiB; query 8 KiB UTF-8; context budget 512–1,048,576 UTF-8 bytes; selected roots 1–50; required closure 256 records. Empty/stop-only questions are invalid. Full signatures/remote trust, semantic abstention and generic units/dimension arithmetic remain future implementation inside the current Measurement milestone.


## Content edition 0.5.0

The contract and runtime are unchanged. Measurement content is expanded under the same data-only interface. The common corpus contains 446 records; the legacy view remains frozen at 370. This changes corpus revisions, not the contract version.

## Content checkpoint 0.6.0

The same contract now serves 467 records, with 103 in Measurement. The new publisher discrepancy uses the existing `contradicts` relation. This is a corpus change, not a new protocol, router or evidence-status promotion.
