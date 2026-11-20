# Chapter 43 — Four-point probe, sheet resistance and Hall metrology

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Electrical metrology starts with geometry and identifiability. For a homogeneous, isotropic, infinite thin conducting sheet and four equally spaced collinear probes, R_sheet=(π/ln 2)(V/I). Finite boundaries, inhomogeneous thickness, contact geometry, sample anisotropy, temperature drift and thermoelectric offsets require correction. The coefficient is not a universal value for arbitrary probe placements.

In a simple one-carrier Hall bar, |n|=|IB/(q t V_H)| from R_H=V_H t/(IB) and |R_H|=1/(q|n|). Carrier-type sign requires a carefully documented voltage, magnetic field and current orientation; the reference function returns magnitude only. Multi-carrier systems, Hall factors and contact nonidealities can substantially alter inference.

A real acquisition should reverse both current and magnetic field to suppress offsets, measure thickness and instrument uncertainties, and preserve raw traces and calibration certificates.

**Worked investigation:** synthesize V and I for R_sheet=50 Ω/□; recover the sheet resistance. Then synthesize a Hall voltage for n=10²² m⁻³ and verify recovery without claiming actual wafer doping was measured. Reject B=0 and V_H=0 as non-identifiable in this model.

## Implementable contract and falsification

- **Reference equation:** `R_sheet=(pi/ln2)(V/I); n=|I B/(q t V_H)|`.
- **Dimensional quantities:** Ohms/square, m⁻³; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `four_point_sheet_resistance;hall_carrier_density`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `NIST-HALL` from the source register. References identify public publication pages, not archived authenticated originals.
