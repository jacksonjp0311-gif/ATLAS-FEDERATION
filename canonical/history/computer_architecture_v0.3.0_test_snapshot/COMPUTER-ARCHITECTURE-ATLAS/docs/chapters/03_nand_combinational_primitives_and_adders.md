# 03. NAND gates, XOR, full adders, and compositional arithmetic

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

NAND gates, XOR, full adders, and compositional arithmetic. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

NAND is functionally complete: NOT(a)=NAND(a,a), AND(a,b)=NOT(NAND(a,b)), and OR(a,b)=NAND(NOT(a),NOT(b)). Four NAND operations implement XOR with an intermediate t=NAND(a,b). An elementary full adder computes s=a XOR b XOR cin and carry=ab+cin(a XOR b). Applying this bit by bit produces the ripple-carry adder. This decomposition provides a bridge from single-gate Boolean truth tables to machine-level ADDI semantics without assuming an existing software arithmetic instruction. The gate library is independently executable with pure Python bitwise arithmetic. Its finite results can be exhaustively checked against integer addition, but these checks do not establish logic-family voltage levels, fanout limits, propagation delay, gate count after synthesis or a semiconductor layout.

Long carry chains have increasing worst-case delay and expose why a combinational proof is not a timing proof. In physical hardware, the register-to-register path must include input setup time, cell delays, interconnect parasitics, clock uncertainty and receiving hold constraints. The preserved Electronics node contains reference timing equations; manufacturing evidence must supply characterized cell data.

## Executable contract and invariants

**Governing statement:** `s=a XOR b XOR cin; cout=(a AND b) OR (cin AND (a XOR b))`.

**Implementation:** `computer_atlas.gates.nand, full_adder, ripple_add`.

**Relevant dimensions:** bits, logic delay unspecified. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Enumerate all eight full-adder input triples and all 16×16 operand pairs for a 4-bit ripple adder; verify s+2cout=a+b+cin.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Truth-table correctness does not imply a physical clock frequency, hazard freedom, or transistor-level correctness.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
