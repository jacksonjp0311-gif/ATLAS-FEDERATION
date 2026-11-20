# Investigation 32 — The same sentence has two scope conditions

**Origin:** hypothetical relation table with agents Ada, Bea and objects X,Y. Known true facts are (Ada,X), (Bea,Y); known false are cross pairs. For `∀agent∃object`, each agent has a witness, so the result is true. For `∃object∀agent`, there is no object shared by all, so the result is false.

Remove one negative fact from the table and a result may become **unknown**, not false, because the model operates under open-world three-valued semantics. A real speaker's intended quantifier reading cannot be inferred from this table. Preserve both formulas and the sentence's discourse context; do not silently select one reading.

The code has complete synthetic input with no real people or language judgments. The result is repeatable propositional/quantifier arithmetic, not a claim about cognition.
