# 04. Four-register file, reset state, and instruction atomicity

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Four-register file, reset state, and instruction atomicity. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A small register file is addressable storage feeding a combinational datapath. AT8 has four architecturally visible registers R0..R3, each exactly 8 bits. On reset all registers and RAM bytes are zero, flags are Z=1,N=C=V=0, PC=0 and I/O tapes begin at their initial positions. An instruction reads its operands from the prior committed state and updates a staged next state. A STORE writes the old source register to RAM only when the instruction commits; MOV reads the specified source register even if its destination is the same register. This is a digital state-transition contract and intentionally not a physical 6T SRAM, flip-flop or clocked netlist.

Instruction atomicity is useful when a fault occurs. If an IN operation has no input on the requested port, the model raises an input-exhaustion trap without partially changing the destination register, flags, I/O cursor or RAM. The microcycle model also defers register and memory changes until COMMIT. This demonstrates rollback semantics in software; whether a physical design can guarantee the same observation in the presence of power failure or asynchronous signals requires separate study.

## Executable contract and invariants

**Governing statement:** `architectural_state_after = commit(architectural_state_before, decoded_operation)`.

**Implementation:** `computer_atlas.spec.SpecMachine.snapshot; computer_atlas.microcoded.MicrocodedMachine.tick`.

**Relevant dimensions:** bits, bytes, abstract instruction cycles. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Reset R0..R3, verify all zeros, execute LDI R0,77; STORE R0,200; LOAD R2,200; check RAM[200]=77 and R2=77.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Do not compare a partially executed microstage with an architectural instruction boundary; only COMMIT is an externally visible instruction state.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
