# Investigation 06: Segmentation versus morphology

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The toy lexicon allows splitting one string into two listed pieces. Nothing in this result proves that the pieces are morphemes, or that the combined meaning follows productively. A linguistic analyst needs paradigms, comparable forms and contextual judgments.

**Reproduced result:**

```json
{
  "schema": "atlas.language-segmentation/1",
  "segmentations": [
    {
      "tokens": [
        "un",
        "seen"
      ],
      "cost": 1
    }
  ],
  "count_listed": 1,
  "saturated": false,
  "complete_count_proven": true,
  "limitations": [
    "Results are relative to the supplied lexicon/cost; unknown words have no path",
    "Cap truncation prevents exact ambiguity counts",
    "This does not implement script-specific word segmentation"
  ]
}
```

## Negative control and next evidence

Replace a component with an unseen entry to get no path. Record this as lack of lexicon coverage, not impossibility of a natural-language form.

**Research limit:** Not morphological truth. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
