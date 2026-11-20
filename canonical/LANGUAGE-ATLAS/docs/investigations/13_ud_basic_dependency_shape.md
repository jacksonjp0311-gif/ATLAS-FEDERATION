# Investigation 13: Tree structure is weaker than annotation correctness

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The toy three-token dependency file satisfies a restricted CoNLL-U shape: 10 tab-separated fields, a single root, and acyclic head links. This does not validate UPOS, morphological features, enhanced dependencies, multiword tokens, or the linguistic analysis itself.

**Reproduced result:**

```json
{
  "schema": "atlas.language-conllu-basic-subset/1",
  "sentences": [
    {
      "forms": [
        "Ada",
        "reads",
        "."
      ],
      "heads": [
        2,
        0,
        2
      ],
      "root_index": 2,
      "comments": [
        "# sent_id = toy1",
        "# text = Ada reads."
      ]
    }
  ],
  "sentence_count": 1,
  "conllu_full_conformance_certified": false,
  "limitations": [
    "Not a complete CoNLL-U validator: no multiword tokens, empty nodes, enhanced dependencies or full feature validation",
    "Valid dependency shape does not imply correct linguistic annotation or grammaticality"
  ]
}
```

## Negative control and next evidence

Compare the file to official UD v2 documentation; try adding a multiword token and observe that the restricted parser refuses unsupported features rather than claiming full compliance.

**Research limit:** Not full UD conformance. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
