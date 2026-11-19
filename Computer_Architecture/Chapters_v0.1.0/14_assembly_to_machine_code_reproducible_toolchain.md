# 14. Offline programming pipeline from assembly to ROM and execution trace

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Offline programming pipeline from assembly to ROM and execution trace. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

The minimum self-hosting pathway for a stored-program machine requires a way to describe a program, encode it unambiguously, load its binary representation, and observe its execution. AT8 provides a two-pass assembler, canonical disassembler, ROM validator, atomic executor and microcycle executor. The tools depend only on Python's standard library and do not access a model or network. An optional independent oracle uses its own execution logic to compare results and record exact per-program checks. This is a *software toolchain* and should not be called a compiler, runtime environment or fully self-hosted system.

Reproducibility requires preserving source text, assembler version, ROM bytes, input event tapes, execution budget, output tape, final state, and hashes of the program and trace. The byte layout, label rules and branch semantics must be versioned. The offline wheel must include the actual schema/registry resources so a model can discover the same exact source records after installation. Test the installed wheel from outside its build checkout to ensure the implementation does not silently depend on local files.

## Executable contract and invariants

**Governing statement:** `assembly -> two_pass_assemble -> ROM -> validate -> execute -> deterministic trace`.

**Implementation:** `computer_atlas.isa.assemble/disassemble; computer_atlas.spec.SpecMachine; evidence/independent_oracle.py`.

**Relevant dimensions:** UTF-8 text, bytes, execution events. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Compile the arithmetic/memory program and run it on an isolated installation. Expected RAM[0]=12 and output on port 0 equals 15; compare with a third interpreter.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

The host Python interpreter is a dependency of this software validation. The Atlas has not yet bootstrapped that interpreter on reconstructibly fabricated hardware.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
