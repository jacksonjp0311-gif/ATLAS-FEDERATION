# Database Optimization v1.0.0 — official bibliographic URL register

Only pointers were consulted; original publisher-file bytes and signatures were **not authenticated**.

- SQLITE_PLANNER: **SQLite Query Planning** — https://www.sqlite.org/queryplanner.html. Role: Index order, covering access paths, selectivity reasoning. Original bytes: HOLD.
- SQLITE_ANALYZE: **SQLite ANALYZE** — https://www.sqlite.org/lang_analyze.html. Role: Statistics collection, stale statistics and query planning. Original bytes: HOLD.
- SQLITE_WAL: **SQLite Write-Ahead Logging** — https://www.sqlite.org/wal.html. Role: Single writer, WAL checkpoints, concurrency and durability caveats. Original bytes: HOLD.
- SQLITE_ISOLATION: **Isolation In SQLite** — https://sqlite.org/isolation.html. Role: Snapshot isolation, busy snapshot behavior and transaction boundaries. Original bytes: HOLD.
- PG_PLANNER: **PostgreSQL Current Documentation: Statistics Used by the Planner** — https://www.postgresql.org/docs/current/planner-stats.html. Role: Single- and multivariate cardinality estimation. Original bytes: HOLD.
- PG_EXPLAIN: **PostgreSQL Current Documentation: EXPLAIN** — https://www.postgresql.org/docs/current/sql-explain.html. Role: Observing estimated plans and actual execution where available. Original bytes: HOLD.
- PG_ISOLATION: **PostgreSQL Current Documentation: Transaction Isolation** — https://www.postgresql.org/docs/current/transaction-iso.html. Role: Isolation anomalies, repeatable read, serializable. Original bytes: HOLD.
- PG_CONCURRENCY: **PostgreSQL Current Documentation: Concurrency Control** — https://www.postgresql.org/docs/current/mvcc.html. Role: MVCC and concurrency interfaces. Original bytes: HOLD.
- PG_INDEX_ONLY: **PostgreSQL index-only scans and covering indexes** — https://www.postgresql.org/docs/current/indexes-index-only-scans.html. Role: MVCC visibility-map constraints, covering indexes and heap fallback. Original bytes: HOLD.
- PG_STATS_DETAILS: **PostgreSQL how the planner uses statistics** — https://www.postgresql.org/docs/current/planner-stats-details.html. Role: Row estimate examples, correlation and multivariate statistics. Original bytes: HOLD.
- SQLITE_EQP: **SQLite EXPLAIN QUERY PLAN** — https://www.sqlite.org/eqp.html. Role: Plan display is debug-only and format can change. Original bytes: HOLD.
