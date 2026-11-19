# 13. Electrode–electrolyte interface as a passive dummy-load circuit

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Recording electrodes may introduce a complex impedance involving solution resistance, interfacial charge transfer, double-layer capacitance and nonideal electrochemistry. A minimal Randles-style network can be treated as solution resistance in series with an interface resistance in parallel with a capacitor. This is a **dummy electrical network** for algebraic checks, not a description of every biological electrode.

## Governing mathematical model

`Z(ω)=R_s + 1/(1/R_ct + jω C_dl)`

**Source orientation:** NEURON-CABLE (`https://www.neuronsimulator.org/en/latest/nmodl/transpiler/contents/cable_equations.html`), DOI not applicable to documentation. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use ohms, farads and hertz with ω=2πf. At zero frequency the capacitive branch is open, so Z=Rs+Rct. As frequency becomes large, the ideal capacitor shorts the parallel charge-transfer resistance and Z approaches Rs. The imaginary impedance of the ideal RC element is nonpositive under the chosen sign convention. This gives a reproducible analytic limiting behavior for independent verification.

Actual electrodes exhibit polarization, constant-phase elements, electrode half-cell offsets, DC drift, biochemical interactions, nonlinearity and safety constraints. An RC model with invented numbers cannot predict current density or safe contact with skin. The reference uses a non-biological dummy load exclusively and should never be wired to a person, animal or implant as a medical or experimental device.

## Independently checkable worked case

Take Rs=100 Ω, Rct=900 Ω, Cdl=1 µF. At DC expect 1000 Ω. As frequency rises, real impedance approaches 100 Ω and phase approaches zero. Verify these limiting cases algebraically and with the standalone code.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Never infer stimulation safety, clinical measurement accuracy, electrode gel compatibility or tissue electrode properties from this synthetic RC network.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
