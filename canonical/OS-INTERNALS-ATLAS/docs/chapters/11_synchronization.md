# 11 — Mutexes, condition variables, lost wakeups and priority inversion

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How do threads wait for state changes without a lost notification or a shared-state race?

## Assumptions and explicit model boundary

The condition predicate is protected by a mutex; a condition-variable wait atomically releases the lock and sleeps, then reacquires the lock before returning. Spurious wakeups are permitted; scheduling priorities and fairness are not guaranteed by mutual exclusion alone.

## Mathematical law or invariant

while not predicate: cond_wait(lock); signal/notify occurs after state update under the same synchronization discipline.

## Derivation and operational interpretation

If a consumer tests the predicate outside a mutex, the producer may signal between the test and the wait, leaving the consumer asleep forever. A correct condition-variable protocol combines predicate evaluation and atomic unlock/sleep, then rechecks after every wake. A semaphore counts tokens while a mutex conveys exclusive ownership; substituting one for another changes invariants. Priority inheritance can bound some priority inversion but requires kernel-level scheduling support.

## Worked constructed investigation

Queue initially empty. Consumer checks empty, producer enqueues and signals, consumer then sleeps: this incorrect sequence loses the signal. Holding a mutex while testing and invoking cond_wait atomically prevents the race. A low-priority lock holder can delay a high-priority waiter while medium-priority work runs.

## Executable or experimental reconstruction procedure

Define the shared predicate, lock invariant and transition schedule. Enumerate adversarial producer/consumer event interleavings and demonstrate one lost-wakeup trace. For a real OS later, use thread sanitizer and stress tests with measured scheduling classes, not just a passing Python unit test.

## Adversarial/negative case

Replacing while with if can fail on spurious wakeup. Holding a mutex while waiting for a worker that needs it deadlocks. Spinning under a single-core preempt-disabled context can starve the producer.

## Failure boundaries, unknowns and acceptance holds

No production mutex, condition variable, futex, priority inheritance or mechanical proof of concurrent program safety.

## Exact-source links and dependent knowledge

Bibliographic pointers: FUTEX2 (https://man7.org/linux/man-pages/man2/futex.2.html), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: control-atlas, distributed-systems-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
