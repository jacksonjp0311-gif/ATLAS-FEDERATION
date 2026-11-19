# ATLAS FORGE — Database Optimization Atlas, original domain #17, scoped reference v1.0.0

> One original 23-node federation only; direct predecessor Network Stacks v1.0.0. Source documents are bibliographic pointers, not authenticated original publisher files.

**Scope:** SQL semantics, pages/indexes, join planning, buffer caches, external sort, multivariate statistics, MVCC, WAL and verifiable offline references. Software tests do not imply physical database certification.

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 01 — Relations, bags, NULL and query meaning

A database is first a collection of statements with defined meaning, not an index. Treat a relation as a finite set of tuples for theoretical relational algebra; SQL commonly uses **bags** (duplicates are retained) unless `DISTINCT` eliminates them. A join over bags multiplies multiplicities: if a key has 3 rows in `A` and 4 in `B`, an inner equijoin produces **12 pairs**. A high-speed join that drops duplicates is wrong.

SQL `NULL` denotes unknown/missing, not zero and not a universally equal value. In a WHERE predicate, only **TRUE** qualifies; FALSE and UNKNOWN do not. The three-valued truth tables imply `FALSE AND UNKNOWN = FALSE`, `TRUE AND UNKNOWN = UNKNOWN`, `TRUE OR UNKNOWN = TRUE`. `NULL = NULL` evaluates UNKNOWN; use `IS NULL` for null tests. Thus an inner equijoin `A.k = B.k` does not match two NULL keys.

**Executable investigation:** Run `python -m unittest test_db_reference.NullSemantics`. The test compares Python tri-state truth values against actual SQLite. Try left `(1,'a'),(1,'b'),(NULL,'n')`, right `(1,'x'),(1,'y'),(NULL,'z')`. The result has 4 pairs for key 1, none for NULL. `db_reference.hash_join` and `merge_join` preserve these bag semantics.

**Negative controls:** Treating unknown as `False` in all Boolean expressions fails `TRUE OR NULL`; treating unknown as a joinable key creates false rows; using a set during optimization loses SQL duplicates. No model here implements full SQL collation, affinities, decimal arithmetic, or arbitrary query parsing.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 02 — Physical pages, rows and the memory hierarchy

A disk file is arranged in pages, but a query works with rows and logical values. An illustrative fixed-width capacity is `R=floor((P-H)/r)` rows per page when page size `P` bytes, header `H` bytes and each row exactly `r` bytes. With 4096-byte pages, 96-byte overhead and 100-byte rows, `R=40`; 100,000 rows need at least `ceil(100000/40)=2500` data pages. Real tables contain variable-length values, free space, pointers and fragmentation; the equation is a *lower-bound planning approximation*, not a measured byte size.

For a sequential scan, a simplified abstract cost is `C_seq = N_pages*c_seq + N_rows*c_cpu`. A random access pattern may cost more per touched page than a sequential scan because of storage and caching effects; however, the actual ratio depends on SSD/HDD, working set, locality and read-ahead. If `c_seq=1` per page and `c_cpu=0.01` per row, the illustrative scan of the example table costs 3,500 abstract units. These are *configured weights*, not milliseconds.

**Reconstruction:** Count your physical SQLite page size using `PRAGMA page_size`, page count using `PRAGMA page_count`, and logical rows with `COUNT(*)`; record the platform, file hash, engine version, and before/after state. Never infer actual row width from a model without checking encoding and overflow pages. Negative: a page-count increase after `VACUUM` or an index rebuild cannot by itself prove query execution got faster.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 03 — Sorted indexes and B+ tree navigation

A B+ tree keeps searchable keys in sorted leaf pages; internal separator keys direct lookups. A true implementation maintains balance, split/merge invariants, concurrent latching and crash-safe updates. This reference intentionally implements only a **bulk-loaded sorted leaf/fence structure**. Its leaf maxima serve as nondecreasing fence keys, allowing binary search for the first leaf whose maximum is at least the target. Duplicates may span leaf boundaries, so equality lookup must continue across leaves until a greater key appears.

