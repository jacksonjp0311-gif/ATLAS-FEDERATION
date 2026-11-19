# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 05 — Cardinality estimation, correlation and uncertainty

Query-plan choices often depend more on estimated cardinality than on algebraic cost expressions. For predicate A, `selectivity(A)=matching_rows/total_rows` in a finite dataset. Under a **conditionally unjustified independence assumption**, `selectivity(A AND B)≈selectivity(A)*selectivity(B)`. If two columns are identical and each equals target value on 20% of rows, the actual conjunction is **20%** while the independence approximation is **4%**, a fivefold underestimate.

PostgreSQL's extended statistics include functional dependencies, combined distinct counts and multivariate most-common-value lists to mitigate such errors when configured; they are not guarantees of exact cardinalities. <https://www.postgresql.org/docs/current/planner-stats.html>. Histograms must state bin boundaries, sample size, estimation algorithm, outliers and whether stale statistics were refreshed. A sample of 100 rows from a million-row table has substantial uncertainty unless a sampling model and error bounds are supplied.

**Reconstruction:** `exact_conjunctive_selectivity` and `independence_selectivity` operate on the same constructed corpus. The unit and independent tests expose correlation deliberately rather than promoting the estimate to measured truth. Negative: if a user supplies a perfect functional dependency, an optimizer assuming independent columns may pick a badly sized hash table or nested loop. Acceptable output reports *estimated*, *actual on constructed corpus*, and *unknown in production* separately.
