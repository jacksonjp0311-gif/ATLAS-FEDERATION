# 02. Ion activities, chemical potential and membrane separation

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

For an ideal dilute solution, an ion electrochemical potential combines concentration and electrical work. The driving force depends on both the logarithm of the activities and the electrical potential. Cells are not ideal salt containers: activity coefficients, binding, fixed charge, osmolarity, transporters and ion gradients may invalidate this simple form.

## Governing mathematical model

`μ_i = μ_i° + R T ln(a_i) + z_i F φ`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

State the sign convention for transmembrane voltage as inside potential minus outside potential. Chemical and electrical terms have dimensions of joules per mole. The relative chemical driving term is R T ln(a_out/a_in), with a dimensionless activity ratio. Concentration ratios may approximate activities only with stated assumptions.

In a physical membrane, gradients are maintained by metabolism, selective permeability and transport pumps. Equal electrochemical potential implies no net passive driving force for that ion, not absence of all other ion fluxes or ATP consumption. Distinguish equilibrium from steady state: maintained pumps can produce stable concentrations under continual net transport. This is critical to designing measurements and interpreting apparent resting voltages.

## Independently checkable worked case

If the activity ratio outside/inside is 10 and z=+1, the ideal chemical contribution is R T ln(10). Its voltage equivalent is positive for the chosen Nernst sign convention. Reversing concentrations reverses sign, and doubling valence halves the voltage.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Do not infer equilibrium from one voltage measurement. No direct material characterization, membrane composition, ion pump work or equilibrium measurements are provided.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
