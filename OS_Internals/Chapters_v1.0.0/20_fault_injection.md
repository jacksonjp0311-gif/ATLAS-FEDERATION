# 20 — Fault injection, independent oracle design, and finite model limitations

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How does a scientific OS reference distinguish a passing regression from a strong independent falsification attempt?

## Assumptions and explicit model boundary

A finite deterministic test can enumerate only the specified state space. Independent oracles use alternate control flow or mathematical formulations; constructing test data and implementation together does not make the work independently peer-reviewed.

## Mathematical law or invariant

coverage := tested_cases / declared_finite_cases; absence_of_counterexample != proof_for_all_inputs. Negative-control expected_fail must be demonstrated.

## Derivation and operational interpretation

For page replacement, compute OPT via a greedy next-reference rule and independently via exhaustive dynamic programming over all legal evictions; agreement over all 3-symbol traces of length 7 tests a nontrivial finite space. For deadlocks, compare Tarjan SCC with transitive reachability. For allocator conservation, compare a buddy block map with a byte-level occupancy bitmap. A negative control must violate a known invariant or generate a known counterexample, such as FIFO Belady anomaly or an unflushed commit.

## Worked constructed investigation

There are 3^7=2187 page-reference sequences of length 7 over three page IDs. Across frame counts 1,2,3, that is 6561 oracle comparisons per replacement policy. OPT should be no worse than FIFO or LRU on every fixed sequence for the same frame count; this does not imply performance on live workloads.

## Executable or experimental reconstruction procedure

Execute the 56+ unit tests, then evidence.independent_oracle and record exact totals and negative controls. Separate test correctness, source provenance, run environment, scientific source authentication and physical acceptance. Include a failure path that leaves the original release pointer untouched.

## Adversarial/negative case

A test suite that compares one implementation to itself has low independence. A corrupted oracle can create falsely passing results; source and fresh archive must run from disjoint paths and receipts must be compared as bytes.

## Failure boundaries, unknowns and acceptance holds

No complete concurrent state-space verification, field failure rates, external replication, power-outage measurements, timing benchmarks or production OS security audit.

## Exact-source links and dependent knowledge

Bibliographic pointers: OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html), FSYNC2 (https://man7.org/linux/man-pages/man2/fsync.2.html)

Cross-domain prerequisites: computation-atlas, measurement-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
