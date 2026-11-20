# Investigation 14: A tree cannot parent itself

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

A word with HEAD equal to its own ID violates the finite basic-tree constraint. The validator detects the cycle; it is a structural error in the supplied annotation, not a judgment about the speaker or the sentence's meaning.

**Reproduced result:**

```json
{
  "refused": true
}
```

## Negative control and next evidence

Construct a two-node cycle and a missing-head reference. Report the exact failure reason and preserve the original annotated file for later correction.

**Research limit:** No semantic annotation assessment. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
