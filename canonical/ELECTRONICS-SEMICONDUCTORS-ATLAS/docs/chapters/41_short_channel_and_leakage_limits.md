# Chapter 41 — Short-channel, subthreshold and device model limits

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Practical transistors exhibit weak inversion, drain-induced barrier lowering, velocity saturation, mobility degradation, gate tunneling, junction leakage and parasitic resistance/capacitance. Many effects make an ideal square-law current versus gate voltage incorrect over the full operating range. A simple subthreshold mnemonic is I_D∝exp[(V_GS−V_T)/(n_s V_T)] with a measured subthreshold slope factor n_s, but the prefactor and boundary conditions are device specific. This memo deliberately does not blend that form into the ideal MOS model without calibrated parameters.

The device should be characterized by families of I_D–V_GS and I_D–V_DS sweeps at several controlled temperatures, drain voltages and body biases; observations must distinguish threshold extraction, leakage floor, current compliance, self-heating and time-dependent bias effects. Cross-corner validity requires model error metrics at process/voltage/temperature corners, not one appealing fit.

A reconstruction package must preserve both the model and evidence of its failures. The present finite references demonstrate long-channel mathematics, not transistor fidelity at nanometer feature sizes.

**Worked investigation:** construct two hypothetical I–V traces with the same textbook threshold but different leakage and slope parameters. Show that a single threshold number cannot identify leakage behavior. Record the identifiability gap as a review blocker rather than tuning arbitrary constants.

## Implementable contract and falsification

- **Reference equation:** `S_sub = (ln(10)) n_s V_T  [V/decade]`.
- **Dimensional quantities:** V, A, K; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `none`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.
