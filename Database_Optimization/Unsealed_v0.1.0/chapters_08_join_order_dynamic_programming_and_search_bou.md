# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 08 — Join order, dynamic programming and search bounds

For a join graph of `n` relations, the number of syntactically possible binary join trees grows combinatorially. A practical optimizer needs a search budget and pruning, because not all joins can be reordered safely in the presence of outer joins, aggregation, volatile functions, or lateral dependencies. A subset dynamic-programming skeleton is:

`best[S] = min_{A proper subset of S} {best[A] + best[S\A] + join_cost(card[A],card[S\A])}`

where `S` is a connected subset of relation IDs, and every `card[•]` is separately estimated. This formula is illustrative; real planner costs include the properties of intermediate ordering, partitioning and indexes, and the plan space should not contain invalid disconnected joins without explicit Cartesian-product authorization.

**Worked case:** If A joins B on a selective predicate (output 100 rows) but B joins C on a poorly estimated broad predicate (output 100,000), selecting the selective pair first can drastically lower intermediate materialization, yet a convenient index may reverse the preference. Exact join order is never derivable from row counts alone. **Negative:** optimizing `LEFT JOIN` as arbitrary commutative inner joins changes SQL results. This chapter provides a derivation and limits, not an executable optimizer.
