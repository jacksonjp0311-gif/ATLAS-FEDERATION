# Chapter 08 — Conservative optimization and trap-preserving transformations

An optimization is permitted only when it preserves the declared observations of all relevant executions. In Tiny-I32 those observations are either a returned checked integer or a trapped execution. Constant folding may replace `2+3*4` with `14`; it must **not** replace `2147483647+1` with an out-of-range literal or silently wrap to a negative integer.

The implementation folds a fully constant arithmetic expression only if evaluating it under the checked semantics succeeds. Otherwise the original subtree remains and the runtime raises a trap if that branch is reached. For `if true then a else b`, the optimizer first requires the *entire expression* to be well typed, then it can eliminate the unreachable branch without evaluating it. This preserves `if true then 3 else 1/0` as a defined value 3.

**Differential experiment:** Compile every seeded candidate with optimization enabled and disabled; run both; compare them against the independent AST interpreter. A result is a tuple `('value',n)` or `('trap',None)`. Compare tuples rather than silently excluding cases that trap. The first oracle includes many trapped cases explicitly.

A known negative case is speculative evaluation: replacing a conditional's result with the eager evaluation of both branches creates a division-by-zero where none existed. Another is folding division using host-language floor semantics, changing `-7/2` from `-3` to `-4`.

**Not implemented:** Loop-invariant code motion, SSA rewriting, common-subexpression elimination with memory effects, alias analysis, target instruction scheduling, interprocedural optimization and register allocation. These are appropriate next-edition tasks, not proofs delivered by v0.1.
