# Investigation 20 — exact linear system with rational residual

**Origin:** author-generated finite mathematical example. No external source observations, AI invocations, or physical measurements were made.

**Observed constructed result:**

```json
{
  "solution": [
    "2",
    "1"
  ],
  "exact_residual_zero": true,
  "status": "unique_solution_for_supplied_rational_matrix",
  "limitations": [
    "No floating-point conditioning estimate or large sparse solver",
    "Input conversion from binary float preserves its rounded value"
  ]
}
```

**Check:** passed. This verifies that the local reference produced the expected outcome for this input; it does not establish universal correctness.

**Limitations:** Input measurement uncertainty not assessed

Reproduce with `python -m computation_atlas v02`; compare numerical and graph claims against independent library oracles. Review the relevant chapter for preconditions and false-generalization examples.
