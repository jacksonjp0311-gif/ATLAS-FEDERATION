# 52. Productive morphology, paradigms, and evidential limits of finite-state rules

Morphology investigates structure within words, including how forms relate to lexical categories and grammatical features. A morpheme can be a useful analytical unit without forcing every language to segment neatly into invariant substrings. Fusional, templatic, nonconcatenative and suppletive morphology create counterexamples to a simplistic prefix-stem-suffix engine. Productive rules can generate new forms, but a rule inferred from a few words is a hypothesis about a morphological system, not a law that overrides native speakers.

## Reconstruction

Separate an *analysis* mapping surface form→possible lemma/features from a *generation* mapping lemma/features→possible surface forms. A finite lexicon can return multiple analyses for one spelling. Preserve each hypothesis with its source, context, part of speech, number, tense, person and relevant feature inventory. A finite-state transducer can encode an explicit relation between lexical and surface strings, but not every feature assignment is deterministic. For example the written English form “flies” can be plural noun or third-person singular verb depending on syntactic context. A lexicon lookup that returns both is more faithful than a function that arbitrarily chooses one.

A morphological reconstruction begins with a table of forms and elicitation conditions. Mark lexical exceptions and analyze allomorphs. Record whether “s” in a form is a segment, suffix, orthographic marker, or part of a non-concatenative pattern. Use an explicit probability or categorical analysis only if backed by a corpus or carefully documented speaker judgments. A toy form recognizer may be correct on its known entries but unknown on novel or borrowed words.

## Failure boundary

Languages differ in what counts as a word, morpheme and phonological unit. Unicode code points, user-perceived grapheme clusters, phonetic segments and linguistic morphemes are different objects. A failure to segment an input with a toy lexicon cannot establish the form is nonexistent or ungrammatical. Real preservation requires paradigms, raw examples, speaker consent, interlinear glossing and context—not only a fixed list of translations.

**Sources:** Leipzig Glossing Rules and Universal Dependencies v2 feature/word documentation; existing Language Atlas morphological ambiguity investigations. This edition does not claim a universal morphology analyzer.
