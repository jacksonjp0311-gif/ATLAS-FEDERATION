# Chapter 05 — I32 arithmetic, division and trap semantics

Signed 32-bit integers occupy `[−2^31, 2^31−1]`. Tiny-I32 arithmetic **checks** bounds rather than wrapping modulo 2^32. `add_i32(a,b)=a+b` when the mathematical result is in range; otherwise evaluation traps. The same applies to subtraction, multiplication and negation. A compiler optimization must preserve both returned values and traps for source programs within this declared semantics.

Division uses truncation toward zero: `div_i32(a,b) = sign(a/b)*floor(|a|/|b|)` for nonzero `b`, provided the quotient is in range. Division by zero traps. In a full i32 language, dividing `−2^31` by `−1` would overflow. The literal parser in this initial version accepts unsigned tokens only through `2^31−1` and therefore does not directly represent `−2^31`; this is a documented coverage gap, not an invitation to claim full i32 literal support.

**Worked checks:** `−7 / 2 = −3`, `7 / −2 = −3`, and `(2^31−1)+1` traps. Python's `//` cannot be substituted directly for negative division because it rounds toward negative infinity: Python computes `−7//2=−4`, violating this language's definition.

**Negative controls:** Overflow during `100000*100000`, division by zero, booleans used as numbers, a positive integer token `2147483648`, and constant folding that assumes overflow can never occur. Unit tests and independent host-language arithmetic checks target these errors.

**Scope:** This is a deliberately checked arithmetic model and must not be described as the semantics of a C or LLVM native signed addition, which can involve poison or undefined behavior under particular flags and program rules.
