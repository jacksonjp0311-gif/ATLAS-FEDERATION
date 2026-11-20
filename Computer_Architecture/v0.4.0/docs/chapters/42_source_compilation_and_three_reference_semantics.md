# 42. Compiler-to-ISA verification by three independently motivated semantics

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`compile(source)=ROM; evaluator(source,input)=SpecMachine(ROM,input)=MicrocodedMachine(ROM,input)`

**Units and representation:** AT8 bytes, bounded operation counts, deterministic I/O traces. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The compiler in ATLAS FORGE v0.2 takes a deliberately small structured language: SET/ADD/XOR/AND/OR, STORE/LOAD, IN/OUT, bounded nested REPEAT/END and one terminal HALT. It compiles to the unchanged 16-opcode, two-byte AT8 ISA. Register R0 holds the public accumulator, while registers R3..R1 are reserved for up to three loop counters; the compiler must not silently allocate beyond those registers. A separate source AST evaluator executes statements independently of machine-code decoding. The AT8 atomic specification and four-stage microcycle reference form two additional execution paths.

The engineering invariant is **agreement of observable states**, not merely the same final console number: check HALT status, R0, all 256 RAM bytes, output events in order and input-tape consumption counts. The microcycle model must agree with the atomic model at every instruction retirement. A deterministic receipt records source/ROM/image hashes, input-tape hash, program limits, result digest and the explicit lack of physical hardware evidence. An agreed-upon error in all models can still exist; external source review and independent implementations improve but do not eliminate this risk.

## Reproduce this investigation offline

Compile `SET 5; ADD 7; STORE 0; XOR 3; OUT 0; HALT`. The software models should store 12 in RAM[0], output 15 on port 0 and halt. Compare the AST evaluator's 256-byte memory with the machine's full memory, and confirm the output event list is exactly [(0,15)]. Repeat with IN port 1 receiving [7] and output 9 after adding 2. Refuse missing tape input, unbounded operation budget and unsupported syntax.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `verify_program, evaluate_source, differential_retirement`.

## Counterexamples, failure modes, and model scope

This verified compiler is not a C compiler, linker, operating system, protected memory runtime, or fabricated processor. A content digest proves neither source authorship nor correct physical realization. The original Compiler Design and Operating Systems domains remain separately planned in the 30-domain program; do not inflate this Computer Architecture increment into their completion.

## Source register and rights

Bibliographic record `NAND2TETRIS-PROJECTS` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
