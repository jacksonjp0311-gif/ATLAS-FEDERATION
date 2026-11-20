# ATLAS FORGE · Database Optimization Atlas · Original domain #17
## Unsealed scientific and executable reference, v0.1.0

**Placement:** This is an incremental domain-content candidate for the one original ATLAS FORGE federation. The authoritative Library release currently remains **OS Internals v1.0.0 (21 nodes)**; Network Stacks #16 is still unsealed. This manuscript does **not** promote #17 to a registered canonical node or change the original 30-domain queue. Any integration must use exact source-record revisions, preserve every predecessor file except explicitly authorized registry metadata, and pass the full fresh-archive regression.

**Purpose:** Reconstruct enough relational database theory and numerical/software evidence to reason about access paths, query cost, data preservation, concurrency, and empirical optimization without a cloud service. All algorithms are deliberately bounded and pedagogical; use established database engines, not these models, to hold valuable data. Units: pages, tuples, comparisons, bytes, logical timestamps, and *abstract* cost units, unless explicitly stated. No I/O latency, storage power-loss, production scaling, or hardware results were measured.

## 01 — Relations, bags, NULL and query meaning

A database is first a collection of statements with defined meaning, not an index. Treat a relation as a finite set of tuples for theoretical relational algebra; SQL commonly uses **bags** (duplicates are retained) unless `DISTINCT` eliminates them. A join over bags multiplies multiplicities: if a key has 3 rows in `A` and 4 in `B`, an inner equijoin produces **12 pairs**. A high-speed join that drops duplicates is wrong.

SQL `NULL` denotes unknown/missing, not zero and not a universally equal value. In a WHERE predicate, only **TRUE** qualifies; FALSE and UNKNOWN do not. The three-valued truth tables imply `FALSE AND UNKNOWN = FALSE`, `TRUE AND UNKNOWN = UNKNOWN`, `TRUE OR UNKNOWN = TRUE`. `NULL = NULL` evaluates UNKNOWN; use `IS NULL` for null tests. Thus an inner equijoin `A.k = B.k` does not match two NULL keys.

**Executable investigation:** Run `python -m unittest test_db_reference.NullSemantics`. The test compares Python tri-state truth values against actual SQLite. Try left `(1,'a'),(1,'b'),(NULL,'n')`, right `(1,'x'),(1,'y'),(NULL,'z')`. The result has 4 pairs for key 1, none for NULL. `db_reference.hash_join` and `merge_join` preserve these bag semantics.

**Negative controls:** Treating unknown as `False` in all Boolean expressions fails `TRUE OR NULL`; treating unknown as a joinable key creates false rows; using a set during optimization loses SQL duplicates. No model here implements full SQL collation, affinities, decimal arithmetic, or arbitrary query parsing.

## 02 — Physical pages, rows and the memory hierarchy

A disk file is arranged in pages, but a query works with rows and logical values. An illustrative fixed-width capacity is `R=floor((P-H)/r)` rows per page when page size `P` bytes, header `H` bytes and each row exactly `r` bytes. With 4096-byte pages, 96-byte overhead and 100-byte rows, `R=40`; 100,000 rows need at least `ceil(100000/40)=2500` data pages. Real tables contain variable-length values, free space, pointers and fragmentation; the equation is a *lower-bound planning approximation*, not a measured byte size.

For a sequential scan, a simplified abstract cost is `C_seq = N_pages*c_seq + N_rows*c_cpu`. A random access pattern may cost more per touched page than a sequential scan because of storage and caching effects; however, the actual ratio depends on SSD/HDD, working set, locality and read-ahead. If `c_seq=1` per page and `c_cpu=0.01` per row, the illustrative scan of the example table costs 3,500 abstract units. These are *configured weights*, not milliseconds.

**Reconstruction:** Count your physical SQLite page size using `PRAGMA page_size`, page count using `PRAGMA page_count`, and logical rows with `COUNT(*)`; record the platform, file hash, engine version, and before/after state. Never infer actual row width from a model without checking encoding and overflow pages. Negative: a page-count increase after `VACUUM` or an index rebuild cannot by itself prove query execution got faster.

## 03 — Sorted indexes and B+ tree navigation

A B+ tree keeps searchable keys in sorted leaf pages; internal separator keys direct lookups. A true implementation maintains balance, split/merge invariants, concurrent latching and crash-safe updates. This reference intentionally implements only a **bulk-loaded sorted leaf/fence structure**. Its leaf maxima serve as nondecreasing fence keys, allowing binary search for the first leaf whose maximum is at least the target. Duplicates may span leaf boundaries, so equality lookup must continue across leaves until a greater key appears.

