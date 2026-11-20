# Chapter 04 — Typing judgments, binding and early rejection

A type checker establishes whether each syntax tree can be assigned a type under an environment Γ. This reference uses exactly two types: `i32` and `bool`. Typing is structural: `Γ ⊢ e : τ` means expression `e` is well typed as `τ` under Γ. A literal integer has type `i32` within the literal range, while `true` and `false` have type `bool`.

The addition rule is `Γ ⊢ a:i32 and Γ ⊢ b:i32 => Γ ⊢ a+b:i32`. The strict comparison rule is `Γ ⊢ a:i32 and Γ ⊢ b:i32 => Γ ⊢ a<b:bool`. Equality requires matching operand types; a conditional requires a boolean guard and equal branch types. The final `return` requires an integer.

Each `let` introduces a new named integer local after its initializer has been checked using *only earlier bindings*. This avoids accidental use before definition and simplifies the VM's definite-initialization check. Duplicate declarations are forbidden rather than shadowed. Maximum locals: 512.

**Worked check:** `let a=2; let b=a+3; return b;` is valid. `let a=a+1;return a;` is invalid because `a` is not in Γ when its initializer is checked. `return if true then 3 else false;` is invalid even though the false branch is unreachable: dead code is still type-checked before optimization.

**Boundary:** These finite typing rules are not generic type inference, ownership checking, region inference, effect types, polymorphism or C's integer-promotion rules. An untyped host language accepting booleans as integers must not leak that convenience into the target semantics.
