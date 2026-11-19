# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 06 — Cost-based access-path decisions

Given a finite plan set, a cost-based optimizer selects the plan with smallest **estimated** cost. The estimate here uses one full scan and one index access path. Let `N` be rows, `R` rows/page, `P=ceil(N/R)` pages, `s` estimated selectivity, and `M=ceil(N*s)` expected matches. This educational model computes

`C_scan=P*c_seq+N*c_cpu`

`C_index=ceil(log2(P+1))*c_rand + min(P, M)*c_rand + M*c_cpu`

for an unclustered access path. The clustered model replaces `M` page touches with `ceil(M/R)`. Read those expressions as *explicit simplifying assumptions*: actual engines account for visibility, page cache, index levels, selectivity distributions, CPU vectorization, parallel workers, and memory grants.

**Worked case:** `N=100000, R=100, s=.00001`, `c_seq=1`, `c_rand=4`, `c_cpu=.01`: scan ≈2000 abstract units; index ≈44.01 (10 levels times 4 + one page times 4 + one row CPU 0.01). With `s=.9`, random base-table accesses can make the index much worse than a sequential scan. The code rejects invalid `s`, negative weights, and zero rows/page. Negative: treating abstract cost units as milliseconds is an invalid inference.
