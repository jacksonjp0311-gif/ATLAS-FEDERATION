# Chapter 53 — Structural gate depth and hypothetical timing envelopes

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## From logic to timing, carefully
The logic graph defines a partial ordering among gates. If each NAND gate is assigned a positive delay interval [d_min,d_max], dynamic programming can propagate possible earliest and latest arrival times through an acyclic graph. At a gate, its earliest possible output response is bounded by the first input change plus the minimum assumed delay, while the latest possible response is bounded by the latest predecessor change plus the maximum assumed delay. These are **structural envelopes**, not sensitized timing paths proven under concrete input transitions.

For a homogeneous gate-delay abstraction with zero wiring delay, the longest path of D NAND levels has upper delay D d_max. The registered path must additionally include clock-to-Q, wire, setup/hold and uncertainty. Physical interconnect, loading and gate input slew can invalidate the single-delay assumption; the envelope must be relabeled hypothetical unless measured parameters are supplied.

## Worked case
Construct a one-bit full adder and an eight-bit ripple chain. Record the deterministic structural depth from the NAND graph. Set synthetic d_min=1 ps and d_max=3 ps, and calculate possible arrival envelopes. Repeat with twice the assumed maximum gate delay and observe the linear scaling. This is an exercise in dimensional reasoning, not a fabricated processor frequency estimate.

## Counterexamples
Reconvergent paths and glitches can cause output transitions not represented by a simple longest-path arrival summary. Fan-out changes effective load; uncharacterized wire lengths add propagation and RC delay; metastability violates a simple bounded binary timing model. The original Electronics timing material documents these caveats. An honest report retains both gate-function proof and independent physical timing HOLD gates.

## Equation, implementation, and provenance

- **Key relation:** `t_latest <= depth_max * t_gate,max (zero interconnect assumption)`.
- **Reference algorithm:** `NandCircuit.structural_depth; NandCircuit.gate_delay_bounds`.
- **Units:** NAND levels, seconds, declared min and max gate delays.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
