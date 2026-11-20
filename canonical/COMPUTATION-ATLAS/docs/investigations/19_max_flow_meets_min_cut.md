# Investigation 19 — max flow meets min cut

**Origin:** author-generated finite mathematical example. No external source observations, AI invocations, or physical measurements were made.

**Observed constructed result:**

```json
{
  "max_flow": 5.0,
  "min_cut_capacity": 5.0,
  "source_side": [
    0
  ],
  "augmentations": 3,
  "flow_cut_gap": 0.0,
  "status": "flow_cut_match_under_declared_network",
  "limitations": [
    "Capacities are caller-supplied; no external effects",
    "Float precision and near-zero residual tolerance may matter for extreme inputs"
  ]
}
```

**Check:** passed. This verifies that the local reference produced the expected outcome for this input; it does not establish universal correctness.

**Limitations:** No provider or traffic measurement

Reproduce with `python -m computation_atlas v02`; compare numerical and graph claims against independent library oracles. Review the relevant chapter for preconditions and false-generalization examples.