With `L` leaf pages, a binary search on leaf fences takes `O(log L)` comparisons, then scans candidate entries. This is a conceptual two-level index; it does not justify calling the structure a fully balanced persistent B+ tree. For an illustrative leaf capacity of 2 and entries `(1,row0)` through `(1,row26)` followed by `(2,row99)`, equality lookup for 1 must return **27** row IDs, not merely those on one page.

**Executable reconstruction:** `SortedLeafIndex.from_entries()` sorts `(key,row_id)` pairs deterministically, builds leaf groups, and provides equality/range lookup. The independent oracle uses a brute-force sorted scan and includes duplicate-boundary adversarial cases. Negative: looking up the last leaf of a duplicated key using an upper-bound fence misses earlier duplicates. Integrity holds only for immutable bulk-loaded lists; concurrent insertion, tombstones and partial page writes are not modeled.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 04 — Covering, composite and partial indexes

An index on `(a,b)` sorts by `a` first, then `b`. Equality on `a` can restrict the search to a contiguous range; equality on `b` alone generally cannot use the same leading-key narrowing without a separate optimization. A covering index additionally includes columns needed to return the query result without fetching the base table row, but may have higher write, storage and maintenance costs. Indexes are valuable only when their maintenance cost and selection benefits fit the workload.

**Constructed example:** `CREATE INDEX idx_parts_category_cost ON parts(category,cost)` followed by `SELECT cost FROM parts WHERE category=7` can be covered by the index. A full scan may still win for a tiny table or a predicate retrieving most rows. SQLite's documented optimizer uses statistics, index order and covering-index opportunities; do not assume any single choice for all versions. <https://www.sqlite.org/queryplanner.html>.

**Reconstruction:** Build a deterministic fixture, record `EXPLAIN QUERY PLAN` before/after index creation, execute and compare identical result bags. `db_reference.sqlite_observation` does this for SELECT statements. Negative: an `EXPLAIN` plan is an optimizer *prediction*, not measured wall-clock speed; a covering index can be a net loss under write-heavy workloads. `ANALYZE` collects statistics but does not certify optimality.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 05 — Cardinality estimation, correlation and uncertainty

Query-plan choices often depend more on estimated cardinality than on algebraic cost expressions. For predicate A, `selectivity(A)=matching_rows/total_rows` in a finite dataset. Under a **conditionally unjustified independence assumption**, `selectivity(A AND B)≈selectivity(A)*selectivity(B)`. If two columns are identical and each equals target value on 20% of rows, the actual conjunction is **20%** while the independence approximation is **4%**, a fivefold underestimate.

PostgreSQL's extended statistics include functional dependencies, combined distinct counts and multivariate most-common-value lists to mitigate such errors when configured; they are not guarantees of exact cardinalities. <https://www.postgresql.org/docs/current/planner-stats.html>. Histograms must state bin boundaries, sample size, estimation algorithm, outliers and whether stale statistics were refreshed. A sample of 100 rows from a million-row table has substantial uncertainty unless a sampling model and error bounds are supplied.

**Reconstruction:** `exact_conjunctive_selectivity` and `independence_selectivity` operate on the same constructed corpus. The unit and independent tests expose correlation deliberately rather than promoting the estimate to measured truth. Negative: if a user supplies a perfect functional dependency, an optimizer assuming independent columns may pick a badly sized hash table or nested loop. Acceptable output reports *estimated*, *actual on constructed corpus*, and *unknown in production* separately.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 06 — Cost-based access-path decisions

Given a finite plan set, a cost-based optimizer selects the plan with smallest **estimated** cost. The estimate here uses one full scan and one index access path. Let `N` be rows, `R` rows/page, `P=ceil(N/R)` pages, `s` estimated selectivity, and `M=ceil(N*s)` expected matches. This educational model computes

`C_scan=P*c_seq+N*c_cpu`

`C_index=ceil(log2(P+1))*c_rand + min(P, M)*c_rand + M*c_cpu`

