# 04. Goldman–Hodgkin–Katz constant-field voltage and limiting cases

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

When Na+, K+ and Cl− contribute to a membrane voltage, their permeabilities and concentration gradients influence the zero-current potential. A simplified constant-field GHK formula uses monovalent ions, fixed permeability ratios and no explicit active pump current. The chloride concentrations reverse sides because its valence is negative.

## Governing mathematical model

`V = (R T/F) ln((P_K K_out+P_Na Na_out+P_Cl Cl_in)/(P_K K_in+P_Na Na_in+P_Cl Cl_out))`

**Source orientation:** GOLDMAN-1943 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC2142582/`), DOI 10.1085/jgp.27.1.37. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

The numerator and denominator contain products of relative permeability and concentrations in consistent units. The ratio remains dimensionless. Scale every permeability by a positive common factor and the potential must not change. As any one permeability dominates, the result should reduce to that ion’s Nernst voltage. This provides an independent suite of limiting-case checks even when no actual membrane has been measured.

The constant-field model is a specific mechanistic approximation, not a general replacement for tissue electrodiffusion or ion-channel current-voltage measurements. Relative permeability may change with voltage or state; channel interactions and ion selectivity can violate the assumed independence. The numerical implementation records these limits and rejects zero-total permeability and nonphysical concentrations.

## Independently checkable worked case

Set all permeability weights to zero except P_K and verify exact Nernst reduction; repeat for P_Na and P_Cl (with sign reversal). Compare a weight tuple (1,0.1,0.01) with (100,10,1): both must give the same voltage.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

A fitted GHK voltage alone does not identify unique permeability values, prove channel abundance or validate any clinical inference. Source-to-equation reviewer acceptance remains absent.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
