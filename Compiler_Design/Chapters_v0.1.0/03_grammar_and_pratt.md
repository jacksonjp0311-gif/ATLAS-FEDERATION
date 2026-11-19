# Chapter 03 — Parsing, binding power and ambiguous expression structure

Parsing converts a token sequence into an abstract syntax tree according to a grammar. For this edition the top level is `zero or more let NAME = expr ;` followed by exactly `return expr ; EOF`. There is no implicit semicolon or interactive expression statement. All references must be bound by a preceding `let`.

Expression grammar is implemented by a Pratt parser. Binding powers are `* / = 20`, `+ - = 10`, `== < = 5`; unary `-` binds more tightly than binary arithmetic. A left-associative binary operator with power `p` recursively parses its right operand with minimum power `p+1`. Thus `7-3-1` parses `(7-3)-1 = 3`, while `1+2*3` parses `1+(2*3) = 7`.

Conditional expressions use `if expr then expr else expr`; parentheses make nesting and precedence explicit. `if` is a pure expression, so it returns the value of *one* selected branch. Parser depth is bounded to 128 to avoid recursion exhaustion and adversarially deep token streams.

**Worked check:** Parse `return if 2<3 then 1+2*3 else 9;`. The conditional contains `<` with integer operands, true-branch `+` whose right child is `*`, and else-literal 9. No optimization is needed to establish the AST shape.

**Negative cases:** A missing `else`, unmatched `(`, a missing final `;`, two consecutive returns, or `1 < 2 < 3` whose second comparison is ill-typed must not be guessed into a valid program. Grammar design is not interchangeable with semantic type checking. A successful parser can still produce a program rejected by the type checker.
