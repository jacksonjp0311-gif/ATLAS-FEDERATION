## 19 — WAL recovery, commit markers, and crash-prefix limits

A write-ahead log permits reconstructing committed state from a record stream only under a defined durability and validity protocol. The offline finite model uses ordered records `BEGIN(t)`, `WRITE(t,key,value)`, `COMMIT(t)`. It accumulates tentative writes in a transaction workspace and applies them to committed state only after a matching commit record. Incomplete transactions at the end of the preserved log are ignored. `COMMIT` without `BEGIN`, `WRITE` without `BEGIN`, duplicate active `BEGIN` and malformed event types are rejected.

**Worked recovery:** `[BEGIN(1),WRITE(1,'x',7),COMMIT(1),BEGIN(2),WRITE(2,'x',9)]` replays to `x=7`. The second transaction lacks a durable commit marker. Appending `COMMIT(2)` replays `x=9`. `db_extended.wal_committed_prefix` is a pure in-memory *prefix replay* oracle. It does not model disk flush ordering, torn sectors, checkpoints, page-level log sequence numbers, concurrent transaction rollback, or cryptographic authentication.

**Procedure:** execute `test_db_extended.WALTests` and independent `independent_oracle_v1.py` with randomly interrupted prefixes. For SQLite real-engine observations, consult `https://www.sqlite.org/wal.html` and `https://www.sqlite.org/isolation.html`; record journal mode, synchronous setting, filesystem and storage assumptions before drawing durability conclusions. For a physical system, power interruption, controller flushes and media behavior must be separately measured.

**Negative control:** a successfully returned userspace commit does not prove persistence after a hard power cut without demonstrated correct sync and storage semantics. A syntactically valid but corrupt or malicious WAL is outside the model.
