# ATLAS FORGE · Database Optimization original #17 · Scoped reference v1.0.0

## 11 — MVCC visibility, snapshots and anomalies

Multiversion concurrency control stores multiple committed versions so a snapshot can read a consistent historical view. In this bounded model, each commit has a strictly increasing logical timestamp `t`; for a key and snapshot `s`, the visible value is the latest commit where `t≤s`, or absent if none exists. A deletion is represented by a tombstone. These rules are enough to test *visibility*, but not to implement safe transaction scheduling.

**Worked case:** At t=1 insert A=5. Snapshot s=1 reads 5, even after later commit A=8 at t=2; new snapshot s=2 reads 8. A tombstone at t=3 does not retroactively remove the prior snapshot's value. The independent oracle reconstructs states from the original commit log and compares every returned snapshot.

**Critical negative:** Snapshot isolation alone does not imply serializability; simultaneous transactions may each read a common condition and write disjoint rows, causing write skew. This model provides no conflict detection, GC/vacuum, transaction aborts, distributed consistency or SSI; it must never be used as a transactional storage engine.
