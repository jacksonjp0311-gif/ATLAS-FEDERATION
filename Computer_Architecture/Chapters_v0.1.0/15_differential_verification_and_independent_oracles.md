# 15. Differential testing: atomic model, microcycles, and third oracle

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Differential testing: atomic model, microcycles, and third oracle. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A system can pass its own unit tests and still contain shared mistakes if the tests reuse the same algorithm. AT8 therefore includes two separately structured DUT implementations and an independent byte interpreter in its evidence suite. The architectural model uses direct arithmetic for ADDI and CMP; the microcycle model uses a NAND-only 8-bit ALU; the third oracle decodes bytes independently and uses native arithmetic. The oracle performs exhaustive gate addition and signed-overflow comparisons for all 65,536 operand pairs, random full-program comparisons, assembler/disassembler round trips, explicit branch fixtures and negative input cases.

Independence is a spectrum, not a binary property. The three implementations share the publicly documented ISA and the same runtime Python environment; a specification error could be repeated in all of them. For scientific acceptance we would need external expert review, hardware-vs-software conformance tests, physically characterized RAM and control timing, and external replication with truly independent tooling. Source-history preservation and independent software oracle agreement establish a strong bounded engineering baseline, not independent scientific certification.

## Executable contract and invariants

**Governing statement:** `forall test_program: state_Spec == state_Micro == state_Independent_reference`.

**Implementation:** `evidence/independent_oracle.py; tests/test_microcoded.py`.

**Relevant dimensions:** finite test cases, SHA-256 receipts. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Generate 700 deterministic random programs, execute all three references, compare full state and output, and repeat with different ROM seeds. Exhaust the 8-bit adder input space separately.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

A finite test suite cannot prove universal correctness of arbitrary future instruction extensions, real silicon faults or all program paths.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
