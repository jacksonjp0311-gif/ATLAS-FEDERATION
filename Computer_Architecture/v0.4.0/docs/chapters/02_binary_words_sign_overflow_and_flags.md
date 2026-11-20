# 02. Binary words, two’s complement, carry, and signed overflow

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Binary words, two’s complement, carry, and signed overflow. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

For an n-bit unsigned word, the mathematical state space is the ring of residues modulo 2^n. A stored 8-bit value ranges from 0 to 255, with arithmetic wraparound. Signed two’s complement reinterprets bit 7 as weight −128 and retains the same stored 8 bits. Signed and unsigned meanings differ; there is no separate physical storage representation. For 8-bit ADDI, form integer t=a+b, store t mod 256, carry=1 iff t>255. Signed overflow holds if the two operands have equal sign and the result has a different sign. Zero and negative flags follow from the result. For CMP, compute a−b modulo 256, use carry=1 to mean no unsigned borrow (a>=b), and calculate signed subtraction overflow from differing input sign bits. CMP updates flags but not a register. In AT8, conditional branches test the selected register, *not* the flags; failing to state this would make the instruction-set specification ambiguous.

A reconstruction needs a table of arithmetic cases, not only a formula. Test 255+1→0 with carry, 127+1→128 with signed overflow, 0−1→255 without unsigned carry, and equal operands yielding zero. The numerical oracle exhaustively covers all 65,536 8-bit operand pairs for the NAND adder, including carry and signed overflow.

## Executable contract and invariants

**Governing statement:** `ADD8(a,b)= (a+b) mod 256; C=[a+b>=256]; V=signs_equal(a,b) AND signs_differ(a,result)`.

**Implementation:** `computer_atlas.gates.alu8 and computer_atlas.spec.SpecMachine`.

**Relevant dimensions:** 8-bit words, Boolean flags. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

For 127 + 1, result is 128, carry 0, signed overflow 1; for 255 + 1, result is zero, carry 1, signed overflow 0.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

A zero flag, negative flag, unsigned carry and signed overflow are distinct properties. Omitting any of them loses information needed for software and verification.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
