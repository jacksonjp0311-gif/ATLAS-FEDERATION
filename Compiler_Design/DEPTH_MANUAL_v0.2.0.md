# Compiler Design Atlas — v0.1.0 scientific depth manual

Original canonical ATLAS FORGE federation · original planned domain #18

The original chapters below are a bounded *scientific reference*, not a professional compiler certification. The executed test report and independent oracle receipt are separate versioned evidence.

## Chapter 01 — Compiler correctness and semantic preservation

A compiler is a transformation between *meaningful programs*, not merely text and machine instructions. The scientific question is whether the compiled result has the intended observable behavior. For an expression program `p` with well-defined semantics, the finite, testable relation in this edition is:

`Eval_AST(p) = Eval_VM(compile(p))`

Both sides have a domain of defined inputs. The language here is *Tiny-I32*, not a subset of C, Rust, Python, LLVM IR, or WebAssembly: it includes checked 32-bit integers, variables assigned once, integer arithmetic, pure comparisons, conditional expressions, and a final integer return. Source text is restricted to ASCII identifiers and tokens. There are no arrays, pointers, functions, I/O, concurrency or mutable aliases.

An executable reconstruction has five explicit transitions: `source bytes -> token stream -> typed AST -> stack bytecode -> machine state transition`. Each transition has a negative validation test. Existence of a byte-identical produced artifact is *not* the same as semantic correctness; a deterministic compiler can consistently produce a wrong answer.

In the reference implementation, `typecheck` precedes optimization, the validator checks the bytecode's abstract stack types and initialized local slots, and the interpreter runs with an instruction bound. The oracle separately evaluates the parsed AST and independently compares host integer arithmetic for finite samples. This is software evidence on a bounded grammar, not a general proof of compiler correctness.

**Worked check:** `let x=3; return if x<5 then x*2 else x/0;` must return 6; the unreachable division traps if incorrectly hoisted or evaluated speculatively. A faulty optimizer that evaluates all branches fails. A source with `return true;` must fail static typing instead of returning `1` because Python's `bool` is an integer subclass.

**Unknowns:** Real compiler equivalence also requires handling memory, calling conventions, target arithmetic, undefined behavior and effects. They are deliberately excluded here. See CompCert documentation for an example of what machine-checked semantics-preservation proof entails.

## Chapter 02 — Lexical analysis and bounded tokenization

A lexer recognizes a sequence of tokens from raw characters. Formally, a tokenization is a partition of the accepted input into a finite sequence of nonoverlapping recognized spans plus permitted ignored spans (whitespace and `//` comments). A common reconstruction failure is accepting only a prefix and silently dropping unrecognized characters. The lexer must consume **all input characters** or reject with the first offending offset.

Tiny-I32 accepts decimal unsigned integer tokens, ASCII identifiers, reserved words `let`, `return`, `if`, `then`, `else`, `true`, `false`, parentheses, semicolon, basic arithmetic, comparison and assignment. The longest-match requirement distinguishes `==` from `=`. Lexical identifiers match `[A-Za-z_][A-Za-z_0-9]*` exactly. Unicode names are not silently normalized or accepted.

The scanner is bounded to 32,768 source characters and 4,096 emitted tokens. `Token(text, offset)` records source offsets for reproducible failure diagnostics. The EOF sentinel is explicit, preventing a parser from completing after trailing garbage. A parser that returns after the first semicolon without consuming EOF would falsely accept `return 1; return 2;`.

**Worked check:** `let rate=3; // note\n return rate*2;` tokenizes to `let rate = 3 ; return rate * 2 ; EOF`. Comments produce no semantic token. `return 1@2;` is rejected at the `@`, not reinterpreted as `return 12;`.

**Failure controls:** Unknown glyph, excessive characters, excessive token count, incomplete multi-character comparisons, and non-ASCII identifiers. This finite lexer intentionally omits strings, escapes, preprocessing, tabs-in-indentation significance, conditional compilation and macro expansion.

## Chapter 03 — Parsing, binding power and ambiguous expression structure

