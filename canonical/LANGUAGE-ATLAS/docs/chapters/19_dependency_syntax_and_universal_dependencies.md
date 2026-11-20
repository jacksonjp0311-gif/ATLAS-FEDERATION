# Chapter 19. Dependency syntax and Universal Dependencies

**Area:** Syntax  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Dependency grammar describes syntactic structure through relations between words or other nodes. In a basic dependency tree, most nodes have one head, a designated root has head zero, and cycles are forbidden. Universal Dependencies offers a cross-linguistic annotation framework with part-of-speech tags, morphological features and typed syntactic relations. A valid graph shape is not evidence that its labels are correct: a parser can create a formally well-formed tree that is linguistically implausible. Furthermore, word segmentation and empty elements can complicate a naïve one-row-per-word model.

## Underlying mathematical, grammatical or methodological principle

CoNLL-U represents annotations in ten tab-separated fields per word line, with comments and blank sentence boundaries. It supports multiword token ranges, empty nodes and enhanced dependencies under special rules. The package implements only a declared **basic integer-word subset** with sequential IDs, exactly one root and acyclic HEAD links. It refuses multiword and enhanced structures rather than pretending complete CoNLL-U coverage. A tree's structural validity and source provenance should be audited independently from label accuracy and typological applicability.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Validate the constructed “Ada reads.” sentence with three rows. Change the last dependency head to itself to create a structural error; the checker must reject it. Then describe a real case with multiword tokens and explain why this restricted parser must abstain until a compliant extension is written.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

The validator checks tree shape but not all formatting constraints or UD language-specific conventions. UD release versions and treebank licenses vary and should be pinned before importing source data.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Universal Dependencies annotation framework, version 2](https://universaldependencies.org/) — UD v2 official overview: cross-linguistic POS, morphology, dependency syntax, public 2026 releases
- [Universal Dependencies CoNLL-U Format](https://universaldependencies.org/format.html) — Official 10-column UTF-8 tab-separated sentence format, fields and multiword/empty-node distinctions
- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
