# Chapter 15. Canonical and compatibility normalization are different

**Area:** Writing and encoding  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Unicode normalization addresses multiple encoded representations that are equivalent under defined rules. NFC and NFD concern canonical equivalence; NFKC and NFKD also apply compatibility transformations that can collapse visually or historically distinct characters. A program that normalizes all text with NFKC can change distinctions that matter for textual scholarship, mathematical notation or identifiers. The appropriate form depends on a declared use case. The source text should remain available for forensic and linguistic reconstruction even when a normalized search copy is created.

## Underlying mathematical, grammatical or methodological principle

For a canonical-equivalent sequence x,y, Unicode normalization NFC(x)=NFC(y) under the same conformant Unicode version. This does not imply a reversible mapping from normalized output to original bytes. If a compatibility character becomes a different sequence under NFKC, retain both original and normalized forms. The package's Unicode profile reports raw byte SHA, code-point count, NFC/NFKC outputs and a compatibility-change warning; it deliberately does not compute user-perceived grapheme boundaries.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Normalize a decomposed accent and demonstrate equal NFC output. Normalize a circled digit and observe NFKC replacement with a plain digit. Keep the original raw form in a local notebook and explain why a historical document shouldn't be overwritten by a search index representation.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

A normalization check is not a language identification method or full security policy for confusable identifiers. Record the Unicode database version and never silently call NFKC lossless.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Unicode Standard Annex #15 — Normalization Forms](https://www.unicode.org/reports/tr15/) — Unicode 18.0, published 2026-08-12; inspected summary, definitions of NFC/NFD/NFKC/NFKD
- [The Unicode Standard and character model](https://www.unicode.org/standard/standard.html) — Bibliographic pointer to Unicode standard character properties; full specification not audited

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