for an unclustered access path. The clustered model replaces `M` page touches with `ceil(M/R)`. Read those expressions as *explicit simplifying assumptions*: actual engines account for visibility, page cache, index levels, selectivity distributions, CPU vectorization, parallel workers, and memory grants.

**Worked case:** `N=100000, R=100, s=.00001`, `c_seq=1`, `c_rand=4`, `c_cpu=.01`: scan ≈2000 abstract units; index ≈44.01 (10 levels times 4 + one page times 4 + one row CPU 0.01). With `s=.9`, random base-table accesses can make the index much worse than a sequential scan. The code rejects invalid `s`, negative weights, and zero rows/page. Negative: treating abstract cost units as milliseconds is an invalid inference.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 07 — Equijoins: nested, hash and sort-merge

An inner equijoin produces one output pair for each pair of input rows with equal non-NULL keys. A naive nested loop uses up to `N*M` comparisons but has minimal build memory. A hash join builds a hash table for one input and probes the other, offering expected `O(N+M+outputs)` time under appropriate hashing assumptions, at the cost of memory and potentially partitioning/spill. Sort-merge joins sort both inputs (`O(N log N + M log M)` comparisons for in-memory sorting), then scan groups; preordered inputs can avoid sorting.

**Constructed case:** Left keys `[1,1,2,NULL]`, right keys `[1,1,3,NULL]` yield 4 pairs. Both `hash_join` and `merge_join` are verified against a separate nested-loop oracle **and** SQLite's actual inner-join result bags. The reference uses Python hashable/comparable keys; it does not model real hash-table memory, collation, late materialization, partition spilling or vectorization. Negative: a merge join advancing only one side after matching a duplicate key loses multiplicity; a hash join equating NULL to NULL invents rows.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 08 — Join order, dynamic programming and search bounds

For a join graph of `n` relations, the number of syntactically possible binary join trees grows combinatorially. A practical optimizer needs a search budget and pruning, because not all joins can be reordered safely in the presence of outer joins, aggregation, volatile functions, or lateral dependencies. A subset dynamic-programming skeleton is:

`best[S] = min_{A proper subset of S} {best[A] + best[S\A] + join_cost(card[A],card[S\A])}`

where `S` is a connected subset of relation IDs, and every `card[•]` is separately estimated. This formula is illustrative; real planner costs include the properties of intermediate ordering, partitioning and indexes, and the plan space should not contain invalid disconnected joins without explicit Cartesian-product authorization.

**Worked case:** If A joins B on a selective predicate (output 100 rows) but B joins C on a poorly estimated broad predicate (output 100,000), selecting the selective pair first can drastically lower intermediate materialization, yet a convenient index may reverse the preference. Exact join order is never derivable from row counts alone. **Negative:** optimizing `LEFT JOIN` as arbitrary commutative inner joins changes SQL results. This chapter provides a derivation and limits, not an executable optimizer.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 09 — External sorting, run generation and merge

Large sorts can exceed RAM. Given `N` tuples, an in-memory budget `M` tuples creates `ceil(N/M)` sorted runs, which are merged using a priority queue. If all runs are held in RAM, as this reference does, the algorithm tests the **ordering logic** but not actual disk-spilling I/O. A full external implementation requires file formats, fsync/restart design, stable ordering, bounded open file handles, temporary-file cleanup and space estimation.

For 1,000,000 tuples and a 20,000-tuple run budget, at least 50 runs are produced in the first pass. If only 8 runs can be merged in each pass, a minimum of `ceil(log_8 50)=2` merge passes are needed after initial run generation, assuming stable fan-in and no replacement selection. `db_reference.external_merge_sort` uses sorted chunks and k-way heap merge with original run order, preserving duplicates and stable equal-key ordering. Independent oracle compares it to Python's stable `sorted` on 7,000 deterministic examples. Negative: silently dropping duplicate sort keys changes query answer semantics.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 10 — Buffer replacement and cache-aware reasoning

