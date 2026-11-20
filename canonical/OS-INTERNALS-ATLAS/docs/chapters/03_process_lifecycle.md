# 03 — Processes, threads, fork, exec, wait and state transitions

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How can a kernel represent process lifetimes without leaking resources or confusing parent and child?

## Assumptions and explicit model boundary

Represent a process by an identity, address-space identity, open handles, credentials, threads and a state among NEW, READY, RUNNING, BLOCKED, ZOMBIE and REAPED. Thread scheduling and process ownership are related but not identical.

## Mathematical law or invariant

turnaround_i = completion_i - arrival_i; waiting_i = turnaround_i - CPU_service_i (single CPU, no I/O blocking).

## Derivation and operational interpretation

A child created by fork inherits a logical snapshot of memory mappings and descriptor references; copy-on-write can delay physical page copying. exec replaces the execution image while preserving selected process properties. exit ends execution but retains completion status until the parent reaps it. A kernel must distinguish process identifiers from reusable slots with generation identity, and account for zombie processes. CPU waiting-time formula is valid only for the stated simplified workload.

## Worked constructed investigation

Task A arrives tick 0 and requires 3 ticks; task B arrives tick 1 and requires 2. With two-tick round robin, the run trace A,A,B,B,A completes B at tick 4 and A at tick 5. B turnaround=3 and wait=1; A turnaround=5 and wait=2. Blocking I/O would change this equation.

## Executable or experimental reconstruction procedure

Use os_atlas.scheduling to calculate the trace and completion metrics. Create a process-lifecycle event table to distinguish READY-to-BLOCKED from READY-to-RUNNING and exit-to-reap. Construct a handle list that demonstrates identity reuse; specify which handles would be close-on-exec in a real system.

## Adversarial/negative case

If exit immediately frees all process identification, a concurrent wait may read the completion status of a new process reusing the same identifier. Omitting reaping causes zombies. A thread is not guaranteed to inherit the same scheduling class or signal mask as a separately created process.

## Failure boundaries, unknowns and acceptance holds

No real fork/exec/wait syscalls or scheduler context-switch assembly are implemented. Actual POSIX implementation details depend on platform/version.

## Exact-source links and dependent knowledge

Bibliographic pointers: FORK2 (https://man7.org/linux/man-pages/man2/fork.2.html), EXECVE2 (https://man7.org/linux/man-pages/man2/execve.2.html), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: software-design-patterns-atlas, computer-architecture-digital-hardware-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
