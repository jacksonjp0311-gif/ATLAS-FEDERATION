# Investigation 31 — Finite acceptance does not establish natural-language grammar

**Origin:** constructed automaton. States A,B,C have transitions A—x→B and B—y→C; C accepts. Input [x,y] is accepted while [y,x] is rejected. Add an ε-transition A→B and [y] becomes accepted without consuming an extra token. The closure algorithm terminates on epsilon cycles because visited states are finite.

The result is a mathematical membership statement **only for the supplied transition system**. It does not determine whether either string is meaningful or grammatical in any human language. Preserve the symbol inventory, transition IDs, state set, original source and tested input when extending this exercise. **Negative control:** reject an undefined target state or repeated transition rather than guessing.

Run `python -m language_atlas v1-casebook`, then inspect the trace of reachable states. No speaker, corpus or model was evaluated.
