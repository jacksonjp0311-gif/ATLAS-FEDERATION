# Investigation 11: A counterexample can refute a universal proposition

**Origin:** constructed offline fixture. No human speaker or authentic corpus.

## Observed result within the specified toy model

Within the invented two-person domain, one individual is explicitly marked not to satisfy the supplied predicate. Under the finite three-valued interpretation, that known negative is sufficient to make a universal statement false, even if other facts are missing.

**Reproduced result:**

```json
{
  "schema": "atlas.language-three-valued/1",
  "truth": "false",
  "operations": 3,
  "world_truth_grounded": false,
  "limitations": [
    "Finite three-valued first-order fragment only",
    "Unknown is not equivalent to false",
    "Predicate assignments are supplied, not observations verified from real world",
    "Natural language interpretation and quantifier scope must be supplied separately"
  ]
}
```

## Negative control and next evidence

Remove the negative fact without adding positive evidence, and inspect how the answer becomes unknown. No real person's occupation or behavior is inferred.

**Research limit:** Depends on provided domain and facts. A passing algorithm check is not a universal linguistic truth.

`python -m language_atlas` reproduces this case without any network connection.
