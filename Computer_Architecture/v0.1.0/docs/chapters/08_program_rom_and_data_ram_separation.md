# 08. Program ROM, data RAM, and the memory address map

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Program ROM, data RAM, and the memory address map. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

AT8 uses separate immutable program ROM and mutable data RAM. ROM is 2..256 bytes with fixed two-byte instruction alignment; RAM has 256 independent byte locations addressed 0..255. This is a deliberately simple Harvard-style division, though real embedded systems may map memory-mapped devices into an address space, execute from RAM, implement caches, or unify instruction/data storage. In AT8, STORE cannot modify ROM: it writes only RAM. The PC is a byte address into ROM, not a RAM index and not an instruction count. Branch destinations are absolute even byte addresses.

Memory read/write contracts need a collision policy when physical ports can read and write the same location at once. AT8's sequential single-instruction model avoids simultaneous asynchronous accesses at the architectural level, but the preserved Electronics node independently records read-first/write-first/undefined physical memory semantics. The software machine guarantees logical LOAD/STORE behavior only, not SRAM retention time, bitline delay, refresh, ECC strength or physical memory manufacture.

## Executable contract and invariants

**Governing statement:** `ROM read: instruction=ROM[PC:PC+2]; RAM store: RAM[address]=register; PC byte aligned`.

**Implementation:** `computer_atlas.spec.SpecMachine, computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** ROM/RAM bytes, PC addresses. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Execute STORE R1,200 followed by LOAD R2,200 and verify R2 has the stored byte; verify that ROM bytes and the program checksum do not change.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

ROM/RAM separation alone does not prevent malicious programs from producing harmful behavior or all control-flow errors; the software is an educational bounded model.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
