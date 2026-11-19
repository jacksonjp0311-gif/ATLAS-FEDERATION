# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 09 — External sorting, run generation and merge

Large sorts can exceed RAM. Given `N` tuples, an in-memory budget `M` tuples creates `ceil(N/M)` sorted runs, which are merged using a priority queue. If all runs are held in RAM, as this reference does, the algorithm tests the **ordering logic** but not actual disk-spilling I/O. A full external implementation requires file formats, fsync/restart design, stable ordering, bounded open file handles, temporary-file cleanup and space estimation.

For 1,000,000 tuples and a 20,000-tuple run budget, at least 50 runs are produced in the first pass. If only 8 runs can be merged in each pass, a minimum of `ceil(log_8 50)=2` merge passes are needed after initial run generation, assuming stable fan-in and no replacement selection. `db_reference.external_merge_sort` uses sorted chunks and k-way heap merge with original run order, preserving duplicates and stable equal-key ordering. Independent oracle compares it to Python's stable `sorted` on 7,000 deterministic examples. Negative: silently dropping duplicate sort keys changes query answer semantics.
