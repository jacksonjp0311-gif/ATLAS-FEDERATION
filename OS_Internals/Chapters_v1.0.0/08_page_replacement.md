# 08 — Page replacement, reference locality and Belady anomaly

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How many compulsory and capacity misses occur under FIFO, LRU and offline optimal replacement?

## Assumptions and explicit model boundary

All pages and frames are the same size; a finite ordered reference trace is known; prefetch, dirty writes, page pinning, kernel memory and disk timings are ignored. Optimal replacement has future knowledge and is a lower-bound oracle, not a deployable online policy.

## Mathematical law or invariant

Faults(policy, trace, F) = sum_t 1[reference_t not resident]; OPT evicts the page with maximal next-use position.

## Derivation and operational interpretation

FIFO evicts the earliest admitted resident page, regardless of recency; LRU evicts the least recently used resident page. OPT chooses the resident page whose next reference lies farthest in the future, which minimizes total faults in this model by an exchange argument. LRU has the stack property; increasing its capacity cannot increase misses on the same trace. FIFO lacks this property and can exhibit Belady anomaly.

## Worked constructed investigation

For trace 1,2,3,4,1,2,5,1,2,3,4,5, FIFO yields 9 faults with 3 frames but 10 with 4 frames. The independent Bellman dynamic-programming oracle enumerates all legal eviction choices on small traces and matches the OPT model exhaustively.

## Executable or experimental reconstruction procedure

Run page_faults for all three policies with frame counts 1..4 on a fixed 12-reference trace. Reproduce the FIFO anomaly and use the optimal exhaustive search on all 3-symbol traces of length 7. Record miss count, not invented I/O latency, and specify cold start as empty frames.

## Adversarial/negative case

A claim that more RAM always decreases page faults is false for arbitrary FIFO policies. One trace does not demonstrate a general workload benefit. Ignoring dirty-page writeback makes an I/O cost comparison incomplete.

## Failure boundaries, unknowns and acceptance holds

No storage-latency measures, working-set sampling, Linux multi-generation LRU conformance, swap wear or real memory pressure.

## Exact-source links and dependent knowledge

Bibliographic pointers: OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/), KERNEL_PGT (https://docs.kernel.org/mm/page_tables.html)

Cross-domain prerequisites: computation-atlas, mathematics-physics-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
