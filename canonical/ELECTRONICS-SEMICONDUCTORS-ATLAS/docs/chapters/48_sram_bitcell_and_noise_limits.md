# Chapter 48 — SRAM cell state, noise margins and read disturbance

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The classic six-transistor SRAM bitcell contains two cross-coupled inverters and two access devices. Its binary abstraction has two stable logical states under suitable bias conditions, but actual stability depends on the analog inverter transfer curves, supply voltage, mismatch, noise, bitline precharge and read/write conditions. The static noise margin is not simply the digital VIH−VIL gap; the butterfly-curve construction or an equivalent qualified analog extraction is required.

Write ability and read stability compete through device ratios; an idealized bit array cannot demonstrate either property. A digital register test can verify logical read/write semantics, but cannot certify analog bitcell retention or minimum voltage. The Atlas's prior digital memory models deliberately return unknown when concurrent access policy is unspecified.

**Worked investigation:** compare an ideal bitcell under zero analog noise with an explicitly unknown transfer characteristic. Demonstrate that a Boolean state table alone cannot estimate physical SRAM yield. Build an acquisition table for butterfly curves, write margin, Vdd corners, temperature, mismatch samples and soft-error logging; leave all empirical fields empty pending real measurements.

## Implementable contract and falsification

- **Reference equation:** `static noise margin must derive from analog transfer curves`.
- **Dimensional quantities:** V, s, bit error probability; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `prior_memory_models`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.
