# 09 — Buddy allocator, fragmentation, alignment and free-space invariants

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How can contiguous physical memory be allocated and coalesced with constant-order lookup families?

## Assumptions and explicit model boundary

A single 2^M-byte region is aligned at address zero and subdivided to minimum block size 2^m. Each allocation consumes the smallest available power-of-two block. We ignore multiple NUMA nodes, reserved memory holes, DMA constraints and slab caches.

## Mathematical law or invariant

k = max(m,ceil(log2(request_bytes))); block_bytes = 2^k; buddy_address = address XOR 2^k.

## Derivation and operational interpretation

Find the smallest free block order k that fits a request, or a larger available block and recursively split it. The companion of a block at order k differs in the k-th bit, hence XOR with 2^k. On release, merge only if that exact companion is free at the same order; repeat until no merge applies. The disjoint union of allocated and free intervals must cover the original arena exactly.

## Worked constructed investigation

In a 1024-byte arena with 8-byte minimum blocks, a 9-byte request consumes 16 bytes, leaving 1008 free. After release, all split companions coalesce into the original 1024-byte block. Internal fragmentation is 7 bytes for this request, distinct from external fragmentation caused by scattered allocations.

## Executable or experimental reconstruction procedure

Use Buddy.alloc/release with deterministic random operations and compare the interval map against an independent 512-byte occupancy bitmap. Enforce double-free rejection, physical alignment and conservation after every step. Record the maximum and minimum block order and the exact requested versus allocated byte totals.

## Adversarial/negative case

Freeing a nonallocated pointer or coalescing nonbuddy addresses can create overlapping free ranges and double allocation. A request of 17 bytes needing 32 can fail despite total free bytes exceeding 32 when only small noncoalescible blocks remain.

## Failure boundaries, unknowns and acceptance holds

No Linux buddy zone migration, page migration, huge pages, hardware DMA address restrictions, concurrent allocator locking or actual physical pages.

## Exact-source links and dependent knowledge

Bibliographic pointers: OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/), KERNEL_PGT (https://docs.kernel.org/mm/page_tables.html)

Cross-domain prerequisites: computer-architecture-digital-hardware-atlas, computation-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
