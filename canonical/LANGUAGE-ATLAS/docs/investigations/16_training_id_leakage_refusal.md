# Investigation 16: Explicit task exposure breaks the split

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The model refuses evaluation under an ID present in the training set. This is a minimal leakage defense; a new ID containing an identical sentence or paraphrase can still reveal the correct answer or source text.

**Reproduced result:**

```json
{
  "refused": true
}
```

## Negative control and next evidence

Construct an exact NFC-equivalent duplicate under a new ID and run the separate hash audit. Explain why a clean exact audit cannot certify semantic independence.

**Research limit:** Paraphrase leakage not checked. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
