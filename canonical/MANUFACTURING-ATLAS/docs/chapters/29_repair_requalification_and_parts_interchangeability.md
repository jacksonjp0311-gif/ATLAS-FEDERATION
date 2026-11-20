# Chapter 29: Repairs must regenerate qualification evidence

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`postrepair acceptance = spec ∧ traceable_measurement ∧ evidence_of_changed_components`

## Scientific derivation and engineering reasoning

Technological continuity requires maintenance and rebuilding as much as first-time manufacturing. When a machine component is replaced, a formerly calibrated assembly may no longer meet its previous accuracy, alignment, stiffness or thermal specifications. Repair is a state transition that should invalidate dependent qualifications unless fresh evidence confirms applicable performance.

A repair trace starts from symptoms and out-of-tolerance observations, records replaced components and their provenance, updates geometric and uncertainty budgets, then schedules controlled post-repair measurements against appropriate references. The validity of prior inspection data must be reviewed. For example, changing a measuring probe tip affects offset and possibly uncertainty, while replacing a leadscrew can change backlash and axis response.

The graph does not assume all repairs require a full factory requalification or that a single passing dimension proves success. It identifies which evidence types depend on the changed component. A future competence-reviewed policy must set specific criteria for releasing machinery to service.

Constructed test: a repair step requests a new calibration record and an alignment measurement. Without either, the subsequent inspection step is blocked even if the prior drawing and parts list exist. This is a software demonstration of evidence dependencies, not an instruction to operate repaired equipment.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_evidence_gate; covariance_budget_psd`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Maintenance planning is not machine safety certification or control-system functional-safety testing.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
