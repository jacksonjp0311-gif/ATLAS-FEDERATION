# 16. Electrogenic pumps, metabolic work and non-equilibrium ion gradients

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Biological membranes maintain ion gradients through selective permeability and active transport. An instantaneous equilibrium potential is only one part of this system. Maintaining a gradient against dissipation requires energy input and mechanisms such as ATP-consuming pumps; a complete model must conserve matter and charge at the system boundary.

## Governing mathematical model

`dN_i/dt=J_pump,i−J_leak,i; C_m dV/dt=Σ_i I_i + I_external (specified signs)`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

A physically adequate model would track ionic inventories on both sides, membrane geometry, osmotic effects, channel state, buffering, binding and metabolic energy. The present Bioelectric Atlas does not implement a validated multi-species electrodiffusion solver or a pump ATP cycle; it records those as independent scientific requirements and future computational nodes. Treat the source of free energy and charge continuity as prerequisites before interpreting a steady membrane potential.

When quantities are written per area, concentration and flux must be converted to total amounts using surface area and compartment volume. Charge neutrality can hold approximately in bulk electrolytes while thin interfacial double layers carry electrical charge. The capacitor picture is thus a useful abstraction but cannot replace a full electrochemical model. The checkable software components here cover ideal potentials and passive charge; biological pump rates remain unmeasured.

## Independently checkable worked case

Use the capacitor formula Q=C(V−V_ref) and a passive cable of five segments with sealed ends and zero leak. Under internal axial current redistribution, the sum of charge stays constant, showing the mathematical accounting needed before adding active flux terms.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

No active pump kinetic parameters, biological viability, wound healing mechanism, or human physiology prediction is certified. This chapter is a dependency map, not a clinical procedure.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
