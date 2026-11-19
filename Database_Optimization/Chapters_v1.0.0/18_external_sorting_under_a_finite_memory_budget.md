## 18 — External sorting under a finite memory budget

Sorting a dataset larger than available memory motivates **external merge sorting**. In a simplified page model, assume `N` data pages, `B` buffer frames (`B >= 3`), initial in-memory sorted runs of at most `B` pages, and merge fan-in `k=B-1` (one output buffer). The initial number of runs is `R_0=ceil(N/B)` and merge passes recursively produce `R_{i+1}=ceil(R_i/k)` until `R<=1`. For fully materialized intermediate and final output, reads and writes for run generation plus all merges total `2*N*(1 + passes)` page operations. These count *logical* page transfers, not measured device IOPS or latency.

**Worked example:** `N=100` pages, `B=10`: initially ten runs, the first merge produces two runs, and the next produces one. There are two merge passes and `2*100*(1+2)=600` modeled page transfers. `B=2` cannot use the assumed two-way-or-better merge with separate output buffer; reject it instead of pretending an infinite fan-in.

**Procedure:** call `db_extended.external_sort_page_io(100,10)` and independently construct a list of run lengths, repeatedly merging `B-1` runs. Compare pass counts and transfer totals. Invoke `db_reference.external_merge_sort` for semantic sorting only; it holds all runs in memory and does not perform true disk I/O. Record data-page size, row format, available buffers, and whether the output can be pipelined into the next operator.

**Negative control:** failing to charge a final write in a materialized-output problem understates traffic, while charging one in an actual pipeline overstates it. Real storage includes seek costs, asynchronous I/O, write amplification, compression, SSD behavior and cache effects; the reference deliberately omits these.
