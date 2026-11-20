# 44. Cache lines, address tags, write-through coherence, and memory locality

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`line=floor(address/line_size), index=line mod line_count, tag=floor(address/line_size)`

**Units and representation:** bytes, lines, tags, read hits/misses. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The direct-mapped cache reference introduces one bounded memory-hierarchy mechanism while leaving the AT8 ISA unchanged. A 256-byte RAM is divided into cacheable lines of 4, 8 or 16 bytes. Each access uses an aligned line base and a cache index equal to the line number modulo 2,4,8 or 16 lines. The tag is the corresponding base address. On a read miss the line is fetched from backing RAM; on a hit the cached byte is returned. Writes are **write-through and write-allocate**: backing RAM is updated immediately, and the indexed cache line is either patched or filled from the new RAM state.

The primary invariant is observational coherence for a single logical CPU: every cache read returns the value that would be returned by an immediate read of the backing RAM after the same writes. Two blocks may collide at the same cache index, causing eviction and a future miss. A cache invalidation discards local cached copies, but not backing RAM contents. The independent oracle executes thousands of random address reads/writes against a separate 256-byte array to check correctness even when tags collide repeatedly.

## Reproduce this investigation offline

Start with bytes 0–255 in RAM, an eight-byte line and four cache lines. Read address 0: miss; read address 1: hit; read address 32: conflicts at index 0 and evicts line 0; read address 0 again: miss. Write value 173 at address 14, invalidate the entire cache and read address 14: return 173 from backing RAM. Vary line sizes and line counts and compare against a direct RAM oracle after every operation.

**Executable implementation:** `computer_atlas/v03_cache.py`. Public functions: `SmallRAMCache`.

## Counterexamples, failure modes, and model scope

This is not an implemented transistor SRAM array or a tested FPGA cache. It excludes write buffering, stalls, refill latency, energy, concurrency, DMA, multiprocessor coherence, cache hierarchy, memory consistency, address translation and cache side-channel mitigations. A later software or hardware architecture can use it as an executable policy reference, not a hardware claim.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
