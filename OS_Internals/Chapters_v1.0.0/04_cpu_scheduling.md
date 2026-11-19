# 04 — Round-robin, deadline scheduling, fairness, and utilization

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How does an operating system allocate one CPU among runnable tasks while declaring fairness and deadline assumptions?

## Assumptions and explicit model boundary

Tasks have finite integer arrival ticks and CPU bursts; our model has one logical CPU, no shared-cache or context-switch overhead, no blocking, deterministic pid tie-breakers and no deadline admission control. We do not equate the model with a live Linux scheduler.

## Mathematical law or invariant

U = sum(C_i / T_i); single-CPU utilization U <= 1 is necessary but not sufficient for general deadline feasibility. Response_i = first_run_i - arrival_i.

## Derivation and operational interpretation

Round-robin chooses a runnable process for at most q ticks before placing it at the tail; smaller q reduces worst-case response at the cost of more switching. Earliest-deadline-first chooses the smallest absolute deadline among ready jobs, preempting as needed. Formal EDF schedulability requires assumptions about deadlines, execution, sporadic arrivals and interference. Modern Linux documents EEVDF as a transition from CFS; its virtual-deadline/lag mechanism is distinct from our simple EDF teaching model.

## Worked constructed investigation

For A(arrival0, burst4, deadline10) and B(arrival1, burst1, deadline2), the one-CPU EDF teaching trace is A,B,A,A,A: B preempts at tick1 and completes by tick2. If an unbounded higher-priority interrupt storm occurs, the software model’s deadline guarantee no longer applies.

## Executable or experimental reconstruction procedure

Run round_robin and earliest_deadline_first on constructed workloads, independently recompute each tick’s runnable set and compare traces. Measure throughput, turnaround, waiting, response, deadline misses, idle time and context switches. Reject unsupported hard-real-time claims unless worst-case execution and admission have been measured.

## Adversarial/negative case

A utilization sum below 1 does not guarantee all arbitrary constrained-deadline task sets are schedulable. Setting quantum=0 would make the time-slice model ill-defined. Strict priorities can starve lower-priority work.

## Failure boundaries, unknowns and acceptance holds

No measured CPU dispatch, EEVDF conformance, multicore load balancing, CPU frequency scaling, interrupt jitter, or real-time certification.

## Exact-source links and dependent knowledge

Bibliographic pointers: SCHED7 (https://man7.org/linux/man-pages/man7/sched.7.html), KERNEL_EEVDF (https://docs.kernel.org/scheduler/sched-eevdf.html), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: control-atlas, mathematics-physics-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
