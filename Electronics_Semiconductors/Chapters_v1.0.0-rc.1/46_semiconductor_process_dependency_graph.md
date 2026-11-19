# Chapter 46 — Oxidation, deposition, etch, doping and process order

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Chip fabrication is a dependency-controlled sequence of transformations of the wafer, not one material recipe. A minimal account distinguishes starting substrate inspection, surface preparation, electrical isolation, dielectric growth/deposition, lithographic patterning, selective material removal, dopant introduction and activation, conductor formation, interconnect and passivation, probe, packaging and final testing. Each operation changes geometry, stress, composition, electrical behavior or defect population; the order matters because later thermal and chemical steps can modify earlier layers.

For each transformation preserve inputs, outputs, material identity, measurement checkpoints, safety controls, process-window assumptions and evidence grade. A step should not be called successfully reproduced merely because its name exists in a flowchart. Require instrument logs and physical inspection, plus independent validation of wafer purity, overlay, film thickness, sheet resistance, line continuity, and yield.

The reference edition provides a process dependency graph and failure taxonomy, not detailed high-purity cleanroom instructions, chemical specifications or a proven fabrication route.

**Worked investigation:** trace a gate dielectric from target electrical capacitance backward to material permittivity, area, thickness, oxide formation, uniformity measurement, leakage test and circuit-level switching consequences. Flag every handoff where no physical measurement dataset exists.

## Implementable contract and falsification

- **Reference equation:** `gate_C = epsilon A/t; process steps preserve ordering dependencies`.
- **Dimensional quantities:** F, m, s, K; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `none`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `IBM-SEMICONDUCTOR` from the source register. References identify public publication pages, not archived authenticated originals.
