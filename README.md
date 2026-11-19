<p align="center">
  <img src="assets/atlas-federation-hero.png" alt="ATLAS FEDERATION — Knowledge that endures. A luminous brass armillary sphere above a distant horizon." width="100%" />
</p>

<h1 align="center">ATLAS Federation</h1>

<p align="center">
  <strong>A scientific and technological continuity federation.</strong><br />
  Source-linked knowledge. Preserved reasoning. Reproducible foundations.
</p>

<p align="center">
  <a href="#start-here">Start here</a> ·
  <a href="#domain-directory">Domain directory</a> ·
  <a href="#research-amortization">Research amortization</a> ·
  <a href="#for-people-and-ai-systems">People &amp; AI</a> ·
  <a href="#evidence-and-integrity">Evidence</a> ·
  <a href="#restoration-and-preservation">Restoration</a>
</p>

---

## Why ATLAS exists

Knowledge can survive as text and still be lost as capability. A formula without its assumptions, a design without its materials, or a result without its evidence leaves the next person to reconstruct the reasoning before they can begin.

**ATLAS Federation exists to preserve that reasoning.** It connects scientific and engineering domains into one versioned research federation: reference material, source records, equations, assumptions, executable models, experiments, and the evidence needed to examine them. Its purpose is to help people and AI systems understand, test, and carry useful knowledge forward—even when access to networks, services, or the original research process is limited.

The long-term goal is **technological continuity**: preserving enough context for future investigators to learn, repair, reproduce, and eventually rebuild within the limits of their tools and evidence. Each domain contributes to that shared foundation. Each revision should leave the next investigator with a clearer starting point.

> Preserve what is known. Keep the evidence attached. Leave the next person a place to begin.

Created by **James Paul Jackson**. ATLAS Federation continues the original **ATLAS FORGE** program; historical names, scientific records, and release filenames retain their original identities. The [founding charter](Standards/Human_Knowledge_Survival_Charter_v1.md) and [common research contract](Standards/Atlas_Common_Contract_v0.6.0.md) describe the mission and structure.

**Public status:** this repository is an expanding public source mirror. The canonical checkpoint is **Compiler Design v0.2.0**. The complete historical archive is still pending public release and public download verification. See [publication status](PUBLICATION_STATUS.md) before treating this checkout as a complete recovery copy.

## Start here

