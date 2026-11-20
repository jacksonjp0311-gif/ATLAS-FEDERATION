# Chapter 19: From resistor-capacitor networks to timed node voltages

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
Given capacitances to ground, conductive edges and applied current or voltage sources, reconstruct the voltages after a finite time step. This is the circuit analogue of a finite-volume conservation law. A future engineer must distinguish a calculated digital delay from measured voltage transitions.

## Derivation and dimensions
Write Kirchhoff current conservation at each free node as

\[C_i\frac{dV_i}{dt}+\sum_j G_{ij}V_j=I_i,\]

where capacitance is in farads, conductance is in siemens, voltage is in volts, and current is in amperes. Each edge \(g_{ij}\) contributes \(+g_{ij}\) to two diagonal entries and \(-g_{ij}\) to the corresponding off-diagonals. A grounded resistor contributes only to the diagonal. For backward Euler,

\[(C/\Delta t+G)\,V^{n+1}=C V^n/\Delta t+I^{n+1}.\]

A prescribed Dirichlet voltage is removed from the free-node system and transferred to the right-hand side. For positive grounding and capacitance this finite system is positive definite on free nodes. The reference implementation uses bounded pivoted Gaussian elimination, not production sparse factorization.

## Worked investigation
One capacitor \(C=1\ \mu\mathrm F\), shunt \(R=1\ \mathrm{k}\Omega\) (\(G=1\ \mathrm{mS}\)), \(V_0=2\ \mathrm V\), and \(\Delta t=1\ \mathrm{ms}\) gives \(V_1=(2)/(1+\Delta t/(RC))=1\ \mathrm V\). For an edge from a fixed 1 V node through a 1 kΩ resistor to a 1 µF node starting at 0 V, the first step gives 0.5 V.

## Limits and counterexamples
An exact time-continuous exponential is not equal to one backward-Euler step: at \(\Delta t=RC\), \(V_1/V_0=1/2\) versus \(e^{-1}\) analytically. Small discrete KCL residual does not establish small time-discretization error. Ideal fixed voltage sources do not predict source limitations, device parasitics, dielectric leakage or electromagnetic radiation. Large ill-conditioned networks require sparse solvers and measurement-validated elements.

## Reconstruct and verify offline
Run `rc_nodal_backward_euler` and compare every free-node voltage against a separately assembled linear system. Check graph indexing, finite inputs, positive R/C, discrete KCL residuals, step refinement and the effect of controlled voltage sources. Reject malformed graphs instead of silently inventing a reference node.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `rc_nodal_backward_euler`.
- **Equation/invariant:** `C dV/dt+G V=I; (C/dt+G)V_next=C V_old/dt+I`.
- **Units:** Farad, Siemens, Volt, Ampere, seconds.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.
