# 30. Byte-wide SECDED (13,8) error control for executable ROM

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A stored eight-bit value can be protected with an extended Hamming code using parity bits at one-based positions 1,2,4,8, data bits at 3,5,6,7,9,10,11,12 and overall even parity at position 13. This gives 13 stored bits per original byte. The codeword is a finite mathematical redundancy scheme, distinct from the underlying physical failure mechanism.

## Technical derivation and invariants

Construct four parity-check bits from the binary positions. On reading, compute syndrome s∈[0,15] and overall parity p. (s,p)=(0,0) means no detected error. Nonzero syndrome with odd overall parity identifies a candidate corrupted location 1..12; zero syndrome and odd parity identifies position 13. Nonzero syndrome and even parity indicates an uncorrectable two-bit pattern; never return a decoded byte then. This guarantees correction of any one flipped bit and detection of every two-bit pattern, but not reliable recovery from arbitrary triple or higher-weight faults.

## Executable method and reproduction requirements

`encode_byte` validates exact 8-bit input and returns 13-bit codeword; `decode_word` marks clean, corrected or detected_double. `protect_rom` adds one such word per byte, and `recover_rom` refuses double-error codewords. An optional independently trusted ROM SHA-256 detects changes that parity alone may miss. Neither ECC nor a raw digest authenticates external origin.

## Constructed investigation

For each of the 256 byte values, verify an untouched codeword, all 13 one-bit flips and all C(13,2)=78 double-bit flips. That is 256×92=23,552 cases before optional ROM-level recovery tests. An independently written parity-matrix encoder should agree with the reference to avoid copying the implementation under test.

## Counterexamples, scientific limits and missing evidence

SECDED cannot certify DRAM/SRAM retention or radiation upset rates. Burst patterns can exceed distance-four guarantees; decoders and metadata may also be faulty. A physically useful memory subsystem requires measured fault distributions, address/data-path protection, scrubbing policy, and well-defined recovery failure behavior.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
