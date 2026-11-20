# Chapter 16 — Differential compiler laboratory, negative controls and preservation

### Experimental design

A scientific compiler reference should distinguish a passing example from a tested semantic relation. Version 0.2 uses **four** execution paths and **two** parser algorithms under a declared source semantics: direct AST big-step evaluation; optimized and unoptimized stack-machine execution; optimized and unoptimized typed-register execution. A generated source program is evaluated under both parser implementations to compare exact AST structure, then all executable pathways are checked against the independent big-step result. The laboratory records the random seed, program count, semantic comparisons, expected traps, malformed grammar rejects and invalid-register rejects.

The methods are intentionally nonidentical: the Pratt parser and recursive parser differ; the stack VM and register VM have different instruction representations and validation. However they still share some code, data and semantics. In particular, arithmetic operations use the same declared checked i32 model. A correlated bug in the common language specification can therefore evade every finite comparison.

### Valid comparison cases

Generated programs contain nested conditionals, integer arithmetic, variable binding and branch-specific divisions; in some cases correct behavior is an arithmetic **trap**, not a number. The checker compares outcome categories and numbers. Deliberately bad IR cases must be rejected rather than counted as extra successful executions. A malformed grammar must independently fail both parsing algorithms. Identical output for a single input is not evidence of universal compiler soundness.

### Reproducible commands

```sh
python -m unittest discover -s tests -q
python -m evidence.independent_oracle
python -m evidence.independent_oracle_v02
python -m compiler_atlas example.tiny --ir
```

The independent laboratory's JSON receipt must be archived verbatim, including seed and failure controls. To reproduce the full federation, apply the deterministic v0.2 patch to the exact **Compiler Design v0.1.0** predecessor, with every source hash verified. The predecessor contains 24 nodes; v0.2 must keep that count while extending only the existing Compiler Design node. Its original 54 records and 54 relations retain their exact revisions and all older 23 node manifests remain byte-identical.

### Residual risks and acceptance gates

There is no test of a native executable, assembler/linker, real ABI, C or C++ language semantics, concurrency, unspecified behavior in a real host language, adversarial compiler supply chain, or independent qualified review. Evidence is finite numerical/software consistency, not a formal universal correctness theorem. Unknown original publisher-file authenticity and off-machine durability remain explicit HOLDs. A future scoped v1 should require a separately specified target, stronger grammar/typing coverage, and reproducible software and acceptance testing, not merely a larger test count.
