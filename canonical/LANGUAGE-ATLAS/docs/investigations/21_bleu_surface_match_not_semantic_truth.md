# Investigation 21: BLEU scores are not semantic correctness

**Origin:** constructed offline study unless otherwise stated. No human participant or original media data was acquired.

The constructed candidate/reference pair “we study language” matches exactly, so unsmoothed BLEU3 computes 1.0. That is not proof the translation is factually accurate or appropriate: a faulty reference produces the same number. A second toy pair has zero n-gram overlap and an exact zero score. These cases demonstrate explicit arithmetic, not a translation system.

**Adversarial case:** calculate BLEU4 on a sentence with fewer than four tokens. Unsmoothed precision at order four has no observed candidate n-grams and is defined here as zero, driving this implementation's geometric score to zero. A different smoothing convention would give a different value.

**Research requirement:** preserve original tokenization, Unicode normalization, case, references, evaluator version, domain, and human judgments. The implementation is **not SacreBLEU** and carries no comparability signature. Compare with the official WMT 2018 reporting cautions.

**Evidence status:** This is a reproducible bounded algorithm/method example. Human-language validity and independent review are not established.
