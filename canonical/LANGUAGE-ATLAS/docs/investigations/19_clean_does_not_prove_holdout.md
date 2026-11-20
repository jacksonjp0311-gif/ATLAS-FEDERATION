# Investigation 19: Absence of overlap evidence is not independence

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

Two distinct IDs and different exact normalized hashes pass the simple leakage check. This does not guarantee that the texts were never used during model training, nor that they are unrelated paraphrases or answer-contaminated examples.

**Reproduced result:**

```json
{
  "schema": "atlas.language-leakage-audit/1",
  "overlapping_ids": [],
  "exact_nfc_text_hashes": [],
  "clean_under_exact_tests": true,
  "semantic_leakage_ruled_out": false,
  "limitations": [
    "NFC exact hashes do not detect paraphrases, translations or answer exposure",
    "A split that passes this test is not independently verified as held out"
  ]
}
```

## Negative control and next evidence

Precommit the dataset, inspect provenance and keep a record of model training/exposure before concluding that tasks were truly unseen.

**Research limit:** Cannot certify independent benchmark. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
