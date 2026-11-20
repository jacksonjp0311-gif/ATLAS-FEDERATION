# 22. Evidence-gated bridge from mathematical CPU to manufactured electronics

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Evidence-gated bridge from mathematical CPU to manufactured electronics. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

ATLAS FORGE now has Manufacturing and Electronics references capable of expressing missing process evidence. The computer architecture's new continuity challenge compiles and executes an AT8 program, then asks the existing Manufacturing Evidence Gate whether the prerequisites for a physical CPU are documented. The software passes; the gate reports missing substrate/mobility measurements, lithographic overlay, oxide characterization, transistor I–V/C–V curves, gate voltage noise margins and timing, memory retention/ECC tests, and a signed independent hardware execution trace. Supplying placeholder metadata may satisfy syntactic process dependencies but cannot authenticate their truth; the manufacturing model expressly refuses to call such metadata independent certification.

This is the most important separation for the technological-continuity mission: a logically correct instruction set is an ingredient, not a physically reconstructed computer. A credible reconstruction would demonstrate a transistor or discrete gate implementation, power and clock, stored ROM and RAM, controlled measurement, repeatable execution of the golden binary, logged output events and independent review. Every stage needs raw measurements and uncertainty. The Atlas should retain missing evidence as first-class data so future systems know precisely what remains to be built.

## Executable contract and invariants

**Governing statement:** `software_verified AND physical_evidence_missing -> physical_reconstruction_status=HOLD`.

**Implementation:** `evidence/continuity_challenge.py; Manufacturing manufacturing_evidence_gate`.

**Relevant dimensions:** source files, measured SI units pending. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Run the original Electronics accumulator and the new AT8 program: both store 12 and compute 15. Then verify all 12 types of physical evidence remain missing across six stages.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Passing both software simulators does not certify a fabricated chip or computer; recorded metadata alone cannot provide independent hardware evidence.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
