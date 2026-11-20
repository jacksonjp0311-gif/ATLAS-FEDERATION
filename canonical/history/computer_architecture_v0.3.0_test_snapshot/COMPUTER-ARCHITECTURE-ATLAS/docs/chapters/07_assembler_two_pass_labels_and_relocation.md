# 07. An auditable two-pass assembler with labels and diagnostics

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

An auditable two-pass assembler with labels and diagnostics. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Assembly language is a human-friendly notation for machine code. The AT8 assembler first scans labels and assigns addresses at two bytes per instruction, then resolves operand symbols and encodes bytes. This separation avoids accidental dependency on declaration order and permits forward branch references. Labels have a restricted ASCII identifier grammar and are case-insensitive. Numeric operands may be decimal, hexadecimal (0x) or binary (0b), but they must be unsigned bytes; negative numbers and floats are not silently truncated. A branch to a non-existent label, odd target address, duplicate label, reserved opcode, invalid register or ROM image exceeding 256 bytes is rejected with an explicit error.

The disassembler produces canonical numeric-target assembly. Assembling its result must reproduce the original bytes exactly for every valid image. That round-trip is an information-preservation invariant: it proves the tooling does not discard reserved fields or alter the binary representation. It does not prove the original program terminates or that its output is correct. Reconstructible computer systems should keep original assembly sources, exact binary hashes and semantic regression vectors together.

## Executable contract and invariants

**Governing statement:** `assemble(disassemble(valid_ROM)) == valid_ROM`.

**Implementation:** `computer_atlas.isa.assemble and computer_atlas.isa.disassemble`.

**Relevant dimensions:** UTF-8 assembly, ROM bytes. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Assemble START: LDI R0,3; LOOP: OUT R0,0; ADDI R0,255; JNZ R0,LOOP; HALT. The loop target is byte address 2 and its output is 3,2,1.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

An assembler is not a optimizing compiler, linker or operating-system bootloader. AT8 supports neither object files nor relocatable binaries beyond its two-pass fixed-image labels.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