Parsing converts a token sequence into an abstract syntax tree according to a grammar. For this edition the top level is `zero or more let NAME = expr ;` followed by exactly `return expr ; EOF`. There is no implicit semicolon or interactive expression statement. All references must be bound by a preceding `let`.

Expression grammar is implemented by a Pratt parser. Binding powers are `* / = 20`, `+ - = 10`, `== < = 5`; unary `-` binds more tightly than binary arithmetic. A left-associative binary operator with power `p` recursively parses its right operand with minimum power `p+1`. Thus `7-3-1` parses `(7-3)-1 = 3`, while `1+2*3` parses `1+(2*3) = 7`.

Conditional expressions use `if expr then expr else expr`; parentheses make nesting and precedence explicit. `if` is a pure expression, so it returns the value of *one* selected branch. Parser depth is bounded to 128 to avoid recursion exhaustion and adversarially deep token streams.

**Worked check:** Parse `return if 2<3 then 1+2*3 else 9;`. The conditional contains `<` with integer operands, true-branch `+` whose right child is `*`, and else-literal 9. No optimization is needed to establish the AST shape.

**Negative cases:** A missing `else`, unmatched `(`, a missing final `;`, two consecutive returns, or `1 < 2 < 3` whose second comparison is ill-typed must not be guessed into a valid program. Grammar design is not interchangeable with semantic type checking. A successful parser can still produce a program rejected by the type checker.

## Chapter 04 — Typing judgments, binding and early rejection

A type checker establishes whether each syntax tree can be assigned a type under an environment Γ. This reference uses exactly two types: `i32` and `bool`. Typing is structural: `Γ ⊢ e : τ` means expression `e` is well typed as `τ` under Γ. A literal integer has type `i32` within the literal range, while `true` and `false` have type `bool`.

The addition rule is `Γ ⊢ a:i32 and Γ ⊢ b:i32 => Γ ⊢ a+b:i32`. The strict comparison rule is `Γ ⊢ a:i32 and Γ ⊢ b:i32 => Γ ⊢ a<b:bool`. Equality requires matching operand types; a conditional requires a boolean guard and equal branch types. The final `return` requires an integer.

Each `let` introduces a new named integer local after its initializer has been checked using *only earlier bindings*. This avoids accidental use before definition and simplifies the VM's definite-initialization check. Duplicate declarations are forbidden rather than shadowed. Maximum locals: 512.

**Worked check:** `let a=2; let b=a+3; return b;` is valid. `let a=a+1;return a;` is invalid because `a` is not in Γ when its initializer is checked. `return if true then 3 else false;` is invalid even though the false branch is unreachable: dead code is still type-checked before optimization.

**Boundary:** These finite typing rules are not generic type inference, ownership checking, region inference, effect types, polymorphism or C's integer-promotion rules. An untyped host language accepting booleans as integers must not leak that convenience into the target semantics.

## Chapter 05 — I32 arithmetic, division and trap semantics

Signed 32-bit integers occupy `[−2^31, 2^31−1]`. Tiny-I32 arithmetic **checks** bounds rather than wrapping modulo 2^32. `add_i32(a,b)=a+b` when the mathematical result is in range; otherwise evaluation traps. The same applies to subtraction, multiplication and negation. A compiler optimization must preserve both returned values and traps for source programs within this declared semantics.

Division uses truncation toward zero: `div_i32(a,b) = sign(a/b)*floor(|a|/|b|)` for nonzero `b`, provided the quotient is in range. Division by zero traps. In a full i32 language, dividing `−2^31` by `−1` would overflow. The literal parser in this initial version accepts unsigned tokens only through `2^31−1` and therefore does not directly represent `−2^31`; this is a documented coverage gap, not an invitation to claim full i32 literal support.

**Worked checks:** `−7 / 2 = −3`, `7 / −2 = −3`, and `(2^31−1)+1` traps. Python's `//` cannot be substituted directly for negative division because it rounds toward negative infinity: Python computes `−7//2=−4`, violating this language's definition.