With `L` leaf pages, a binary search on leaf fences takes `O(log L)` comparisons, then scans candidate entries. This is a conceptual two-level index; it does not justify calling the structure a fully balanced persistent B+ tree. For an illustrative leaf capacity of 2 and entries `(1,row0)` through `(1,row26)` followed by `(2,row99)`, equality lookup for 1 must return **27** row IDs, not merely those on one page.

**Executable reconstruction:** `SortedLeafIndex.from_entries()` sorts `(key,row_id)` pairs deterministically, builds leaf groups, and provides equality/range lookup. The independent oracle uses a brute-force sorted scan and includes duplicate-boundary adversarial cases. Negative: looking up the last leaf of a duplicated key using an upper-bound fence misses earlier duplicates. Integrity holds only for immutable bulk-loaded lists; concurrent insertion, tombstones and partial page writes are not modeled.

## 04 — Covering, composite and partial indexes

An index on `(a,b)` sorts by `a` first, then `b`. Equality on `a` can restrict the search to a contiguous range; equality on `b` alone generally cannot use the same leading-key narrowing without a separate optimization. A covering index additionally includes columns needed to return the query result without fetching the base table row, but may have higher write, storage and maintenance costs. Indexes are valuable only when their maintenance cost and selection benefits fit the workload.

**Constructed example:** `CREATE INDEX idx_parts_category_cost ON parts(category,cost)` followed by `SELECT cost FROM parts WHERE category=7` can be covered by the index. A full scan may still win for a tiny table or a predicate retrieving most rows. SQLite's documented optimizer uses statistics, index order and covering-index opportunities; do not assume any single choice for all versions. <https://www.sqlite.org/queryplanner.html>.

**Reconstruction:** Build a deterministic fixture, record `EXPLAIN QUERY PLAN` before/after index creation, execute and compare identical result bags. `db_reference.sqlite_observation` does this for SELECT statements. Negative: an `EXPLAIN` plan is an optimizer *prediction*, not measured wall-clock speed; a covering index can be a net loss under write-heavy workloads. `ANALYZE` collects statistics but does not certify optimality.

## 05 — Cardinality estimation, correlation and uncertainty

Query-plan choices often depend more on estimated cardinality than on algebraic cost expressions. For predicate A, `selectivity(A)=matching_rows/total_rows` in a finite dataset. Under a **conditionally unjustified independence assumption**, `selectivity(A AND B)≈selectivity(A)*selectivity(B)`. If two columns are identical and each equals target value on 20% of rows, the actual conjunction is **20%** while the independence approximation is **4%**, a fivefold underestimate.

PostgreSQL's extended statistics include functional dependencies, combined distinct counts and multivariate most-common-value lists to mitigate such errors when configured; they are not guarantees of exact cardinalities. <https://www.postgresql.org/docs/current/planner-stats.html>. Histograms must state bin boundaries, sample size, estimation algorithm, outliers and whether stale statistics were refreshed. A sample of 100 rows from a million-row table has substantial uncertainty unless a sampling model and error bounds are supplied.

**Reconstruction:** `exact_conjunctive_selectivity` and `independence_selectivity` operate on the same constructed corpus. The unit and independent tests expose correlation deliberately rather than promoting the estimate to measured truth. Negative: if a user supplies a perfect functional dependency, an optimizer assuming independent columns may pick a badly sized hash table or nested loop. Acceptable output reports *estimated*, *actual on constructed corpus*, and *unknown in production* separately.

## 06 — Cost-based access-path decisions

Given a finite plan set, a cost-based optimizer selects the plan with smallest **estimated** cost. The estimate here uses one full scan and one index access path. Let `N` be rows, `R` rows/page, `P=ceil(N/R)` pages, `s` estimated selectivity, and `M=ceil(N*s)` expected matches. This educational model computes

`C_scan=P*c_seq+N*c_cpu`

`C_index=ceil(log2(P+1))*c_rand + min(P, M)*c_rand + M*c_cpu`

for an unclustered access path. The clustered model replaces `M` page touches with `ceil(M/R)`. Read those expressions as *explicit simplifying assumptions*: actual engines account for visibility, page cache, index levels, selectivity distributions, CPU vectorization, parallel workers, and memory grants.

**Worked case:** `N=100000, R=100, s=.00001`, `c_seq=1`, `c_rand=4`, `c_cpu=.01`: scan ≈2000 abstract units; index ≈44.01 (10 levels times 4 + one page times 4 + one row CPU 0.01). With `s=.9`, random base-table accesses can make the index much worse than a sequential scan. The code rejects invalid `s`, negative weights, and zero rows/page. Negative: treating abstract cost units as milliseconds is an invalid inference.

