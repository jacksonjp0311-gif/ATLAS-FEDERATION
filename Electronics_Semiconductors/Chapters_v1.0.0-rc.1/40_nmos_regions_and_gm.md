# Chapter 40 — Long-channel MOSFET current regions and transconductance

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Start from the ideal charge-sheet gradual-channel approximation with channel inversion charge proportional to V_GS−V_T−V(x). Under a constant mobility, uniform width-to-length ratio and negligible velocity saturation, integrate the charge drift term along the channel to get I_D=k[(V_GS−V_T)V_DS−V_DS²/2] for 0≤V_DS<V_GS−V_T. At pinch-off, the ideal saturated result is k(V_GS−V_T)²/2. The factor k normally contains μ_n C_ox(W/L) and its value must be identified experimentally or from a qualified process model.

For V_GS≤V_T, a deliberately ideal *cutoff* branch returns zero; this is not how measured subthreshold leakage behaves. Optional channel-length modulation multiplies by (1+λ V_DS), an empirical convenience, not evidence that short-channel electrostatics is modeled. The transconductance g_m=∂I_D/∂V_GS is k V_DS in the triode region and k(V_GS−V_T) in the ideal saturated region (both scaled by the declared λ factor).

**Worked investigation:** evaluate an NMOS at V_GS=1 V, V_T=0.5 V, V_DS=0.25 V, k=1 mA/V²; compare the 93.75 μA linear-region result to 125 μA in ideal saturation. Check continuity at V_DS=0.5 V. Explicitly reject negative V_DS in the forward-only model.

## Implementable contract and falsification

- **Reference equation:** `I_D,linear=k[(V_GS−V_T)V_DS−V_DS²/2]`.
- **Dimensional quantities:** A, V, S; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `long_channel_nmos`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.
