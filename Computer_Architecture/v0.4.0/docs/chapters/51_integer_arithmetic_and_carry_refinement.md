# Chapter 51 — NAND arithmetic, unsigned carry, and subtraction borrow conventions

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Arithmetic contracts
For a w-bit datapath the result is an unsigned integer in [0,2^w−1], with a carry-out bit encoding the high bit of the sum. The identity a+b+c_in=sum+2^w carry_out holds for every bounded input. Subtraction is implemented by complementing each bit of b and injecting carry_in=1, giving a+(2^w−1−b)+1. The final carry after subtraction is one exactly when unsigned a≥b: it represents **no borrow**, not borrow.

The first integer-width extension uses the same NAND network, not Python arithmetic inside the circuit interpreter. A separate independent oracle calculates ordinary integers and compares them, including edge values and wraps. The netlist has 9w gates for addition, and 10w for subtraction when each b bit is inverted via NAND(b,b).

## Worked cases
For w=8, a=255,b=1, addition yields result 0, carry 1. For a=0,b=1, subtraction yields result 255, carry 0. For a=b=127, subtraction yields zero and carry 1. All 65,536 pairs of 8-bit operands can be tested against an independent integer oracle for addition and again for subtraction. This finite exhaustive check is stronger than a collection of hand-selected examples, but it remains limited to the eight-bit abstract function.

## Signed arithmetic and handoff
Two's-complement overflow is different from carry; e.g. 127+1 overflows signed 8-bit range without an unsigned carry. AT8 flags must maintain the existing published semantics for ADDI and CMP. The Computer Architecture v0.1 ISA must not be extended or silently reinterpreted as RISC-V or the MIT Beta ISA. A hardware implementation would also require gate fan-out, timing, reset and interconnect constraints absent here.

## Equation, implementation, and provenance

- **Key relation:** `a+b+c_in = sum + (2^w) carry_out; a-b=a+(NOT b)+1 (mod 2^w)`.
- **Reference algorithm:** `v04_gatelevel.evaluate_add; computer_atlas.gates.alu8`.
- **Units:** binary words, carry and signed overflow flags.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
