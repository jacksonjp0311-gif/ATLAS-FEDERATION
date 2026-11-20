# 41. Instruction reachability, structural termination, and proof conservatism

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`CFG successors: JMP -> target; JZ/JNZ -> target and fallthrough; HALT -> none`

**Units and representation:** byte-addressed program counters and instruction counts. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

AT8 branches use absolute even ROM byte addresses. The abstract control-flow graph has one node for each decoded two-byte instruction; edges represent every *possible* successor under a conservative interpretation of conditional branches. A JMP has one target, JZ and JNZ have both target and fallthrough, HALT has none, and other instructions use PC+2. An edge that falls beyond ROM is a potential invalid termination, not an implicit HALT. The graph deliberately ignores register values and branches that could be logically infeasible in a particular run.

A reachable directed cycle makes this analysis unable to establish universal termination. It does not prove an infinite execution exists—such loops may be bounded by counter state, as the earlier structured compiler demonstrates. Conversely, an acyclic reachable graph whose every terminal node is HALT gives a bound on normal instruction retirements *provided no execution trap occurs*. This is weaker than a guarantee of successful completion with I/O, because an IN instruction can still trap on an exhausted input tape. Compute the maximum normal path length only for such finite acyclic all-HALT graphs. Unreachable instructions are reported, not deleted.

## Reproduce this investigation offline

For `LDI R0,2; LOOP: ADDI R0,255; JNZ R0, LOOP; HALT`, the graph contains a cycle and must report `cannot_prove_termination`, although actual execution halts after the counter reaches zero. For `LDI; ADDI; OUT; HALT`, it is acyclic with a four-instruction normal bound. A lone NOP has a fallthrough beyond ROM and no HALT, so refuse a normal-termination certificate. Explicitly distinguish reachable PCs from structural dead code after a HALT.

**Executable implementation:** `computer_atlas/v03_control.py`. Public functions: `control_flow_certificate`.

## Counterexamples, failure modes, and model scope

This is conservative static analysis, not SAT/SMT model checking, path sensitization, state-exhaustive proof, or real-time timing qualification. It does not prove absence of all traps, malicious firmware, unbounded physical response time, or liveness of external devices. Keep detailed counterexamples rather than claiming loop-free programs are generally safe.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
