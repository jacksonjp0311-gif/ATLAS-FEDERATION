# ATLAS FORGE — Distributed Systems #12 · v0.1.0

This node extends the ONE canonical Atlas federation, after exact Software Design Patterns v0.1.0; it is not a standalone replacement. Standard-library reference implementations illustrate causality, quorum mathematics, single-decree Paxos acceptors, state-based CRDT merge, two-phase commit, SQLite local command deduplication and replayable integrity checking.

Run from this directory: `python -m distributed_atlas`, `python -m unittest discover -s tests -v`, `python evidence/independent_oracle.py`. The independent oracle enumerates a separate mathematical model rather than calling the production formula as its expected result.

**Validity:** finite crash-stop, non-Byzantine educational models, fixed cluster membership. No live networking, dynamic membership, verified linearizability under concurrency, real power-cut recovery, real device or publisher-original source authentication, independent peer review, or security certification. Never use the package as an unmodified production consensus protocol or safety interlock.

`docs/DEPTH_MANUAL_v0.1.0.md` includes standalone technical chapters, worked examples, uncertainties, failure modes, and links to original bibliography. `data/` and the federation's `common/nodes/distributed-systems-atlas/` are exact versioned record collections with source and qualified relationship provenance. The original 30-domain queue is never edited; Bitwork routing remains frozen.


## Scoped software content v1.0.0 — preserved edition

Original v0.1.0 material remains intact as chapter records, source cards and revision IDs. The v1.0.0 extension includes chapters 17–24, 3 new offline reference modules, bounded two-proposer failure exploration, a standalone independent register-history oracle, and explicit negative evidence. `docs/DEPTH_MANUAL_v1.0.0.md` is a superset of the v0.1 manual; no hosted service or certified network is represented. This is an original 30-domain reference in a single canonical federation.
