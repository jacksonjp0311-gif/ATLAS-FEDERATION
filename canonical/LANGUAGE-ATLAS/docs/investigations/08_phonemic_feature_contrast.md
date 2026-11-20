# Investigation 08: A feature distance is not acoustic similarity

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

Two stipulated phones share place and manner and differ in a binary voicing feature. The algorithm counts one differing category. It has not listened to speech or established that a pair is contrastive in any particular language.

**Reproduced result:**

```json
{
  "differences": [
    "voice"
  ],
  "hamming": 1,
  "features": 3,
  "limitations": [
    "Feature-space differences are a stipulated analytical model, not universal phonetic distance",
    "Distinctive features and phone inventories vary by analysis and language"
  ]
}
```

## Negative control and next evidence

Add a third sound and compare categorical feature dimensions. Test a real contrast only after measuring speakers and finding meaningful lexical evidence.

**Research limit:** Not acoustic distance. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
