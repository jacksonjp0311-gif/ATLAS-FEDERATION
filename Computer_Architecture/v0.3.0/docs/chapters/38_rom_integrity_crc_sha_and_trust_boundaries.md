# 38. ROM verification, corruption detection, and the limits of checksums

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`CRC32(ROM)==header_crc and SHA256(ROM)==header_hash`

**Units and representation:** CRC polynomial, bytes, hexadecimal digests. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

Error detection and source authenticity are independent claims. CRC32 is a bounded polynomial remainder optimized for common accidental bit errors; SHA-256 is a cryptographic digest with stronger collision resistance. Recomputing either from the payload only verifies correspondence to the expected value, and that expected value must have its own trustworthy provenance. An archive containing an altered ROM and its matching altered digest can be internally consistent and still be unauthorized or scientifically incorrect.

The AT8 v0.3 decoder first validates the version and total length, then checks both CRC and SHA, and finally runs the inherited `validate_rom` instruction checker. Those steps deliberately fail closed. They protect against truncated images, altered reserved fields, odd instruction counts, unsupported opcodes, invalid branch targets, and inconsistent payload digests. ECC recovery is a separate layer that needs a known expected image digest. Its 13-bit codeword representation does not replace the ordinary image or secretly add bytes to the AT8 ISA.

## Reproduce this investigation offline

Build two valid images for different eight-byte programs and confirm their hashes differ. Corrupt the final payload byte but leave header intact: parser refuses. Now recalculate both CRC and SHA to match the changed payload: a self-consistent image may parse, but **there is still no proof that it came from the authorized creator**. Verify that changing reserved flags or writing a forged header of length 257 causes rejection. Preserve a clear evidence field `secure_boot_signature_verified=False`.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `decode_boot_image, ecc_recover_image_payload`.

## Counterexamples, failure modes, and model scope

CRC32 is not a signature and SHA-256 is not an authorization policy. Authenticity requires separately protected keys and a verified trust chain, revocation rules and physical recovery mechanisms. Publisher citations are likewise not authenticated source-file bytes. None of these controls is physically tested or installed on an actual processor.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
