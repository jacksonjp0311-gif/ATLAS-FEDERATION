# Chapter 37 — Junction I–V, diode stable numerics and missing parasitics

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The ideal Shockley law I=I_s(exp(V/(n V_T))−1) follows from low-level injection, quasi-neutral regions and diffusion transport under a limited p–n junction model. It is not an avalanche-breakdown equation, a series-resistance model, a high-injection model, or a thermal device model. Logarithmic current plots can hide the difference between measured leakage and an assumed saturation current.

Use `expm1(x)` for the difference exp(x)−1 when |x| is small. Direct subtraction loses relative precision near zero bias. In reverse bias many thermal voltages below zero, the ideal current approaches −I_s, but real reverse leakage and breakdown are absent. At large forward voltages, the ideal exponential overflows or predicts unphysical currents; the reference implementation reports its bounded range rather than returning an invented value.

A measured I–V acquisition plan records T, current compliance, fixture contact resistance, forward and reverse sweep direction, dwell time, self-heating, and repeatability. Only after measuring these can one estimate ideality factor from d ln I/dV, and only in an empirically justified bias interval.

**Worked investigation:** compute I at 0, ±0.1 and +0.3 V at T=300 K, with a declared synthetic I_s and n. Show exactly zero current at V=0 and the −I_s asymptote in the ideal model. Independently calculate with high precision and mark that as numerical, not laboratory evidence.

## Implementable contract and falsification

- **Reference equation:** `I = I_s expm1(V/(n V_T))`.
- **Dimensional quantities:** A, V, K; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `ideal_diode_current`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.