The buffer pool maps persistent pages into a bounded number of frames. LRU evicts the least recently accessed resident page; FIFO evicts the earliest inserted resident page, regardless of intervening hits. Neither is universally optimal. For access trace `[1,2,1,3,2]` at capacity 2, LRU hits at the third reference and misses at the fifth, while FIFO hits at both the third and fifth. The distinction matters when judging repetitive scans or hot lookup workloads.

**Reconstruction:** `lru_trace` and `fifo_trace` return per-access hit booleans and final resident order. Two independently written list-based models compare results over randomized traces. Units are hits and page requests, not seconds. Real buffer managers also have dirty-page writeback, pin counts, concurrency, shared cache, prefetching, eviction costs, and OS page caching. Negative: applying the model's hit-rate improvement to claim an observed application latency improvement is unsupported without controlled measurements.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 11 — MVCC visibility, snapshots and anomalies

Multiversion concurrency control stores multiple committed versions so a snapshot can read a consistent historical view. In this bounded model, each commit has a strictly increasing logical timestamp `t`; for a key and snapshot `s`, the visible value is the latest commit where `t≤s`, or absent if none exists. A deletion is represented by a tombstone. These rules are enough to test *visibility*, but not to implement safe transaction scheduling.

**Worked case:** At t=1 insert A=5. Snapshot s=1 reads 5, even after later commit A=8 at t=2; new snapshot s=2 reads 8. A tombstone at t=3 does not retroactively remove the prior snapshot's value. The independent oracle reconstructs states from the original commit log and compares every returned snapshot.

**Critical negative:** Snapshot isolation alone does not imply serializability; simultaneous transactions may each read a common condition and write disjoint rows, causing write skew. This model provides no conflict detection, GC/vacuum, transaction aborts, distributed consistency or SSI; it must never be used as a transactional storage engine.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 12 — WAL, transactions, checkpoints and failure boundaries

Write-ahead logging records transactional changes before the main database is updated, enabling crash recovery when the engine and storage stack preserve required write ordering. In SQLite WAL mode, readers can coexist with a writer, but there is still only one writer at a time; checkpoints may be delayed by long-running readers. WAL's same-host shared-memory requirements and checkpoint starvation are documented at <https://www.sqlite.org/wal.html>.

**Reconstruction:** Use Python `sqlite3` to create a temporary database, enable WAL (`PRAGMA journal_mode=WAL`), create a table, insert a row inside an explicit transaction, close the connection, reopen, verify the value, and run `PRAGMA integrity_check`. This tests ordinary process-level persistence in the current filesystem, **not** the behavior of sudden power removal, torn pages or hostile concurrent processes.

**Negative:** Never claim that a successful reopen proves write durability after a blackout. `fsync` behavior depends on OS and device; SQLite `synchronous` setting changes barriers. A long-lived reader may prevent WAL truncation and increase disk requirements. Preserve all three related files (database, `-wal` and `-shm`, when present) according to the engine's backup guidance rather than naively copying one live file.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 13 — Evidence-based optimization with SQLite

Reconstruct a reproducible workload with: engine version, schema, exact query, parameter distribution, row population seed, page size, index list, statistics status, transaction mode, filesystem details, and machine hardware. First verify correctness: capture output rows before/after adding an index, compare as bags unless ORDER BY guarantees order, and check integrity. Then collect several warmed and cold trials (where your environment can actually isolate caches), report median and dispersion, and record environmental limits.

Run `EXPLAIN QUERY PLAN SELECT ...` to inspect a **chosen plan**, not as a substitute for timing. SQLite `ANALYZE` updates optimizer statistics; their reliability degrades if data distribution changes, so preserve the date and corpus revision used to collect them. `PRAGMA optimize` may perform analysis as needed in supported SQLite versions. <https://www.sqlite.org/lang_analyze.html>.

An illustrative in-memory table of 2,500 rows with `(part_id,category,cost)` uses `category=part_id mod 37`. Query `SELECT part_id,cost FROM parts WHERE category=7`. Build index `(category,cost)`, execute, and confirm both result sets match. The code records plan outputs without asserting a particular provider's plan text. **Negative:** no single observed plan or microbenchmark establishes worldwide or hardware-independent performance.