**Negative controls:** Overflow during `100000*100000`, division by zero, booleans used as numbers, a positive integer token `2147483648`, and constant folding that assumes overflow can never occur. Unit tests and independent host-language arithmetic checks target these errors.

**Scope:** This is a deliberately checked arithmetic model and must not be described as the semantics of a C or LLVM native signed addition, which can involve poison or undefined behavior under particular flags and program rules.

## Chapter 06 — Intermediate representation and stack-machine code generation

An intermediate representation (IR) is useful because it separates the source grammar from the machine where instructions execute. This initial version compiles typed AST nodes to a small stack bytecode. Operations include `PUSH_I32`, `PUSH_BOOL`, `LOAD`, `STORE`, `NEG`, `ADD`, `SUB`, `MUL`, `DIV`, `LT`, `EQ`, `JMP_IF_FALSE`, `JMP`, and `RETURN`.

The code-generation invariant for an expression is: if the machine begins with a valid stack σ, its emitted code (when it terminates normally) leaves the value of the expression above σ, without changing previously held stack entries. For a binary arithmetic node, emit the left child, then the right, then an arithmetic opcode. `SUB` pops right followed by left, preserving the required operand order.

A conditional compiles to `compile(cond); JMP_IF_FALSE else; compile(yes); JMP end; else:compile(no); end:`. Conditional jumps pop exactly one boolean. The code builder patches forward offsets after branch instructions have been laid out. Backward jumps are forbidden in v0.1, making the control-flow graph acyclic.

**Worked example:** `let x=4; return if x<5 then x*2 else x/0;` emits a `STORE` for local 0, then `LOAD, PUSH_I32(5), LT, JMP_IF_FALSE, ...`. The false branch is still included unless an optimizer proves a condition constant. The VM returns 8 without touching division.

**Reconstruction:** `python -m compiler_atlas example.tiny --ir` emits canonical JSON containing declared language ID, slot names and opcode arrays. SHA-256 of the canonical bytes is a reproducibility identifier, not cryptographic proof that code is correct or safely signed.

## Chapter 07 — Control-flow analysis, abstract stack types and initialization

Executing malformed bytecode without validation can underflow the operand stack, misinterpret booleans as integers, read an uninitialized local or jump outside an instruction stream. The validator runs an abstract interpreter **before** execution. Its abstract state at each instruction is `(pc, stack_types, initialized_local_set)`; reachable states are propagated along all control-flow successors.

Transfer functions are deterministic: `PUSH_I32` appends `i32`, `ADD` consumes two `i32` and appends one `i32`, `JMP_IF_FALSE` consumes one `bool` and explores both successors, `STORE(k)` consumes one `i32` and marks local k initialized, and `RETURN` requires exactly one `i32` on the operand stack.

At a join point, incoming abstract stacks and initialized-local sets must agree in this deliberately strict v0.1 validator. This is conservative: other sound analyses may compute intersections of definitely initialized variables and a least upper bound of abstract stack states. In this language, locals are sequentially initialized outside of conditional expressions, so the strict merge rule is adequate for generated programs.

The instruction count is at most 16,384, the abstract maximum stack depth is at most 4,096, and all jump targets must be **forward** and inside the instruction stream. Forward-only control flow avoids needing a fixed-point loop analysis for this edition.

**Counterexamples rejected:** `LOAD 0` before `STORE 0`, `PUSH_BOOL; RETURN`, `PUSH_I32; PUSH_BOOL; ADD`, `JMP 0` from pc 0, and jumps beyond the last opcode. Type checking of source code is *not* a replacement for verifying a serialized or potentially corrupted bytecode artifact.

## Chapter 08 — Conservative optimization and trap-preserving transformations

An optimization is permitted only when it preserves the declared observations of all relevant executions. In Tiny-I32 those observations are either a returned checked integer or a trapped execution. Constant folding may replace `2+3*4` with `14`; it must **not** replace `2147483647+1` with an out-of-range literal or silently wrap to a negative integer.

