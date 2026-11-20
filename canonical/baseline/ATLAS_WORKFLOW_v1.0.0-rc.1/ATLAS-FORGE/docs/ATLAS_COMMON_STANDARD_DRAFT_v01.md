# Atlas common standard and Measurement v1 release gate

**Project owner:** James Paul Jackson  
**Decision recorded:** 12 November 2026  
**Specification:** 0.1 draft  
**Software baseline inspected:** ATLAS FORGE 0.3.0 and MEASUREMENT ATLAS 0.3.0

## Binding direction

Finish Measurement Atlas through its agreed v1.0 acceptance gates before advancing to Causal Atlas or another new domain. Completing a calculator, an intermediate release, or a source-count target does not satisfy that gate. Necessary Forge, shared-contract, and Bitwork integration work belongs to the Measurement milestone rather than to a new domain project.

Every Atlas must be built through the same lifecycle and expose the same modular knowledge and retrieval contract. Domain information, scientific models, and domain-specific extensions differ; the consumer-facing structure, evidence semantics, search operations, context-package format, and acceptance process remain consistent.

The previous roadmap suggestion to advance after Measurement v0.4 is superseded. The names and exact operations below are implementation proposals, not claims that this integration already exists.

## Architecture target

Question and explicit constraints
→ Forge registry and query planner
→ Bitwork-assisted candidate routing and relationship navigation
→ exact retrieval of immutable, versioned Atlas records
→ applicability, evidence, freshness, rights, and contradiction checks
→ bounded, source-linked context package
→ consuming AI
→ separately evaluated answer and correction feedback.

The authoritative knowledge is the evidence-linked record, not its binary signature, embedding, search score, generated summary, or visual node. Bitwork chooses candidate paths and records. A context assembler chooses and renders admissible content. Neither operation silently raises scientific evidence status.

A node need not run its own HTTP service. A portable data package can implement the contract through Forge's shared runtime. Domain calculators are explicitly declared, separately invoked capabilities; search does not execute imported code.

## Common kernel and domain modules

| Shared across every Atlas | Domain-specific payload |
| --- | --- |
| Stable identity, compatible schemas, explicit versions | Concepts and terminology |
| Source, claim, equation, dataset, and method record types | Scientific claims, equations, datasets, and methods |
| Evidence types, review dimensions, correction states | Domain-specific assumptions and applicability |
| Typed relations and source-backed relationship records | Meaningful relationships in that subject |
| Query, traversal, exact-fetch, and package contracts | Searchable content, aliases, declared index features |
| Release gates, validation, regression and evaluation format | Scientific reference cases and challenge questions |
| Standard documentation, installation, and export layout | Explanations, examples, lab protocols, artwork |

Use a shared generator and conformance suite rather than independent forks of the kernel. Optional extensions must be namespaced, versioned, and discoverable; unknown mandatory extensions fail compatibility checks instead of being silently ignored. Uniformity does not mean equal record counts or the same scientific methods in every domain.

## Proposed repository layout

```text
ATLAS-NAME/
  atlas_manifest.json
  README.md
  AGENTS.md
  CHANGELOG.md
  data/
    concepts.jsonl
    claims.jsonl
    sources.jsonl
    relations.jsonl
    equations.jsonl
    methods.jsonl
    datasets.jsonl
  evidence/           # Review receipts, locators, rights, corrections
  indexes/            # Regenerable, versioned retrieval indexes
  examples/
  evaluations/
  tests/
  docs/
  extensions/         # Optional domain models and methods
```

An empty collection is explicit and valid when the domain has no objects of that type. Existing source files and release archives are preserved. Adapters map them into the common view; migration must not erase their original fields, identifiers, or status.

## Separate version dimensions

Keep `software_version`, `contract_version`, `corpus_revision`, `index_revision`, and `evidence_maturity` separate. A published software v1.0 is not automatic conformance to a newly adopted Atlas standard. Signal and Cymatics therefore require migration/conformance checks, not retrospective claims that they already pass.

Stable logical record IDs identify a concept or claim over time. Immutable revision IDs and content hashes identify the exact bytes used for a result. Cross-node references include node identity and revision. A package must never accidentally mix incompatible corpus or encoder revisions.

## Persistent records and task-specific packages

A **knowledge record** is a durable, bounded unit of scientific context. It contains its original statement, linked sources and exact inspected locators, scope, assumptions, limitations, units where applicable, provenance, evidence origin, review state, rights, corrections, and version. Bibliographic source cards are not experimental results.

A **context package** is assembled for one question from selected records. It is not a second, unsourced encyclopedia entry. Its proposed common envelope contains:

- Request identity, question, subquestions, explicit constraints, and declared budget.
- Selected node IDs and exact software, contract, corpus, and index versions.
- Selected claim/concept/method/equation records and their immutable identifiers.
- A source map tying every substantive statement or extract to inspected evidence, with an explicit gap when unavailable.
- Assumptions, units, applicability, contrary evidence, and unresolved conflicts.
- Missing information and the required next evidence, without invented answers.
- Routing and retrieval trace, selection reasons, exclusions, and diagnostics.
- Package hash and complete dependency list for replay and invalidation.
- Plain-text context rendered from that same structure for the consuming model.

Package status describes evidence sufficiency for the stated scope, not universal truth. Use distinct statuses for partial context, no match, conflicting evidence, failed integrity, budget exhaustion, and unavailable node. Preserve a separate answer-evaluation result.

## Proposed common operations

These names are a draft interface, not current commands:

