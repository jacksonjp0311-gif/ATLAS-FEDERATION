# Chapter 02 — Lexical analysis and bounded tokenization

A lexer recognizes a sequence of tokens from raw characters. Formally, a tokenization is a partition of the accepted input into a finite sequence of nonoverlapping recognized spans plus permitted ignored spans (whitespace and `//` comments). A common reconstruction failure is accepting only a prefix and silently dropping unrecognized characters. The lexer must consume **all input characters** or reject with the first offending offset.

Tiny-I32 accepts decimal unsigned integer tokens, ASCII identifiers, reserved words `let`, `return`, `if`, `then`, `else`, `true`, `false`, parentheses, semicolon, basic arithmetic, comparison and assignment. The longest-match requirement distinguishes `==` from `=`. Lexical identifiers match `[A-Za-z_][A-Za-z_0-9]*` exactly. Unicode names are not silently normalized or accepted.

The scanner is bounded to 32,768 source characters and 4,096 emitted tokens. `Token(text, offset)` records source offsets for reproducible failure diagnostics. The EOF sentinel is explicit, preventing a parser from completing after trailing garbage. A parser that returns after the first semicolon without consuming EOF would falsely accept `return 1; return 2;`.

**Worked check:** `let rate=3; // note\n return rate*2;` tokenizes to `let rate = 3 ; return rate * 2 ; EOF`. Comments produce no semantic token. `return 1@2;` is rejected at the `@`, not reinterpreted as `return 12;`.

**Failure controls:** Unknown glyph, excessive characters, excessive token count, incomplete multi-character comparisons, and non-ASCII identifiers. This finite lexer intentionally omits strings, escapes, preprocessing, tabs-in-indentation significance, conditional compilation and macro expansion.
