# Chapter 21. Ambiguity in attachment, ellipsis and scope

**Area:** Syntax  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

A sentence may support several syntactic structures, each potentially contributing different meaning. Prepositional phrase attachment, coordination scope, pronoun antecedents and omitted but contextually recoverable material are familiar sources of ambiguity. Grammars generate analyses, not intentions. A parser that returns one plausible tree may conceal alternatives, and a high model confidence score does not independently validate the intended structure. Some ambiguities are grammatically constrained; others arise from missing discourse context or lexical sense distinctions. Researchers should compare proposed parses with speaker judgments and controlled continuation contexts.

## Underlying mathematical, grammatical or methodological principle

In a CYK chart, an accepted span can have multiple derivations under the same nonterminal. Parse count sums products over valid split positions and rules, conditional on a finite grammar. A tree witness demonstrates one derivation; if the count is two, it proves structural ambiguity **under the supplied rules**, not semantic ambiguity across all interpretations. If a resource limit saturates a count, report at least or capped rather than an exact total. Different theories can assign structurally different analyses to the same utterance.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

For the toy “robots see astronomers with telescopes,” draw two phrase-structure trees that attach the prepositional phrase differently. Translate each into a simple logical description of who has the telescope. Then identify additional contextual evidence that would select one reading.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

The exercise is constructed and does not establish actual English speaker judgments. Real parsing evaluation needs annotated corpora, licensing and independent assessment of ambiguous inputs.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details
- [Compositionality](https://plato.stanford.edu/entries/compositionality/) — Stanford Encyclopedia 2025 revision: structure, constituent meaning, theories and counterarguments
- [Three Models for the Description of Language (1956)](https://doi.org/10.1109/TIT.1956.1056813) — Bibliographic historical paper pointer for formal grammar classification; no paper body inspected

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
