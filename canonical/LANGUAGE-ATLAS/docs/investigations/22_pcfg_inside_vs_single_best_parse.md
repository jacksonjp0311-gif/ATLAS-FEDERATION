# Investigation 22: Inside mass versus maximum derivation

**Origin:** constructed offline study unless otherwise stated. No human participant or original media data was acquired.

A toy grammar assigns N→birds and V→sing probability one and S→N V probability one. Its inside probability for “birds sing” is exactly one. Replace “sing” with an unlisted word and the grammar assigns probability zero. That means it is *unlicensed by this tiny grammar*, not impossible in a human language.

**Ambiguity test:** two alternative binary derivations of the same two-token sentence receive weights p and 1−p. Inside probability sums to one, while the single highest-probability derivation has probability max(p,1−p). Returning one tree without total mass conceals competing analyses.

**Limit:** this code handles only small CNF grammars, normalized per nonterminal, no epsilon/unary rules or learned probabilities. True syntax, semantics and speaker acceptance require independent data.

**Evidence status:** This is a reproducible bounded algorithm/method example. Human-language validity and independent review are not established.
