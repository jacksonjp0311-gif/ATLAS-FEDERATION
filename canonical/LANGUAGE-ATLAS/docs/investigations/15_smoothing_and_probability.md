# Investigation 15: Predictive likelihood is not language understanding

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The bigram model scores a held-out ID using a vocabulary and additive smoothing trained on two toy sentences. The calculation is a conditional probability of token transitions, not a model of causal reality, speaker intent, or translation correctness.

**Reproduced result:**

```json
{
  "schema": "atlas.language-bigram-score/1",
  "evaluation_id": "heldout-c",
  "tokens_scored": 3,
  "log2_probability": -4.614709844115208,
  "perplexity": 2.904392866781852,
  "train_id_disjoint": true,
  "independent_language_understanding_verified": false,
  "limitations": [
    "This is a small-order surface distribution; low perplexity is not semantic understanding",
    "Exact-sequence training leakage checks cannot detect paraphrases or other contamination",
    "OOV mapping and caller-provided tokens determine all scores"
  ]
}
```

## Negative control and next evidence

Calculate the add-alpha denominator by hand and compare perplexity before and after adding an unseen token. Record every tokenization and out-of-vocabulary choice.

**Research limit:** Perplexity is not understanding. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
