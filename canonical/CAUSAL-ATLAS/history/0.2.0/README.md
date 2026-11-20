![Approved Atlas Forge collection artwork](assets/atlas_forge_knowledge_hub.png)

# Causal Atlas

**Reference development edition0.2.0 · common contract1.0 · James Paul Jackson research program**

When a process changes and results improve, the difficult question is why. Causal Atlas organizes the definitions, assumptions, designs, calculations and counterexamples needed to investigate that question without confusing association with an established effect.

This edition goes beyond a catalog. Eight reference chapters connect the question, identification argument, estimator, diagnostics, sensitivity analysis and report. Three detailed original investigations show successful adjustment, failure of wrong working models, and observations that do not determine even an effect's sign. The underlying evidence is reusable by people and the existing Forge runtime.

**Scope:**73 records:38 bounded literature capsules,19 authored method/example/protocol records and16 source cards. Twenty-six typed relations retain conditions with claims. These counts are not measures of completeness or independent validation. All34 earlier record revisions remain intact.

## Explore

| Entry | Purpose |
|---|---|
| [Reference guide](docs/REFERENCE_GUIDE.md) | Eight substantive chapters and an investigation reading path |
| [Worked investigations](docs/investigations/01_process_change.md) | Move from a question to calculations, failures and data requests |
| [Original casebook](docs/CASEBOOK.md) | Five retained synthetic cases |
| [Source register](docs/SOURCE_REGISTER.md) | Exact inspected portions, authors, versions, correction and rights limits |
| [Coverage and gaps](docs/COVERAGE_MATRIX.md) | What is developed, implemented, limited or absent |
| [Estimator contract](docs/ESTIMATOR_CONTRACT.md) | Input shapes, formulas, size limits and no-inference boundary |
| [Study templates](docs/templates/TARGET_STUDY.md) | Blank design, assumptions, analysis and reporting aids |
| [Development review rubric](evaluations/depth_review_v0.2.0.json) | Twenty additional authored questions, not an independent held-out benchmark |
| [Validation](docs/VALIDATION.md) | Executed checks and unrun work |

## Reproduce

From this source folder, Python3.10+:

```sh
python -m causal_atlas investigations
python -m causal_atlas estimate examples/process_rows.json --nuisance-origin synthetic_oracle
python -m causal_atlas population examples/process_both_models_wrong.json
python -m causal_atlas missing-bounds examples/missing_outcomes.json
python -m unittest discover -s tests -v
```

Use the complete collection runner for Forge-dependent integration tests; standalone Causal testing can skip those when Forge is absent. CLI estimates use supplied nuisance predictions, never fit or authenticate them, and do not provide confidence intervals. No weights are silently clipped.

## What the failures teach

Correctly supplied models in the authored job-mix case recover+0.10 where the crude comparison is−0.26. When both working components are wrong, augmented weighting can also return−0.26. In a separate missing-outcome case, an observed-only+0.20 comparison is compatible with full-arm differences from−0.16 to+0.34. Successful code execution preserves these failures rather than turning them into accepted causal findings.

Every example is synthetic. No participant or production dataset, independently reviewed causal conclusion, final scientific v1 or improved AI performance is claimed. Existing Forge navigation is unchanged, desktop transfer is later, and Materials remains queued. The approved artwork is decorative, not a scientific graph. Linked publications retain their rights; full texts are not mirrored.
