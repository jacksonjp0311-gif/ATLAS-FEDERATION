# 10. Program counter, conditional branches, and bounded termination

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Program counter, conditional branches, and bounded termination. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A stored-program machine's computation is determined not only by its arithmetic but also by its sequence of instruction addresses. The AT8 PC begins at zero and normally increases by two. JMP substitutes an absolute aligned ROM address. JNZ and JZ test one specified register for nonzero or zero respectively; they do *not* examine the ALU zero flag, even if a preceding CMP set that flag. This is a deliberate architectural choice that must be stated to avoid a misleading program interpretation. The assembler rejects out-of-range targets and unaligned addresses; the runtime separately checks that a fetched PC is valid.

Program termination is not decidable for arbitrary unbounded general-purpose programs, but this tiny model can always enforce a finite step budget. `run(max_steps)` either halts at HALT or returns an explicit bounded-budget status. It never silently declares an infinite loop successful. A looping program such as JMP 0 is syntactically valid and will repeatedly execute until the chosen bound is reached. A program that falls off the end without HALT raises a program-counter trap. This separation between ROM syntax, execution safety, and eventual termination is important for offline reconstruction and agent-driven experimentation.

## Executable contract and invariants

**Governing statement:** `PC_next = branch_condition ? target : PC+2; bounded run stops at max_steps`.

**Implementation:** `computer_atlas.spec.SpecMachine.step; computer_atlas.isa.assemble`.

**Relevant dimensions:** byte addresses, step counts. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

The countdown code initializes R0=3, emits R0, decrements by ADDI 255, and JNZs to the output instruction until R0=0. Expected output: (0,3),(0,2),(0,1).

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Loop-bound completion is a resource limit, not a mathematical proof that the program would eventually halt.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
