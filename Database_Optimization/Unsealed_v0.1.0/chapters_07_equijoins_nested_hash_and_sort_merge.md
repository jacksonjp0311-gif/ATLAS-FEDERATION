# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 07 — Equijoins: nested, hash and sort-merge

An inner equijoin produces one output pair for each pair of input rows with equal non-NULL keys. A naive nested loop uses up to `N*M` comparisons but has minimal build memory. A hash join builds a hash table for one input and probes the other, offering expected `O(N+M+outputs)` time under appropriate hashing assumptions, at the cost of memory and potentially partitioning/spill. Sort-merge joins sort both inputs (`O(N log N + M log M)` comparisons for in-memory sorting), then scan groups; preordered inputs can avoid sorting.

**Constructed case:** Left keys `[1,1,2,NULL]`, right keys `[1,1,3,NULL]` yield 4 pairs. Both `hash_join` and `merge_join` are verified against a separate nested-loop oracle **and** SQLite's actual inner-join result bags. The reference uses Python hashable/comparable keys; it does not model real hash-table memory, collation, late materialization, partition spilling or vectorization. Negative: a merge join advancing only one side after matching a duplicate key loses multiplicity; a hash join equating NULL to NULL invents rows.