The implementation folds a fully constant arithmetic expression only if evaluating it under the checked semantics succeeds. Otherwise the original subtree remains and the runtime raises a trap if that branch is reached. For `if true then a else b`, the optimizer first requires the *entire expression* to be well typed, then it can eliminate the unreachable branch without evaluating it. This preserves `if true then 3 else 1/0` as a defined value 3.

**Differential experiment:** Compile every seeded candidate with optimization enabled and disabled; run both; compare them against the independent AST interpreter. A result is a tuple `('value',n)` or `('trap',None)`. Compare tuples rather than silently excluding cases that trap. The first oracle includes many trapped cases explicitly.

A known negative case is speculative evaluation: replacing a conditional's result with the eager evaluation of both branches creates a division-by-zero where none existed. Another is folding division using host-language floor semantics, changing `-7/2` from `-3` to `-4`.

**Not implemented:** Loop-invariant code motion, SSA rewriting, common-subexpression elimination with memory effects, alias analysis, target instruction scheduling, interprocedural optimization and register allocation. These are appropriate next-edition tasks, not proofs delivered by v0.1.

## Chapter 09 — Executable evidence and independent finite oracles

A single implementation agreeing with itself can conceal systematic errors. This edition uses an independently written **big-step AST interpreter** as the principal oracle for code generation and stack machine execution. It does not call the compiler's VM or arithmetic helper. Its checked arithmetic uses separate formulas, and it catches independently raised zero-division and signed overflow errors.

A deterministic generator produces valid typed expression programs with sequential integer bindings, arithmetic, comparisons, nested conditional expressions and bounded depths. For each program, compute `Eval_AST`, `Run_VM(Compile_unoptimized)` and `Run_VM(Compile_optimized)`; compare results or trap classes. Additional small integer cross-products use Python arithmetic for direct external numeric comparison within the safe range.

The oracle seeds and exact comparison counts are preserved in `evidence/INDEPENDENT_ORACLE_RECEIPT_v0.1.0.json`. Tests also corrupt bytecode intentionally and require rejection, so success does not simply mean all samples returned a number. Outputs are deterministic under the stated Python interpreter version and input seed.

**Limitations:** The two execution pathways *share the parser*, and therefore this is not an independent parser oracle. The host arithmetic comparison partially reduces shared arithmetic risk but only on finite samples. There is no machine-checked semantics preservation proof, no symbolic verification of all programs and no real target instruction execution.

**Next verification step:** Introduce a separately specified parser and a second execution backend, plus bounded exhaustive program enumeration. Preserve exact receipts for both runs, report any counterexamples and resist promoting syntactic equivalence into certified security or hardware behavior.

## Chapter 10 — Deterministic compiler artifacts, provenance and restoration

Reproducibility requires identifying the *input source*, compiler edition, declared semantics, normalization, validation policy and output serialization. This reference's bytecode encoder produces sorted-key, compact UTF-8 JSON with an explicit language identity `atlas-compiler-tiny-i32/1`; the same source and flags produce the same bytes. Its SHA-256 digest is suitable for integrity checks only when the expected digest is anchored independently.

A correct federation release involves more than serializing new code. Source documents and corpus data have exact file hashes, record revisions and source relationships. The incremental patch is from the **specific Database Optimization v1.0.0** canonical predecessor, whose archive SHA-256 is `13d8f5d19ed98d052dad9c424b22295599722b82a2938ec6f94f2a95122fe8c2`.

The release process must verify that no old science data or original 30-domain queue entry was deleted, changed outside the authorized integration files, or silently reassigned a different revision. The deterministic patch is applied to the exact prior archive, a new whole-federation ZIP is reconstructed and compared byte-for-byte to the development ZIP, then the full test suite runs again in the restored source tree.

**Failure controls:** Wrong predecessor digest, missing patch member, extra member, path traversal, duplicate ZIP member, wrong uncompressed file SHA, wrong full archive SHA, malformed source-linked record revision and mismatched source/fresh test receipts. These produce `FAIL_CLOSED`; no authoritative checkpoint advances.

**External limit:** SHA-256 on its own does not authenticate the person or organization who created the archive. Cryptographic signatures, trusted keys, reproducible toolchains across different machines and physical storage reliability require separately validated components.

