# 13. Nodal circuit analysis, conductance matrices and power accounting

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Nodal circuit analysis, conductance matrices and power accounting. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`Σ_j (V_i−V_j)/R_ij=I_i^inj; P_R=Σ_edges (V_a−V_b)^2/R_ab`

**Units:** Ω, S, V, A, W. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

Kirchhoff’s current law at each free node states that current leaving through connected resistors equals externally injected current. Assemble conductance matrix G: G_ii=Σ_j 1/R_ij and G_ij=−Σ_(i,j)1/R_ij. Move fixed-potential neighbors to the right-hand side, retaining their source reaction currents. With positive resistances and at least one fixed potential per connected component, the reduced G is symmetric positive definite. A floating component has a gauge degree of freedom; refuse it instead of silently assigning ground.

The power certificate follows by multiplying each KCL row by V_i and summing. Every edge contributes (V_a−V_b)²/R, so total resistive loss equals the sum of injected-current power and fixed-voltage-source reaction power. This equality checks sign conventions and assembly without asserting a physical resistor’s actual tolerance or temperature behavior.

## Independently executable algorithm

Use `resistor_network` with bounded node count (≤64), positive finite resistances and finite fixed potentials/current injections. Independently assemble dense NumPy G and solve with `numpy.linalg.solve` in the optional oracle. Verify KCL on every free node, source-current sum, Joule positivity and power balance. Deliberately test an isolated component, self-loop, zero resistance and negative resistance.

## Worked scientific investigation

A 3 V source drives a 1 kΩ and 2 kΩ series divider to ground. KCL gives V_mid=3×(2/3)=2 V, I=1 mA, P_R=(1 mA)²×3 kΩ=3 mW. Compute fixed-node source reactions and verify the 3 mW external delivery. For a distributed network, insert parallel edges and independent current injections and compare the result with a second dense assembly.

## Failure conditions and counterexamples

This solver covers linear DC resistors, ideal current injections and fixed voltages. It does not model capacitors, inductors, nonlinear junctions, wires at high frequency or parasitic thermal coupling. Solving KCL does not prove manufacturability.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.
