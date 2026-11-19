# 06 — Virtual address translation, page-table hierarchy, ASID and TLB shootdown

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How can isolated virtual address spaces share physical memory while enforcing permissions?

## Assumptions and explicit model boundary

An address a is unsigned 48-bit, the simplified model uses P=2^k-byte pages, each mapped VPN has a bounded physical frame number PFN and explicit r/w/x/user permissions. Real hardware page tables are architecture-specific and may have multiple levels and huge pages.

## Mathematical law or invariant

VPN = floor(a/P); offset = a mod P; physical = PFN * P + offset; C_TLB = hits*C_hit + misses*C_walk (simplified).

## Derivation and operational interpretation

A page table maps a virtual page number to a physical frame number plus rights. The offset survives translation unchanged because frames and pages have equal alignment. A TLB caches recent translations; modifying or revoking a mapping without invalidating all relevant cached translations risks stale rights or addresses. Process address-space identifiers are also part of the lookup key. Any performance model must include page-walk cost, page faults and memory hierarchy effects.

## Worked constructed investigation

For P=4096, a=0x305B, VPN=3 and offset=91. If VPN3 maps to PFN7, physical=7*4096+91=28763. Remap to PFN9; after shootdown, physical=36955. A user read from a supervisor-only mapping must fail regardless of cached translation.

## Executable or experimental reconstruction procedure

Use AddressSpace.map/translate/unmap with two different PFNs and r,w,x access requests; compare each result against an independent quotient/remainder oracle. Count hits/misses; inject a remap and verify no stale TLB response. Document user/kernel split, shootdown ordering and the fact that these Python objects do not model hardware races.

## Adversarial/negative case

Checking only the lowest page of a cross-page memory range can expose unauthorized memory. Treating TLB entries as global, without address-space tags, leaks data across processes. Unmapped pages must fault, not silently return physical frame zero.

## Failure boundaries, unknowns and acceptance holds

No 4/5-level hardware walks, huge-page splitting, page-table locking, real copy-on-write faults, side channels or TLB shootdown across CPUs.

## Exact-source links and dependent knowledge

Bibliographic pointers: KERNEL_PGT (https://docs.kernel.org/mm/page_tables.html), MMAP2 (https://man7.org/linux/man-pages/man2/mmap.2.html), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html)

Cross-domain prerequisites: computer-architecture-digital-hardware-atlas, mathematics-physics-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
