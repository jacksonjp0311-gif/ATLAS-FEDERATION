# Chapter 35 — SI electrical constants, units and measurement traceability

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The chain from electrons to a computer begins with *measured* electric charge, time, temperature, length and geometry. Do not substitute unitless constants or assume that a textbook material parameter is a reference standard. In the SI, the elementary charge q is exactly 1.602176634×10⁻¹⁹ C and Boltzmann's constant is exactly 1.380649×10⁻²³ J K⁻¹ by definition. Vacuum permittivity is not a defined exact constant; use the cited CODATA edition and record uncertainty when needed.

Thermal voltage is V_T=k_B T/q. Checking dimensions: (J/K)(K)/(C)=J/C=V. At T=300 K the reference implementation yields approximately 25.852 mV. Conversion of dopant density must be explicit: 1 cm⁻³ = 10⁶ m⁻³. Resistivity is Ω·m, sheet resistance is Ω per square, mobility is m²/(V·s), Hall carrier density is m⁻³ and oxide capacitance per area is F/m².

An audit chain should name the instrument, its measurement quantity, calibration certificate, uncertainty, traceability, date, temperature, fixtures, and sampling method. In this edition no physical instrument results or accredited calibrations have been received. All numerical values used in examples are constructed inputs.

**Worked investigation:** calculate V_T at 250, 300 and 350 K, then show that an ideal diode current's voltage sensitivity varies with 1/V_T. Retain the input temperatures and q/k_B constants in a machine-readable receipt. Reject T≤0 K as physically outside the model. Source references: BIPM SI Brochure and NIST semiconductor metrology pages, bibliographic links only.

## Implementable contract and falsification

- **Reference equation:** `V_T = k_B T/q`.
- **Dimensional quantities:** V, K, J, C; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `thermal_voltage`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `BIPM-SI` from the source register. References identify public publication pages, not archived authenticated originals.
