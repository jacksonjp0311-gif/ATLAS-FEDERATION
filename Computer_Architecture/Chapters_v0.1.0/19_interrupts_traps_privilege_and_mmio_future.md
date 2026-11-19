# 19. Interrupts, privilege, timers, and memory-mapped I/O: missing architecture

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Interrupts, privilege, timers, and memory-mapped I/O: missing architecture. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

AT8 intentionally has no asynchronous interrupts, privileged mode, exception vector table, virtual memory, timer register or memory-mapped I/O. Its four abstract ports are deterministic event tapes, not physical bus-mapped devices. This limitation matters because a system can execute simple assembly successfully yet fail to coordinate external equipment, recover from hardware faults, protect memory or support an operating system. A more complete architecture would need a documented reset/trap vector, saved PC and cause registers, interrupt arbitration and masks, deterministic memory/IO ordering, privilege separation and device register interfaces. It would also need test vectors for nested interrupts, timing races and invalid memory access.

The present edition explicitly reserves all ISA opcode encodings for its own 16 operations and does not silently assign future privileged functions. Any extended ISA must receive a new version and migration/conformance tests rather than reinterpret old ROM bytes. The future Computer Architecture release can add these mechanisms only after preserving the current contract and verifying interoperability. AT8 v0.1 is a research kernel, not an OS-capable processor.

## Executable contract and invariants

**Governing statement:** `interrupt_pending -> trap_entry(PC, flags, cause) [NOT IMPLEMENTED IN AT8/0.1]`.

**Implementation:** `Future ISA extension contract; no executable interrupt model in v0.1`.

**Relevant dimensions:** bytes, interrupt vectors, time (future). Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Test that unsupported opcode spelling such as INT is refused by the assembler rather than accepted with undocumented semantics.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

The absence of privilege/interrupts prevents OS, safety, device driver and real-time guarantees. No secure or industrial controller claims.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
