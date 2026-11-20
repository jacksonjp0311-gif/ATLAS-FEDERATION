# Chapter 13 — Independent parsing and unambiguous precedence

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
