# Investigation 12: Unknown is not a negative label

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The hypothetical relation has no positive or negative fact for the queried tuple. An existential query remains unknown rather than false. This protects an evidence archive from converting missing observations into universal denials.

**Reproduced result:**

```json
{
  "schema": "atlas.language-three-valued/1",
  "truth": "unknown",
  "operations": 3,
  "world_truth_grounded": false,
  "limitations": [
    "Finite three-valued first-order fragment only",
    "Unknown is not equivalent to false",
    "Predicate assignments are supplied, not observations verified from real world",
    "Natural language interpretation and quantifier scope must be supplied separately"
  ]
}
```

## Negative control and next evidence

Add one declared positive witness and recompute. Then add all explicit negatives and compare; the rule remains conditional on the declared finite domain.

**Research limit:** Missing is not false. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
