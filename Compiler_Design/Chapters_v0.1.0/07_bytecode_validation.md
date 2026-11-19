# Chapter 07 — Control-flow analysis, abstract stack types and initialization

Executing malformed bytecode without validation can underflow the operand stack, misinterpret booleans as integers, read an uninitialized local or jump outside an instruction stream. The validator runs an abstract interpreter **before** execution. Its abstract state at each instruction is `(pc, stack_types, initialized_local_set)`; reachable states are propagated along all control-flow successors.

Transfer functions are deterministic: `PUSH_I32` appends `i32`, `ADD` consumes two `i32` and appends one `i32`, `JMP_IF_FALSE` consumes one `bool` and explores both successors, `STORE(k)` consumes one `i32` and marks local k initialized, and `RETURN` requires exactly one `i32` on the operand stack.

At a join point, incoming abstract stacks and initialized-local sets must agree in this deliberately strict v0.1 validator. This is conservative: other sound analyses may compute intersections of definitely initialized variables and a least upper bound of abstract stack states. In this language, locals are sequentially initialized outside of conditional expressions, so the strict merge rule is adequate for generated programs.

The instruction count is at most 16,384, the abstract maximum stack depth is at most 4,096, and all jump targets must be **forward** and inside the instruction stream. Forward-only control flow avoids needing a fixed-point loop analysis for this edition.

**Counterexamples rejected:** `LOAD 0` before `STORE 0`, `PUSH_BOOL; RETURN`, `PUSH_I32; PUSH_BOOL; ADD`, `JMP 0` from pc 0, and jumps beyond the last opcode. Type checking of source code is *not* a replacement for verifying a serialized or potentially corrupted bytecode artifact.
