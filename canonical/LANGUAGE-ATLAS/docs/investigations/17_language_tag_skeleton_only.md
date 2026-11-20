# Investigation 17: A plausible tag is not registry validation

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

The structural BCP47-like parser canonicalizes the casing of a language/script/region skeleton, but it neither queries the IANA registry nor accepts the full grammar with variants or extensions. Rejection by this subset is not a statement that an actual BCP47 tag is invalid.

**Reproduced result:**

```json
{
  "schema": "atlas.language-tag-skeleton/1",
  "canonical_casing_only": "sr-Latn-RS",
  "language": "sr",
  "script": "Latn",
  "region": "RS",
  "registry_validated": false,
  "normative_BCP47_validated": false,
  "limitations": [
    "No IANA language-subtag registry lookup, variants, extensions, private use, grandfathered tags or language matching",
    "Well-formed skeleton does not guarantee actual language-tag registration"
  ]
}
```

## Negative control and next evidence

Compare `sr-Latn-RS` with a tag containing a Unicode extension. The second must be left to a complete versioned tag validator, not guessed from a simplified regex.

**Research limit:** Not full BCP47. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
