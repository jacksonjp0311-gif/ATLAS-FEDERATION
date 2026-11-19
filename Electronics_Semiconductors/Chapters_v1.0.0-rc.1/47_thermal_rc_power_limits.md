# Chapter 47 — Thermal conduction, self-heating and power budgeting

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

An electronic circuit stores and dissipates energy. Charging a capacitor C from a supply V stores E_C=½CV²; in a resistive charge cycle the supply delivers CV² and dissipates the remaining half in the path, under the ideal charge model. Activity factor α, clock frequency f and total switched capacitance lead to the common dynamic-power approximation P_dynamic≈α C V² f. Leakage and short-circuit power must be accounted for separately.

The simplest lumped thermal response is C_th dT/dt=P−(T−T_ambient)/R_th. For constant power P, T(t)=T_ambient+PR_th+[T(0)−T_ambient−PR_th]exp[−t/(R_th C_th)]. It does not model hot spots, nonlinear thermal conductivity, multiple packages or electromagnetic coupling.

A temperature limit cannot be established from this model without independent package/interface characterization, steady-state cooling configuration and measured device temperature. Refuse unsupported claims of safe operating conditions.

**Worked investigation:** T_amb=300 K, T(0)=300 K, P=2 W, R_th=10 K/W, C_th=0.1 J/K; the model approaches 320 K with a 1 s time constant. Verify initial and long-time bounds.

## Implementable contract and falsification

- **Reference equation:** `T(t)=T_amb+P R_th+(T0−T_amb−P R_th)exp(−t/(R_th C_th))`.
- **Dimensional quantities:** K, J/K, K/W, W; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `thermal_rc`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.
