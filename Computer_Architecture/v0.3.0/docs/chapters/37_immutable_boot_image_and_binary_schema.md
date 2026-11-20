# 37. Immutable boot-image structure and AT8 machine-code identity

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`image=header(magic,version,flags,length,CRC32,SHA256) || ROM`

**Units and representation:** bytes, bit strings, aligned instruction PCs. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

An original programmable machine needs a finite contract for loading instructions before it can run any compiler or operating system. AT8 uses a fixed two-byte instruction format, four general-purpose registers and 256 bytes maximum of ROM. The boot-image wrapper does not change the instruction set. It defines a **44-byte header**: 4-byte ASCII magic `AT8R`, 1-byte format version 3, 1-byte reserved flags 0, 2-byte big-endian ROM length, 4-byte big-endian CRC32, and a 32-byte raw SHA-256 digest, followed by the unmodified ROM payload. Total image length is exactly 44 + ROM length. The length must be even and within 2–256 bytes. The canonical encoder and decoder must agree byte-for-byte, not merely interpret the same program.

The mathematical property of a fixed header is that the parser can decide where each field begins without invoking code from the payload. The checksum protects against some accidental or unmodeled corruption; SHA-256 provides a cryptographic *digest*. Neither provides source authentication without an independently trusted reference and an appropriate signature or authenticated boot root. The decoder therefore reports `sha256_is_authentication=False`, and the image is not a secure-boot design. NIST SP 800-193 distinguishes firmware integrity from protecting authorized firmware changes; we use its categories as bibliography, not as a claim of NIST conformity.

## Reproduce this investigation offline

Assemble `LDI R0, 5; ADDI R0, 7; OUT R0, 0; HALT` to an eight-byte ROM. Generate an image of exactly 52 bytes. Parse magic/version/length independently with `struct.unpack('>4sBBHI32s', header)`, recalculate CRC32 and SHA-256 from the eight ROM bytes, then compare a second encoding byte-for-byte. Mutate the magic, reserved flags, version, payload length, CRC, digest and final byte one at a time. Every corruption must be rejected without executing any instruction.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `encode_boot_image, decode_boot_image`.

## Counterexamples, failure modes, and model scope

The reference does not include a persistent root of trust, key custody, signing authority, anti-rollback fuse, physical memory map, reset hardware, firmware flashing, ROM manufacturing, or measured boot timing. Parser success establishes syntax and self-consistency only. If an attacker controls both image and digest, the ordinary hash cannot identify an unauthorized image.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
