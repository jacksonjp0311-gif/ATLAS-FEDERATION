# Investigation 04: Reject silent Unicode corruption

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

Ill-formed UTF-8 is rejected rather than converted with replacement characters. Replacing bytes may make a file displayable while obscuring the original error location and losing the ability to reconstruct the input. The correct archival response is a documented decoding failure and preserved raw bytes.

**Reproduced result:**

```json
{
  "refused": true
}
```

## Negative control and next evidence

Change the malformed byte sequence and compare strict versus replacement decoding in a separate scratchpad. The reference implementation deliberately supports only strict mode.

**Research limit:** Malformed transport is rejected. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
