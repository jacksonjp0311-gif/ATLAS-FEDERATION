# Investigation 20: Token alignment versus communicative adequacy

**Origin:** constructed offline study unless otherwise stated. No human participant or original media data was acquired.

A wholly authored reference sequence “i like cats” and a hypothesis “i adore cats” differ by one substitution under unit-cost token editing. The method returns the full edit-operation witness and reports a reference-normalized rate of 1/3. That is a mathematical statement about **these tokens**, not about whether the utterance preserves the original intention. Changing a tokenizer, removing case, merging compounds, or using grapheme units changes the result.

**Counterfactual:** when the reference is empty, a nonempty hypothesis has insertion distance greater than zero, but WER's denominator is zero; report the normalized rate as undefined, not 0 or infinity claimed as a statistical estimate. Multiple optimal alignments can exist and one traceback is not a unique linguistic analysis.

**Reproduction:** `python -m language_atlas advanced-casebook`, then `aligned_edit_distance` and the associated unit tests. Do not replace a bilingual speaker's adequacy judgment with edit distance.

**Evidence status:** This is a reproducible bounded algorithm/method example. Human-language validity and independent review are not established.
