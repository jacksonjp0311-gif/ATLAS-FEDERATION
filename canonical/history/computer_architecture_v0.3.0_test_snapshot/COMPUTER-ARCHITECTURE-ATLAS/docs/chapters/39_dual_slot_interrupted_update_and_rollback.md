# 39. Two-slot boot recovery, staged updates, and version monotonicity

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`selected = argmax_generation(committed AND checksum_valid slots)`

**Units and representation:** generation uint32, exact byte images. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

An update should not render a known-good boot path unreachable merely because a new image write was interrupted. The illustrative design stores two candidate slots, each with a nonnegative 32-bit generation counter, a complete versioned boot image and a Boolean commit marker. Selection rejects absent, uncommitted, malformed and digest-invalid slots; it selects the highest valid committed generation. If equal-generation slots have different ROM identities, selection refuses ambiguity instead of silently guessing. A new update must have a strictly higher generation than the selected committed version.

The staged model represents three abstract interruption points: before writing new bytes, after writing but before commit, and after commit. Until a new slot is committed and validated, the previous committed slot remains the preferred recovery candidate. A random torn-write pattern is outside this simplified model, so we must not claim real flash atomicity or rollback resistance against a capable attacker. An actual design needs write ordering, durable media guarantees, storage erase semantics, power-failure testing, authentication, secure anti-rollback state and wear limits.

## Reproduce this investigation offline

Start with generation 1 in slot A. Stage generation 2 in slot B and stop after data. The selection remains A. Resume and commit generation 2; the selection becomes B. Stage generation 3 back to A and commit; A becomes the latest. Corrupt the higher-generation payload and confirm the old committed slot is selected again. Attempt a generation-2 update onto generation 3: reject. Construct an equal-generation image conflict: refuse. Record each decision and its reason without asserting it happened to physical memory.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `BootSlot, stage_update, select_boot_slot`.

## Counterexamples, failure modes, and model scope

A mathematical commit Boolean is not an atomic persistent write. Boot selection is not a bootloader implemented in hardware, and no electrical test was performed. There are no authenticated firmware keys, nonvolatile endurance tests, tamper-resistant counters or power-loss waveforms. This is an educational recovery invariant and a checklist for a future real system.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
