# 01. Dimensional consistency for bioelectric systems

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The membrane potential is an electrical potential difference, not a force, current or chemical concentration. All quantities must be dimensioned explicitly. Core constants from the SI defining system are kB=1.380649e−23 J/K, e=1.602176634e−19 C, and NA=6.02214076e23 mol−1. Hence R=kB NA and F=e NA are algebraic combinations of exact SI definitions; practical experiment measurement of temperature, concentration, cell area and currents remains uncertain.

## Governing mathematical model

`V_T=k_B T/e; F=e N_A; C_mem=C_specific*A; U_C=0.5 C_mem V^2`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use K for thermodynamic temperature, mol/m³ (or a declared consistent concentration unit for ratios), C for charge, A for current, F for capacitance, S for conductance and V for voltage. Equations using mV or ms must provide explicit conversion factors. A common reconstruction failure is mixing microfarads per square centimeter with farads per square meter, creating a factor-of-ten-thousand error in area scaling. Biological signals are usually small enough that grounding and interference can dominate observations; none of those physical errors is automatically represented by a software trace. Test formula dimensions before interpreting numerical outputs.

A membrane capacitor is a useful electrical approximation because the lipid bilayer impedes charge transport while its faces support charge separation. This does not mean every biological membrane is a perfect linear, lossless capacitor; voltage-dependent capacitance, membrane geometry, access resistance and electrode artifacts can matter. The Atlas retains the assumptions as part of the scientific result.

## Independently checkable worked case

For area A=0.5 m² and specific capacitance c=0.02 F/m², the model predicts C=0.01 F. For C=2 F and V=3 V, ideal stored energy is 9 J. These synthetic examples verify dimensions only, not an actual cell.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

No membrane geometry, injury threshold, live-cell permeability or patient outcome is measured. The numerical tests must never become unqualified equipment specifications or stimulation guidance.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
