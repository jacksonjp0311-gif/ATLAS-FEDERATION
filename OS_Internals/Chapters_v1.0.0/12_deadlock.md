# 12 — Deadlocks, wait-for graphs and resource-allocation assumptions

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How can a finite system identify cycles of mutual waiting and distinguish them from slow progress?

## Assumptions and explicit model boundary

A wait-for graph edge A -> B means A cannot progress until B releases a single-instance resource. Resource allocation and wait edges are captured in one consistent snapshot. For multiple-instance resources, a cycle alone is not generally sufficient for deadlock.

## Mathematical law or invariant

Deadlock criterion (single-instance): exists nontrivial strongly connected component or self-loop in W=(V,E) under no external preemption.

## Derivation and operational interpretation

Tarjan’s algorithm tracks discovery indices, low links and a DFS stack to identify strongly connected components. In a single-instance wait-for graph, a directed cycle indicates circular wait when no participant can complete without release. An independent oracle can compute transitive reachability and group mutually reachable vertices. The two algorithms are structurally different and should agree on every bounded graph.

## Worked constructed investigation

A waits on B, B on C, C on A produces component {A,B,C}. A -> B -> C without a return edge has no deadlock component. Two disjoint pairs A<->B and C<->D yield two components. Self-wait A->A also forms a cycle.

## Executable or experimental reconstruction procedure

Run deadlocked_components and independently compute all-pairs reachability for random directed graphs with up to six nodes. Record detected components and a concrete witness wait chain. For real processes, capture lock ownership and waiting state atomically or explicitly describe snapshot skew.

## Adversarial/negative case

A false positive occurs if the graph snapshot combines edges from different moments; a false negative occurs when required edges are missing. A directed cycle need not indicate permanent deadlock in systems permitting resource preemption/timeouts.

## Failure boundaries, unknowns and acceptance holds

No kernel lockdep instrumentation, multi-instance Bankers algorithm, real thread sampling or proof of deadlock freedom for arbitrary software.

## Exact-source links and dependent knowledge

Bibliographic pointers: OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html)

Cross-domain prerequisites: mathematics-physics-atlas, distributed-systems-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
