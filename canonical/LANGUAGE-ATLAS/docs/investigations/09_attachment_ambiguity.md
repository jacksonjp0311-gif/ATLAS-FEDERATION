# Investigation 09: Two parse trees, one token sequence

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The constructed CNF grammar has two syntactic analyses of a prepositional-phrase attachment. CYK counts derivations while retaining one tree witness. A ranking or capped count may hide ambiguity; grammatical acceptance does not establish speaker intention.

**Reproduced result:**

```json
{
  "schema": "atlas.language-cyk/1",
  "accepted": true,
  "parse_count_cap": 1000000,
  "parse_count": 2,
  "saturated": false,
  "count_is_exact": true,
  "witness_tree": [
    "S",
    [
      "NP",
      "robots"
    ],
    [
      "VP",
      [
        "V",
        "see"
      ],
      [
        "NP",
        [
          "NP",
          "astronomers"
        ],
        [
          "PP",
          [
            "P",
            "with"
          ],
          [
            "NP",
            "telescopes"
          ]
        ]
      ]
    ]
  ],
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

Draw both trees by hand and explain how context might make one interpretation more likely. To evaluate real syntax, obtain independently annotated data rather than treating the toy grammar as English grammar.

**Research limit:** Grammar is constructed CNF. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
