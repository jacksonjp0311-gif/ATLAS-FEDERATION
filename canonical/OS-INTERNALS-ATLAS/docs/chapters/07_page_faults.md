# 07 — Demand paging, copy-on-write, protection faults and memory pressure

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How should a kernel distinguish missing pages from forbidden accesses and recover if memory allocation fails?

## Assumptions and explicit model boundary

A fault is classified by address validity, mapping presence, access type and privilege. Lazy allocation may supply a clean frame; copy-on-write may allocate and copy a private frame; invalid permissions or illegal addresses require a defined failure. Available physical memory and backing storage are finite.

## Mathematical law or invariant

Fault_class in {not-present, protection, privilege, invalid-address}; successful COW: old_content = new_content at fork instant, old_frame != new_frame after write.

## Derivation and operational interpretation

The MMU signals a fault when a present translation lacks required permissions or a translation is absent. The kernel must inspect VMA policy and fault metadata before deciding to allocate, retrieve from backing storage, copy a page, or terminate the process. For copy-on-write, read-only sharing is safe only while write faults update the writer’s mapping atomically with reference counts and appropriate TLB invalidation.

## Worked constructed investigation

Two processes initially map a shared read-only frame containing 0xAA at offset 12. On a write by process A, A receives a new frame initialized from the prior content; B still sees 0xAA, while A sees its new byte. Without a new frame, process B’s memory would change unexpectedly. In the educational model, permission faults are enforced but actual frame-copying is left for future target-specific implementation.

## Executable or experimental reconstruction procedure

Construct a fault-decision table for read, write and execute against r/w/x, user/supervisor and present/absent states. Test the AddressSpace exceptions for each class. To validate real COW on a later host, measure physical page identity and process isolation under controlled fork/write sequences.

## Adversarial/negative case

Retrying a missing-page fault indefinitely after out-of-memory can livelock. Swapping an active pinned DMA page can corrupt a device transaction. Conflating a not-present fault with an access-violation fault opens a security boundary.

## Failure boundaries, unknowns and acceptance holds

No kernel page-fault handler, swap I/O, huge pages, OOM killer policy, NUMA placement or actual COW implementation.

## Exact-source links and dependent knowledge

Bibliographic pointers: KERNEL_PGT (https://docs.kernel.org/mm/page_tables.html), MMAP2 (https://man7.org/linux/man-pages/man2/mmap.2.html), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: materials-atlas, computer-architecture-digital-hardware-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
