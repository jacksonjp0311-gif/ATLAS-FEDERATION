# Chapter 01 — Compiler correctness and semantic preservation

A compiler is a transformation between *meaningful programs*, not merely text and machine instructions. The scientific question is whether the compiled result has the intended observable behavior. For an expression program `p` with well-defined semantics, the finite, testable relation in this edition is:

`Eval_AST(p) = Eval_VM(compile(p))`

Both sides have a domain of defined inputs. The language here is *Tiny-I32*, not a subset of C, Rust, Python, LLVM IR, or WebAssembly: it includes checked 32-bit integers, variables assigned once, integer arithmetic, pure comparisons, conditional expressions, and a final integer return. Source text is restricted to ASCII identifiers and tokens. There are no arrays, pointers, functions, I/O, concurrency or mutable aliases.

An executable reconstruction has five explicit transitions: `source bytes -> token stream -> typed AST -> stack bytecode -> machine state transition`. Each transition has a negative validation test. Existence of a byte-identical produced artifact is *not* the same as semantic correctness; a deterministic compiler can consistently produce a wrong answer.

In the reference implementation, `typecheck` precedes optimization, the validator checks the bytecode's abstract stack types and initialized local slots, and the interpreter runs with an instruction bound. The oracle separately evaluates the parsed AST and independently compares host integer arithmetic for finite samples. This is software evidence on a bounded grammar, not a general proof of compiler correctness.

**Worked check:** `let x=3; return if x<5 then x*2 else x/0;` must return 6; the unreachable division traps if incorrectly hoisted or evaluated speculatively. A faulty optimizer that evaluates all branches fails. A source with `return true;` must fail static typing instead of returning `1` because Python's `bool` is an integer subclass.

**Unknowns:** Real compiler equivalence also requires handling memory, calling conventions, target arithmetic, undefined behavior and effects. They are deliberately excluded here. See CompCert documentation for an example of what machine-checked semantics-preservation proof entails.
