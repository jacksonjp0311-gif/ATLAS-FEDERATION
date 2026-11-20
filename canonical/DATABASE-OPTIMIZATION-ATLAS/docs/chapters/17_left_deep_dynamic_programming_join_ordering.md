## 17 — Left-deep dynamic-programming join ordering

For `n` input relations, many join orders produce the same relational result but dramatically different intermediate cardinalities. A **left-deep** plan repeatedly joins one new input relation to a previously constructed result. It is a restricted plan space: bushy plans, streaming joins and physical operator choice are not represented by this model.

Assign each relation `i` a nonnegative base row count `N_i` and each pair `(i,j)` an independent selectivity factor `s_ij` between zero and one. Define `r(S) = product_{i in S} N_i * product_{i<j in S} s_ij`. A nested-loop **abstract comparison cost** for extending subset `S` by `j` is `r(S)*N_j`. Define `DP[{i}]=N_i` and `DP[S]={min}_{j in S} (DP[S\{j}] + r(S\{j}) N_j)` with a stable tie break. This recurrence is valid for the stated cost and subset-size model, not for arbitrary real database plans. Complexity is `O(n² 2^n)` when cached subset cardinalities are precomputed, versus `n!` permutations.

**Worked investigation:** for base counts `(2,50,200)`, and all pair factors equal one, evaluate all six orders using `itertools.permutations`. Compare the minimum brute-force cost with `db_extended.left_deep_dp`. Re-run with a selective pair `(0,2)=0.01`; the optimal order can change. The original `db_reference.hash_join` and `merge_join` are semantics oracles, not cost/throughput measurements.

**Negative control:** permitting a cyclic `s_ij`, a value above one under this declared model, an unspecified cross product, or arbitrary floating tie comparisons can make an apparent optimal plan meaningless. Real systems add operator startup cost, memory spill, sort order, parallelism, locality, filters, and workload statistics.

**Verification:** run `test_db_extended.JoinOrderTests` and the independent `permutations` brute oracle on up to six finite relations. Never infer general optimizer optimality or production benchmarks from this result.
