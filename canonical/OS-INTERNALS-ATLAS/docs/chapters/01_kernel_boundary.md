# 01 — Privilege boundaries, traps and minimum kernel responsibilities

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

What separates a fault-containable application from privileged control of memory, devices and scheduling?

## Assumptions and explicit model boundary

Model two privilege domains U and K with a memory protection unit and a trap vector. User instructions are untrusted. The kernel must validate syscall number, address ranges, lengths and permissions before reaching hardware resources. Real CPUs have rings, exception levels or other protection mechanisms with architecture-specific details.

## Mathematical law or invariant

allowed(op) := authenticated_subject AND authorized_handle AND valid_bounds AND valid_state; trap: (U,pc,sp) -> (K,vector,controlled_kernel_stack).

## Derivation and operational interpretation

A system call must not simply branch into privileged code using an attacker-supplied stack. Hardware changes privilege and chooses a controlled entry point; software validates arguments and changes back on return. The essential safety invariant is that an untrusted program cannot map arbitrary physical frames, execute supervisor instructions or write kernel control structures. Isolation fails if kernel code dereferences an unchecked user pointer or trusts a stale handle.

## Worked constructed investigation

An application asks to write 100 bytes starting at virtual address 0x1FF0. With 4 KiB pages the range crosses a page boundary. Verifying only the starting address is insufficient: the kernel must validate both pages or use a fault-tolerant copy-from-user primitive. A numeric handle 4 reused after close may refer to a different object; our generation-tagged model rejects the old token.

## Executable or experimental reconstruction procedure

In os_atlas.capabilities, grant a read handle, demonstrate denied write, revoke and reuse its slot. In os_atlas.addressing, map one user page and one supervisor-only page, and verify a user read of the latter faults. Write down the trap preconditions, state returned on success, and precise failure modes. This does not execute actual syscalls.

## Adversarial/negative case

A raw integer descriptor without generation and rights can suffer an ABA reuse problem; a pointer validated once before concurrent unmapping may become invalid. Capability metadata in a Python object is not a hardened security boundary.

## Failure boundaries, unknowns and acceptance holds

The model does not implement CPU privilege transitions, interrupts, speculative execution containment, KPTI, actual kernel entry assembly, or malicious-host resistance.

## Exact-source links and dependent knowledge

Bibliographic pointers: OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/), OPENAT2 (https://man7.org/linux/man-pages/man2/openat2.2.html), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html)

Cross-domain prerequisites: computer-architecture-digital-hardware-atlas, cryptographic-protocols-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
