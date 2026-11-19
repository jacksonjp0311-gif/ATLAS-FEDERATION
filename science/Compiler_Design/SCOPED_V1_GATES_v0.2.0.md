# Scoped Compiler Design v1 content evidence gates (v0.2 status)

| Gate | v0.2 state | Additional evidence for scoped v1 |
|---|---|---|
| Grammar + parser | Two independent parser algorithms; finite AST agreement | Adversarial fuzzing and formal grammar conformance |
| Semantic execution | Direct AST, stack VM, typed register VM | Independent external implementation, more language constructs |
| Safety/typing | Static type and must-defined register verifier | Formalization or independent bounded model checking of transfer rules |
| Optimization | Conservative constant folding tested vs unoptimized | Broader pass-level preservation and invalid-program negative controls |
| Target backend | Portable register/stack bytecode | Explicit native/Wasm target, ABI/conformance tests if included in scope |
| Sources | Bibliographic URLs; not authenticated originals | Publisher-file edition, exact claim mapping, rights verification |
| Independent review | Not performed | Qualified external editorial and scientific assessment |
| Hardware durability | Not tested | Real hardware/failure harness and independent restore where needed |

**v0.2 is a finite software research edition only.** Advancement to scoped v1 requires meaningful technical closure; no arbitrary version increments.
