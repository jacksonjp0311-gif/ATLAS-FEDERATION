# ATLAS FORGE — Human Knowledge Survival Charter

**Edition 1.0 · 13 November 2026 · Foundational design contract**  
**Owner's standard:** Construct the collection as though it might be the last usable store of humanity's knowledge. **This is an aspiration and an acceptance criterion, not a claim that the existing collection already holds all human knowledge.**

## 1. The standard

A useful surviving library must allow future readers—human or machine—to recover **what a proposition means**, **why it was believed**, **how its supporting observation was obtained**, **how to reproduce the calculation or experiment**, **where its limits lie**, and **how it interacts with knowledge elsewhere**. Merely saving abstracts, embedding vectors, URLs, or a popular conclusion cannot preserve a scientific civilization's reasoning. An equation without symbols and units can be useless or dangerous; a measured number without instrument, sample and conditions is not transferable; a source summary without attribution cannot be corrected when the original disappears.

The library must work in stages of resource scarcity. At the lowest level a reader has only a filesystem and a UTF-8 text viewer. The next level has a standard Python interpreter and a modest CPU. Higher levels may use relational databases, specialized solvers, GPU models and search indexes. No critical theorem, provenance declaration, or document location may *require* proprietary cloud authentication, a vector index, or a language model to be decoded. Bitwork-powered routing, when built at the end of the 30-domain content program, will accelerate retrieval but must not be the only path to knowledge.

## 2. Every domain's minimum scientific package

A finished content domain needs original explanatory chapters and navigable source cards, but **volume is insufficient**. A chapter should cover: the question, definitions and physical/mathematical objects, variables and units, relevant historical foundations, assumptions, derivation or causal mechanism, observation/experiment or computational method, an independently reproducible numerical or procedural example, competing or contradictory views, uncertainty, invalid use cases, and connections to other chapters. Algorithms need versioned source code and known tests; a simulation must identify its assumptions and seed. A failure case is part of the knowledge, not noise to delete.

It should be possible for an apprentice to begin with basic prerequisites, build a working understanding, and tell what additional data would be needed to solve a real problem. **No fabricated confidence, novelty, measurement, or peer review.** If a gap prevents an answer, preserve the gap and the experiment that would resolve it. Verified, refuted, contradicted, plausible, and unknown claims remain distinguishable.

We preserve at least three distinct representations: readable **UTF-8 Markdown**, machine-readable **canonical JSON/JSONL** with explicit schema and qualified links, and executable **plain Python** or well-specified pseudocode where computational knowledge is essential. Tabular datasets should use documented field names, units, missing-value semantics and reproducible parsing. Non-text scientific media require an accessible descriptive equivalent (equations, alt text, dimensions and metadata) without falsely claiming the textual description reproduces their full data.

## 3. Evidence ranks are not ratings of truth

Evidence is recorded by access and validation capability, not compressed to one misleading percentage:

- **L0 — Citation or unresolved locator.** A source is named; its bytes and exact passages may be unavailable. Useful as a lead, **not independently recoverable**.
- **L1 — Source-scoped notes.** A selected passage, metadata or publisher abstract was reviewed and paraphrased. Original file still may be missing and rights remain external.
- **L2 — Locally retained source bytes with provenance and permitted rights.** Include canonical origin, retrieval date, SHA-256, parser version, license and exact inspected portion. A hash proves bytes, not accuracy.
- **L3 — Reproduced analysis against an authentic documented dataset.** Include original raw bytes where legally permitted, transformation scripts, outputs and discrepancies; still distinct from conducting the original laboratory experiment.
- **L4 — Independently corroborated science.** Separate scientific teams, data or high-quality methodological reviews support the claim under specified conditions; evidence and disagreement must be retained. This cannot be conferred by passing unit tests.

These levels describe *specific claims and sources*, not entire domains. A repository may have L3 mathematical code and only L0 primary research. **Never display L2–L4 without the applicable supporting files and reviewer attribution.** A paper's two different webpages may be one experiment; don't count them as two replications. Raw observations are retained separately from normalized derived values.

