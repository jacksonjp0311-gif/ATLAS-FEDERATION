# Investigation 21 — FFT round trip

**Origin:** author-generated finite mathematical example. No external source observations, AI invocations, or physical measurements were made.

**Observed constructed result:**

```json
[
  "(1+0j)",
  "(2+5.721188726109833e-18j)",
  "(3+0j)",
  "(4-5.721188726109833e-18j)"
]
```

**Check:** passed. This verifies that the local reference produced the expected outcome for this input; it does not establish universal correctness.

**Limitations:** Round trip is not general numerical stability

Reproduce with `python -m computation_atlas v02`; compare numerical and graph claims against independent library oracles. Review the relevant chapter for preconditions and false-generalization examples.