## 07 — Equijoins: nested, hash and sort-merge

An inner equijoin produces one output pair for each pair of input rows with equal non-NULL keys. A naive nested loop uses up to `N*M` comparisons but has minimal build memory. A hash join builds a hash table for one input and probes the other, offering expected `O(N+M+outputs)` time under appropriate hashing assumptions, at the cost of memory and potentially partitioning/spill. Sort-merge joins sort both inputs (`O(N log N + M log M)` comparisons for in-memory sorting), then scan groups; preordered inputs can avoid sorting.

**Constructed case:** Left keys `[1,1,2,NULL]`, right keys `[1,1,3,NULL]` yield 4 pairs. Both `hash_join` and `merge_join` are verified against a separate nested-loop oracle **and** SQLite's actual inner-join result bags. The reference uses Python hashable/comparable keys; it does not model real hash-table memory, collation, late materialization, partition spilling or vectorization. Negative: a merge join advancing only one side after matching a duplicate key loses multiplicity; a hash join equating NULL to NULL invents rows.

## 08 — Join order, dynamic programming and search bounds

For a join graph of `n` relations, the number of syntactically possible binary join trees grows combinatorially. A practical optimizer needs a search budget and pruning, because not all joins can be reordered safely in the presence of outer joins, aggregation, volatile functions, or lateral dependencies. A subset dynamic-programming skeleton is:

`best[S] = min_{A proper subset of S} {best[A] + best[S\A] + join_cost(card[A],card[S\A])}`

where `S` is a connected subset of relation IDs, and every `card[•]` is separately estimated. This formula is illustrative; real planner costs include the properties of intermediate ordering, partitioning and indexes, and the plan space should not contain invalid disconnected joins without explicit Cartesian-product authorization.

**Worked case:** If A joins B on a selective predicate (output 100 rows) but B joins C on a poorly estimated broad predicate (output 100,000), selecting the selective pair first can drastically lower intermediate materialization, yet a convenient index may reverse the preference. Exact join order is never derivable from row counts alone. **Negative:** optimizing `LEFT JOIN` as arbitrary commutative inner joins changes SQL results. This chapter provides a derivation and limits, not an executable optimizer.

## 09 — External sorting, run generation and merge

Large sorts can exceed RAM. Given `N` tuples, an in-memory budget `M` tuples creates `ceil(N/M)` sorted runs, which are merged using a priority queue. If all runs are held in RAM, as this reference does, the algorithm tests the **ordering logic** but not actual disk-spilling I/O. A full external implementation requires file formats, fsync/restart design, stable ordering, bounded open file handles, temporary-file cleanup and space estimation.

For 1,000,000 tuples and a 20,000-tuple run budget, at least 50 runs are produced in the first pass. If only 8 runs can be merged in each pass, a minimum of `ceil(log_8 50)=2` merge passes are needed after initial run generation, assuming stable fan-in and no replacement selection. `db_reference.external_merge_sort` uses sorted chunks and k-way heap merge with original run order, preserving duplicates and stable equal-key ordering. Independent oracle compares it to Python's stable `sorted` on 7,000 deterministic examples. Negative: silently dropping duplicate sort keys changes query answer semantics.

## 10 — Buffer replacement and cache-aware reasoning

The buffer pool maps persistent pages into a bounded number of frames. LRU evicts the least recently accessed resident page; FIFO evicts the earliest inserted resident page, regardless of intervening hits. Neither is universally optimal. For access trace `[1,2,1,3,2]` at capacity 2, LRU hits at the third reference and misses at the fifth, while FIFO hits at both the third and fifth. The distinction matters when judging repetitive scans or hot lookup workloads.

**Reconstruction:** `lru_trace` and `fifo_trace` return per-access hit booleans and final resident order. Two independently written list-based models compare results over randomized traces. Units are hits and page requests, not seconds. Real buffer managers also have dirty-page writeback, pin counts, concurrency, shared cache, prefetching, eviction costs, and OS page caching. Negative: applying the model's hit-rate improvement to claim an observed application latency improvement is unsupported without controlled measurements.

## 11 — MVCC visibility, snapshots and anomalies

Multiversion concurrency control stores multiple committed versions so a snapshot can read a consistent historical view. In this bounded model, each commit has a strictly increasing logical timestamp `t`; for a key and snapshot `s`, the visible value is the latest commit where `t≤s`, or absent if none exists. A deletion is represented by a tombstone. These rules are enough to test *visibility*, but not to implement safe transaction scheduling.

