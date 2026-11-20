# Chapter 52 — From transistors to a reconstructible stored-program machine

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The technological-continuity chain should end at an independently testable demonstration, not a claim of a fabricated processor. A software reference can connect word-level arithmetic, registers, state transitions and memory semantics: a finite 8-bit accumulator machine supports loading an immediate value, addition modulo 256, XOR, storing/loading from a 16-byte memory, conditional branches and explicit halting.

The instruction stream encodes each instruction as two bytes. A *step* is an ideal abstract state transition; it does not represent clock gates, transistor layout, power delivery, ROM fabrication, silicon validation, interrupts or a compiler toolchain. Program counter validity, alignment, bounded execution and unsupported opcodes are part of the contract. Arithmetic wraps modulo 256 by definition, while more extensive system architecture belongs in the next Computer Architecture node.

**Worked investigation:** execute LDI 5; ADD 7; STORE 0; XOR 3; HALT. The machine stores 12 in RAM[0] and halts with accumulator 15. Independently exhaust all 256×256 operand pairs with a separate integer arithmetic oracle, and test invalid opcodes and loop limits. This is evidence of finite software semantics; implementing the same state machine in CMOS remains an unfinished physical challenge.

The next milestone is to preserve a full computer-architecture stack—ISA specification, gates-to-register RTL semantics, deterministic boot ROM, assembler, instruction decoding, memory buses, interrupts and transparent end-to-end programs—while retaining all semiconductor parameter calibration gaps. Do not move Bitwork routing forward until all planned domain content libraries are addressed.

## Implementable contract and falsification

- **Reference equation:** `state_next=decode(opcode,operand,state); acc_add=(a+b) mod 256`.
- **Dimensional quantities:** bits, bytes, cycles; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `EightBitAccumulator`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.
