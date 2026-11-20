# 03. Nernst equilibrium voltage with explicit valence and units

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The Nernst potential of a permeant ion is the voltage at which the electrochemical potential differences balance under the ideal single-ion model. The sign depends on which side is called inside and on the ion charge. It is particularly easy to reverse the chloride result if valence is omitted.

## Governing mathematical model

`E_ion = (R T / z F) ln(a_out/a_in)`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use a dimensionless activity or consistent-concentration ratio, thermodynamic temperature T>0 and nonzero integer valence z. A log10 expression requires multiplying by 2.303; natural logarithms have no such factor. Unit errors can be caught by comparing the thermodynamic voltage scale R T/F with the exact kB T/e value. For multivalent ions, z appears in the denominator.

The mathematical model is deterministic. Its biological applicability is not: the membrane may be permeable to several species, activity coefficients may deviate from unity and a measured potential may have reference-electrode junction offsets. The implementation therefore refuses zero or negative concentrations and invalid valence rather than silently defaulting to a membrane voltage.

## Independently checkable worked case

For a positive monovalent species, T=310.15 K, c_in=140 and c_out=5 in identical units, E≈−89 mV. Swapping inside/outside makes +89 mV. For an anion with the same concentration ratio, the sign reverses.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

This is not a personal health measurement or a recipe for applying potentials to tissue. No transport pumps, geometry, Nernst-Planck field gradients or clinical thresholds are inferred.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