---

# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 14 — Offline reconstruction, integrity and release gates

A minimal recoverable relational system can begin with well-documented **SQLite** and standard-library Python, keeping structured scientific records and provenance off the internet. The work is reconstructible only if data format, source exact revision, schema migrations, query semantics, index strategy and backup procedure can be independently checked. Keep the original database file unmodified, test on an expendable copy, and preserve `sha256sum` or Python `hashlib.sha256` receipts for every input and output.

**Procedure:** (1) record interpreter and SQLite versions; (2) create a throwaway database; (3) load deterministic rows with specified schema; (4) execute truth, join, lookup, snapshot and integrity tests; (5) add an index, compare exact results; (6) record EXPLAIN text and environment; (7) produce repeatable hashes for source, tests and outputs; (8) independently restore and rerun. Link the results to OS Internals (paging and WAL), Software Design Patterns (data contracts/idempotent journals), Distributed Systems (replication and commit), and Cryptographic Protocols (integrity/provenance) using exact record revisions, not unqualified names.

**Acceptance gates:** This increment has an executable mathematical/software reference and independent finite oracles. It lacks a native persistent B+ tree engine, query optimizer with exhaustive planner proof, distributed replica implementation, real measurement suite, long-duration fault injection, independent scientific review, publisher-original archive authentication, fresh full federation regression, and a verified patch from canonical OS Internals. These remain *HOLD*. Never increment the canonical checkpoint from this unsealed artifact.


---

## 15 — Index-only scans, visibility maps, and heap fallback

An **index-only scan** is a conditional optimization, not a blanket guarantee that secondary-index entries are sufficient to answer a query. PostgreSQL's B-tree implementation can serve columns directly from an index only when the index stores the required values, but the engine still must establish MVCC visibility. The visibility map permits a fast decision on heap pages known to be all-visible. An unmarked page normally requires a heap check. There is a crucial distinction between **covering predicate columns**, **covering projection columns**, and **certifying visibility**.

Let `m` be the number of candidate index entries and `A` the all-visible heap-page set. For candidate row `i` on heap page `p_i`, the educational reference computes `H = sum_i 1[p_i not in A]` potential row-level heap visibility checks, and `m-H` rows answerable from index values under the all-visible model. Real systems deduplicate and cache heap page visits; the model explicitly counts per-row checks and does **not** predict I/O. With candidates on pages `(5,5,8,9)` and `A={5,9}`, the result is two potential heap checks and two index-only rows. It would be invalid to claim four index-only rows because the query projected only columns from the index.

**Procedure:** Use `db_extended.index_only_visibility((5,5,8,9), frozenset({5,9}))`, then perturb membership in `A`. Run `test_db_extended.VisibilityTests` and `independent_oracle_v1.py`; compare against direct filtering (`page not in all_visible_set`). Use a real PostgreSQL installation only if available and collect `EXPLAIN (ANALYZE, BUFFERS)` alongside table/visibility metadata; do not present the model as a measured result.

**Negative control:** an index that lacks a requested projected column is ineligible even if every page is all-visible. Recently updated heap pages are not automatically all-visible. Unverified disk contents, a stale external index, visibility bugs, and concurrent vacuum/reclamation fall outside this finite model.

**Sources:** PostgreSQL documentation, `https://www.postgresql.org/docs/current/indexes-index-only-scans.html`; SQLite covering-index behavior is a separate implementation (`https://www.sqlite.org/queryplanner.html`).


---

## 16 — Multivariate cardinality estimates and correlated predicates

A cost-based optimizer must estimate the number of rows produced by a predicate and joins. Under the independence assumption, `P(A and B) ≈ P(A) P(B)`; correlated columns violate this. If `(region, postal)` is perfectly dependent for a constructed population, `P(region=r)=0.1` and `P(postal=p)=0.1` may coexist with `P(both)=0.1`, not `0.01`. Tenfold underestimation propagates to downstream join costs.

