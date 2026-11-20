# 06. AT8 encoding: fixed 2-byte instructions and strict decoder

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

AT8 encoding: fixed 2-byte instructions and strict decoder. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

An instruction encoding is a byte-level contract, independent of how a processor might fetch the instruction. AT8 encodes every operation as exactly two bytes. The first byte uses its upper four bits for one of 16 operation codes and the lower nibble for a register index when the operation accepts a register. Only low-nibble values 0..3 are valid register indices, leaving other encodings reserved. NOP, JMP and HALT require the low nibble to be zero. The second byte is an unsigned 8-bit immediate, absolute branch target, memory address, source register for MOV, or port index depending on opcode. NOP and HALT require the second byte to be zero; MOV and I/O operands are bounded to indices 0..3. Branches require 2-byte-aligned absolute byte addresses.

Reserved encodings are rejected, not interpreted as future extensions or wrapped into legal values. The decoder should refuse any byte sequence of odd length, more than 256 program bytes or an invalid branch destination. These constraints establish a small, auditable image format. However, valid syntax and a present HALT instruction do not prove termination: a program may jump forever before reaching HALT. The assembler and runtime both enforce appropriate bounds.

## Executable contract and invariants

**Governing statement:** `word0 = (opcode << 4) OR reg4; word1 = unsigned_operand8; PC_next = PC+2 unless branch`.

**Implementation:** `computer_atlas.isa.encode, decode, validate_rom`.

**Relevant dimensions:** bytes, bit fields, PC byte addresses. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

For LDI R0,5, the exact bytes are 0x10 0x05. For HALT they are 0xF0 0x00. The illegal byte sequence 0xF0 0x01 must fail validation.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

An encoding table alone does not supply a PCB, boot ROM programmer, bus electrical standard or instruction-timing design.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
