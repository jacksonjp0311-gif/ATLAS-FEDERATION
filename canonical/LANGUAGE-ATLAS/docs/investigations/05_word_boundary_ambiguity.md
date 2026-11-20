# Investigation 05: A lexicon creates alternatives

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The string can be segmented according to several whole-string paths supplied by a toy lexicon. An inexpensive path is a mathematical ranking under given weights, not a verified intended word boundary. Real writing systems require language-specific data and Unicode boundary conventions.

**Reproduced result:**

```json
{
  "schema": "atlas.language-segmentation/1",
  "segmentations": [
    {
      "tokens": [
        "therapist"
      ],
      "cost": 0
    },
    {
      "tokens": [
        "the",
        "rapist"
      ],
      "cost": 5
    }
  ],
  "count_listed": 2,
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

Assign a different cost to one candidate and show that a new ranking does not create a linguistic fact. Maintain all source alternatives before claiming a context has resolved the choice.

**Research limit:** Toy lexicon, not UAX 29. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