For `N` input rows and selectivity estimate `s`, the **estimated cardinality** is `N*s` before rounding and algorithm-specific adjustments. This is an expected count, not a guaranteed exact output size. PostgreSQL documents extended statistics for functional dependencies, multiple-column distinct counts, and MCV (most common value) lists. They are gathered by `ANALYZE` and may become stale. A dependency statistic cannot, by itself, rule out an impossible combination of values.

**Procedure:** Construct 100 tuples `(i mod 10, i mod 10)`. Use `db_reference.exact_conjunctive_selectivity(rows,0,3,1,3)` and `independence_selectivity` and confirm `0.1` versus `0.01`. Repeat on anti-correlated columns and a dataset with skew. Document whether a given statistic is independent, observed, sampled, or modeled. For a real PostgreSQL system, use `CREATE STATISTICS ... (dependencies,ndistinct,mcv)` and `ANALYZE`, then compare plan estimates against actual rows; never use those plans as an independent proof of physical latency.

**Negative control:** a plan expected to return one row but returning hundreds is not saved by a correct B-tree implementation; the optimizer may choose the wrong join sequence. Sample errors, independence assumptions, data drift, parameter-sensitive plans, null values and correlation limits must accompany any estimated cardinality claim.

**Sources:** PostgreSQL `https://www.postgresql.org/docs/current/planner-stats.html` and `https://www.postgresql.org/docs/current/planner-stats-details.html`.


---

## 17 — Left-deep dynamic-programming join ordering

For `n` input relations, many join orders produce the same relational result but dramatically different intermediate cardinalities. A **left-deep** plan repeatedly joins one new input relation to a previously constructed result. It is a restricted plan space: bushy plans, streaming joins and physical operator choice are not represented by this model.

Assign each relation `i` a nonnegative base row count `N_i` and each pair `(i,j)` an independent selectivity factor `s_ij` between zero and one. Define `r(S) = product_{i in S} N_i * product_{i<j in S} s_ij`. A nested-loop **abstract comparison cost** for extending subset `S` by `j` is `r(S)*N_j`. Define `DP[{i}]=N_i` and `DP[S]={min}_{j in S} (DP[S\{j}] + r(S\{j}) N_j)` with a stable tie break. This recurrence is valid for the stated cost and subset-size model, not for arbitrary real database plans. Complexity is `O(n² 2^n)` when cached subset cardinalities are precomputed, versus `n!` permutations.

**Worked investigation:** for base counts `(2,50,200)`, and all pair factors equal one, evaluate all six orders using `itertools.permutations`. Compare the minimum brute-force cost with `db_extended.left_deep_dp`. Re-run with a selective pair `(0,2)=0.01`; the optimal order can change. The original `db_reference.hash_join` and `merge_join` are semantics oracles, not cost/throughput measurements.

**Negative control:** permitting a cyclic `s_ij`, a value above one under this declared model, an unspecified cross product, or arbitrary floating tie comparisons can make an apparent optimal plan meaningless. Real systems add operator startup cost, memory spill, sort order, parallelism, locality, filters, and workload statistics.

**Verification:** run `test_db_extended.JoinOrderTests` and the independent `permutations` brute oracle on up to six finite relations. Never infer general optimizer optimality or production benchmarks from this result.


---

## 18 — External sorting under a finite memory budget

Sorting a dataset larger than available memory motivates **external merge sorting**. In a simplified page model, assume `N` data pages, `B` buffer frames (`B >= 3`), initial in-memory sorted runs of at most `B` pages, and merge fan-in `k=B-1` (one output buffer). The initial number of runs is `R_0=ceil(N/B)` and merge passes recursively produce `R_{i+1}=ceil(R_i/k)` until `R<=1`. For fully materialized intermediate and final output, reads and writes for run generation plus all merges total `2*N*(1 + passes)` page operations. These count *logical* page transfers, not measured device IOPS or latency.

