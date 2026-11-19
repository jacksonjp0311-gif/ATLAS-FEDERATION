# Chapter 14 — Typed three-address register intermediate representation

### Why a second backend matters

The v0.1 compiler lowers AST expressions to a typed **stack machine**. A defect in stack-machine code generation, stack verification or runtime may survive comparison with a second execution path that shares the same stack instructions. Version 0.2 adds a genuinely different execution substrate: a typed **register machine**. Every instruction names its output and input registers, and control-flow branch destinations are explicit program counters. All registers are program-local. There are no pointers, memory effects, system calls or hidden I/O.

The register IR is not LLVM IR or machine ISA code. It is a small typed three-address language with `CONST_I32`, `CONST_BOOL`, `LOAD_LOCAL`, `STORE_LOCAL`, `NEG`, `ADD`, `SUB`, `MUL`, `DIV`, `LT`, `EQ`, `COPY`, `BR_FALSE`, `JUMP`, and `RETURN`. Integer operations share the specified checked-i32 trap semantics, and integer division truncates toward zero, including the signed-min/-1 overflow case. The IR remains within explicit instruction, register and local-slot budgets.

### Worked lowering

Consider:

```
let n=9;
return if n<5 then n+2 else n/3;
```

The compiler allocates a local slot for `n`, emits a constant register and `STORE_LOCAL`, then creates a register for `LOAD_LOCAL n`, another for `CONST_I32 5`, and an `LT` result of static type `bool`. A `BR_FALSE` jumps to the else block. The then block computes `n+2` and moves it into a join register, then jumps forward to the end. The else block computes `n/3`, moves it into the same typed join register, and falls through to `RETURN join`. Only one branch executes, so any trap in the unselected branch has no observable effect.

### Semantic relation

For every tested well-typed source `p` under the specified finite semantics,

\[
\operatorname{Outcome}(\operatorname{AST}(p))
=\operatorname{Outcome}(\operatorname{StackVM}(C_s(p)))
=\operatorname{Outcome}(\operatorname{RegVM}(C_r(p))).
\]

`Outcome` includes an exact integer or the category of a checked-arithmetic trap. This is an **experimentally tested relation**, not a universal theorem. Optimization is tested separately with `optimized=False` and `optimized=True`. In particular, constant folding must not erase a trap on the taken path, and conditional elimination must not evaluate the unselected path.

### Provenance, serialization and limits

The register format is deterministic canonical UTF-8 JSON tagged `atlas-compiler-typed-registers/1`; SHA-256 is an integrity identifier for fixed input and compiler version, not authentication of its author. The second backend avoids using stack opcodes, but both backends still share the source parser and arithmetic specification. Disassemblers, native ABI, instruction selection, register allocation to real CPU registers, and toolchain interoperability are **not** implemented.
