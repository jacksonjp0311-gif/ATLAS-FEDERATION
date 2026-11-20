# 11. Input/output ports as deterministic recorded event tapes

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Input/output ports as deterministic recorded event tapes. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

External input is a major source of nondeterminism and unreproducible experiments. Rather than invoking devices or network services, AT8 represents each of its four input ports by an explicitly supplied sequence of byte values. An IN instruction reads the next available value on the selected port, then advances an input cursor *only when the instruction commits*. If no value is available it raises an input-exhaustion trap without modifying architectural state. OUT appends a pair (port,byte) to an output event tape and does not communicate with actual hardware. The output tape can be included in a signed-by-hash software test receipt, along with the ROM and input tapes.

This gives a reproducible software interface suitable for scientific verification: the same ROM and input sequences produce the same output and final state under the specified model. It does not establish electrical bus behavior, input synchronizers, output drivers, memory-mapped device timing, interrupt hazards or cybersecurity properties. Real device communication must be designed and characterized separately. The manufacturing evidence gate retains all physical I/O validation as outstanding.

## Executable contract and invariants

**Governing statement:** `IN: R[r]=tape[port][cursor]; cursor++ on COMMIT; OUT: tape_out.append((port,R[r]))`.

**Implementation:** `computer_atlas.spec.SpecMachine and computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** byte ports, event order. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Supply input port 1=[7], execute IN R1,1; ADDI R1,2; STORE R1,4; LOAD R3,4; OUT R3,2; HALT, and verify one byte (2,9) is output.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

If the input tape is exhausted, do not return a default zero or consume an input event before a failed instruction commits.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