## Chapter 11 — From a toy compiler to real targets: LLVM, Wasm, RISC-V and CompCert

LLVM's intermediate language has SSA values and explicit control-flow blocks, but it also has nuanced semantics for poison, undef and freeze. A correct optimization must respect these semantics rather than assuming every integer arithmetic operation is pure mathematical arithmetic. For example, `nsw`-annotated addition has poison behavior when signed overflow occurs. This differs from Tiny-I32, which explicitly traps on overflow.

The WebAssembly Core Specification 3.0, released in November 2026, separates decoding, validation and execution. The Atlas validator's stack-type simulation illustrates the *shape* of this reasoning, but it validates only the educational opcode grammar and must not claim to validate actual Wasm modules. WebAssembly's stack typing, polymorphic control flow, memory and real binary format are not implemented here.

The current ratified RISC-V ISA reference is a source for eventually mapping target-independent IR to machine instructions. Real RV32I code generation must account for its actual instruction encodings, ABI, register allocation, integer arithmetic and calling conventions. A JSON stack machine is not RISC-V machine code.

CompCert demonstrates a much higher evidence bar by proving preservation of behavior for an officially specified subset of C across compilation passes using a proof assistant. Tiny-I32's finite oracle checks are **not** comparable to a proof of all compiler passes for a real language.

**Suggested scientific upgrade path:** v0.2 add a second independently executable backend and an SSA form with dominance and phi-node checks; subsequent versions add memory semantics and verified instruction selection on a bounded RISC-V subset. Avoid replacing evidence with a version label.

## Chapter 12 — Offline reconstruction, worked laboratory and known gaps

A future user needs enough information to rebuild the compiler without a cloud service: the grammar, type rules, arithmetic semantics, bytecode ISA, validator transfer functions, deterministic reference source, tests, seeded oracle, negative cases and source-provenance metadata. All software in this domain is pure Python standard library, with no network calls during execution.

**Hands-on lab:** Create a file `test.tiny` containing `let base=7; let count=4; return if count<base then base*count else base/count;`. From the domain directory run `python -m compiler_atlas test.tiny` and expect `{"value":28,"semantics":"checked-i32"}`. Run `python -m compiler_atlas test.tiny --ir`, then `python -m unittest discover -s tests -q`, then `python -m evidence.independent_oracle`. Record interpreter version, actual counts, elapsed time and any violations. A failed test must remain a failed receipt until corrected and independently rerun.

**Reconstruction exercise:** Implement your own parser from the precedence table without importing `compiler_atlas.core.parse`. Generate bytecode using the provided instruction table, then independently execute test cases. Compare not only values but also traps and error categories. Start with arithmetic precedence and sequential bindings, then conditional control flow, then deliberately malformed bytecode and misaligned jump targets.

**Boundary checklist:** Not a complete C compiler, no native assembler or linker, no object format, no executable file loader, no hardware ABI, no memory model, no macros, no loops, no function calls, no security guarantee, no independent expert validation and no primary-source bytes authenticated. Any future version claiming those must add source coverage and executable evidence rather than relying on this edition's tests.


## Chapter 13 — Independent parsing and unambiguous precedence

### What is being verified

The original v0.1 compiler uses a Pratt parser with numeric binding powers. A parser bug can silently change an expression's structure and produce a plausibly typed but incorrect program, which bytecode-vs-AST testing will not detect if the reference interpreter consumes the *same incorrect AST*. Edition v0.2 therefore adds an independently implemented **recursive-descent grammar**. It shares the lexer and data model, but it does not invoke the Pratt parser or copy its precedence loop. This separation catches a class of misbindings and keyword-termination errors that the first edition's AST-vs-bytecode oracle cannot.

### Grammar and precedence

A simplified interpretation of the accepted language is:

```
program := ("let" identifier "=" E ";")* "return" E ";" EOF
E       := C
C       := A (("<" | "==") A)*
A       := M (("+" | "-") M)*
M       := P (("*" | "/") P)*
P       := "-" P | "(" E ")" | "if" E "then" E "else" E
         | INT32 | "true" | "false" | identifier
```

