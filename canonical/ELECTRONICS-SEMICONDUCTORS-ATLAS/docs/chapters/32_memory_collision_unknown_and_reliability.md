# Chapter 32: Addressable memory: collisions, unknowns, and reliability boundaries

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Explicit memory transition semantics
Physical storage arrays require refresh or retention assumptions, word lines, bit lines, sense amplifiers and peripheral circuits. The abstract memory kernel exposes only one bounded edge-to-edge update for a finite list of words. Valid addresses and word widths are checked rather than silently wrapped. An UNKNOWN stored word remains unknown.

A simultaneous read and write of the same address has **no universal semantic convention**. Read-first returns the old word, write-first returns the new word, and undefined returns UNKNOWN. A future computer architecture must declare which convention its instructions and memory bus require. The model does not assert any read/write transition time, endurance or bitcell stability.

## Worked investigation
Start with words [1,2,3], address 1, and write value 9. The post-cycle words are [1,9,3]. For read-first the response is 2; for write-first it is 9; for undefined it is UNKNOWN. Each is a different *declared* contract, and pretending one is universal would make a reconstructed machine nondeterministic across implementations.

## Reliability and verification
Pair this transition model with the v0.3 SECDED code for a bounded detection/correction exercise, including explicit double-error detection. That does not prevent all multi-bit faults, address corruption, errors within the decoder, soft-error bursts, or data corruption during writes. A full memory requires measured bitcell retention, read disturb, static noise margin, access delay, sense-amplifier error rates, ECC overhead and temperature drift.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `bounded_memory_cycle; previous SECDED encode/decode`.
- **Governing relation:** `M_next[a]=data if write=1 else M[a]; read-collision must declare read-first/write-first/undefined`.
- **Units:** words and addresses, dimensionless.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
