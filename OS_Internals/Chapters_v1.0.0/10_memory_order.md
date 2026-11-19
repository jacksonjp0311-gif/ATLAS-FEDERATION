# 10 — Memory ordering, data races, barriers, and happens-before reasoning

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

When can two CPUs observe shared data in different orders, and what does a lock guarantee?

## Assumptions and explicit model boundary

Out-of-order execution, compiler reordering, store buffering and noncoherent I/O devices can alter observation order. A release/acquire pair is meaningful only for a correctly synchronized object with the appropriate language and architecture memory model.

## Mathematical law or invariant

Sequenced-before ∪ synchronizes-with => happens-before (transitive closure). A data race is unordered conflicting shared accesses with insufficient synchronization under the language model.

## Derivation and operational interpretation

A producer storing a payload then a flag cannot assume a consumer observing flag=1 also sees the payload unless a permitted ordering mechanism exists. A release store paired with an acquire load constrains visibility under suitable models. Kernel barriers may have stronger or weaker scope and architecture mappings than language atomics; a compiler barrier alone need not order hardware.

## Worked constructed investigation

Initially payload=0 and ready=0. Producer writes payload=42 then ready=1. Consumer busy-waits on ready and reads payload. With unspecified plain accesses, visibility may be reordered or undefined in a data-race model; an appropriate release/acquire publication pattern orders the payload. This is a logical litmus scenario, not a measured CPU event.

## Executable or experimental reconstruction procedure

Write a happens-before graph and explicitly mark program-order, synchronization and conflicting accesses. Compare the graph to official memory-ordering documentation. Do not treat nondeterminism absence in a Python thread experiment as proof of race freedom. Future validation needs compiled C/C++/Rust litmus tests on specific CPUs.

## Adversarial/negative case

A lock that protects the write but not the read leaves a data race. A barrier on only one CPU generally cannot replace a synchronization handshake. DMA coherent memory can still require ordering protocols.

## Failure boundaries, unknowns and acceptance holds

No live weak-memory litmus suite, formal herd7/CAT model, C/C++ memory-model proof, or architecture-specific barrier execution.

## Exact-source links and dependent knowledge

Bibliographic pointers: MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: computer-architecture-digital-hardware-atlas, mathematics-physics-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
