# Chapter 31: Reconstructing a word ALU from gate-level addition

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Binary operations and two's-complement representation
A word-level ALU is built from Boolean gates, adders and controlled multiplexing. For w-bit nonnegative operands a,b, let mask=2^w−1. A NAND-built ripple-carry adder computes ADD modulo 2^w and reports the final unsigned carry. SUB uses a+(mask XOR b)+1. For subtraction the final carry equal to 1 means **no unsigned borrow**; conflating carry and borrow would corrupt later arithmetic.

Signed two's-complement overflow is not the same as unsigned carry. For ADD, overflow is true when the operand sign bits agree and the result sign differs. For SUB, overflow is true when operand signs disagree and result sign differs from a. Zero and negative flags are derived from the result; other operations explicitly define carry rather than implicitly preserving an undocumented flag.

## Worked investigation
In 4 bits: 7+1 produces result 8 (binary 1000), no unsigned carry, but signed overflow=1 because +8 exceeds the signed range [−8,7]. In contrast 15+1 produces result 0 and carry=1 without signed overflow. For 8−1, result=7 and signed overflow=1 because −8−1 is below representable range.

## Reconstruction boundary
The model accepts widths 1–16, validates exact integers and refuses unsupported operations. It is *combinational semantics*, not a clocked ISA, datapath schedule, gate-count synthesis, physical layout, memory bus, or silicon CPU. A later Computer Architecture node must define control sequencing, instruction decoding and observable machine state. Exhaustive 4-bit and random 8-bit oracles detect implementation mistakes without proving a physically fabricated ALU.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `primitive_alu (uses nand_ripple_add from v0.3)`.
- **Governing relation:** `sum=(a+b+cin) mod 2^w; carry_out=floor((a+b+cin)/2^w); SUB=a+not(b)+1`.
- **Units:** binary words and flags.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
