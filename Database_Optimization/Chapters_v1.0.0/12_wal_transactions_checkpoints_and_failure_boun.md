# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 12 — WAL, transactions, checkpoints and failure boundaries

Write-ahead logging records transactional changes before the main database is updated, enabling crash recovery when the engine and storage stack preserve required write ordering. In SQLite WAL mode, readers can coexist with a writer, but there is still only one writer at a time; checkpoints may be delayed by long-running readers. WAL's same-host shared-memory requirements and checkpoint starvation are documented at <https://www.sqlite.org/wal.html>.

**Reconstruction:** Use Python `sqlite3` to create a temporary database, enable WAL (`PRAGMA journal_mode=WAL`), create a table, insert a row inside an explicit transaction, close the connection, reopen, verify the value, and run `PRAGMA integrity_check`. This tests ordinary process-level persistence in the current filesystem, **not** the behavior of sudden power removal, torn pages or hostile concurrent processes.

**Negative:** Never claim that a successful reopen proves write durability after a blackout. `fsync` behavior depends on OS and device; SQLite `synchronous` setting changes barriers. A long-lived reader may prevent WAL truncation and increase disk requirements. Preserve all three related files (database, `-wal` and `-shm`, when present) according to the engine's backup guidance rather than naively copying one live file.
