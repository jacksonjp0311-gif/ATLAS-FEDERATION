# 18 — Multicore scheduling, coherence, TLB invalidation and interprocessor coordination

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

What changes when CPU scheduling and memory modification happen concurrently on more than one core?

## Assumptions and explicit model boundary

Each CPU may have private caches and TLBs, and memory coherence does not automatically confer high-level operation ordering. CPU affinity, NUMA placement, interrupt routing and process migration can change performance and race behavior.

## Mathematical law or invariant

Speedup(N) <= 1 / (s+(1-s)/N) under a simplified serial fraction s and ideal parallel fraction (1-s); real coherence and synchronization add costs.

## Derivation and operational interpretation

Moving a thread can improve throughput but invalidate warm caches or require remote memory access. Page table changes demand coordinated invalidation of stale TLB entries across cores before old access permissions can be relied on as revoked. Locks require atomic operations with ordering semantics. Amdahl’s bound states speedup cannot outrun serial work; it is not a benchmark result or an estimate of an actual machine.

## Worked constructed investigation

If 10% of a program is serial, ideal eight-core Amdahl speedup is 1/(0.1+0.9/8) ≈ 4.706 rather than 8. A process page mapped writable on CPU1 but revoked in a page table on CPU0 must not continue writing from an uninvalidated stale TLB entry.

## Executable or experimental reconstruction procedure

Calculate the speedup limit for s=0.1 and N=1..16. Build a happens-before chart for a page-table update and shootdown acknowledgments. Distinguish modeled CPU cache coherence from device DMA coherence and record how real host benchmarks would be controlled.

## Adversarial/negative case

Assuming thread migration has zero cost or that a local TLB flush affects all other CPUs causes incorrect memory-isolation reasoning. Amdahl’s model omits queueing, cache, thermal and interconnect effects.

## Failure boundaries, unknowns and acceptance holds

No actual SMP kernel, cache-coherence litmus proof, NUMA experiments, IPIs, measured scalability or verified CPU-specific ordering.

## Exact-source links and dependent knowledge

Bibliographic pointers: KERNEL_PGT (https://docs.kernel.org/mm/page_tables.html), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html), KERNEL_EEVDF (https://docs.kernel.org/scheduler/sched-eevdf.html)

Cross-domain prerequisites: mathematics-physics-atlas, computer-architecture-digital-hardware-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
