# 16 — Handles, generation tags, rights checks and stale-reference hazards

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How do capabilities reduce accidental authority over newly reused resources?

## Assumptions and explicit model boundary

Represent a handle as (slot,generation), a rights set among r,w,x, and an object reference. A new grant chooses an unused slot; revoke increments its generation. Python objects and public integers are not protected by hardware, secrets or process isolation.

## Mathematical law or invariant

authorize(h,op) := slot_in_range AND gen(h)=table[slot].gen AND op in rights(h); revoke(slot) => gen++.

## Derivation and operational interpretation

Raw slot reuse creates ABA: slot 4 originally points to object A, then gets freed and reused for object B. An old client carrying only slot 4 can accidentally operate on B. A generation tag distinguishes the two lifetimes. Permissions are necessary for least privilege, but time-of-check/time-of-use races require synchronization and kernel-controlled object lifetimes.

## Worked constructed investigation

Grant file A a read handle at slot0, generation0. Revoke it, then grant B at slot0, generation1. A stale generation0 handle is denied; the generation1 handle reads B. An attempt to use a read-only handle for write must fail.

## Executable or experimental reconstruction procedure

Use HandleTable.grant/check/revoke. Test stale reuse, duplicate invalid handles, wrong permissions and capacity exhaustion. Map each handle permission to a real syscall API contract only as a design exercise. Record the absence of secrecy, unforgeability and concurrent guarantees in this educational model.

## Adversarial/negative case

If a caller can fabricate both slot and generation and the host trusts them across a security boundary, this data structure alone cannot authenticate the caller. Long-running wraparound generations or unsynchronized reuse can reintroduce ABA.

## Failure boundaries, unknowns and acceptance holds

No real OS descriptor-table implementation, kernel credential enforcement, reference counting, file-offset sharing or process isolation.

## Exact-source links and dependent knowledge

Bibliographic pointers: OPENAT2 (https://man7.org/linux/man-pages/man2/openat2.2.html), POSIX2024 (https://pubs.opengroup.org/onlinepubs/9799919799/), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: cryptographic-protocols-atlas, software-design-patterns-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
