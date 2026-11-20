# 34. Independent source-language semantics and bounded compilation comparisons

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

To bootstrap future tools, it is useful to carry a tiny language implementation along with a separately executable definition of what its programs mean. The AT8 v0.2 language has no hidden host file system, network operations, calls or unbounded allocation; each program consists of bounded integer operations, memory reads/writes, port events, structured counted loops and explicit halt.

## Technical derivation and invariants

The key comparison is between the AST evaluator and the compiled machine, after projecting away reserved compiler counters. Compare the source accumulator, full 256-byte memory image, output trace, input consumption and termination. It is not meaningful to compare AST statement count with hardware microtick count; they measure different abstractions. Differential testing gains strength when the implementation paths are distinct.

## Executable method and reproduction requirements

An independent oracle exhausts all 65,536 pairs of immediate 8-bit addition inputs using compiled AT8 ROM, then tests hundreds of randomly nested loop programs against both atomic and microcycle emulators. Because the compiler produces labels and assembly, an assembler bug or source binding bug can manifest as an incorrect image, trapped branch or mismatched output.

## Constructed investigation

Use the nested source program `SET 0; REPEAT 2; REPEAT 3; ADD 2; END; END; HALT` to demonstrate 12. Check inputs and outputs by a separate evaluator and compare ROM hashes. Invalid source such as `REPEAT 0`, depth four, bad port or missing terminal HALT must be rejected.

## Counterexamples, scientific limits and missing evidence

Finite experiments do not prove arbitrary compiler correctness or absence of unknown optimization bugs. This edition makes no claims about self-hosting, C/LLVM compatibility, memory management, high-level OS services or real silicon.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
