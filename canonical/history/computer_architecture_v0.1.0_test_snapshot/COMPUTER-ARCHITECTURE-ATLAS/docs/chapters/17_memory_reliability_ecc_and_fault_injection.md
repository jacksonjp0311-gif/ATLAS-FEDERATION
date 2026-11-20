# 17. Memory reliability: parity, SECDED, retention and fault detection

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Memory reliability: parity, SECDED, retention and fault detection. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Digital memory semantics are not physical memory reliability. The inherited Electronics node models a finite Hamming SECDED code, abstract SRAM/DRAM behavior, retention limits and read/write collision conventions. AT8's 256 RAM bytes are perfectly retained in the Python model, and ROM is immutable; this is a simplifying assumption, not a demonstrated memory cell design. A real memory would have finite read access times, energy costs, soft-error rates, partial writes, timing constraints and fault propagation. Error-correcting codes can detect or correct a stated subset of corruptions but do not guarantee correctness against arbitrary burst faults, controller failures or malicious modifications.

For reconstruction, define the memory word/byte layout, read and write ordering, reset behavior, sample ECC codewords and an independent oracle, then introduce fault injection. Test that a bit flip is detected or corrected where guaranteed, and that two-bit errors are rejected by the SECDED model. At the architecture level, choose whether ECC correction is transparent to software or triggers a visible trap; AT8 v0.1 does not encode a physical ECC controller. The manufacturing evidence gate requires actual retention and ECC measurements before claiming working memory.

## Executable contract and invariants

**Governing statement:** `RAM_next[a] = STORE ? R[r] : RAM_old[a]; ECC_correctable_errors <= defined bound`.

**Implementation:** `Electronics v0.3 Hamming SECDED and computer_atlas.spec.SpecMachine`.

**Relevant dimensions:** bits, bytes, BER and time (unmeasured). Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Store a byte at RAM address 200 and compare round-trip LOAD. Separately inject single/double errors into a Hamming(8,4) reference code and retain explicit failure records.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Neither software RAM nor an ECC truth table establishes SRAM noise margins, DRAM refresh requirements or radiation reliability in fabricated memory.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
