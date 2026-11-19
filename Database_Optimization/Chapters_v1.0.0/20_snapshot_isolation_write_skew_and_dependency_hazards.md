## 20 — Snapshot isolation, write skew, and dependency hazards

Multiversion concurrency control (MVCC) provides a consistent read snapshot under stated transaction isolation, but **snapshot isolation alone is not generally serializable**. In classic write skew, two concurrent transactions each read one invariant and write a *different* record, so there is no direct write/write conflict even though both commits together violate the invariant. A dependency graph can expose a potential cycle of read/write anti-dependencies.

**Worked case:** state `(doctor_A_on_call=1, doctor_B_on_call=1)` satisfies `A or B`. Transaction T1 sees both on-call and writes `A=0`. Transaction T2 sees both on-call in the same old snapshot and writes `B=0`. Both can commit under an isolation scheme that does not prevent the write-skew cycle, leaving `0,0`. Each transaction alone preserved the invariant. `db_extended.detects_two_tx_write_skew` returns `True` when each transaction's read set intersects the other's write set. This is only a bounded warning for one two-transaction pattern; it is NOT a complete serializability checker.

**Procedure:** instantiate `db_reference.MVCCVisibility`, take a common snapshot before each transaction, and separately replay the writes under allowed interleavings. Compare the offline result against the relevant documented SQLite or PostgreSQL isolation modes, not against an unspecified generic 'SQL' isolation definition.

**Negative control:** a read/write dependency cycle in a simplified static set model does not prove a real engine executed that schedule, and absence of the pattern does not establish serializability. Locking, predicate ranges, phantoms, SI conflict detection and transaction retries are excluded.

**Sources:** PostgreSQL transaction isolation `https://www.postgresql.org/docs/current/transaction-iso.html`, SQLite `https://sqlite.org/isolation.html`.
