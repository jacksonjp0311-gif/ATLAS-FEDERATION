# ATLAS FORGE · Database Optimization original #17 · Unsealed v0.1.0

## 01 — Relations, bags, NULL and query meaning

A database is first a collection of statements with defined meaning, not an index. Treat a relation as a finite set of tuples for theoretical relational algebra; SQL commonly uses **bags** (duplicates are retained) unless `DISTINCT` eliminates them. A join over bags multiplies multiplicities: if a key has 3 rows in `A` and 4 in `B`, an inner equijoin produces **12 pairs**. A high-speed join that drops duplicates is wrong.

SQL `NULL` denotes unknown/missing, not zero and not a universally equal value. In a WHERE predicate, only **TRUE** qualifies; FALSE and UNKNOWN do not. The three-valued truth tables imply `FALSE AND UNKNOWN = FALSE`, `TRUE AND UNKNOWN = UNKNOWN`, `TRUE OR UNKNOWN = TRUE`. `NULL = NULL` evaluates UNKNOWN; use `IS NULL` for null tests. Thus an inner equijoin `A.k = B.k` does not match two NULL keys.

**Executable investigation:** Run `python -m unittest test_db_reference.NullSemantics`. The test compares Python tri-state truth values against actual SQLite. Try left `(1,'a'),(1,'b'),(NULL,'n')`, right `(1,'x'),(1,'y'),(NULL,'z')`. The result has 4 pairs for key 1, none for NULL. `db_reference.hash_join` and `merge_join` preserve these bag semantics.

**Negative controls:** Treating unknown as `False` in all Boolean expressions fails `TRUE OR NULL`; treating unknown as a joinable key creates false rows; using a set during optimization loses SQL duplicates. No model here implements full SQL collation, affinities, decimal arithmetic, or arbitrary query parsing.
