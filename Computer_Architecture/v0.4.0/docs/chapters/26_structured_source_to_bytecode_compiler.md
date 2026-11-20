# 26. A bounded structured-language compiler from source to AT8 ROM

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

AT8 already has a label-capable assembler. The next reconstruction tier is a source language that captures intent without asking a human to manage every jump. It has SET, ADD, XOR, AND, OR, LOAD, STORE, IN, OUT, REPEAT/END and terminal HALT. Every statement requires declared byte-sized operands or ports. The parser builds an immutable abstract syntax tree rather than directly emitting bytes while reading text.

## Technical derivation and invariants

Let ⟦S⟧ be the reference source interpreter state transformation and C(S) the compiler output. The desirable finite property is `project(Exec_AT8(C(S),I)) == ⟦S⟧(I)`, where project selects R0, RAM, output stream, consumed input cursors and halting status, excluding compiler-private counter registers. This property is tested, not universally proved for all arbitrary source texts. The source language is purposefully finite, with ROM≤256 bytes and exact integer inputs.

## Executable method and reproduction requirements

`parse_source` rejects malformed blocks, missing terminal HALT, out-of-range ports/bytes, early halt and loop nesting deeper than three. `compile_source` produces assembler instructions and calls the already-preserved AT8 assembler; `evaluate_source` interprets the AST without compiling. A separate test compares final state with both atomic and four-stage execution engines. Each evaluator has a bounded execution budget.

## Constructed investigation

Source: `SET 5; ADD 7; STORE 4; XOR 3; OUT 0; HALT`. The AST reference obtains stored 12, output 15; the AT8 ROM obtained through the compiler must do the same. A compiler that mistakenly maps `SET` to ADDI would fail this test and the exhaustive addition comparisons.

## Counterexamples, scientific limits and missing evidence

This is a small original educational compiler, not a C/LLVM replacement or complete high-level programming language. It lacks variables beyond R0, subroutines, relocation, debugging symbols and standard libraries. Source SHA-256 is identity/provenance, not proof that code is safe or externally authored.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
