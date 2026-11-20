# Investigation 10: Reject under this grammar only

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The parser refuses a sequence that cannot be derived by its current finite grammar. This is a relative formal result. It does not prove the string is ungrammatical in every language, or even in a variety of English outside the toy grammar.

**Reproduced result:**

```json
{
  "schema": "atlas.language-cyk/1",
  "accepted": false,
  "parse_count_cap": 1000000,
  "parse_count": 0,
  "saturated": false,
  "count_is_exact": true,
  "witness_tree": null,
  "grammar_fragment": "CNF lexical and binary productions only",
  "limitations": [
    "No universal/natural-language grammaticality inference",
    "Specified grammar alone controls ambiguity",
    "Parse count is not exact if cap saturated",
    "Unknown tokens are rejected by this grammar, not impossible in human language"
  ]
}
```

## Negative control and next evidence

Add a new lexical or binary production and re-evaluate. The changed result demonstrates sensitivity to model assumptions, not a change in human linguistic reality.

**Research limit:** Unknown under this grammar, not universally ungrammatical. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
