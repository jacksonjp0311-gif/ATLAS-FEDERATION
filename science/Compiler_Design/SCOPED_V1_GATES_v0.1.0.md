# Compiler Design — original-domain content v1 acceptance gates

**The current edition is v0.1.0. Not v1.0.** Accept a version increase only after substantive scientific software or verification improvements, never because a fixed version count has elapsed.

| Capability | v0.1 evidence | Remaining gap |
|---|---|---|
| Tokenization and parsing | Bounded finite lexer, Pratt AST, offsets, malformed-token negatives | Independent parser oracle, complete grammar error corpus |
| Type and scope judgment | Static `i32`/`bool` and sequential locals, negative cases | Formal progress/preservation proof or stronger independent model |
| Semantics and arithmetic | Checked i32 and truncation-to-zero division | Full `-2^31` literal, structured memory/effects |
| Code generation | Deterministic stack bytecode, branch linking | Second backend and target ISA instruction validation |
| Optimization | Conservative constant folding and branch elimination | SSA, dominance, phi, alias/effects proof obligations |
| Bytecode validation | Forward CFG typed abstract stack and initialized slots | Fixed-point dataflow for loops and arbitrary merges |
| Differential evidence | Finite seeded AST vs optimized/unoptimized VM plus independent host arithmetic | Independent grammar, exhaustive bounded enumerations, fault injection |
| Artifact reproducibility | Canonical IR JSON + SHA256 | Multi-host independent toolchain byte replay |
| Federation exact identity | Exact old record dependencies and full regression receipt | Fresh complete restoration + Library readback for every edition |
| Real compiler interoperability | **Not implemented** | Certified C/LLVM/Wasm/RV target, ABI and safety checks |
| Independent scientific acceptance | **HOLD** | Original standard files, qualified expert verification, independent replication |

No Bitwork routing, desktop transfer, native compiler certification, or production security acceptance is implied by the software checks.
