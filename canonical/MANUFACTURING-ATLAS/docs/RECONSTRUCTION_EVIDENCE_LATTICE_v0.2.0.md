# ATLAS FORGE — Reconstruction Evidence Lattice (research proposal)

**Status:** original preliminary engineering formulation, NOT a proven new scientific theorem, peer-reviewed protocol, production controller, source-authentication service or verified manufacturing method.

## Why a single "passed" flag is inadequate

A mathematical solver can pass every unit test while predicting a device that has never been fabricated. A paper may be correctly cited but not archived with rights or source-integrity evidence. A manufacturing route can be causally well structured even when its material, metrology and safety dependencies are absent. Therefore a reconstruction certificate needs distinct evidence dimensions.

For any scientific/engineering claim or node `v`, define a declared evidence vector

\[E(v)=(e_{math}, e_{software}, e_{source}, e_{physical}, e_{review})\in\{0,1\}^{5}.\]

The dimensions represent demonstrated mathematical consistency under stated assumptions, executable software reproduction, authenticated publisher-original source fidelity and rights, actual calibrated physical measurement, and independent qualified review. An entry set to `1` means **a specific identified receipt exists and has been independently verified**, not that an author supplied a boolean string. Each dimension retains a content-addressed receipt ID, scope, assumptions, expiry/edition and reviewer identity where applicable. The actual ATLAS FORGE v0.2 implementation is currently a *metadata gate*, and does not authenticate any of these externally.

The componentwise partial order `E1 <= E2` means no evidence dimension becomes weaker. For claims requiring all components simultaneously, use the **meet** (componentwise minimum) across prerequisite dependencies, but do not globally combine unrelated evidence: a theorem's software test and an experiment's raw data answer different questions. The evidence vector is a decision-support abstraction, not an objective five-dimensional measure of truth.

## Reconstruction proof obligation

A proposed artifact `A` defines a **typed dependency graph** `G=(V,E)`, plus an explicit set of required evidence dimensions `Q_A(v)` for every stage. The artifact is *eligible for review* only if all required evidence types are actually present, valid, within their stated time/edition scope and traceable to a verifiable source. Eligibility is distinct from engineering qualification. A source URL, asserted SHA-256 text or synthetic dataset never automatically satisfies the original-source or physical-measurement dimension.

For a critical chain, the weakest required evidence dimension is a bottleneck. A validated calculation cannot promote a missing physical calibration, and one successful device test cannot certify the complete production process. Negative findings must travel with the relevant node and must not be erased by later software passes.

## Executable seed

`manufacturing_atlas.v02_models.manufacturing_evidence_gate` currently checks typed input artifact availability, prerequisite order and recorded evidence labels, propagates HOLD across dependency edges and distinguishes `structurally_complete` from `independently_certified`. `evidence/reconstruction_challenge.py` demonstrates this boundary by successfully executing an Electronics 8-bit interpreter but flagging all six physical fabrication stages as blocked by absent genuine metrological and manufacturing evidence. **This is not physical reconstruction of a computer.**

## Falsification and research route

1. Give independent reviewers version-pinned tasks with missing and contradictory evidence. Test whether the graph refuses unjustified promotion, even when every local Python test passes.
2. Introduce authentic instrument data, authenticated publisher originals and independent review receipts. Audit type-specific validators and adversarial attempts to forge or mismatch documents.
3. Run controlled comparisons against ordinary document retrieval on manufacturing fault diagnosis and component reconstruction; report accuracy, missing-evidence detection, cost, and actual physical reproduction success.
4. Include failures, withdrawn certificates, calibration expiration and revisions. Re-run dependent claims to test evidence invalidation and restoration.

The full research question is whether preserving *evidence-bearing dependency chains* improves independent reproducibility and reduces erroneous physical conclusions. This is a hypothesis that still needs outside experiments and critical review.

## Architecture guardrail

This memorandum lives as content inside the original Manufacturing node. It **does not** implement a new Bitwork router, new AI model, autonomous factory controller or second ATLAS FORGE federation. The original 30-domain roadmap remains authoritative and immutable.
