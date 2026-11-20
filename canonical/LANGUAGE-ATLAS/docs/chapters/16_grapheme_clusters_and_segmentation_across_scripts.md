# Chapter 16. Grapheme clusters and segmentation across scripts

**Area:** Writing and encoding  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Users perceive text in units that do not always match code points or visible glyphs. The Unicode Text Segmentation annex describes default grapheme, word and sentence boundary rules, with tailoring possible for language-specific behavior. Emoji sequences, joiner behavior, combining marks and script-specific clusters make naive one-codepoint counting unreliable. A display glyph may depend on font shaping and context, while the grapheme cluster is an algorithmic text-boundary concept. A program that counts code points correctly has not automatically implemented UAX 29's rules.

## Underlying mathematical, grammatical or methodological principle

Boundary determination is a versioned procedure over Unicode properties and explicit rule precedence. A proper implementation must use the matching Unicode data tables and pass conformance test files. Simple regular expressions like `\w+` or splitting at spaces do not implement the full annex. For preservation, retain source bytes, Unicode normalization version and any segmentation profile/tailoring. The package intentionally returns `grapheme_cluster_count = null` until a conformant grapheme implementation and its data tables are installed and tested.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Inspect a combining-accent string and an emoji ZWJ sequence, counting code points while leaving the perceived grapheme count unresolved. Use a fully licensed Unicode test suite in future work before asserting UAX conformance. Write down how a chosen script requires tailoring.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

No full Unicode UAX 29 grapheme, word or sentence segmenter is implemented in this release; no Unicode 18.0 conformance test has been executed.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Unicode Standard Annex #29 — Text Segmentation](https://www.unicode.org/reports/tr29/) — Unicode 18.0, published 2026-09-01; inspected abstract and grapheme/word/sentence boundaries
- [Unicode Standard Annex #15 — Normalization Forms](https://www.unicode.org/reports/tr15/) — Unicode 18.0, published 2026-08-12; inspected summary, definitions of NFC/NFD/NFKC/NFKD
- [W3C Internationalization: Language Tags](https://www.w3.org/International/articles/language-tags/) — Bibliographic educational overview of language tag choices; no full text reviewed

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
