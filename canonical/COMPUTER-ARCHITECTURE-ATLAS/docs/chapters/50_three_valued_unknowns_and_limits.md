# Chapter 50 — Unknown-state propagation without invented register certainty

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Scientific question
What should a digital reconstruction report when a signal has not been shown to carry a valid binary voltage? Returning zero by default would silently hide uncertainty. A stronger reference uses the three-value set {0,1,X}, where X means a bit cannot be determined under the available logical information.

## Conservative logic
NAND has one useful forcing input: if either input is definitely zero, the output is definitely one, even if the other input is unknown. With both inputs definitely one, the output is zero; otherwise return X. This is a partial-information interpretation of Boolean NAND, not a probabilistic model of a transistor. It does not calculate whether a metastable latch resolves at a particular time. A known Boolean reconvergence can remain X in this simple calculus because it does not use relational constraints between unknown signals.

## Worked case
For a=0 and b=X, NAND is definitely 1. For a=1 and b=X, NAND is X. For a=b=1, it is 0. Feed these into an explicit one-bit full-adder netlist; the unknown can propagate through the carry path while specific outputs may remain determined when a forcing constant exists. Test all nine combinations of the three-valued inputs and require the interpreter to reject True/False booleans, strings and floating-point approximations as invalid logical encodings.

## Limits
A three-valued simulation does not guarantee physical safety. Hazards, simultaneous switching, metastability, analog thresholds, glitches, unknown-resolution times, static noise margin, race conditions, crosstalk and clock skew require different models and calibrated observations. For real devices, the Electronics node's voltage-noise windows and timing chapters are prerequisites. An X value is an epistemic indicator, not a new physical particle or discovery.

## Equation, implementation, and provenance

- **Key relation:** `NAND(0,X)=1; NAND(1,X)=X; NAND(X,X)=X`.
- **Reference algorithm:** `v04_gatelevel.nand3; NandCircuit.eval`.
- **Units:** 0, 1 and X (UNKNOWN, symbolic).
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