**Worked example:** `N=100` pages, `B=10`: initially ten runs, the first merge produces two runs, and the next produces one. There are two merge passes and `2*100*(1+2)=600` modeled page transfers. `B=2` cannot use the assumed two-way-or-better merge with separate output buffer; reject it instead of pretending an infinite fan-in.

**Procedure:** call `db_extended.external_sort_page_io(100,10)` and independently construct a list of run lengths, repeatedly merging `B-1` runs. Compare pass counts and transfer totals. Invoke `db_reference.external_merge_sort` for semantic sorting only; it holds all runs in memory and does not perform true disk I/O. Record data-page size, row format, available buffers, and whether the output can be pipelined into the next operator.

**Negative control:** failing to charge a final write in a materialized-output problem understates traffic, while charging one in an actual pipeline overstates it. Real storage includes seek costs, asynchronous I/O, write amplification, compression, SSD behavior and cache effects; the reference deliberately omits these.


---

## 19 — WAL recovery, commit markers, and crash-prefix limits

A write-ahead log permits reconstructing committed state from a record stream only under a defined durability and validity protocol. The offline finite model uses ordered records `BEGIN(t)`, `WRITE(t,key,value)`, `COMMIT(t)`. It accumulates tentative writes in a transaction workspace and applies them to committed state only after a matching commit record. Incomplete transactions at the end of the preserved log are ignored. `COMMIT` without `BEGIN`, `WRITE` without `BEGIN`, duplicate active `BEGIN` and malformed event types are rejected.

**Worked recovery:** `[BEGIN(1),WRITE(1,'x',7),COMMIT(1),BEGIN(2),WRITE(2,'x',9)]` replays to `x=7`. The second transaction lacks a durable commit marker. Appending `COMMIT(2)` replays `x=9`. `db_extended.wal_committed_prefix` is a pure in-memory *prefix replay* oracle. It does not model disk flush ordering, torn sectors, checkpoints, page-level log sequence numbers, concurrent transaction rollback, or cryptographic authentication.

**Procedure:** execute `test_db_extended.WALTests` and independent `independent_oracle_v1.py` with randomly interrupted prefixes. For SQLite real-engine observations, consult `https://www.sqlite.org/wal.html` and `https://www.sqlite.org/isolation.html`; record journal mode, synchronous setting, filesystem and storage assumptions before drawing durability conclusions. For a physical system, power interruption, controller flushes and media behavior must be separately measured.

**Negative control:** a successfully returned userspace commit does not prove persistence after a hard power cut without demonstrated correct sync and storage semantics. A syntactically valid but corrupt or malicious WAL is outside the model.


---

## 20 — Snapshot isolation, write skew, and dependency hazards

Multiversion concurrency control (MVCC) provides a consistent read snapshot under stated transaction isolation, but **snapshot isolation alone is not generally serializable**. In classic write skew, two concurrent transactions each read one invariant and write a *different* record, so there is no direct write/write conflict even though both commits together violate the invariant. A dependency graph can expose a potential cycle of read/write anti-dependencies.

**Worked case:** state `(doctor_A_on_call=1, doctor_B_on_call=1)` satisfies `A or B`. Transaction T1 sees both on-call and writes `A=0`. Transaction T2 sees both on-call in the same old snapshot and writes `B=0`. Both can commit under an isolation scheme that does not prevent the write-skew cycle, leaving `0,0`. Each transaction alone preserved the invariant. `db_extended.detects_two_tx_write_skew` returns `True` when each transaction's read set intersects the other's write set. This is only a bounded warning for one two-transaction pattern; it is NOT a complete serializability checker.

**Procedure:** instantiate `db_reference.MVCCVisibility`, take a common snapshot before each transaction, and separately replay the writes under allowed interleavings. Compare the offline result against the relevant documented SQLite or PostgreSQL isolation modes, not against an unspecified generic 'SQL' isolation definition.

**Negative control:** a read/write dependency cycle in a simplified static set model does not prove a real engine executed that schedule, and absence of the pattern does not establish serializability. Locking, predicate ranges, phantoms, SI conflict detection and transaction retries are excluded.

