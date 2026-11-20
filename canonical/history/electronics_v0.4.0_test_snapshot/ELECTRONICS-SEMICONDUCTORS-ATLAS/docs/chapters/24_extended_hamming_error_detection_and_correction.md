# Chapter 24: Preserving data integrity with a small error-correcting code

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
Stored or transmitted bits may flip. A minimal reconstructible error-correcting demonstration is the extended Hamming (8,4) single-error-correct/double-error-detect (SECDED) code. Its guarantees depend on a bounded error model.

## Construction
Place four data bits in 1-based codeword positions 3,5,6,7. Compute even parity at positions 1,2,4, each covering the positions whose binary indices share that parity bit. Set global position 8 to make total eight-bit parity even. To decode, compute the three-bit syndrome \(s\) over positions 1..7 and overall parity \(p\).

- \(s=0,p=0\): accept as clean.
- \(s\ne0,p=1\): one error at position \(s\), flip it and accept as corrected.
- \(s=0,p=1\): error in global parity bit 8, correct it.
- \(s\ne0,p=0\): a two-bit error is detected and data is **not** returned.

The code has minimum distance four. All one-bit errors are correctable, all two-bit errors detectable; higher-weight errors are not guaranteed to be detected or correctly interpreted.

## Worked investigation
For each of 16 data nibbles, the archive reference tests its clean codeword, all eight one-bit flips and all 28 two-bit flips. That is 16 × (1+8+28)=592 finite cases, with uncorrectable doubles returning no payload.

## Limitation and reconstruction
Coding-theoretic checks are not measured memory-error rates, radiation-hardening qualification or proof of long-term archival survival. Rebuild the parity-check matrix independently and compare syndrome behavior; document exactly which error patterns remain unprotected. Add checksums, redundancy, error logs and archival refresh outside this local coding model.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `hamming84_encode,hamming84_decode`.
- **Equation/invariant:** `minimum Hamming distance 4; SECDED syndrome and overall parity`.
- **Units:** dimensionless binary codewords.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.
