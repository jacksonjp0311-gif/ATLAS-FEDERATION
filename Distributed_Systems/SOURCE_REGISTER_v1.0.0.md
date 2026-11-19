# Bibliographic source register (not authenticated publisher files)

- `LAMPORT1978` 1978, Time, Clocks, and the Ordering of Events in a Distributed System, https://doi.org/10.1145/359545.359563. Source-to-formula expert check: HOLD.
- `FLP1985` 1985, Impossibility of Distributed Consensus with One Faulty Process, https://doi.org/10.1145/3149.214121. Source-to-formula expert check: HOLD.
- `DLS1988` 1988, Consensus in the Presence of Partial Synchrony, https://research.ibm.com/publications/consensus-in-the-presence-of-partial-synchrony. Source-to-formula expert check: HOLD.
- `CHANDRA1996` 1996, Unreliable Failure Detectors for Reliable Distributed Systems, https://doi.org/10.1145/226643.226647. Source-to-formula expert check: HOLD.
- `PAXOS1998` 1998, The Part-Time Parliament, https://www.microsoft.com/en-us/research/publication/part-time-parliament/. Source-to-formula expert check: HOLD.
- `RAFT2014` 2014, In Search of an Understandable Consensus Algorithm, https://web.stanford.edu/~ouster/cgi-bin/papers/raft-atc14.pdf. Source-to-formula expert check: HOLD.
- `CAP2002` 2002, Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services, https://doi.org/10.1145/564585.564601. Source-to-formula expert check: HOLD.
- `PAXOS2015` 2015, Paxos Made Moderately Complex, https://doi.org/10.1145/2673577. Source-to-formula expert check: HOLD.
- `LINEAR1990` 1990, Linearizability: A Correctness Condition for Concurrent Objects, https://www.cs.columbia.edu/~wing/publications/HerlihyWing90.pdf. Source-to-formula expert check: HOLD.
- `CRDT2011` 2011, A Comprehensive Study of Convergent and Commutative Replicated Data Types, https://asc.di.fct.unl.pt/~nmp/pubs/tr-inria-2011.pdf. Source-to-formula expert check: HOLD.
- `BAYOU1995` 1995, Managing Update Conflicts in Bayou, a Weakly Connected Replicated Storage System, https://doi.org/10.1145/224056.224070. Source-to-formula expert check: HOLD.
- `GRAY1978` 1978, Notes on Database Operating Systems, https://doi.org/10.1007/3-540-08755-9_9. Source-to-formula expert check: HOLD.


## Scoped v1 bibliography additions (no original authenticated bytes)
- PAXOS_SIMPLE2001: Paxos Made Simple, Leslie Lamport (2001). https://www.microsoft.com/en-us/research/publication/paxos-made-simple/. Boundary: proposer adopts highest-numbered previously accepted proposal at phase one quorum
- SQLITE_WAL: Write-Ahead Logging and PRAGMA synchronous, SQLite project (2026). https://www.sqlite.org/wal.html. Boundary: single-host WAL file and acknowledgement, physical power-cut durability configuration
- SQLITE_SYNCHRONOUS: SQLite PRAGMA synchronous, SQLite project (2026). https://www.sqlite.org/pragma.html. Boundary: WAL synchronous FULL and VFS xSync intended guarantee; local hardware remains untested
- ELLE_2020: Elle: black-box transactional safety checker, Jepsen / Kyle Kingsbury and collaborators (2020). https://github.com/jepsen-io/elle. Boundary: observational history anomaly reasoning and scope limitations
- RAFT_DISSERTATION2014: Consensus: Bridging Theory and Practice, Diego Ongaro (2014). https://github.com/ongardie/dissertation. Boundary: Raft configuration, leader completeness, snapshot and state-machine replication source context
