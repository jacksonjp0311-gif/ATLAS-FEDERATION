# Chapter 27: Evidence-carrying process plans refuse unsupported completion

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`ready_i = inputs_present ∧ required_evidence_present ∧ all_dependencies_ready`

## Scientific derivation and engineering reasoning

A process graph can list perfectly plausible steps but still be impossible to execute. Each stage needs input artifacts, outputs, prerequisite stages and a declared set of evidence types. The evidence-gated planner propagates missing inputs and missing evidence through the dependency graph, returning HOLD rather than inventing a completed manufacturing step. This is the major integration principle connecting ATLAS FORGE's scientific library with reconstructible operations.

The result has two independent dimensions. **Structural completeness** means the required item names and evidence declarations exist according to the supplied metadata. **Scientific/physical certification** requires authentic measurements, competent reviewers and physical inspections and is never inferred by this method. A recorded hash or a user-supplied certificate label cannot turn a synthetic plan into an authenticated fabricated component.

Constructed case: raw stock feeds inspection with required calibration and measurement evidence. If calibration is present but measurement absent, inspection HOLDs and all downstream dependent stages remain blocked. If both are provided only as synthetic metadata, the planner can be structurally complete, but `independently_certified` remains false.

Graph cycles, unknown inputs, duplicate produced artifacts and malformed metadata are errors, not states silently skipped. This provides an executable audit scaffold for the future Manufacturing-to-Computer Architecture handoff.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_evidence_gate`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Recorded evidence metadata does not authenticate a lab, physical part or safety control.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
