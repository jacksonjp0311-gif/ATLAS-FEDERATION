# Chapter 23: An unbroken metrology chain needs real evidence

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`measurand → instrument → lab reference → SI realization, each with uncertainty`

## Scientific derivation and engineering reasoning

A measurement is traceable through a documented chain of comparisons, each carrying a defined quantity, uncertainty and competent calibration source. The chain is a graph of certificates and reference standards, not a marketing claim attached to a measuring tool. At each edge preserve the measured standard, procedure, uncertainty budget, date, environmental control, correction factor and interval before recalibration.

The software checks a declared chain for missing parent records, cycles, missing units, absent uncertainties, expired dates and malformed SHA-256 strings. It still returns `documentation_present_not_source_authenticated` when all metadata looks complete. That distinction is essential: a syntactically plausible 64-character checksum does not prove the original certificate bytes were inspected, or that its issuer was competent.

Constructed case: a gauge references a lab certificate, which references a root standard. The metadata has consistent units, valid dates and checksum strings. The graph is structurally complete, but no actual certificate was retrieved or signed; hence external authentication remains false. A missing parent or expired certificate blocks the declared chain.

For genuine metrological evidence, inspect authentic documents, certificate signatures, measurement logs and accredited competence, and preserve their exact bytes and cryptographic hashes separately from interpretation records.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.traceability_chain_audit`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

The tool is a metadata integrity audit, not NIST accreditation or a device calibration.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
