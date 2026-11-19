# Chapter 39 — MOS substrate body effect, threshold definition and signs

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

For a long-channel NMOS with a p-type body under the standard depletion approximation, reverse source–body bias increases the magnitude of depletion charge. One compact threshold expression is V_T(V_SB)=V_T0+γ(√(2φ_F+V_SB)−√(2φ_F)), with φ_F taken as a positive potential magnitude and V_SB≥0. Gamma carries units √V. The square-root term can be derived by combining Poisson charge in the depleted bulk with the oxide gate-charge relation.

This relation is not universal for short-channel transistors, forward-bias bulk junctions, nonuniform doping, floating body or strong interface-charge effects. Always state the sign convention: V_SB=V_source−V_body. Permitting negative V_SB in a model documented only for reverse bias can silently invalidate the derivation.

Threshold voltage itself depends on an operational extraction definition, not a single primitive constant. Device characterization should record how threshold was extracted from current–voltage curves, temperature, drain bias and body bias.

**Worked investigation:** for synthetic V_T0=0.6 V, γ=0.3√V, φ_F=0.3 V, V_SB increasing 0→2 V, demonstrate monotone threshold increase. Check that V_SB=0 reproduces V_T0. Mark measured γ and φ_F as unavailable.

## Implementable contract and falsification

- **Reference equation:** `V_T(V_SB)=V_T0+gamma(sqrt(2phi_F+V_SB)-sqrt(2phi_F))`.
- **Dimensional quantities:** V, sqrt(V); all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `mos_body_effect_threshold`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.
