# Chapter 56 — Finite fair bus arbitration and its assumptions

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Causal arbitration model
When multiple masters compete for a shared bus, an explicit rule is required to select a winner. The simple round-robin arbiter rotates a pointer to one position after the last granted master. On every abstract arbitration cycle it grants the first requesting master encountered while traversing the master IDs modulo N. If none request, it grants no one and does not invent an access.

Under the assumptions that requests are sampled each cycle, a ready master remains requesting, and the arbiter is never reset or stalled, each continuously requesting master gets service within at most N arbitrations. This is **conditional fairness**. It does not prove bounded service under priority resets, hardware starvation, preemption, malformed requests, or clock-domain crossing.

## Worked case
For three masters all continuously requesting, the grant sequence is 0,1,2,0,1,2... . If only master 1 requests, it may be repeatedly granted, independent of the pointer. The reference returns `None` when nobody requests. Exhaust across N from two to eleven, and test boolean/type rejection to avoid accidentally treating Python `True` as an unsigned binary request.

## Interfaces to architecture
AT8 v0.1 does not have DMA or a multi-master architectural bus. This is a separate component-level research model, not an ISA extension. Before implementation in hardware, a bus designer must specify request/acknowledge timing, clock-domain boundaries, stalls, reset, error response, arbitration metadata, and fairness assumptions. The Electronics and Manufacturing nodes contain prerequisite timing and measurement evidence rules.

## Equation, implementation, and provenance

- **Key relation:** `grant_t = first requesting master at/after pointer_t (mod N)`.
- **Reference algorithm:** `v04_memory.RoundRobinArbiter`.
- **Units:** clock-indexed binary requests and master identifiers.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
