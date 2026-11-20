# Chapter 42 — Diffusion equation and bounded dopant redistribution

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Under Fick diffusion with constant D, the concentration obeys ∂C/∂t=D∂²C/∂x². For an idealized surface sheet dose Q distributed into the nonnegative half-space with reflecting boundary and no loss, the Gaussian solution is C(x,t)=Q exp[−x²/(4Dt)]/√(πDt). Its integral over x∈[0,∞) is Q, showing dose conservation. The finite-depth integral is Q erf[x/(2√Dt)].

This is *not* a furnace diffusion recipe. Real implants, oxide interfaces, vacancies, activation, clustering, electric-field effects and temperature-dependent diffusivity invalidate the constant-D, delta-initial-dose model. Restoring actual semiconductor processing requires distinct measurement, safety and contamination-control methods; the Atlas preserves the equation and its falsifiable assumptions, not an unverified physical process.

**Worked investigation:** Q=10¹⁶ m⁻², D=10⁻¹⁴ m²/s, t=10 s. Verify that the integrated dose approaches Q at large depth and that the surface concentration declines with √t. Compare erf-integral against a high-precision oracle; report absolute and relative numerical errors. Reject t≤0 and D≤0.

## Implementable contract and falsification

- **Reference equation:** `C(x,t)=Q exp(-x²/(4Dt))/sqrt(pi D t)`.
- **Dimensional quantities:** m⁻³, m²/s, m⁻²; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `half_space_gaussian_dopant`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.
