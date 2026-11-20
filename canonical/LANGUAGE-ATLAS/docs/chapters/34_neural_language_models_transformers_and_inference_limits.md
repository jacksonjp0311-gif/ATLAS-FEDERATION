# Chapter 34. Neural language models, transformers and inference limits

**Area:** Computation  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Modern language models use learned numerical representations to predict or generate token sequences. Transformer architectures employ attention and other transformations to combine information from a context window; training and inference require substantial data, compute, objective choices and engineering infrastructure. Producing grammatical or persuasive text is not identical to grounded reasoning, communicative competence or truth. Token probabilities depend on the model, decoding strategy, prompt, version, training distribution and hidden system context. A language archive should describe those mechanisms without making access to a proprietary hosted model necessary to understand their basic mathematics.

## Underlying mathematical, grammatical or methodological principle

In scaled dot-product attention, for supplied query, key and value matrices, attention weights are a softmax of QKᵀ/√d, optionally with a mask, and the output is a weighted value combination. This is a computation graph operation; it does not itself establish whether the model represents syntax, reasons causally, or knows a particular fact. Multiple layers and learned parameters create capabilities that depend on training, model architecture, and evaluation conditions. An apparent improvement from retrieving cached source text could be a simpler retrieval benefit, not neural weight learning.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Work through a two-token attention example with invented 2D vectors and compare how a mask changes a weight. Note the assumptions about dimensions, softmax numerical stability and data rights. Sketch how an unseen-task benchmark would distinguish learned competence from repeated prompt examples.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

No transformer implementation, new language-model training, GPU efficiency claim or scientific evaluation of actual models occurs in Language Atlas v0.1. Formal architecture explanation is not production-capability proof.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details
- [Compositionality](https://plato.stanford.edu/entries/compositionality/) — Stanford Encyclopedia 2025 revision: structure, constituent meaning, theories and counterarguments
- [Universal Dependencies annotation framework, version 2](https://universaldependencies.org/) — UD v2 official overview: cross-linguistic POS, morphology, dependency syntax, public 2026 releases

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
