# Investigation 18: Equivalent Unicode can conceal exact duplicates

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

Two differently encoded strings normalize to the same NFC text and are flagged as an exact normalized duplicate across training and evaluation. A raw-byte-only test would miss this duplication. The audit remains bounded to chosen normalization, not semantic equivalence.

**Reproduced result:**

```json
{
  "schema": "atlas.language-leakage-audit/1",
  "overlapping_ids": [],
  "exact_nfc_text_hashes": [
    "850f7dc43910ff890f8879c0ed26fe697c93a067ad93a7d50f466a7028a9bf4e"
  ],
  "clean_under_exact_tests": false,
  "semantic_leakage_ruled_out": false,
  "limitations": [
    "NFC exact hashes do not detect paraphrases, translations or answer exposure",
    "A split that passes this test is not independently verified as held out"
  ]
}
```

## Negative control and next evidence

Add whitespace differences or a translation and show they can evade exact NFC hashes. A credible held-out evaluation must consider source document, paraphrase and speaker overlap.

**Research limit:** No semantic duplicates checked. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
