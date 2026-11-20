# Investigation 03: Preserve every source byte

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

A well-formed UTF-8 sequence decodes and re-encodes to the identical bytes. The invariant verifies transport-byte consistency under strict UTF-8, not the correctness of the language, spelling or document attribution. A byte checksum needs a trusted expected value.

**Reproduced result:**

```json
{
  "text": "mañana",
  "bytes_sha256": "f968682da39382523ffa34f7e9e8e84e337eacc30fa2e70435c8ed70e1ff0ff7",
  "roundtrip": true
}
```

## Negative control and next evidence

Run the same test on a short sample in a non-Latin script and record both code-point and byte length. Do not equate the count with visible graphemes.

**Research limit:** No broken UTF-8 accepted. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
