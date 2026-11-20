# Investigation 02: Compatibility normalization is not reversible

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

A circled digit can become a plain digit under NFKC. That is a deliberate compatibility transformation and may be useful for a controlled identifier comparison, but it discards typographic distinction. Keeping only the transformed output can destroy evidence about historical orthography or source notation.

**Reproduced result:**

```json
{
  "schema": "atlas.language-unicode-profile/1",
  "raw_sha256": "9e96ca1ce18ffb97f67c1230d8282320058da75aa86fc44fb435d25c512a5423",
  "utf8_bytes": 3,
  "code_point_count": 1,
  "categories": {
    "No": 1
  },
  "nfc": "①",
  "nfkc": "1",
  "nfc_changed": false,
  "compatibility_mapping_changed": true,
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

Compare NFC and NFKC for characters with compatibility mappings, retain original bytes, and document when such transformations would be inappropriate for a source archive.

**Research limit:** NFKC loses some distinctions. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
