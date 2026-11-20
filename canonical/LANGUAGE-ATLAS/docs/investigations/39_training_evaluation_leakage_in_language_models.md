# Investigation 39 — A translation benchmark can leak through normalization

Suppose a training split contains decomposed `café` and a purportedly held-out split contains composed `café`. File IDs differ but Unicode NFC normalization makes the strings equal. A strict exact-ID-only leakage check would miss this. A normalization-aware check can report a collision, but it still cannot detect all paraphrases or semantic duplicates.

Language Atlas's prior corpus-leakage method checks a narrow, authored normalization example. A realistic translation evaluation must preserve source provenance, versioned tokenization, speaker consent, dataset sampling, and independent human judgment. A small BLEU/chrF score difference is not evidence that a model understood a language.

No actual training or evaluation model was executed.
