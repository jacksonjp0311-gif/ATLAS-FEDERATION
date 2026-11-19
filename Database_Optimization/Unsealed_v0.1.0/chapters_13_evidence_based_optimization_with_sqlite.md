# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 13 — Evidence-based optimization with SQLite

Reconstruct a reproducible workload with: engine version, schema, exact query, parameter distribution, row population seed, page size, index list, statistics status, transaction mode, filesystem details, and machine hardware. First verify correctness: capture output rows before/after adding an index, compare as bags unless ORDER BY guarantees order, and check integrity. Then collect several warmed and cold trials (where your environment can actually isolate caches), report median and dispersion, and record environmental limits.

Run `EXPLAIN QUERY PLAN SELECT ...` to inspect a **chosen plan**, not as a substitute for timing. SQLite `ANALYZE` updates optimizer statistics; their reliability degrades if data distribution changes, so preserve the date and corpus revision used to collect them. `PRAGMA optimize` may perform analysis as needed in supported SQLite versions. <https://www.sqlite.org/lang_analyze.html>.

An illustrative in-memory table of 2,500 rows with `(part_id,category,cost)` uses `category=part_id mod 37`. Query `SELECT part_id,cost FROM parts WHERE category=7`. Build index `(category,cost)`, execute, and confirm both result sets match. The code records plan outputs without asserting a particular provider's plan text. **Negative:** no single observed plan or microbenchmark establishes worldwide or hardware-independent performance.
