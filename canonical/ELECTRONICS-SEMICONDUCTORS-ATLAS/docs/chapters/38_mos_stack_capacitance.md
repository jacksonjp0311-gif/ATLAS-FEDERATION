# Chapter 38 — MOS oxide capacitance and material thickness

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A metal–insulator–semiconductor stack first requires geometrical capacitance. A uniform planar oxide of thickness t_ox, electrode area A and relative permittivity ε_r has C_ox=ε₀ ε_r A/t_ox. Its per-area capacitance is C_ox/A=ε₀ ε_r/t_ox. Derivation: E≈V/t in the ideal uniform slab; D=εE; Q=DA; C=dQ/dV=εA/t. The derivation assumes no fringing, no dielectric dispersion, no breakdown, and uniform dimensions.

A real MOS capacitance–voltage curve differs from the oxide-only expression because space-charge, interface-state, depletion, accumulation and inversion capacitances can contribute in series or frequency-dependent ways. Forcing a measured C–V curve to equal this simple equation would erase critical semiconductor information.

Manufacturing reconstruction requires dielectric composition and thickness metrology; ellipsometry, capacitance measurement, reference geometry and contact calibration must be separately documented. A single tabulated ε_r value does not certify a process.

**Worked investigation:** double the oxide thickness at constant area and composition. The model predicts a capacitance ratio of 1/2. Multiply area by four and verify a fourfold capacitance change. Reject t_ox=0 and ε_r≤0. The implementation is explicitly parallel-plate only.

## Implementable contract and falsification

- **Reference equation:** `C_ox = epsilon_0 epsilon_r A/t_ox`.
- **Dimensional quantities:** F, F/m², m; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `mos_oxide_capacitance`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.
