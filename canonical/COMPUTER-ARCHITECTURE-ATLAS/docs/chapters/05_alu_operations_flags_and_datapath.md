# 05. ALU functions and the register-to-register datapath

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

ALU functions and the register-to-register datapath. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

The arithmetic logic unit (ALU) takes finite byte operands and a selected operation. AT8 supports addition with immediate, XOR, AND, OR and subtraction-like comparison; it also exposes LDI, LOAD and MOV as data movement. Datapath control must select source registers, immediate operand, function, destination register and flag updates. A physically implemented datapath would connect multiplexers, an ALU, register file, memory and program counter. The software reference deliberately describes these choices without pretending the machine has a verified silicon area or switching power.

Flags form part of the instruction-visible state, and each instruction specifies whether they change. Arithmetic or byte-producing operations update zero and negative, with carry and overflow set only where they have defined arithmetic meaning. STORE, branches, OUT and HALT preserve the existing flags. CMP affects flags but leaves the input register unchanged. This explicitness prevents a programmer from relying on accidental host-language behavior. The separate microcoded implementation computes the ADDI arithmetic using NAND-based gate functions, while the atomic specification uses native integer arithmetic; agreement across many cases is stronger than testing the same code twice.

## Executable contract and invariants

**Governing statement:** `ALUout = f(register_byte, immediate_byte); flags_next=flag_function(ALUout, operands)`.

**Implementation:** `computer_atlas.gates.alu8; computer_atlas.spec.SpecMachine; computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** 8-bit words, 4 Boolean flags. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Execute LDI R0,127 then ADDI R0,1; verify R0=128, N=1, V=1 and C=0. Compare microcoded and atomic snapshots.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

ALU throughput, power and gate count depend on physical implementation; no PPA (power, performance, area) claim is certified here.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
