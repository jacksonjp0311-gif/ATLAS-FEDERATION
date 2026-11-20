# Chapter 52 — Verifying gate arithmetic at each AT8 instruction retirement

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Refinement obligation
A computer can be modeled at several abstraction levels. The ISA specification defines architectural state transitions, a microcycle engine stages their implementation, and a Boolean datapath implements arithmetic expressions. A meaningful consistency check compares the externally visible committed state after each instruction, not just a final program output. A precise trap must leave the previous committed state unchanged.

The original AT8 exposes ADDI and CMP. At each such retirement, sample the pre-instruction register and immediate operand. The new NAND-only datapath calculates addition or complement-plus-one subtraction. Compare its result and carry with the existing atomic ISA state after the instruction. Then compare atomic and microcycle snapshots using the predecessor edition's differential retirement verifier. Do not modify original interpretation of reserved registers, flags or program-counter alignment.

## Worked execution
`LDI R0,255; ADDI R0,1; CMP R0,0; HALT` includes wraparound and comparison. The NAND adder must produce result zero with carry one on ADDI, and the comparator must not modify R0. A second program compiled from `SET 5; ADD 7; STORE 0; XOR 3; OUT 0; HALT` is verified from source AST to ROM, boot payload, atomic/microcycle execution and NAND arithmetic. Its output event is port 0, byte 15.

## Safety and scope
If either implementation traps, fails to halt within a bounded budget, or disagrees, return HOLD. Do not manufacture a successful refinement receipt after a failure. Testing finite programs does not prove all future programs are correct, and correctness of the simulated datapath does not demonstrate any CMOS implementation. Real silicon equivalence additionally needs gate-level RTL/netlist extraction, characterized timing, reset behavior, scan or formal validation and measured I/O.

## Equation, implementation, and provenance

- **Key relation:** `Refinement: GateResult(operand,immediate) = ISAResult(operand,immediate)`.
- **Reference algorithm:** `v04_gatelevel.certify_at8_arithmetic; v02_trace.differential_retirement`.
- **Units:** byte values and instruction retirement indexes.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