Every repetition is **left associative**; the precedence hierarchy is comparison (lowest), addition/subtraction, multiplication/division and unary negation (highest). The `if` prefix parses its condition to the `then` delimiter and the selected branch to the `else` delimiter. Its use as a primary expression allows a parent comparison to consume a complete conditional. Conditional branches must be identically typed by the separate typing pass.

For example, `1+2*3` must parse as `1+(2*3)`, but `(1+2)*3` must produce `(1+2)*3`. The structurally unequal trees are a scientifically meaningful distinction, even if they happen to agree for a particular input. A nested expression such as `return (if 3<4 then 7 else 1/0)+2;` must preserve the branch semantics: the unselected `1/0` cannot trap.

### Independent oracle and failure controls

Each generated program is parsed twice. Both parsers must return **structurally equal immutable AST dataclasses** before either backend is allowed to run. The strict comparison includes operator kind, operand order, conditional branch structure, literal type and ordered variable bindings. Deliberately malformed expressions must be rejected by both parsers. The independent parser has explicit token, expression and prefix-depth budgets.

### Limits and reconstructibility

The two parsers share one tokenizer, AST shape and lexical grammar, so their agreement cannot establish complete lexical correctness or absence of shared specification bugs. Rebuild from the grammar table and independently implement every precedence level. Expand future validation to external parsing engines, more elaborate language features, adversarial fuzzing, and formal grammar properties before claiming production-grade language acceptance.


## Chapter 14 — Typed three-address register intermediate representation

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


## Chapter 15 — Definite assignment across control-flow joins

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


## Chapter 16 — Differential compiler laboratory, negative controls and preservation

### Experimental design

A scientific compiler reference should distinguish a passing example from a tested semantic relation. Version 0.2 uses **four** execution paths and **two** parser algorithms under a declared source semantics: direct AST big-step evaluation; optimized and unoptimized stack-machine execution; optimized and unoptimized typed-register execution. A generated source program is evaluated under both parser implementations to compare exact AST structure, then all executable pathways are checked against the independent big-step result. The laboratory records the random seed, program count, semantic comparisons, expected traps, malformed grammar rejects and invalid-register rejects.

The methods are intentionally nonidentical: the Pratt parser and recursive parser differ; the stack VM and register VM have different instruction representations and validation. However they still share some code, data and semantics. In particular, arithmetic operations use the same declared checked i32 model. A correlated bug in the common language specification can therefore evade every finite comparison.

### Valid comparison cases

Generated programs contain nested conditionals, integer arithmetic, variable binding and branch-specific divisions; in some cases correct behavior is an arithmetic **trap**, not a number. The checker compares outcome categories and numbers. Deliberately bad IR cases must be rejected rather than counted as extra successful executions. A malformed grammar must independently fail both parsing algorithms. Identical output for a single input is not evidence of universal compiler soundness.

### Reproducible commands

```sh
python -m unittest discover -s tests -q
python -m evidence.independent_oracle
python -m evidence.independent_oracle_v02
python -m compiler_atlas example.tiny --ir
```

The independent laboratory's JSON receipt must be archived verbatim, including seed and failure controls. To reproduce the full federation, apply the deterministic v0.2 patch to the exact **Compiler Design v0.1.0** predecessor, with every source hash verified. The predecessor contains 24 nodes; v0.2 must keep that count while extending only the existing Compiler Design node. Its original 54 records and 54 relations retain their exact revisions and all older 23 node manifests remain byte-identical.

### Residual risks and acceptance gates

There is no test of a native executable, assembler/linker, real ABI, C or C++ language semantics, concurrency, unspecified behavior in a real host language, adversarial compiler supply chain, or independent qualified review. Evidence is finite numerical/software consistency, not a formal universal correctness theorem. Unknown original publisher-file authenticity and off-machine durability remain explicit HOLDs. A future scoped v1 should require a separately specified target, stronger grammar/typing coverage, and reproducible software and acceptance testing, not merely a larger test count.
