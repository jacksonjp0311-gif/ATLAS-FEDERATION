# Chapter 36 — Carrier statistics, neutrality and coupled charge

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A semiconductor model must distinguish mobile electron concentration n from mobile hole concentration p, ionized donors N_D⁺, ionized acceptors N_A⁻, and trapped or fixed charge. For nondegenerate thermal equilibrium, the mass-action approximation is np≈n_i². The local space-charge density under the elementary drift–diffusion model is ρ=q(p−n+N_D⁺−N_A⁻)+ρ_fixed. These are not interchangeable with net dopant inventory: a compensated wafer can have large N_D and N_A but small net carrier density.

Electric potential couples into carrier statistics through electrochemical potentials. To avoid sign errors, explicitly write φ as electrostatic potential in volts, E=−∂φ/∂x, and the electron-charge sign as −q; use current J_n and J_p with their own sign conventions. Mathematically the coupled problem involves Poisson and two continuity equations; the Mathematics & Physics node already preserves a bounded 1D reference. Reuse it as an exact revisioned dependency instead of silently reimplementing a conflicting equation.

Boundary cases are as important as typical examples: n,p>0, total charge balance, contact and insulator boundary conditions, and uniqueness of the solutions are not guaranteed merely by a small nonlinear residual. A measured I–V curve needs additional mobility, recombination, trap, interface, and geometry calibration.

**Worked investigation:** choose n=10²¹ m⁻³, p=10¹⁹ m⁻³, N_D⁺=10²¹ m⁻³, N_A⁻=10¹⁹ m⁻³. The bracketed net ρ/q is zero; then perturb one term to demonstrate that charge neutrality is not hard-coded.

## Implementable contract and falsification

- **Reference equation:** `rho = q(p − n + N_D⁺ − N_A⁻) + rho_fixed`.
- **Dimensional quantities:** C/m³, m⁻³; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `coupled_math_dependency`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.
