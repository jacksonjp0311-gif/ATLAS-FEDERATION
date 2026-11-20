# Chapter 36. Language identification, tags and multilingual metadata

**Area:** Translation  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

An archive may need to identify the language, script, region, variety and writing conventions associated with an object. BCP 47 language tags provide a structured notation for interchange, while ISO 639 and related registries organize named codes; these are standards and conventions rather than measurements of linguistic identity. One document may contain multiple languages or scripts, and some language boundaries and labels are politically or historically contested. A code selected by a machine classifier must not override a community's own name or the actual content of a source.

## Underlying mathematical, grammatical or methodological principle

The restricted demonstration parser recognizes only a language–optional script–optional region skeleton such as `sr-Latn-RS`. It normalizes casing but **does not query the IANA subtag registry**, so its output is not complete BCP 47 validation. A full language tag can include variants, extensions, private-use values, grandfathered forms and registry-based constraints, and language matching is a separate process. A metadata pipeline should preserve the raw tag, its source, the version of the relevant registry and unresolved uncertainty.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Pass `sr-latn-rs` to the casebook skeleton parser, examine the case normalization and `registry_validated=false`. Then show an extension-rich tag that the toy parser rejects, explaining why that rejection does not invalidate the tag under the full standard.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

Do not mistake ISO language identifiers for a complete catalogue of all historical varieties, nor treat a syntactically plausible tag as evidence that a person speaks the labeled language.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [RFC 5646 — Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646) — BCP47 official abstract: syntax, structure, semantics and registered subtags
- [RFC 4647 — Matching of Language Tags](https://www.rfc-editor.org/rfc/rfc4647) — BCP47 official abstract about filtering and lookup matching
- [W3C Internationalization: Language Tags](https://www.w3.org/International/articles/language-tags/) — Bibliographic educational overview of language tag choices; no full text reviewed

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
