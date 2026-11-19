# 18. Constructing loops, branching programs, and stateful computations

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Constructing loops, branching programs, and stateful computations. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A useful computer must execute algorithms whose behavior depends on prior state, not only one fixed arithmetic expression. AT8 can implement a bounded countdown with a register, arithmetic decrement modulo 256, an OUT event and a JNZ branch to an earlier ROM address. Another program loads a byte from a scripted input port, modifies it, stores it in RAM and emits it on an output port. These examples provide complete traces of state changes. The data values and output sequence are independently reproducible without external services or machine-learning inference.

A stateful execution model must explicitly define program counter updates on branches, arithmetic wraparound, input exhaustion, RAM visibility and final termination. Bounded runtime execution prevents accidental infinite loops from hanging the test harness. Every exception should be reported as a precise failure, rather than hiding errors behind a successful process exit. These properties help future agent systems use the Atlas to verify generated programs. They do not demonstrate memory safety, a typed language, compilers, operating systems or arbitrary real-world peripherals.

## Executable contract and invariants

**Governing statement:** `R0_(k+1)=(R0_k+255) mod 256; JNZ(R0)->loop if R0 != 0`.

**Implementation:** `computer_atlas.programs.COUNTDOWN; computer_atlas.spec.SpecMachine.run`.

**Relevant dimensions:** instruction counts, state variables. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Assemble LDI R0,3; LOOP: OUT R0,0; ADDI R0,255; JNZ R0,LOOP; HALT. Verify output 3,2,1 and termination after 11 instructions.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Loop-step bounds are a resource control and not a proof of termination for all possible programs.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