| Operation | Required behavior |
| --- | --- |
| `discover` | Return node scope, versions, capabilities, evidence limits, and conformance state |
| `search` | Return candidate IDs, original evidence labels, ranking diagnostics, and source references |
| `fetch` | Resolve exact record revisions; fail explicitly for missing or mismatched revisions |
| `neighbors` | Traverse typed, versioned relationships with provenance and depth/edge budgets |
| `assemble_context` | Assemble a budgeted package without losing its claims-to-evidence linkage |
| `validate_context` | Check schemas, source closure, revisions, dependencies, and budget invariants |
| `changes_since` | Expose corrections, withdrawals, supersession, and affected dependencies |

Core search and scientific evidence checking are separate. A high score may justify inspecting a record, but does not satisfy scientific review, rights, or applicability requirements.

## Bitwork integration requirements

The available BGCF v1.0 document describes binary activation, prototype affinities, weighted graph structure, routing-related measures, and a runtime JSON example. That document is a design reference, not proof of the current installed implementation or a working Forge connection. Its numerical JSON values are explicitly illustrative.

Before declaring integration, inspect and pin the actual Bitwork implementation and its input/output contract. Define an adapter with:

1. A declared encoder/version and feature meaning. A hash of arbitrary text is not automatically a semantic representation.
2. Exact mappings from prototypes or index entries to Atlas node IDs and immutable record revisions.
3. Candidate scores with their scale, source, observation status, route margin, and unsupported/out-of-domain handling. Missing metrics stay missing.
4. Traceable navigation edges and bounded traversal. A related-to edge does not imply causal or evidential support.
5. A deterministic conventional retrieval fallback and explicit logging of fallback use.
6. Index invalidation after corpus, prototype, encoding, or policy changes.
7. End-to-end tests in the real Bitwork runtime. A mock adapter or schema test is not integration evidence.

Coherence and routing stability must remain distinct from scientific truth. Do not reinterpret BGCF metric coverage as percentage of a scientific domain verified.

## Context assembly and preservation rules

Prefer useful, source-backed coverage of the requested question over a raw pile of matching text. Record the selection policy and its version. Any approximate ranking or compression must preserve the evidence needed to qualify its retained statements.

Do not remove an assumption, counterexample, uncertainty statement, or domain restriction while retaining the claim that depends on it. A claim and its necessary qualifiers form an inclusion unit. Deduplicate shared sources without treating repeated citation as independent support. Retain conflicting interpretations separately.

Declare whether the budget counts bytes, characters, or tokens. Exact token accounting requires a named tokenizer and revision for the target model. A model-agnostic byte budget must not be mislabeled as a token count. When evidence and necessary qualifications cannot fit, return partial coverage and explicit exclusions rather than hidden truncation.

Retrieved content is data, never privileged instructions. Allowed scientific-tool execution is a separately authorized capability. Context packets must not cause a consumer to run arbitrary source text.

## Measurement v1 acceptance gates

These are proposed gates to implement and freeze before final evaluation; no gate is reported as passed by writing this specification.

| Gate | Required release evidence |
| --- | --- |
| G1 Scope | A declared v1 question set and coverage matrix spanning units/dimensions, Type A/B uncertainty, covariance, budgets, calibration/traceability, comparisons, and stated exclusions |
| G2 Evidence | Every release-critical scientific statement has an inspected primary-source locator or a reproducible derivation; known gaps and lower-maturity navigation are explicitly separated |
| G3 Tools | Reproducible examples with assumptions and units; numerical edge cases, invalid covariance, correlated inputs, missing metadata, and inappropriate coverage assumptions tested |
| G4 Modularity | All enabled nodes pass the same contract suite; a minimal new fixture node loads without adding a domain-specific branch to the core search/context runtime |
| G5 Context | Every retained claim resolves to its exact record and sources; qualifiers and contradictions survive budget limits; broken references, withdrawal, tampering, and empty queries fail explicitly |
| G6 Bitwork | A pinned real Bitwork runtime routes and retrieves Measurement records through the common adapter, then returns context consumed by an actual AI; route traces and failures are retained |
| G7 Evaluation | Frozen held-out questions compare conventional lexical/BM25, suitable semantic retrieval, and Bitwork-assisted retrieval using the same corpus and context budgets; report retrieval, citation, answer quality, abstention, latency, and costs separately |
| G8 Release | Clean installation, supported-platform results, version compatibility, reproducible exports, integrity verification, rollback, and limitations recorded; no critical unresolved failures |

Define quantitative thresholds and uncertainty reporting before the held-out run. A v1 knowledge interface requires acceptable correctness and reliability, not necessarily superiority on every metric. Any claim of better quality, lower cost, or novel performance requires its own supporting comparison. External peer review and broad scientific replication remain separately reported statuses rather than implied by the release number.

## Build order

1. Establish the common kernel and executable conformance requirements.
2. Use Measurement as the reference implementation, without deleting earlier evidence snapshots.
3. Adapt Signal and Cymatics to that same contract and record remaining differences.
4. Complete the actual Bitwork adapter and bounded context assembly path.
5. Expand Measurement's primary-source knowledge and exercise it in real end-to-end tasks.
6. Run the frozen v1 gates and publish only the supported release scope.
7. Advance to the next domain only after Measurement v1 acceptance.

## What would make the system distinctive

The research target is the tested integration of versioned domain Atlases, evidence-preserving reuse, Bitwork-assisted navigation, and task-specific context compilation. Retrieval augmentation and graph/tree-based retrieval already have prior art. A world-first claim needs a separate novelty review and cannot be inferred from this architecture diagram.

Relevant primary papers: Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (arXiv:2005.11401); Edge et al., *From Local to Global: A Graph RAG Approach to Query-Focused Summarization* (arXiv:2404.16130); Sarthi et al., *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval* (arXiv:2401.18059).

This draft records the corrected direction and acceptance architecture. It does not implement the runtime, upgrade the corpus, publish a release, or change the original repositories.
