# 60. Translation evaluation: character overlap is not meaning

Machine-translation evaluation can quantify certain surface correspondences between a candidate translation and reference text. BLEU uses n-gram precision and a brevity penalty under specific tokenization and reference rules. chrF considers character n-gram precision and recall. Both metrics can be useful for comparisons on declared datasets, but neither proves semantic adequacy, cultural appropriateness, factual correctness, safety, register or speaker acceptance. A source report without tokenization and metric configuration is often not reproducible.

## Reconstruction

The v1 `bounded_character_ngram_overlap` computes a simple illustrative Fβ based on Unicode *code-point* n-grams, with precision and recall averaged across available orders. It does **not** reproduce a specific official chrF, chrF++ or SacreBLEU configuration. Declare maximum n-gram order, beta, normalization, case folding, whitespace handling, reference set and sentence/corpus aggregation. For candidate and reference identical under the same representation, overlap is 1 for available n-gram orders. The decomposed `café` and composed `café` show how normalization changes scores despite similar perceived spelling.

The original chrF paper by Popović (WMT 2015) provides scientific motivation for character n-gram overlap. The v1 implementation is intentionally bounded and independent, with explicit differences from published metric packages. Do not publish its score as an official WMT result. Small or missing references can make high-order n-grams undefined; the return value includes counts and `None` for an unscorable pair rather than inventing perfect overlap.

## Evaluation and social context

An authentic evaluation needs held-out sentences, rights-cleared and accurately aligned references, multiple speakers or professional translators where relevant, language/variety and domain coverage, and measures of error with uncertainty. Reference variation can penalize valid paraphrase. Endangered-language translation requires community governance and should not assume that one publicly available reference is normatively correct for all dialects.

**Source:** Popović 2015, ACL Anthology W15-3049 (abstract/metadata inspected), with older BLEU sources preserved. No real machine-translation output was scored here.