**Sources:** PostgreSQL transaction isolation `https://www.postgresql.org/docs/current/transaction-iso.html`, SQLite `https://sqlite.org/isolation.html`.


---

## 21 — Cost-model drift, regret, and explain-plan evidence

An optimizer selecting a low estimated-cost plan can be wrong when statistics, cost parameters, or workload characteristics have drifted. For candidate plans `i`, define predicted costs `c_i` and separately observed costs `t_i` on the **same controlled workload**. The chosen plan is `argmin_i c_i`. A simple regret diagnostic is `regret = t_chosen - min_i t_i >= 0`. This quantifies loss from the estimator on the supplied observations; it does not measure anything by itself.

**Worked example:** predicted costs `(1,2)` choose plan 0, while controlled measured costs `(100,1)` imply regret `99` measured-cost units. `db_extended.plan_regret` computes that number and marks model certification `False`. In a real engine, changing only the plan must preserve the **bag-semantic output**; verify query-result equality separately before comparing latency. SQLite `EXPLAIN QUERY PLAN` is a human-readable debug interface, not a stable machine protocol; its output can change between releases.

**Procedure:** compare index/scan model output against actual SQLite planner decisions on a constructed dataset; use `ANALYZE`, record SQLite version and index definitions, and run several isolated repetitions if evaluating timings. Keep predicted, observed and independently verified result sets separate. Do not invent measurements where no physical query execution occurred.

**Negative control:** a plan that runs faster but returns a different set or multiplicity of rows is invalid; a cost curve from estimated row counts cannot be used as if it were measured latency. Parameter sensitivity, warm-cache bias, blocked transactions and plan output instability require explicit handling.

**Sources:** `https://www.sqlite.org/eqp.html`, `https://www.sqlite.org/optoverview.html`, PostgreSQL `https://www.postgresql.org/docs/current/sql-explain.html`.


---

## 22 — Rebuilding a verified database-research reference offline

The purpose of this atlas node is to let a future engineer reconstruct **the reasoning needed to build a database system**, not merely install an arbitrary database binary. Minimum recoverable knowledge includes row and page layout, SQL/null semantics, ordered search, physical and logical plan cost, joins and sorting, buffer replacement, MVCC and WAL invariants, statistics, and documented failure assumptions. Each reference model is deliberately bounded and standard-library-only.

**Reconstruction protocol:** first verify the complete inherited ATLAS FORGE archive SHA and exact-node registry. Restore the direct incremental patch on the exact Network Stacks v1.0.0 predecessor, not on a random high-version filename. Check the full output ZIP hash, validate every source-file hash and immutable record revision, and rerun source and freshly reconstructed federation regressions. Run `python -m unittest discover -s DATABASE-OPTIMIZATION-ATLAS -p 'test_*.py' -q` with its local import path, then `independent_oracle.py` and `independent_oracle_v1.py`. Keep negative controls and machine-readable receipts. Preserve the original 30-domain queue byte-for-byte.

**Practical lab sequence:** begin with integer keys and finite rows in an in-memory engine. Implement NULL truth tables and deterministic bag joins; use SQLite as an independent semantic oracle. Add `SortedLeafIndex`, then confirm its duplicate-boundary behavior and compare indexed versus scan costs without claiming hardware calibration. Add finite MVCC histories and a WAL replay with incomplete tails, then prove which properties tests actually establish. Only after these steps attempt a real file-backed engine with checksummed pages and controlled crash testing. Maintain per-step source, units, fixtures and limits.

**Negative control:** a successfully reconstructed ZIP and 3,000-plus software tests do not prove storage-controller reliability, database security, crash-consistent real filesystems, capacity scaling, or independent scientific acceptance. The complete federation remains content-ready only within a stated scope; production and physical acceptance remain separate gates.


---

## Source verification, negative controls and acceptance

All concepts, claims, equations, methods and cross-domain dependencies use immutable exact revisions under the original `atlas.common/1` contract. Independent finite oracles are bounded to constructed workloads and do not certify a production database, security, hardware durability or external expert review.
