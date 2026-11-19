# Chapter 09 — Executable evidence and independent finite oracles

A single implementation agreeing with itself can conceal systematic errors. This edition uses an independently written **big-step AST interpreter** as the principal oracle for code generation and stack machine execution. It does not call the compiler's VM or arithmetic helper. Its checked arithmetic uses separate formulas, and it catches independently raised zero-division and signed overflow errors.

A deterministic generator produces valid typed expression programs with sequential integer bindings, arithmetic, comparisons, nested conditional expressions and bounded depths. For each program, compute `Eval_AST`, `Run_VM(Compile_unoptimized)` and `Run_VM(Compile_optimized)`; compare results or trap classes. Additional small integer cross-products use Python arithmetic for direct external numeric comparison within the safe range.

The oracle seeds and exact comparison counts are preserved in `evidence/INDEPENDENT_ORACLE_RECEIPT_v0.1.0.json`. Tests also corrupt bytecode intentionally and require rejection, so success does not simply mean all samples returned a number. Outputs are deterministic under the stated Python interpreter version and input seed.

**Limitations:** The two execution pathways *share the parser*, and therefore this is not an independent parser oracle. The host arithmetic comparison partially reduces shared arithmetic risk but only on finite samples. There is no machine-checked semantics preservation proof, no symbolic verification of all programs and no real target instruction execution.

**Next verification step:** Introduce a separately specified parser and a second execution backend, plus bounded exhaustive program enumeration. Preserve exact receipts for both runs, report any counterexamples and resist promoting syntactic equivalence into certified security or hardware behavior.
