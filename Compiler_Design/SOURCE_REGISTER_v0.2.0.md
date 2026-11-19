# Original Compiler Design v0.1.0 — source registry

These are official bibliographic pointers only, not a deposit of authenticated original publisher bytes. The explanatory chapters are original AI-assisted educational prose and do not reproduce the protected standards.

1. [LLVM Language Reference Manual](https://llvm.org/docs/LangRef.html): SSA, poison, undef, freeze. The reference implements none of LLVM IR's poison semantics.
2. [W3C WebAssembly Core Specification 3.0](https://www.w3.org/TR/wasm-core/), Candidate Recommendation Draft 16 November 2026: decoding, validation, execution and stack typing. Not a Wasm binary implementation.
3. [CompCert 3.18 commented Coq development](https://compcert.org/doc/), 31 August 2026: a verified compiler and preservation proof architecture. The Atlas finite oracle is not a formal proof.
4. [RISC-V Ratified Specifications Library](https://docs.riscv.org/), Unprivileged ISA release 2026-01-20: reference for eventual machine-code targets. Not executed or generated in v0.1.
5. [Python 3 Lexical Analysis](https://docs.python.org/3/reference/lexical_analysis.html): comparative tokenizer source, not a language-grammar assertion for Tiny-I32.

Verification label: bibliographic pointer checked as a public page, original publisher bytes unauthenticated, independent review unperformed. Do not mark the original document as locally preserved.


## v0.2 addition: compiler design practice and CFG semantics

- LLVM project. *Kaleidoscope: Implementing a Language with LLVM, Chapter 3 — Code Generation.* https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl03.html — external pedagogical pointer for AST, IR and code-generation architecture; original publisher bytes **not authenticated** here. The reference register machine is independently authored and does not implement LLVM IR.
- LLVM Language Reference https://llvm.org/docs/LangRef.html — reused v0.1 bibliographic source for understanding real IR semantics; the atlas does **not** inherit LLVM validation or certification.

The original source register and every historical source revision are retained verbatim.
