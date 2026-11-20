# Chapter 32. Corpora, sampling and annotation disagreement

**Area:** Methodology  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

A language corpus is a selected set of communication events or documents, not a transparent window onto every possible utterance. Its representativeness depends on modality, genre, social context, language variety, sampling, time, collection method and rights. Token frequencies can be useful but inherit those biases. Annotation adds another layer of uncertainty: parts of speech, word boundaries, senses, syntactic edges and discourse acts often permit legitimate disagreement. An annotation guideline defines operational categories; it does not make labels infallible.

## Underlying mathematical, grammatical or methodological principle

An evaluation should preserve raw texts/recordings under permitted rights, exact train/dev/test identifiers, annotation rubric version, coder identities or provenance, adjudication protocol and unknown labels. A model trained on examples that are repeated or near-duplicated in its evaluation split may appear artificially successful. Exact normalized-text hashing detects some duplicates but does not detect translations, paraphrases or leaked expected answers. Inter-annotator agreement describes convergence of labels under a rubric; it cannot independently establish semantic ground truth or a person's intention.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Create a fictional ten-document dataset with five train and five test IDs. Copy one test sentence using decomposed Unicode into training, then run NFC-based leakage detection to show the duplicate. Change the copied sentence to a paraphrase and explain why an exact-hash audit can no longer prove separation.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

This package imports no large real-world multilingual corpus. Source-specific licensing and permissions can differ by dataset and treebank, and evaluation scores are not supplied as measured model performance.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Universal Dependencies annotation framework, version 2](https://universaldependencies.org/) — UD v2 official overview: cross-linguistic POS, morphology, dependency syntax, public 2026 releases
- [TalkBank linguistic interaction and transcript resources](https://talkbank.org/) — Bibliographic overview of corpus, transcription and speaker data; no corpora inspected
- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
