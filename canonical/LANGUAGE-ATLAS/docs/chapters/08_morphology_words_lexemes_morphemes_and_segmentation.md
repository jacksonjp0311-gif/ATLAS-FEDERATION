# Chapter 08. Morphology: words, lexemes, morphemes and segmentation

**Area:** Morphology  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Morphology studies how word forms relate to lexical meanings and grammatical functions. A lexeme is an abstract lexical unit, while a word form is a particular realization; a morpheme is a theoretical minimal meaningful unit whose surface realization may be conditioned by context. Segmentation can be ambiguous: an apparently meaningful substring may be coincidental, and a lexical item may not admit a clean concatenative analysis. Analysts must distinguish inflectional features, derivational relationships, clitics and compounds and must not assume that the English space-separated “word” is a universal linguistic unit.

## Underlying mathematical, grammatical or methodological principle

A finite lexicon can map a surface string to multiple analyses with lemma, features and evidence provenance. It may return “unknown” when a form is missing, but that result means the lexicon is incomplete, not that the word is impossible. Finite-state transducers can encode regular relations between underlying and surface strings; this does not guarantee that every language's morphology is regular or concatenative. Lexicon source IDs and language variety must remain attached to the output.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Compare the invented surface form “flies” with analyses as a plural noun and present-tense verb. Use the morphology lookup to preserve both instead of choosing one without context. Add a constructed suppletive pattern, and explain why simply splitting the suffix cannot recover all inflectional structure.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

The supplied entries are toy descriptions, not a universal morphological dictionary. An empty analysis list is an explicit coverage gap and must not be treated as a negative human-language judgment.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Leipzig Glossing Rules](https://www.eva.mpg.de/lingua/resources/glossing-rules.php) — Official ten rules and interlinear gloss conventions page, last stated change 2015
- [Universal Dependencies annotation framework, version 2](https://universaldependencies.org/) — UD v2 official overview: cross-linguistic POS, morphology, dependency syntax, public 2026 releases
- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
