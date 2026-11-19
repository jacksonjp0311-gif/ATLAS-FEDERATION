# Chapter 15 — Definite assignment across control-flow joins

### Failure model and static safety objective

A register-machine program is not safe to execute merely because its control-flow targets lie inside the instruction array. A malicious or corrupted instruction stream can read a register or local before initialization, use the wrong operand type, jump backward into an unintended loop, duplicate a definition along one reachable path, or reach a return of the wrong type. These errors are **statically checkable** for the educational IR, before running it.

### Forward abstract interpretation

Each program point `pc` has an incoming abstract state `(D_R, D_L)`: sets of definitely initialized registers and local slots. The entry state is `(∅,∅)`. Each instruction checks operand types and that all reads are defined, then produces an outgoing state by inserting its write destinations. Across alternative incoming edges, *must-definite* information merges by **intersection**:

\[
D_R^{\mathrm{in}}(v)=\bigcap_{u\in\mathrm{Pred}(v)}D_R^{\mathrm{out}}(u),\qquad
D_L^{\mathrm{in}}(v)=\bigcap_{u\in\mathrm{Pred}(v)}D_L^{\mathrm{out}}(u).
\]

A register is safe to read at a join only when it belongs to **every** incoming predecessor state, not merely one. The implementation performs a finite worklist iteration; a changed intersection triggers reanalysis. Forward-only branch targets make the reference CFG acyclic, but the worklist formulation also explains the general dataflow technique.

### Negative-control counterexample

```
0: CONST_BOOL r0, true
1: BR_FALSE r0, 3
2: CONST_I32 r1, 12
3: RETURN r1
```

Register `r1` is initialized on the fallthrough edge but **not** on the branch edge. A validator that checks only one execution path could accept this program. The v0.2 must-def analysis rejects it, even though the concrete constant condition happens to select the initialized path in this one run. This conservative rejection is appropriate for static verification under unknown inputs.

### Types and limitations

A successful verifier pass establishes only an internal property of the finite educational register IR under its own opcode transfer functions. The verifier does not establish safety of actual machine code, absence of side channels, race freedom, memory isolation, stack protection, or resilience to arbitrary host-process corruption. The backend is deterministic and single-threaded and performs no external I/O. Subsequent work should add block-structured SSA, dominance checks, formal proof obligations and memory operations with explicit aliasing semantics before stronger correctness claims.
