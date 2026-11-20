# Investigation 07: One surface can have two analyses

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

Two explicitly supplied analyses of a form produce distinct grammatical feature bundles. A dictionary lookup should preserve both, with source identifiers, rather than selecting one based on the order of rows. Word-form, lemma and grammatical annotation are distinct fields.

**Reproduced result:**

```json
{
  "schema": "atlas.language-morphology/1",
  "surface": "flies",
  "analyses": [
    {
      "lemma": "fly",
      "features": {
        "Number": "Plur",
        "POS": "NOUN"
      },
      "source_id": "toy-n1"
    },
    {
      "lemma": "fly",
      "features": {
        "Number": "Sing",
        "POS": "VERB",
        "Person": "3"
      },
      "source_id": "toy-v1"
    }
  ],
  "status": "found",
  "disambiguated_by_context": false,
  "limitations": [
    "Lexicon is caller-supplied and incomplete",
    "No universal morphology rules or semantics inferred"
  ]
}
```

## Negative control and next evidence

Add a contradictory sourced analysis and an unknown form, then confirm the system marks absence as unknown. An authentic morphology project requires a versioned corpus and speaker/linguist review.

**Research limit:** Analyses are corpus-supplied. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
