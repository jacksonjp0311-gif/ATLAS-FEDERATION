# 49. Predictive metrics are not communicative intelligence

Probabilistic models assign likelihoods to sequences under a chosen alphabet and tokenization. Perplexity is the exponent of average negative log likelihood per token. It is useful for comparing models under identical data and token conventions, but it is not calibrated factual accuracy or a measure of human understanding. Two language models with different tokenizers may report different perplexity values even if their generated content is similarly useful. Their training corpora may overlap with evaluation texts, making memorization appear to be generalization.

## Units and estimands

A token-level perplexity `PP=exp(-(1/N)Σ log p(token_i|history))` depends on the tokenization unit and the test distribution. Character, subword, morpheme and word perplexity are different quantities. In a strongly inflected language, words may have many surface variants, so naïve cross-language comparisons of word-level perplexity are misleading. Evaluation must report unknown tokens, smoothing, calibration, model version and held-out split provenance.

BLEU and edit distance measure surface agreement with references, not semantic truth. A high BLEU score can coexist with a serious negation error; low BLEU may reflect a valid synonym or idiomatic translation. A grammar parser can reject a natural utterance absent from its tiny lexicon. A morphological analyzer can return two analyses for one form without deciding which a speaker intended. These are expected limits of the operational models, not software errors to conceal.

## Experimental design

To demonstrate that Language Atlas improves AI communication, use unseen tasks that test grammaticality, factual meaning, pragmatic appropriateness, multilingual translation, dialect sensitivity and signed-language accessibility. Include native speakers, trained annotators and transparent consent where relevant. Avoid one numerical score collapsing systematic failures on rare languages into good performance on high-resource English.

The Atlas itself is an evidence reference. It does not train a language model, call a provider, or claim a downstream model gain. Its purpose is to make future models and people more capable of reasoning about language with correct qualifications and reproducible methods.

**Sources:** Jurafsky/Martin language-model overview; Papineni BLEU; Post SacreBLEU reporting cautions; Unicode text-processing standards. No real multilingual evaluation run in this edition.
