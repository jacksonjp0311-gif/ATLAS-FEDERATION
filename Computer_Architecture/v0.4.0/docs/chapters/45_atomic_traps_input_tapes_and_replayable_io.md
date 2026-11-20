# 45. Instruction atomicity, input tapes, traps and replayable I/O

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`valid instruction -> one committed state transition; trap -> no committed change`

**Units and representation:** instruction retirements, input bytes, output events. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

An instruction-level abstract machine should distinguish a valid execution step from a trap before architectural changes are committed. The existing AT8 model stages register, memory, I/O and program counter changes. If an IN instruction encounters an empty tape, the step traps without consuming input or modifying registers. If a conditional branch targets an invalid address, the fetch/decode contract rejects it. The four-stage microcycle model is compared with the atomic model at instruction retirement boundaries rather than claiming a physical clock rate.

The v0.3 job receipt includes the full observable input consumption, output event order and memory digest. Different input tapes may produce different legitimate outputs; a reproducible evaluation must preserve the exact tape bytes, port indices, and declared execution budget. A watchdog step budget bounds the simulator's work and should return an explicit bounded-stop result or refusal, not claim that an arbitrary source program terminated normally. The machine's `cycles` represent retired abstract instructions. A four-stage `microticks` count does not encode transistor path delay.

## Reproduce this investigation offline

For `IN R0, 1; ADDI R0, 2; OUT R0, 2; HALT`, a tape [7] on input port 1 yields [(2,9)] and advances cursor 1 by exactly one. With an empty tape, input exhaustion is a trap; compare pre- and post-state for equality. Audit the staged microcycle COMMIT events to ensure a trap does not mutate the architectural state. Repeat from a fresh machine instance and compare output and state digests.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `SpecMachine, MicrocodedMachine, differential_retirement`.

## Counterexamples, failure modes, and model scope

No physical port peripheral, bus, synchronizer, interrupt controller, DMA, I/O timing or system-call boundary is implemented. A deterministic event tape is a software reference, not equipment measurement or a real-time interaction certificate. Signed data origin and input authorization remain separate requirements.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
