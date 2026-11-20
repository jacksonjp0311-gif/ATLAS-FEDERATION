# 40. SECDED ROM redundancy, fault injection, and byte-identity restoration

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`extended Hamming(13,8): 1-bit correction, 2-bit detection`

**Units and representation:** 13-bit codewords; eight data bits per codeword. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The prior Computer Architecture v0.2 release already preserves a SECDED(13,8) reference encoding. This edition uses it as a local ROM recovery layer without changing ROM instruction bytes or the ISA. Each 8-bit source byte is mapped to 13 bits using positions 1,2,4,8 for Hamming parity, positions 3,5,6,7,9,10,11,12 for data and position 13 for overall parity. An odd total parity plus a nonzero syndrome identifies a single-bit error in positions 1–12; odd parity plus zero syndrome identifies the overall parity bit; even total parity with nonzero syndrome detects a double-bit corruption. Triple-bit patterns are **not** guaranteed to be detected or corrected.

A recovery pipeline first records the expected complete ROM identity, encodes its bytes and simulates a fault in a specific codeword. It decodes each codeword, rejects known double faults, and independently compares the fully reconstructed ROM's SHA-256 to the trusted expected image. A small coding-theory guarantee does not imply a storage-media failure-rate guarantee; actual SRAM, ROM, flash and radiation faults may be correlated in time and location.

## Reproduce this investigation offline

Take the eight-byte arithmetic ROM in chapter 37. For its first encoded byte, independently toggle each of 13 bits and verify recovery of the original ROM and one corrected word. Exhaust the 78 unordered pairs of bit positions and require every double-bit case to raise an uncorrectable error. Reconstruct the original boot-image digest and reject any result that does not match it. The finite oracle repeats the fault campaign on multiple other ROMs.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `ecc_encode_image_payload, ecc_recover_image_payload`.

## Counterexamples, failure modes, and model scope

Extended Hamming(13,8) does not guarantee protection against three or more errors, burst corruption, memory address faults, malicious image replacement, ECC decoder faults or bad power supply. The trusted digest must be acquired through a separate authenticated channel for security claims. Physical fault-injection measurements remain an explicit HOLD gate.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
