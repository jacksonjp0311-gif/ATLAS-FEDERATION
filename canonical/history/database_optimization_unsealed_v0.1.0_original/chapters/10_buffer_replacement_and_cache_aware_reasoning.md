# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 10 — Buffer replacement and cache-aware reasoning

The buffer pool maps persistent pages into a bounded number of frames. LRU evicts the least recently accessed resident page; FIFO evicts the earliest inserted resident page, regardless of intervening hits. Neither is universally optimal. For access trace `[1,2,1,3,2]` at capacity 2, LRU hits at the third reference and misses at the fifth, while FIFO hits at both the third and fifth. The distinction matters when judging repetitive scans or hot lookup workloads.

**Reconstruction:** `lru_trace` and `fifo_trace` return per-access hit booleans and final resident order. Two independently written list-based models compare results over randomized traces. Units are hits and page requests, not seconds. Real buffer managers also have dirty-page writeback, pin counts, concurrency, shared cache, prefetching, eviction costs, and OS page caching. Negative: applying the model's hit-rate improvement to claim an observed application latency improvement is unsupported without controlled measurements.