**Worked case:** At t=1 insert A=5. Snapshot s=1 reads 5, even after later commit A=8 at t=2; new snapshot s=2 reads 8. A tombstone at t=3 does not retroactively remove the prior snapshot's value. The independent oracle reconstructs states from the original commit log and compares every returned snapshot.

**Critical negative:** Snapshot isolation alone does not imply serializability; simultaneous transactions may each read a common condition and write disjoint rows, causing write skew. This model provides no conflict detection, GC/vacuum, transaction aborts, distributed consistency or SSI; it must never be used as a transactional storage engine.

## 12 — WAL, transactions, checkpoints and failure boundaries

Write-ahead logging records transactional changes before the main database is updated, enabling crash recovery when the engine and storage stack preserve required write ordering. In SQLite WAL mode, readers can coexist with a writer, but there is still only one writer at a time; checkpoints may be delayed by long-running readers. WAL's same-host shared-memory requirements and checkpoint starvation are documented at <https://www.sqlite.org/wal.html>.

**Reconstruction:** Use Python `sqlite3` to create a temporary database, enable WAL (`PRAGMA journal_mode=WAL`), create a table, insert a row inside an explicit transaction, close the connection, reopen, verify the value, and run `PRAGMA integrity_check`. This tests ordinary process-level persistence in the current filesystem, **not** the behavior of sudden power removal, torn pages or hostile concurrent processes.

**Negative:** Never claim that a successful reopen proves write durability after a blackout. `fsync` behavior depends on OS and device; SQLite `synchronous` setting changes barriers. A long-lived reader may prevent WAL truncation and increase disk requirements. Preserve all three related files (database, `-wal` and `-shm`, when present) according to the engine's backup guidance rather than naively copying one live file.

## 13 — Evidence-based optimization with SQLite

Reconstruct a reproducible workload with: engine version, schema, exact query, parameter distribution, row population seed, page size, index list, statistics status, transaction mode, filesystem details, and machine hardware. First verify correctness: capture output rows before/after adding an index, compare as bags unless ORDER BY guarantees order, and check integrity. Then collect several warmed and cold trials (where your environment can actually isolate caches), report median and dispersion, and record environmental limits.

Run `EXPLAIN QUERY PLAN SELECT ...` to inspect a **chosen plan**, not as a substitute for timing. SQLite `ANALYZE` updates optimizer statistics; their reliability degrades if data distribution changes, so preserve the date and corpus revision used to collect them. `PRAGMA optimize` may perform analysis as needed in supported SQLite versions. <https://www.sqlite.org/lang_analyze.html>.

An illustrative in-memory table of 2,500 rows with `(part_id,category,cost)` uses `category=part_id mod 37`. Query `SELECT part_id,cost FROM parts WHERE category=7`. Build index `(category,cost)`, execute, and confirm both result sets match. The code records plan outputs without asserting a particular provider's plan text. **Negative:** no single observed plan or microbenchmark establishes worldwide or hardware-independent performance.

## 14 — Offline reconstruction, integrity and release gates

A minimal recoverable relational system can begin with well-documented **SQLite** and standard-library Python, keeping structured scientific records and provenance off the internet. The work is reconstructible only if data format, source exact revision, schema migrations, query semantics, index strategy and backup procedure can be independently checked. Keep the original database file unmodified, test on an expendable copy, and preserve `sha256sum` or Python `hashlib.sha256` receipts for every input and output.

**Procedure:** (1) record interpreter and SQLite versions; (2) create a throwaway database; (3) load deterministic rows with specified schema; (4) execute truth, join, lookup, snapshot and integrity tests; (5) add an index, compare exact results; (6) record EXPLAIN text and environment; (7) produce repeatable hashes for source, tests and outputs; (8) independently restore and rerun. Link the results to OS Internals (paging and WAL), Software Design Patterns (data contracts/idempotent journals), Distributed Systems (replication and commit), and Cryptographic Protocols (integrity/provenance) using exact record revisions, not unqualified names.

**Acceptance gates:** This increment has an executable mathematical/software reference and independent finite oracles. It lacks a native persistent B+ tree engine, query optimizer with exhaustive planner proof, distributed replica implementation, real measurement suite, long-duration fault injection, independent scientific review, publisher-original archive authentication, fresh full federation regression, and a verified patch from canonical OS Internals. These remain *HOLD*. Never increment the canonical checkpoint from this unsealed artifact.

---

## References and rights

See `sources.json` for exact URLs, source roles, access classification and verification limitations. Source pointers refer to public standards and maintained engineering documentation, not reproduced publisher source bytes. Original prose and reference models are AI-assisted ATLAS FORGE research artifacts. No third-party code is copied. Source versions can change; offline copies require separate rights and authenticity checks.
