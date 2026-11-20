# 12. Traps, illegal opcodes, and failure atomicity

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Traps, illegal opcodes, and failure atomicity. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A reconstructible architecture must define what happens when execution cannot continue according to its contract. AT8 distinguishes malformed ROM encodings (DecodeError), assembly source errors (AssemblyError), and runtime traps (AT8Trap). Examples include reserved register encodings, nonzero reserved HALT operands, unaligned or out-of-ROM branches, invalid PC fetch and a missing required input. An illegal instruction is rejected before execution or trapped without silently skipping bytes. A fall-through beyond the last ROM word is an error, not an implicit HALT.

Failure atomicity prevents a partially completed instruction from corrupting the architectural state. The atomic and microcycle models stage register, memory, flags and I/O effects until their final commit. A trap in the input phase must leave all those externally visible properties unchanged, even if internal microstage counters or pending latches have been touched. This behavior is a software model property. A physical processor requires trap vectors, privileged state, precise exceptions, reset circuitry and interrupts; AT8 does not claim those mechanisms.

## Executable contract and invariants

**Governing statement:** `on trap: S_after = S_before (architectural effects); event=structured trap(code,PC)`.

**Implementation:** `computer_atlas.spec.AT8Trap and computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** machine state, error classes. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

For ROM IN R0,0; HALT with an empty input tape, snapshot state before the instruction, attempt execution, then assert the trap code is input_exhausted and the architectural snapshot is byte-identical.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Not all real hardware failures are architecturally precise; power loss, analog metastability and memory corruption are outside this digital contract.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
