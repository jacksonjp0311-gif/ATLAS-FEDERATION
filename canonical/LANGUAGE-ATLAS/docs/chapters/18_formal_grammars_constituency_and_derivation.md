# Chapter 18. Formal grammars, constituency and derivation

**Area:** Syntax  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

A formal grammar specifies a set of expressions and derivational rules. A context-free grammar (CFG) can express nested constituency patterns, but no single CFG provided with this package is a grammar of every human language. Linguistic structure is established by evidence from distribution, interpretation, morphosyntax and speaker judgments. Phrase structure trees are useful hypotheses about constituent groupings, and multiple derivations of the same token sequence reflect structural ambiguity under a grammar. A parser returning a tree demonstrates only membership and a witness relative to its rules.

## Underlying mathematical, grammatical or methodological principle

The Chomsky normal form subset used by CYK has lexical rules A→terminal and binary rules A→BC. For an input of n tokens, dynamic programming considers spans [i,j), split points k and rule categories. A state can store both a count of derivations and a sample witness. Counts can grow rapidly; if a cap is applied, exact ambiguity claims must stop. Epsilon productions, unary nonterminals and unknown words are not in this bounded implementation, even though broader grammars can represent them.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Use the supplied constructed grammar for “robots see astronomers with telescopes.” Enumerate the attachment of “with telescopes” to the noun phrase and verb phrase, and inspect two derivations. Compare with a different order that the toy grammar rejects, emphasizing that the grammar—not nature—determines this result.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

No syntactic parse here verifies real acceptability, discourse interpretation or the intentions of a speaker. Many languages have structures that require grammar extensions, statistical modeling or competing theories.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Three Models for the Description of Language (1956)](https://doi.org/10.1109/TIT.1956.1056813) — Bibliographic historical paper pointer for formal grammar classification; no paper body inspected
- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details
- [Compositionality](https://plato.stanford.edu/entries/compositionality/) — Stanford Encyclopedia 2025 revision: structure, constituent meaning, theories and counterarguments

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
