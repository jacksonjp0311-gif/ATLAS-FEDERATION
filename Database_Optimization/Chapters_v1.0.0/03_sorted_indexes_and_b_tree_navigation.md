# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 03 — Sorted indexes and B+ tree navigation

A B+ tree keeps searchable keys in sorted leaf pages; internal separator keys direct lookups. A true implementation maintains balance, split/merge invariants, concurrent latching and crash-safe updates. This reference intentionally implements only a **bulk-loaded sorted leaf/fence structure**. Its leaf maxima serve as nondecreasing fence keys, allowing binary search for the first leaf whose maximum is at least the target. Duplicates may span leaf boundaries, so equality lookup must continue across leaves until a greater key appears.

With `L` leaf pages, a binary search on leaf fences takes `O(log L)` comparisons, then scans candidate entries. This is a conceptual two-level index; it does not justify calling the structure a fully balanced persistent B+ tree. For an illustrative leaf capacity of 2 and entries `(1,row0)` through `(1,row26)` followed by `(2,row99)`, equality lookup for 1 must return **27** row IDs, not merely those on one page.

**Executable reconstruction:** `SortedLeafIndex.from_entries()` sorts `(key,row_id)` pairs deterministically, builds leaf groups, and provides equality/range lookup. The independent oracle uses a brute-force sorted scan and includes duplicate-boundary adversarial cases. Negative: looking up the last leaf of a duplicated key using an upper-bound fence misses earlier duplicates. Integrity holds only for immutable bulk-loaded lists; concurrent insertion, tombstones and partial page writes are not modeled.
