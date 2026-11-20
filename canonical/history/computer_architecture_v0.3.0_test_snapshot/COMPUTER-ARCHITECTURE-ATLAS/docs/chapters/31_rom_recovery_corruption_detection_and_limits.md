# 31. ROM recovery, failure reporting and verification boundaries

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

An instruction ROM is not equivalent to a mathematical byte sequence if its storage medium can corrupt bits. A reconstruction reference should retain the executable image and a protected codeword representation, then define how to respond when errors are detected. A correct decoder must not silently return a corrupted instruction stream after a double-bit error or after a mismatch against a separately trusted byte hash.

## Technical derivation and invariants

For encoded words c_i, decode each independently; if any word reports detected_double, abort before executing *any* recovered program. After successful decoding, calculate `H(ROM_recovered)` and compare with a pinned expected hash when one exists. A one-bit correction is counted, not concealed. More than two faults within a word may produce undetected or miscorrected patterns, so the checksum adds detection coverage but not absolute security.

## Executable method and reproduction requirements

`recover_rom` checks length and exact 13-bit bounds, counts corrected words, and raises `UncorrectableROMError` for detected two-bit events or hash mismatch. Test one-bit corruption, two-bit corruption, invalid metadata, even-length ROM bounds and independent retention of hash pins. Do not execute a ROM that has failed the gate.

## Constructed investigation

Encode `LDI R0,5; HALT` and flip one encoded parity or data bit. The reference recovers identical ROM bytes and reports exactly one corrected word. Flip two bits in the same word; recovery refuses with an explicit double-error class. Supply the wrong expected SHA-256; recovery refuses even if the ECC decoder sees clean codewords.

## Counterexamples, scientific limits and missing evidence

This handles isolated codeword bit flips, not tampering with the golden hash, provenance identity, unreliable readers, full media failure or hardware fault injection. Real storage protection requires replicated media, calibration, retention tests and external trust roots.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
