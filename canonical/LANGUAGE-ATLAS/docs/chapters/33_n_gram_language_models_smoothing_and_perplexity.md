# Chapter 33. N-gram language models, smoothing and perplexity

**Area:** Computation  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

An n-gram model estimates the probability of a token from a bounded history of preceding tokens. Bigram counts are easy to compute and inspect, making them valuable for teaching conditional probability and sparsity. They do not capture arbitrary long-distance syntax, conversation intention or world knowledge. Unknown tokens and sentence-start/end markers must be handled explicitly. With unsmoothed estimates, many perfectly ordinary unseen sequences receive zero probability; add-k smoothing avoids that but imposes a modeling choice that can distort distributions. Evaluation must use a genuinely held-out corpus and a fixed tokenization policy.

## Underlying mathematical, grammatical or methodological principle

For a conditional bigram estimate, P(w|h)=(count(h,w)+α)/(count(h)+α|V|) with α>0 and prediction vocabulary V. Sentence log-probability is the sum of log probabilities for each transition; perplexity PP=2^{−(1/N)Σ log₂P(w_i|h_i)}. Perplexity is sensitive to tokenization and unknown-token handling; scores from incomparable vocabularies or corpora cannot be directly interpreted as understanding. Low perplexity can result from memorization or repeated strings.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Train the supplied two-sentence toy corpus containing “cats sleep” and “dogs sleep”, then score an independent document ID with the same tokens. Observe nonzero smoothed probability. Attempt to evaluate a training ID and confirm the identity-overlap guard rejects it. Explain why another task ID containing the exact same text can still leak answer knowledge.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

The included model is a bounded, constructed bigram demonstration, not an LLM or evidence of fluent human communication. It has no attention mechanism, speaker identity, ground-truth semantics or independent generalization guarantee.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details
- [A Mathematical Theory of Communication (1948)](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x) — Bibliographic historical pointer for communication and entropy, not a paper reproduction
- [Three Models for the Description of Language (1956)](https://doi.org/10.1109/TIT.1956.1056813) — Bibliographic historical paper pointer for formal grammar classification; no paper body inspected

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
