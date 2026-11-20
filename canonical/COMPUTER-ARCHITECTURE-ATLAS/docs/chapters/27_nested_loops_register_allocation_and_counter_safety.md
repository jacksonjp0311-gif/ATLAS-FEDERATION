# 27. Nested counted loops and compiler-owned register allocation

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A structured counted loop requires the machine to preserve a counter that the body does not overwrite. With only four registers, a conservative allocation reserves R0 for user accumulator and R3, R2, R1 for successively nested loops. An outer loop uses R3 while the inner loop uses R2, preventing counter aliasing. The compiler refuses a fourth nesting level instead of spilling into undocumented memory or silently corrupting state.

## Technical derivation and invariants

For a loop `REPEAT n {B}`, the emitted structure is `LDI Rc,n; L: C(B); ADDI Rc,255; JNZ Rc,L`. Because addition is modulo 256, decrementing 1 by 1 produces zero, and JNZ tests register value, not flags. With 1≤n≤255 and no modification of Rc inside B, the loop body executes exactly n times. Loop expansion consumes three instruction words plus the body, not n explicit source copies, but runtime cost still scales with iteration count.

## Executable method and reproduction requirements

A nested-block parser tracks lexical frames; each END must match one REPEAT, and a block cannot be empty. The independent AST evaluator counts source operations and raises when its budget is exhausted. The AT8 engine has a separate instruction budget. Both must agree about result data, output events, and input consumption; their operation counts need not match.

## Constructed investigation

Run `SET 0; REPEAT 2; REPEAT 3; ADD 2; END; END; HALT`. The result in R0 is 12. Changing the inner repeat to 4 yields 16. With `SET 250; REPEAT 6; ADD 1; END`, R0 wraps to 0, proving byte semantics. A fourth nested loop must be rejected.

## Counterexamples, scientific limits and missing evidence

Counted-loop termination requires the stated compiler-reserved register noninterference and finite input availability. It does not imply termination for arbitrary hand-written AT8 ROM. Nested loops can exceed step budgets; no unknown runtime should be accepted without a bound.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
