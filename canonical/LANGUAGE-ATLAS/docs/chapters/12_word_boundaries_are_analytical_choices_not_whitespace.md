# Chapter 12. Word boundaries are analytical choices, not whitespace

**Area:** Writing and encoding  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Written spaces delimit some orthographic words, but the boundaries of meaningful or grammatical words can differ across scripts, clitics, compounds and languages. In many writing systems, words are not indicated by spaces; in others, spacing conventions differ across genres or historical periods. Computational tokenization must distinguish bytes, Unicode code points, grapheme clusters, word-like segments, morphemes and model tokens. Each choice produces a different count and may affect downstream evaluation. The mere output of a particular tokenizer is not evidence that it found natural language word boundaries.

## Underlying mathematical, grammatical or methodological principle

Segmentation can be modeled as a constrained path problem over a finite lexicon. For a sequence of n code points, each path divides the string into dictionary entries. An additive weight can rank paths, but the lexicon and weights are supplied and may be incomplete. The bounded dynamic program in this package lists multiple segmentations with a cap. Truncation must be reported because an incomplete list does not prove the exact ambiguity count. Unicode default word-break algorithms are more complex and are versioned separately from any toy lexicon.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Use the invented string “therapist” and a lexicon containing “therapist”, “the” and “rapist”. List both parses without implying either is the intended reading. Then use an unknown word and record that it has no path in this lexicon—not that it is an impossible human word.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

A finite dictionary method is not UAX 29, a full morphological parser, or a multilingual tokenization benchmark. Its outputs cannot ground real speech or linguistic correctness without source evidence.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Unicode Standard Annex #29 — Text Segmentation](https://www.unicode.org/reports/tr29/) — Unicode 18.0, published 2026-09-01; inspected abstract and grapheme/word/sentence boundaries
- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details
- [Universal Dependencies annotation framework, version 2](https://universaldependencies.org/) — UD v2 official overview: cross-linguistic POS, morphology, dependency syntax, public 2026 releases

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
