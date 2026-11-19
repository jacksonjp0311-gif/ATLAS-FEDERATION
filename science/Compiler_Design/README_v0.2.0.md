# Compiler Design Atlas — v0.1.0

**Original ATLAS FORGE scientific federation · Original 30-domain priority #18**

This is the *first substantive release edition* of Compiler Design, not scoped v1 acceptance. It extends the exact 23-node Database Optimization v1.0.0 federation without replacing previous records, tests, archives, or the 30-domain roadmap.

## Purpose and scientific scope

An offline, executable reference for a typed, checked-I32 expression compiler with explicit lexical rules, Pratt parsing, static type judgments, conservative constant folding, bytecode generation, abstract stack/CFG validation, a bounded machine interpreter and independently formulated finite comparison oracles. Twelve original technical chapters describe assumptions, derivations, worked examples, negative controls, and realistic reconstruction limits.

## Rebuild and run offline

Requires Python 3.11+ standard library only.

```sh
python -m compiler_atlas example.tiny
python -m compiler_atlas example.tiny --ir
python -m unittest discover -s tests -q
python -m evidence.independent_oracle
```

Expected example value is `28`. The oracle returns actual finite comparison counts and any negative-control failures. The emitted JSON stack bytecode is not executable native machine code and must not be described as RISC-V, LLVM or Wasm compatible.

The federation release uses the exact original common Atlas contract and stores the source, JSONL records with immutable revisions, cross-node exact-revision dependencies, test suite, independent oracle receipt, bibliography pointer cards and full release restoration proofs.

## Current acceptance

Software correctness checks pass for a **bounded finite corpus**, not all programs. No user desktop deployment, external expert scientific review, publisher-original authentication, native architecture target, hardware measurement, or compiler-proof certificate has occurred. Next edition will aim at substantially independent parsing and a second code generation target; do not force v1 before completing scoped requirements.

## Navigation

- `docs/DEPTH_MANUAL_v0.1.0.md` original 12-chapter scientific reference
- `docs/EXACT_PREDECESSOR_LINKS_v0.1.0.json` exact resolved dependencies to the prior 23-node Atlas
- `data/` shared contract's immutable qualified records and typed revision links
- `compiler_atlas/core.py` reference lexer, AST, type checker, optimizer, bytecode and VM
- `tests/test_core.py` negative controls and executable cases
- `evidence/independent_oracle.py` separate AST big-step semantics and arithmetic oracle
- `docs/SCOPED_V1_GATES_v0.1.0.md` objective version evolution and pending hold requirements


## Current edition v0.2.0

The complete original v0.1.0 chapter set remains byte-identical and is preserved under the canonical release chain. Added four substantive chapters, a second typed register backend with a distinct validator, an independent recursive parser, and a seeded differential laboratory. Run `python -m unittest discover -s tests -q` and `python -m evidence.independent_oracle_v02`. This is not scoped scientific v1, a native target compiler, or a formal proof.
