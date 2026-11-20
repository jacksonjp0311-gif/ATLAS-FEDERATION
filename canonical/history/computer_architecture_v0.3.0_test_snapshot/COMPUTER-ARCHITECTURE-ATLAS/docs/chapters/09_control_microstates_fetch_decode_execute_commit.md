# 09. Fetch, decode, execute, commit: a finite control unit

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Fetch, decode, execute, commit: a finite control unit. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

An instruction-level architecture describes what an instruction does but not which internal operations happen first. The AT8 microcycle machine decomposes each instruction into four symbolic phases: FETCH loads the two ROM bytes into a latch; DECODE interprets opcode/register fields; EXECUTE forms pending register, flag, memory and branch effects; COMMIT makes those effects architecturally visible together. The reference treats every phase as one software tick and every instruction as four ticks, without claiming a physical clock frequency. An actual control state machine would need gate-level timing, reset synchronization, clock distribution, setup/hold margins and careful fault behavior.

The atomic reference executes one instruction in a single logical step and is intentionally different code. For every committed instruction, the microcycle machine's registers, RAM, PC, flags, input cursor and output tape must match the atomic machine. Before COMMIT, the architectural snapshot is unchanged. When the input tape is exhausted at EXECUTE, the partial microcycle state may remain internally latched but the externally visible architecture is unchanged. These are model-level atomicity properties, not claims of hardware transactional rollback.

## Executable contract and invariants

**Governing statement:** `microstate sequence FETCH -> DECODE -> EXECUTE -> COMMIT -> FETCH`.

**Implementation:** `computer_atlas.microcoded.MicrocodedMachine.tick and step_instruction`.

**Relevant dimensions:** symbolic phases, instruction steps. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

The LDI R0,5 instruction takes four microsteps. Assert R0 remains zero during FETCH/DECODE/EXECUTE and becomes five after COMMIT. Compare all outputs with the atomic reference.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Four symbolic software microticks do not imply four real CPU cycles, and no electrical timing is measured by this model.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
