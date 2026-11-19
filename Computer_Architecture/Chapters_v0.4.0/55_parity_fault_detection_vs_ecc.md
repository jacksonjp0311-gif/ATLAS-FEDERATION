# Chapter 55 — Parity byte memory: detection, correction limits, and false confidence

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Finite detection theorem
A single even-parity bit is the XOR of all data bits. If an odd number of data bits flip but the stored parity bit remains unchanged, the observed parity differs and the detector flags an error. If an even number of data bits flip, parity remains consistent and the error can be undetected. The detector does not repair the data, identify which bit flipped or prove that the stored byte is authentic.

This is distinct from the predecessor's extended Hamming (13,8) ROM scheme, which provides a defined single-error-correct/double-error-detect guarantee under its codeword model. Neither code is a cryptographic authentication scheme, nor does either establish a physical bit-error rate.

## Counterexample
Write byte zero with even parity. Flip data bit 0: parity reports an error and returns UNKNOWN instead of a guessed byte. Reset the memory; flip bits 0 and 1 together. The resulting byte is 3 but has even parity, so the detector reports *parity consistent*, even though the data differs from the original. An evidence system that labels the second read as 'correct' would be making a false claim.

## Reconstruction controls
Keep injection masks and parity-bit faults as explicit trace events. Test all eight single-bit flips and at least one two-bit counterexample for every byte value. Separate `detected` from `corrected` and label unknown states. Manufacturing acceptance requires physical cell retention measurements, radiation/error-injection characterization, power-failure testing, measured ECC overhead, and independently validated operating limits.

## Equation, implementation, and provenance

- **Key relation:** `parity(byte) = popcount(byte) mod 2; parity(data xor mask) differs iff popcount(mask) odd`.
- **Reference algorithm:** `v04_memory.ParityByteMemory; v02_ecc.protect_rom`.
- **Units:** byte and parity bits.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
