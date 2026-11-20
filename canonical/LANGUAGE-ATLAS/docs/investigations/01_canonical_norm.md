# Investigation 01: Canonical equivalent strings

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The original test pairs a decomposed accent with the corresponding composed form. NFC gives a stable comparison form, but the source's raw encoding must remain separately available to preserve historical evidence. Two strings that normalize to the same code-point sequence can have different original bytes.

**Reproduced result:**

```json
{
  "schema": "atlas.language-unicode-profile/1",
  "raw_sha256": "81ef060bcd98adc7824eb5c1ada83c32491b16018e11e79f00ab9d09e04b015a",
  "utf8_bytes": 6,
  "code_point_count": 5,
  "categories": {
    "Ll": 4,
    "Mn": 1
  },
  "nfc": "café",
  "nfkc": "café",
  "nfc_changed": true,
  "compatibility_mapping_changed": false,
  "grapheme_cluster_count": null,
  "unicode_database_version": "15.1.0",
  "limitations": [
    "Python code points are not user-perceived grapheme clusters",
    "NFKC can erase distinctions; original raw text retained only as a hash here",
    "This is not an implementation of UAX 29 grapheme, word or sentence boundaries"
  ]
}
```

## Negative control and next evidence

Test a second combining-mark order against the Unicode version in the running interpreter. A version mismatch against a newer UAX test suite is unresolved; do not claim Unicode 18.0 conformance from this demonstration.

**Research limit:** Not grapheme segmentation. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
