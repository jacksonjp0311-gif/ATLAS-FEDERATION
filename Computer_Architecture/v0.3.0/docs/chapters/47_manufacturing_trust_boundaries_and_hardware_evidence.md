# 47. Physical measurement requirements for a trusted booting computer

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`hardware_acceptance = AND(material, device, gate, clock, memory, boot, independent_trace)`

**Units and representation:** SI voltage, time, temperature, geometry and verification receipts. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The original Manufacturing and Electronics nodes provide a technical dependency chain for a computer, but a simulation cannot certify that silicon or discrete gates were fabricated. The minimum evidence groups include material identity, wafer or substrate characterization, transistor I–V and C–V, dielectric and contact metrology, gate transfer and timing across process/voltage/temperature, clock/reset integrity, physical memory retention, power/thermal behavior, layout/interconnect records, manufacturing receipts and independent execution traces. No physical evidence types are declared verified just because a JSON object asserts them. The `physical_evidence_matrix` explicitly returns all twelve types as unverified and six staged goals as blocked.

To advance, an independent laboratory or qualified practitioner must publish exact device identifiers, instrument calibration certificates and raw measurements. For firmware resilience, protection/detection/recovery is a useful high-level framework, but adding an unsigned CRC header alone does not implement NIST SP 800-193's protection controls. A real trusted boot would need cryptographic trust anchors, signature verification, rollback authorization, persistent storage semantics, power loss fault tests and physical attack-surface assessment. The abstract two-slot reference is a tool for documenting questions, not evidence those controls exist.

## Reproduce this investigation offline

Execute the AT8 source program through the independent software models, then query the physical evidence matrix. The software section produces a reproducible ROM/result digest. The physical section lists twelve missing evidence types and a HOLD status even when supplied a metadata mapping with all twelve keys set True. This distinguishes *a claim that someone observed a device* from *an independently validated measurement record*. Build the empty measurement dossier for future silicon or discrete-logic experiments.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `physical_evidence_matrix`.

## Counterexamples, failure modes, and model scope

No hardware processor, physical ROM boot, cryptographic authentication root, chip fabrication, device calibration, controlled timing corner, electrical safety approval or external peer review is established by this release. Even full functional software equivalence cannot substitute for those experiments. Explicit uncertainty preserves scientific credibility.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
