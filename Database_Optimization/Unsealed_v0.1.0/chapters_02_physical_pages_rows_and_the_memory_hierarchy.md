# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 02 — Physical pages, rows and the memory hierarchy

A disk file is arranged in pages, but a query works with rows and logical values. An illustrative fixed-width capacity is `R=floor((P-H)/r)` rows per page when page size `P` bytes, header `H` bytes and each row exactly `r` bytes. With 4096-byte pages, 96-byte overhead and 100-byte rows, `R=40`; 100,000 rows need at least `ceil(100000/40)=2500` data pages. Real tables contain variable-length values, free space, pointers and fragmentation; the equation is a *lower-bound planning approximation*, not a measured byte size.

For a sequential scan, a simplified abstract cost is `C_seq = N_pages*c_seq + N_rows*c_cpu`. A random access pattern may cost more per touched page than a sequential scan because of storage and caching effects; however, the actual ratio depends on SSD/HDD, working set, locality and read-ahead. If `c_seq=1` per page and `c_cpu=0.01` per row, the illustrative scan of the example table costs 3,500 abstract units. These are *configured weights*, not milliseconds.

**Reconstruction:** Count your physical SQLite page size using `PRAGMA page_size`, page count using `PRAGMA page_count`, and logical rows with `COUNT(*)`; record the platform, file hash, engine version, and before/after state. Never infer actual row width from a model without checking encoding and overflow pages. Negative: a page-count increase after `VACUUM` or an index rebuild cannot by itself prove query execution got faster.
