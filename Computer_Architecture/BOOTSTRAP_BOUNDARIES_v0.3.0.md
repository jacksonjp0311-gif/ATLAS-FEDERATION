# AT8 reconstruction contract and boundaries

## Inherited AT8 ISA/ABI unchanged

- 16 opcode types with fixed two-byte encoding; four 8-bit general-purpose registers.
- 256 bytes each of ROM and data RAM; byte-addressed, even-aligned program counter.
- Finite port/event tapes rather than actual device registers.
- No CALL/RET; no privilege mode; no memory protection; no real timer interrupts.
- v0.2 bounded source compiler uses R0 as accumulator and R1..R3 for loop counters.

## New *external* v0.3 reference layers

- 44-byte canonical AT8R/3 image envelope, unchanged ROM payload.
- Bounded dual-slot update simulation with generation and commit markers.
- SECDED(13,8) software fault simulation checked against ROM digest.
- Conservative finite control-flow graph and explicit nontermination uncertainty.
- 256-byte direct-mapped reference cache and write-through RAM consistency.
- Bounded sequential job monitor with exact per-job receipts; not a hardware OS.

## Guarantees intentionally not asserted

Cryptographic firmware authorization, full OS scheduling/protection, physical cache/data coherence, electrical timing correctness, physical memory retention, silicon manufacturing or guaranteed metastability resolution. These require future design and external testing. ATLAS FORGE does not use checksums as substitutes for physical provenance, and its 30-domain roadmap remains unchanged.
