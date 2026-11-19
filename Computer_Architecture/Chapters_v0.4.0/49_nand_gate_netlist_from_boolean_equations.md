# Chapter 49 — A reconstructible NAND netlist from the Boolean adder

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Reconstruction question
Can the Boolean ALU function be expressed as an explicit, finite, independently replayable gate network, rather than only Python integer arithmetic? A reproducible gate netlist requires a precise cell primitive, a unique signal name for every output, acyclic dependencies, and a fixed set of primary inputs/outputs.

## Derivation and construction
NAND(a,b)=NOT(a AND b) forms a functionally complete basis. Define n0=NAND(a,b), n1=NAND(a,n0), n2=NAND(b,n0), and x=NAND(n1,n2), so x=a XOR b. Set n3=NAND(x,carry), n4=NAND(x,n3), n5=NAND(carry,n3), sum=NAND(n4,n5), and next_carry=NAND(n0,n3). The nine-gate full-adder outputs satisfy sum+2 next_carry=a+b+carry for every input triple. Chain w such stages, passing the carry to the next lower-to-higher bit position, to implement unsigned addition modulo 2^w with an explicit carry-out.

The original AT8 v0.1 instruction format is left completely unchanged. The gate network supplies one possible implementation of the arithmetic function, not a new instruction-set architecture or a verified transistor layout.

## Reconstructible case
Build an 8-bit ripple netlist with 72 NAND instances. Apply a=255, b=1, c_in=0; the result is 0 with carry 1. Record the canonical sorted-key JSON netlist and SHA-256. A second process regenerates the same graph and digest. Exhaust the 65,536 possible pairs of 8-bit values and independently compare output against Python's native integer arithmetic; this shows finite functional equivalence under the stated Boolean semantics.

## Failure and fabrication boundaries
A correct netlist is not synthesizable physical RTL without clocking and cell mapping constraints. NAND count is not transistor count, die area, critical-path delay, or power consumption. No minimum voltage, fan-out capacity, source current, analog transition shape, process corner or timing library has been characterized. The graph parser rejects unknown wires, duplicate names, feedback introduced as a forward reference, nonbinary inputs and unsupported sizes. This rejection is part of the knowledge to preserve.

## Equation, implementation, and provenance

- **Key relation:** `s=a XOR b XOR c; cout=(ab) OR (c(a XOR b))`.
- **Reference algorithm:** `v04_gatelevel.ripple_adder_netlist; NandCircuit.eval`.
- **Units:** bits, NAND counts and structural gate levels.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
