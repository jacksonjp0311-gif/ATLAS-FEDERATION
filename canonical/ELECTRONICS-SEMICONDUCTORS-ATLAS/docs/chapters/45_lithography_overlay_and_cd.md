# Chapter 45 — Lithographic pattern transfer and overlay error budgets

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Patterned semiconductor devices depend on more than masks: substrate flatness, optical wavelength, numerical aperture, illumination, resist chemistry, focus, etch bias, registration and defect contamination all affect printed critical dimensions. The conventional optical resolution heuristic CD≈k₁ λ/NA is only a scaling relationship; it is not a process-qualified printability equation and should not be extrapolated beyond the applicable system.

An explicit manufacturing reconstruction graph records mask production, lithographic imaging, resist development, etch, alignment verification and final structural metrology. Static tolerance stacking can give a conservative worst-case bound by summing declared independent *bounds*; it cannot establish statistical yield, line-edge roughness or correlated errors.

**Worked investigation:** a hypothetical 40 nm nominal feature has bounded error contributions of 1 nm mask, 2 nm alignment and 3 nm etch bias, producing a 6 nm worst-case additive bound. This is a mathematical budget, not a verified achievable semiconductor process. Compare that bound with an externally established permitted tolerance, and reject negative tolerance inputs.

## Implementable contract and falsification

- **Reference equation:** `CD approx k1 lambda/NA; err_max <= err_mask+err_overlay+err_etch`.
- **Dimensional quantities:** nm, dimensionless; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `line_edge_overlay_budget`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `IBM-SEMICONDUCTOR` from the source register. References identify public publication pages, not archived authenticated originals.
