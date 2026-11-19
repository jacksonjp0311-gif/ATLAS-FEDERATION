## 16 — Multivariate cardinality estimates and correlated predicates

A cost-based optimizer must estimate the number of rows produced by a predicate and joins. Under the independence assumption, `P(A and B) ≈ P(A) P(B)`; correlated columns violate this. If `(region, postal)` is perfectly dependent for a constructed population, `P(region=r)=0.1` and `P(postal=p)=0.1` may coexist with `P(both)=0.1`, not `0.01`. Tenfold underestimation propagates to downstream join costs.

For `N` input rows and selectivity estimate `s`, the **estimated cardinality** is `N*s` before rounding and algorithm-specific adjustments. This is an expected count, not a guaranteed exact output size. PostgreSQL documents extended statistics for functional dependencies, multiple-column distinct counts, and MCV (most common value) lists. They are gathered by `ANALYZE` and may become stale. A dependency statistic cannot, by itself, rule out an impossible combination of values.

**Procedure:** Construct 100 tuples `(i mod 10, i mod 10)`. Use `db_reference.exact_conjunctive_selectivity(rows,0,3,1,3)` and `independence_selectivity` and confirm `0.1` versus `0.01`. Repeat on anti-correlated columns and a dataset with skew. Document whether a given statistic is independent, observed, sampled, or modeled. For a real PostgreSQL system, use `CREATE STATISTICS ... (dependencies,ndistinct,mcv)` and `ANALYZE`, then compare plan estimates against actual rows; never use those plans as an independent proof of physical latency.

**Negative control:** a plan expected to return one row but returning hundreds is not saved by a correct B-tree implementation; the optimizer may choose the wrong join sequence. Sample errors, independence assumptions, data drift, parameter-sensitive plans, null values and correlation limits must accompany any estimated cardinality claim.

**Sources:** PostgreSQL `https://www.postgresql.org/docs/current/planner-stats.html` and `https://www.postgresql.org/docs/current/planner-stats-details.html`.
