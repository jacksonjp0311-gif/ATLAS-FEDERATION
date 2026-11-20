# Chapter 14. Unicode scalar values, UTF-8, and exact source bytes

**Area:** Writing and encoding  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Digital text is stored as bytes under an encoding, often UTF-8. The Unicode standard assigns code points to abstract characters, but a displayed user-perceived character can consist of several code points. Code units, code points, grapheme clusters, words and model tokens must not be conflated. A raw file's exact bytes carry evidence for the original spelling, language tag, punctuation and normalization. Decoding malformed UTF-8 using replacement characters can irreversibly conceal corruption; this archive defaults to strict rejection. A rendering environment can also lack fonts even when the code points have been preserved correctly.

## Underlying mathematical, grammatical or methodological principle

UTF-8 encodes Unicode scalar values as variable-length byte sequences. A round trip under strict encoding/decoding restores the original valid sequence, but not necessarily the appearance of an unavailable font. A code-point length is not a grapheme count: a base letter plus combining mark may represent one perceived character. A source digest identifies bytes relative to a trusted expected hash; it does not verify who authored or measured the text. Record the Unicode version used for any normalization operations.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Compare “café” written with a precomposed `é` and with `e` plus a combining acute mark. Count UTF-8 bytes and code points separately. Decode an intentionally malformed byte sequence with strict error handling and preserve the error rather than silently replacing it.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

The Python runtime's Unicode database may lag behind the latest published Unicode version. Do not claim conformance to a later version simply because an official annex is current.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Unicode Standard Annex #15 — Normalization Forms](https://www.unicode.org/reports/tr15/) — Unicode 18.0, published 2026-08-12; inspected summary, definitions of NFC/NFD/NFKC/NFKD
- [Unicode Standard Annex #29 — Text Segmentation](https://www.unicode.org/reports/tr29/) — Unicode 18.0, published 2026-09-01; inspected abstract and grapheme/word/sentence boundaries
- [The Unicode Standard and character model](https://www.unicode.org/standard/standard.html) — Bibliographic pointer to Unicode standard character properties; full specification not audited

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
