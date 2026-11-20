# 05 — Interrupt dispatch, preemption, exception vectors and context integrity

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How can devices and exceptions interrupt user execution without corrupting recoverable thread state?

## Assumptions and explicit model boundary

The processor saves selected architectural state on a privilege transition; the handler saves further registers as required by ABI. Interrupt priority, mask rules, thread state and interrupt context restrictions vary across architectures. Our research describes the contracts rather than invoking a handler.

## Mathematical law or invariant

T_response = T_masked + T_entry + T_queued + T_handler_start; observed bound requires measured maxima and interrupt priorities.

## Derivation and operational interpretation

A handler first identifies its source and acknowledges or masks it according to its controller. A typical design performs bounded urgent work and defers noncritical activity to a lower-priority execution context. A preemption point must preserve registers, address-space identity, stack ownership and scheduling bookkeeping. Device interrupts may race with driver teardown, so a disconnect must quiesce or synchronize in-flight handlers.

## Worked constructed investigation

If a device interrupts during a task-state transition, updating a task as RUNNING before its kernel stack is valid can lead to an inconsistent return context. A safe event diagram records save-context, switch stack, identify cause, handle/queue, restore and return. A hypothetical 15 microsecond interrupt latency is not a measured claim and must not be placed in an evidence receipt.

## Executable or experimental reconstruction procedure

Construct a state diagram for exception-vs-interrupt, top-half-vs-deferred-work, and masking/acknowledgment. Link a testable simulated event queue to the scheduler and show how highest-priority IRQ storms can cause deadline misses. Record actual measurement requirements: timer calibration, timestamp source, load and device revision.

## Adversarial/negative case

Calling a sleep-capable mutex from an atomic interrupt context can deadlock or violate scheduling rules. Acknowledging an edge-triggered interrupt at the wrong time may lose events; masking indefinitely can halt progress.

## Failure boundaries, unknowns and acceptance holds

No real interrupt controller register access, DMA timing, memory fences, APIC/GIC conformance, or interrupt stress data.

## Exact-source links and dependent knowledge

Bibliographic pointers: GENERICIRQ (https://docs.kernel.org/core-api/genericirq.html), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html), DEVICE_MODEL (https://docs.kernel.org/driver-api/driver-model/overview.html)

Cross-domain prerequisites: electronics-semiconductors-atlas, computer-architecture-digital-hardware-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
