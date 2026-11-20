# 17. From CMOS gates to a full adder and n-bit ripple-carry arithmetic

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

From CMOS gates to a full adder and n-bit ripple-carry arithmetic. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`s=a XOR b XOR c_in; c_out=(a AND b) OR ((a XOR b) AND c_in)`

**Units:** bits, dimensionless Boolean values. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

Boolean arithmetic can be assembled from logic primitives (NAND is functionally complete). A full adder has three binary inputs a, b, carry_in and two outputs sum and carry_out. For all eight input triples the integer identity a+b+c_in=s+2c_out must hold. A ripple-carry adder propagates carry from bit i to bit i+1. Induction on the bit position proves that after processing i bits, accumulated lower output bits and carry encode the lower-i-bit sum exactly. The final result obeys a+b+c_in = sum + 2^width×carry_out.

This constructs an unambiguous *symbolic* arithmetic layer. It does not require transistors to execute the Python reference; its role is to preserve a bridge from transistor-level truth tables to the logical structure of arithmetic hardware. A physical carry chain has finite switching delays, fan-out limits and potential hazards that must be measured separately.

## Independently executable algorithm

Implement `full_adder` from XOR/AND/OR and `ripple_adder_unsigned` from repeated full-adders without Python arithmetic for the result construction. Test all eight full-adder truth cases and exhaust all 3-bit input pairs and carries. Then randomly compare 1–64-bit outputs with Python integer addition, including overflow. Reject out-of-range operands; do not silently reinterpret them as signed two’s-complement values.

## Worked scientific investigation

Use width=4 and add 1101₂ (13) + 0110₂ (6). Bitwise carry produces output 0011₂ (3) and carry_out=1, reconstructing 19 = 3 + 16. Then add the largest 64-bit unsigned word plus 1: the output word is zero and carry_out=1. Neither example demonstrates an actual CMOS chip.

## Failure conditions and counterexamples

This establishes functional Boolean correctness, not a timed latch, register file, clock system, memory, processor ISA or manufactured circuit. Real propagation delay may grow with carry length; a ripple adder is a simple reference, not an optimized architecture.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.
