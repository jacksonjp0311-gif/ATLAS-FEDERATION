# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 04 — Covering, composite and partial indexes

An index on `(a,b)` sorts by `a` first, then `b`. Equality on `a` can restrict the search to a contiguous range; equality on `b` alone generally cannot use the same leading-key narrowing without a separate optimization. A covering index additionally includes columns needed to return the query result without fetching the base table row, but may have higher write, storage and maintenance costs. Indexes are valuable only when their maintenance cost and selection benefits fit the workload.

**Constructed example:** `CREATE INDEX idx_parts_category_cost ON parts(category,cost)` followed by `SELECT cost FROM parts WHERE category=7` can be covered by the index. A full scan may still win for a tiny table or a predicate retrieving most rows. SQLite's documented optimizer uses statistics, index order and covering-index opportunities; do not assume any single choice for all versions. <https://www.sqlite.org/queryplanner.html>.

**Reconstruction:** Build a deterministic fixture, record `EXPLAIN QUERY PLAN` before/after index creation, execute and compare identical result bags. `db_reference.sqlite_observation` does this for SELECT statements. Negative: an `EXPLAIN` plan is an optimizer *prediction*, not measured wall-clock speed; a covering index can be a net loss under write-heavy workloads. `ANALYZE` collects statistics but does not certify optimality.
