# Chapter 57 — Source-to-boot reproduction and explicit trust boundaries

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Reconstructible end-to-end contract
A compiler bootstrap demonstration should connect source text to exact machine bytes and observable execution. The previous structured-language compiler translates a bounded language into an unchanged AT8/0.1 ROM. The canonical assembler/disassembler round-trip is checked for byte identity. The v0.3 AT8R/3 boot image wraps the ROM in a header with CRC32 and SHA-256. The image is decoded and selected through the simulated A/B boot mechanism. Finally, the structured-source AST evaluator, atomic ISA engine, microcycle interpreter and NAND arithmetic datapath must agree on the defined finite test case.

The release certificate records distinct SHA-256 values for source text, canonical assembly, ROM and boot image. They are deliberately not conflated. A receipt also stores output events, final RAM digest and NAND netlist hash. Re-running the same inputs must reproduce the same certificate bytes, including a final receipt hash computed from a canonical serialization of all other fields.

## Worked case
Compile `SET 5; ADD 7; STORE 0; XOR 3; OUT 0; HALT`. The resulting program stores twelve, produces the output byte fifteen on port zero, and halts. Retire it under both processor implementations; verify the ADDI path through the explicit NAND circuit. Then modify `SET 5` to `SET 6` and demonstrate that the source and ROM digests change.

## Security and physical boundaries
CRC32 detects some accidental corruptions; SHA-256 supports content identity if a trusted expected digest exists. Neither is a digital signature or an authenticated boot root. The A/B update is a simulated state transition, not evidence of flash atomicity under loss of power. NIST SP 800-193 discusses protective/detective/recovery properties of platform firmware; this candidate does not assert conformance. Required future evidence includes an authenticated key infrastructure, measured boot ROM behavior, real physical write-protection and independent verification.

## Equation, implementation, and provenance

- **Key relation:** `H_source=SHA256(UTF8 source); H_ROM=SHA256(compile(source)); H_image=SHA256(boot_image)`.
- **Reference algorithm:** `v04_bootstrap.bootstrap_certificate; v03_boot.encode_boot_image`.
- **Units:** UTF-8 bytes, ROM bytes, hashes and execution events.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