## 4. Reproducibility and recovery requirements

Every tagged release should have a self-consistent tree manifest, hash list, schemas, environment requirements, tests, known failures, an offline reading index and a `RESTORE` guide. Preserve immutable previous revisions and add explicit supersession/contradiction relationships instead of editing history to look consistent. The release should be extracted on a clean machine and verified without network access. A knowledge reader must be able to inspect the original chapters even when packages cannot install. A Python-only audit should enumerate source gaps, verify hashes and report potential dependence on online services.

Record the algorithms of human knowledge production: how to form hypotheses; design fair comparisons; calibrate an instrument; collect raw data; distinguish association from causation; quantify uncertainty; falsify claims; and update records after contradictory evidence. Preservation cannot be purely static. Scientific progress requires an *audit of corrections*.

Redundancy is not equal to backup. The final deployment plan should include three separately verified copies, more than one geographic/storage failure domain, periodic fixity checks, read-only archives, documented encryption/key custody where needed, durable software versions and periodic migration of fragile file formats. This program **has not implemented that final off-site archival infrastructure**; the charter specifies its eventual acceptance test. An untested copy is not a verified restore.

## 5. Human and AI pathways

For a human: start with a domain map, prerequisites, explanation, practical worked example, full source citation and failure scenarios. For an AI: return a **bounded citation package** containing a claim, exact source and revision, units and applicability, assumptions and uncertainty, contradiction links and abstention reason. A retrieval score is not scientific credibility. Retrieved documents remain untrusted data, never executable tool instructions or permission grants. A useful result can be **we don't know**, together with a testable plan to learn it.

Memory and self-improvement must be evaluated on independently authored held-out tasks, with precommitted rubrics and budgets, appropriate baseline, truthful uncertain outcomes, effect size and cost, plus tests against contamination and regressions. A cached answer that sounds convincing does not establish learning. Do not use this archive's own teaching tests as a hidden benchmark for models it has taught.

## 6. Build order and discipline

The thirty-domain roadmap governs **content order**. Signal and Cymatics are preserved companion nodes; Measurement, Causal, Materials, Control and Agent are the content domains already built to differing maturity. Subsequent domains will build their complete depth before being considered ready. Agent Atlas is moving toward a scoped v1, followed by Computation Atlas. **Bitwork routing comes only after all thirty domain libraries' content editions**, then comparative integration/evaluation and desktop transfer. Do not opportunistically change the router during corpus authoring. The shared Forge contract must remain versioned and source-closed.

Release labels are always two-dimensional: `content_scope_ready` and `scientific_or_deployment_accepted`. We can call the bounded content edition 1.0 while still honestly retaining unresolved independent review, third-party source acquisition, and live AI measurements. The survival standard means each remaining dependency is **visible and recoverable**, not silently presumed solved.

## 7. What this archive cannot yet claim

As of this charter, it is **not humanity's comprehensive knowledge**, is **not offline-complete for the primary sources it cites**, is **not independently peer-reviewed**, and has **not deployed its final cross-domain routing or distributed backup system**. In particular, many source cards link to web material whose original bytes are not archived. This is a critical survivability debt, not a superficial TODO. Resolve it with appropriately licensed copies, durable identifiers, bibliographic facts and original explanatory reconstruction where reuse rights are restricted.

**Acceptance phrase:** *Every important conclusion must survive with its proof path, limits, and a way to learn more—not merely its words.*

**References:** Library of Congress, *Recommended Formats Statement 2025–2026*, particularly datasets and open character-based formats (https://www.loc.gov/preservation/resources/rfs/data.html); Sutton and Barto, *Reinforcement Learning: An Introduction*, second edition (MIT Press, 2018); OpenTelemetry agent trace conventions; primary sources referenced in each Atlas node. This charter is original project policy, not an international preservation standard or proof of completeness.
