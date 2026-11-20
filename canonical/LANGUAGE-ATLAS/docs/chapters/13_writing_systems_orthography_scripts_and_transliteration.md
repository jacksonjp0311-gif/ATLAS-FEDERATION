# Chapter 13. Writing systems, orthography, scripts and transliteration

**Area:** Writing and encoding  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Writing uses conventional visible symbols to encode aspects of language, but the relationship between writing and speech or sign is variable. Alphabetic, abjad, abugida, syllabic, morphosyllabic and mixed systems involve different mappings. A script is not a language, and a language can use multiple scripts; multiple languages can share a script. Romanization or transliteration maps written forms under a chosen convention, whereas phonetic transcription aims to represent sound. Both can be lossy, and some transliterations are designed to be reversible only under special diacritics or escape conventions. A survivor needs source scripts, encoding, normalization rules, reading order and rendering information.

## Underlying mathematical, grammatical or methodological principle

A reversible transliteration is an injective mapping over the declared input domain, with an inverse. When distinct source symbols map to one target string, the transformation is lossy unless additional side information is stored. Canonical Unicode equivalence may preserve linguistic identity for some purposes but compatibility normalization can merge distinct symbols. A digital archive must retain raw source bytes and a described transformation pipeline rather than saving only a transliteration. Rights and provenance also apply to community-maintained orthographies.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Design a toy alphabet mapping where two distinct symbols both become “a”; demonstrate why the original cannot be recovered from the output alone. Then add explicit escape codes to make the mapping injective, and document that the new code is an artificial demonstration, not a real writing system.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

Do not assume Latin letters, left-to-right orientation or standardized spelling. Normalization and transliteration are different operations and require separate evidence and tests.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Unicode Standard Annex #15 — Normalization Forms](https://www.unicode.org/reports/tr15/) — Unicode 18.0, published 2026-08-12; inspected summary, definitions of NFC/NFD/NFKC/NFKD
- [RFC 5646 — Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646) — BCP47 official abstract: syntax, structure, semantics and registered subtags
- [W3C Internationalization: Language Tags](https://www.w3.org/International/articles/language-tags/) — Bibliographic educational overview of language tag choices; no full text reviewed

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