| Your goal | Entry point |
| :--- | :--- |
| Understand the mission and how to use the material | [Human field guide](Continuity_Toolkit/ATLAS_HUMAN_FIELD_GUIDE.md) |
| Explore a scientific or engineering domain | [Domain directory](#domain-directory) |
| Understand why research is packaged for reuse | [Research amortization](#research-amortization) · [Signal Atlas](https://github.com/jacksonjp0311-gif/SIGNAL-ATLAS) |
| Inspect the current scientific checkpoint | [Checkpoint record](CURRENT_CHECKPOINT.json) · [Edition overview](Atlas_Library_Index_Compiler_Design_v0.2.0.md) |
| Read the active domain in depth | [Compiler Design manual](Compiler_Design/DEPTH_MANUAL_v0.2.0.md) · [Edition notes](Compiler_Design/README_v0.2.0.md) |
| Integrate with a local model or research agent | [Common contract](Standards/Atlas_Common_Contract_v0.6.0.md) · [Use with AI systems](#for-people-and-ai-systems) |
| Inspect or restore an exact historical edition | [Restoration instructions](RESTORATION.md) · [Verification receipts](evidence/Compiler_Design_v0.2.0_incremental/) |
| Contribute a correction or extend the work | [Contribution and release protocol](Continuity_Toolkit/CONTRIBUTOR_AND_RELEASE_PROTOCOL.md) |

## Domain directory

The links below lead to **20 domain folders currently published in this repository**. They are grouped for navigation; the original research roadmap retains its own ordering. A published folder can contain multiple historical editions, and its presence alone does not establish completeness or scientific acceptance.

### Foundations, reasoning, and intelligent systems

| Domain | Browse source | Read first |
| :--- | :--- | :--- |
| Measurement | [Measurement](Measurement/) | [Release scope](Measurement/V1_Release_Scope_rc1.md) |
| Causal reasoning | [Causal](Causal/) | [Reference guide](Causal/Causal_Reference_Guide_v1.0.0.md) |
| Control | [Control](Control/) | [Research editions](Control/) |
| Agents | [Agent](Agent/) | [Reference guide](Agent/Agent_Reference_Guide_v1.0.0.md) |
| Computation | [Computation](Computation/) | [Reference guide](Computation/Computation_Reference_Guide_v1.0.0.md) |
| Language | [Language](Language/) | [Reference guide](Language/Language_Reference_Guide_v1.0.0.md) |
| Neural architectures | [Neural Architectures](Neural_Architectures/) | [Scoped v1.0.0 notes](Neural_Architectures/README_v1.0.0.md) |

### Matter, energy, and fabrication

| Domain | Browse source | Read first |
| :--- | :--- | :--- |
| Materials | [Materials](Materials/) | [Coverage matrix](Materials/Materials_Coverage_Matrix_v1.0.0.md) |
| Chemistry | [Chemistry](Chemistry/) | [Reference guide](Chemistry/Chemistry_Reference_Guide_v1.0.0.md) |
| Energy | [Energy](Energy/) | [Reference guide](Energy/Energy_Atlas_Reference_v1.0.0.md) |
| Bioelectricity | [Bioelectric](Bioelectric/) | [v0.1.0 notes](Bioelectric/README_v0.1.0.md) |
| Manufacturing | [Manufacturing](Manufacturing/) | [v0.2.0 notes](Manufacturing/README_v0.2.0.md) |
| Electronics and semiconductors | [Electronics &amp; Semiconductors](Electronics_Semiconductors/) | [v1.0.0-rc.1 scope](Electronics_Semiconductors/README_v1.0.0-rc.1.md) |

### Software and computing infrastructure

| Domain | Browse source | Read first |
| :--- | :--- | :--- |
| Software design patterns | [Software Design Patterns](Software_Design_Patterns/) | [v0.1.0 notes](Software_Design_Patterns/README_v0.1.0.md) |
| Distributed systems | [Distributed Systems](Distributed_Systems/) | [Scoped v1.0.0 notes](Distributed_Systems/README_v1.0.0.md) |
| Cryptographic protocols | [Cryptographic Protocols](Cryptographic_Protocols/) | [Scoped v1.0.0 notes](Cryptographic_Protocols/README_v1.0.0.md) |
| Operating system internals | [OS Internals](OS_Internals/) | [Scoped v1.0.0 notes](OS_Internals/README_v1.0.0.md) |
| Network stacks | [Network Stacks](Network_Stacks/) | [Scoped v1.0.0 notes](Network_Stacks/README_v1.0.0.md) |
| Database optimization | [Database Optimization](Database_Optimization/) | [Scoped v1.0.0 notes](Database_Optimization/README_v1.0.0.md) |
| Compiler design · **active** | [Compiler Design](Compiler_Design/) | [v0.2.0 notes](Compiler_Design/README_v0.2.0.md) |

The **24-node canonical checkpoint** also includes Computer Architecture / Digital Hardware, Cymatics, Mathematics / Physics, and Signal. Their corresponding domain directories are not yet present in this public mirror. The separate [Signal Atlas research project](https://github.com/jacksonjp0311-gif/SIGNAL-ATLAS) is available publicly; it is not a replacement for the federation's exact historical Signal node.

### Federation resources

| Location | Purpose |
| :--- | :--- |
| [Standards](Standards/) | Shared record contract, build principles, provenance, and mission charters |
| [Roadmaps](Roadmaps/) | Original 30-domain plan, preserved priority decisions, and current active pointer |
| [Continuity Toolkit](Continuity_Toolkit/) | Human guides, offline tooling, preservation procedures, and evidence boundaries |
| [Federation indexes](federation/) | Historical cross-domain indexes and checkpoint records |
| [Release records](Releases/) | Versioned manifests and deterministic restoration material |
| [Evidence](evidence/) | Preserved test, oracle, history-preservation, and replay receipts |
| [Initial science export](science/Compiler_Design/) | The earlier browsable Compiler Design export, retained alongside the domain folders |

Historical indexes describe their own editions. For the latest canonical counts and active work, use [`CURRENT_CHECKPOINT.json`](CURRENT_CHECKPOINT.json) and the [current priority pointer](Roadmaps/ATLAS_FORGE_CURRENT_ACTIVE_PRIORITY.json).

## Research amortization

**Careful research should become a reusable foundation.** Discovery, validation, and synthesis require work. Research amortization carries that investment forward across later readers, projects, and model calls by preserving a versioned body of evidence that can be inspected and reused.

The approach is developed in **[Signal Atlas](https://github.com/jacksonjp0311-gif/SIGNAL-ATLAS)**. Read its [Research Amortization implementation note](https://github.com/jacksonjp0311-gif/SIGNAL-ATLAS/blob/main/docs/research/RESEARCH_AMORTIZATION.md) for the definition, packet model, and evaluation plan.

<p align="center"><strong>Discover → Verify → Connect → Teach → Reuse → Measure</strong></p>

In ATLAS, the intended reusable unit carries the claim or method together with its source references, exact revision, assumptions, applicability, uncertainty, and relevant dependencies. That context gives the next investigator a way to assess whether earlier work still applies.

| Research effort | What should survive for the next use |
| :--- | :--- |
| Discover and inspect sources | Source identity, edition, locators, rights, and remaining evidence gaps |
| Develop an explanation or model | Assumptions, equations, worked examples, scope, and limitations |
| Test a result | Reproducible method, finite test scope, counterexamples, and receipts |
| Apply the material to a new question | Exact record revisions, dependencies, and a fresh applicability check |
| Learn that something changed | A traceable correction and a new revision, with prior evidence preserved |

For example, a later engineering task can start from an existing measurement method and its uncertainty model, then examine the new operating conditions and missing evidence. The value comes from retaining the earlier reasoning while making the new work explicit.

**The benefit must be measured.** Signal Atlas demonstrates deterministic retrieval of curated metadata and provenance-preserving packets. End-to-end savings in model compute, latency, or total research cost remain an evaluation question. Its [published evaluation boundary](https://github.com/jacksonjp0311-gif/SIGNAL-ATLAS/blob/main/docs/research/RESEARCH_AMORTIZATION_v05.md) distinguishes implemented retrieval from unproven performance claims. Any fair comparison must include preparation, maintenance, cache misses, freshness checks, and answer quality.

## For people and AI systems

For a human reader, begin with a domain guide, follow the cited sources, and read the assumptions beside each result. Use executable examples and experiments to understand the stated model. Keep the difference between a software result and a physical measurement visible.

For an AI system, the [common contract](Standards/Atlas_Common_Contract_v0.6.0.md) describes manifests and eight explicit collections: **concepts, claims, sources, equations, methods, datasets, reviews, and relations**. Records have stable identities and immutable revisions; relationships name exact revisions at both endpoints.

An integration should:

1. **Select an edition.** Identify the node, manifest, and corpus revision before retrieval.
2. **Retrieve with context.** Carry source references, dependencies, qualifications, contradictions, units, and uncertainty with the selected material.
3. **Check applicability.** Reassess freshness and scope for the current question; expose missing evidence.
4. **Return traceable work.** Cite the specific record revision and source, and keep new inferences distinguishable from the retrieved material.
5. **Preserve corrections.** Propose new revisions through the contribution process while retaining historical records.

The intended use includes local models, research agents, code assistants, and human investigators. Runtime commands documented inside historical editions apply to their restored package layouts. The browsable public export does not yet provide the complete canonical runtime and archive.

## Evidence and integrity

The **Compiler Design v0.2.0 canonical checkpoint, dated November 19, 2026**, records the following. These figures describe the preserved federation checkpoint, not the completeness of this public checkout. Source: [`CURRENT_CHECKPOINT.json`](CURRENT_CHECKPOINT.json).

| Recorded measure | Checkpoint value |
| :--- | ---: |
| Federation nodes | **24** |
| Scientific records | **4,120** |
| Exact-revision relationships | **3,357** |
| Bibliographic source cards | **657** |
| Original roadmap domains represented | **18 / 30** |
| Source-tree tests passed | **3,405 across 54 suites** |
| Fresh-restored tests passed | **3,405 across 54 suites** |
| Prior files preserved byte-for-byte | **11,433** |

These are **recorded checkpoint results**. The [preserved receipts](evidence/Compiler_Design_v0.2.0_incremental/) describe the source and fresh-restored evaluations; they are not a fresh GitHub CI run or independent scientific certification.

A checksum establishes byte identity. A finite test establishes behavior within its tested scope. Independent scientific review and physical reproduction require their own evidence. The [evidence boundaries](Continuity_Toolkit/SCIENCE_EVIDENCE_BOUNDARIES.md) and [current scientific scope](evidence/Compiler_Design_v0.2.0_incremental/SCIENTIFIC_AND_OPERATIONAL_HOLD_v0.2.0.md) preserve these distinctions. Compiler Design has not yet reached scoped scientific v1 acceptance.

## Restoration and preservation

Historical fidelity is part of the research. The canonical edition retains original scientific revisions, predecessor records, restoration instructions, and verification receipts under the **ATLAS FORGE** names used when they were created.

| Canonical artifact | Recorded value |
| :--- | :--- |
| Target edition | Compiler Design v0.2.0 |
| Complete historical archive | **735,193,042 bytes** |
| Deterministic v0.1.0 → v0.2.0 delta | **3,233,432 bytes** |
| Public release asset and public download verification | **Pending** |

<details>
<summary><strong>Expected SHA-256 checksums</strong></summary>

Complete original archive:

```text
0ca19d26cda186a43ed994b9a2c9bb87b38d90d65a07f4ba4edde3a8ccfafae7
```

Original v0.1.0 → v0.2.0 delta:

```text
4cbe54fe29729c8895670f1efa31628d1501a848593a677798424dd03e46b3ed
```

The [release manifest](evidence/Compiler_Design_v0.2.0_incremental/ATLAS_FORGE_RELEASE_COMPILER_DESIGN_v0.2.0.json) records the exact base, delta, and final archive identities.

</details>

Follow [RESTORATION.md](RESTORATION.md) and the [deterministic restoration script](Releases/Compiler_Design_v0.2.0_incremental/RESTORE_ATLAS_FORGE_COMPILER_V02.py). Exact reconstruction requires the original predecessor archive and delta. The complete ZIP is kept out of Git history; the original preservation source remains unchanged. See [publication status](PUBLICATION_STATUS.md) and [release status](RELEASE_STATUS.md) for outstanding publication work and source-rights clearance.

## Roadmap and participation

The [original 30-domain roadmap](Roadmaps/Atlas_30_Domain_Roadmap_2026-11-12.md) remains the historical plan. The [current priority](Roadmaps/ATLAS_FORGE_CURRENT_ACTIVE_PRIORITY.json) is to strengthen **Compiler Design** through deeper control-flow graph checking, independent grammar fuzzing, and an explicit backend target scope. **Formal Verification, original priority 19, follows.** Domain content work precedes further Bitwork routing work.

Useful contributions include a well-sourced correction, a reproducible counterexample, a clearer derivation, an independent reproduction, a documented evidence gap, or improved offline instructions. Cite the relevant domain, record revision or file, exact source, and conditions needed to reproduce the finding.

Follow the [contribution and release protocol](Continuity_Toolkit/CONTRIBUTOR_AND_RELEASE_PROTOCOL.md). Preserve earlier scientific records and releases; add revisions that make the history inspectable. Respect the rights attached to each source: a bibliography entry or public URL does not grant redistribution rights to the underlying material.

---

<p align="center">
  <strong>ATLAS Federation</strong><br />
  Knowledge that endures because its evidence, context, and history endure with it.<br />
  <sub>James Paul Jackson · Original program: ATLAS FORGE</sub>
</p>
