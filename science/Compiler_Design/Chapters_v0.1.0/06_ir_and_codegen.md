# Chapter 06 — Intermediate representation and stack-machine code generation

An intermediate representation (IR) is useful because it separates the source grammar from the machine where instructions execute. This initial version compiles typed AST nodes to a small stack bytecode. Operations include `PUSH_I32`, `PUSH_BOOL`, `LOAD`, `STORE`, `NEG`, `ADD`, `SUB`, `MUL`, `DIV`, `LT`, `EQ`, `JMP_IF_FALSE`, `JMP`, and `RETURN`.

The code-generation invariant for an expression is: if the machine begins with a valid stack σ, its emitted code (when it terminates normally) leaves the value of the expression above σ, without changing previously held stack entries. For a binary arithmetic node, emit the left child, then the right, then an arithmetic opcode. `SUB` pops right followed by left, preserving the required operand order.

A conditional compiles to `compile(cond); JMP_IF_FALSE else; compile(yes); JMP end; else:compile(no); end:`. Conditional jumps pop exactly one boolean. The code builder patches forward offsets after branch instructions have been laid out. Backward jumps are forbidden in v0.1, making the control-flow graph acyclic.

**Worked example:** `let x=4; return if x<5 then x*2 else x/0;` emits a `STORE` for local 0, then `LOAD, PUSH_I32(5), LT, JMP_IF_FALSE, ...`. The false branch is still included unless an optimizer proves a condition constant. The VM returns 8 without touching division.

**Reconstruction:** `python -m compiler_atlas example.tiny --ir` emits canonical JSON containing declared language ID, slot names and opcode arrays. SHA-256 of the canonical bytes is a reproducibility identifier, not cryptographic proof that code is correct or safely signed.
