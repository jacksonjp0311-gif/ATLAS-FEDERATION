# Investigation 13 — Vector clocks establish partial order, not authorization

**Origin:** constructed two-worker distributed system. Worker A has event clock (1,0) and worker B has (0,1); these events are concurrent under vector-clock semantics. After B receives a message from A, it merges the two vectors and increments its own component; the resulting event records that A's earlier event happened before B's receipt.

**Missing evidence:** the supplied clock is not a digital signature, and the message's sender is not authenticated. A malicious peer could forge counters. No amount of vector-clock comparison proves whether a worker was authorized to mutate a database, whether a provider operation committed, or whether the human operator pressed Stop. Host identity and durable request receipts must be evaluated separately.

**Source scope:** Lamport's 1978 ordering paper (public bibliographic summary). No distributed network system was run.
