# 35. Physical manufacturing dependencies and the limits of metadata-based assurance

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A software ISA is not a fabricated computer. An engineer attempting to reconstruct AT8 on real silicon or discrete logic needs material identity, wafer/device characterization, dielectric and contact metrology, voltage-transfer curves, clock/reset integrity, memory retention, power/thermal testing, interconnect/layout documentation and independently measured hardware execution traces. The Manufacturing and Electronics nodes define these as separate physical evidence obligations.

## Technical derivation and invariants

The physical evidence condition is a conjunction of necessary verified predicates: `AcceptedHardware = AND_i VerifiedByQualifiedProcess(E_i)`. A text field named `verified`, a copied SHA-256, or an AI-generated report is not an external calibration witness. Without trusted origin and independent measurements, every physical requirement remains open even if all placeholders are populated. The checker therefore never promotes assertions supplied as metadata into a physical pass.

## Executable method and reproduction requirements

`physical_evidence_matrix` lists 12 required types and the blocking stages. It accepts at most recognized names as asserted metadata, reports those claims separately, and retains all unverified physical requirements under HOLD. The Manufacturing evidence lattice remains the source of the full process/assurance graph; v0.2 deliberately does not duplicate or overwrite it.

## Constructed investigation

Supply `{"wafer_characterization":{"claimed":true}, ...}` for all 12 categories. The output reports 12 claimed metadata types and 12 unverified types. The software arithmetic and ROM protection tests can pass in the same session, but the hardware gate stays HOLD. This is a meaningful negative control against false confidence.

## Counterexamples, scientific limits and missing evidence

This is an audit protocol, not a real metrology experiment. Future reviewers must independently examine raw instrumentation records, calibrations, geometry, materials, foundry process receipts, test-chip traces and revision hashes before claims of physical reconstructibility.

## Source and dependency ledger

**Primary orientation:** `MIT-6004` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
