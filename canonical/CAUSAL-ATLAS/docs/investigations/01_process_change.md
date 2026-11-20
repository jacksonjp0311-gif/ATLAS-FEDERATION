# Investigation A A process improves within groups but looks worse overall

**Data origin: original synthetic example. No workplace measurements.**

## Question and design

The target is the difference in pass probability under two assigned processes for a population with equal easy/difficult job shares. Difficulty is defined before assignment. The example stipulates that difficulty is the only needed adjustment variable; an actual investigation would need evidence for that omission assumption, consistent process versions and stable inspection definitions.

| Difficulty | Existing jobs | Existing successes | New jobs | New successes |
|---|---:|---:|---:|---:|
| Easy | 80 | 64 | 20 | 18 |
| Difficult | 20 | 4 | 80 | 24 |

The existing process passes68/100 jobs, while the new process passes42/100. The crude difference is−0.26. Within easy jobs the difference is0.90−0.80=0.10; within difficult jobs it is0.30−0.20=0.10. Equal target weighting gives0.60−0.50=0.10. The new process was deliberately assigned disproportionately to difficult work.

## Compare the implemented estimators

The shipped `examples/process_rows.json` expands these counts into200 synthetic units. Each row includes a declared baseline covariate, the generating propensity, and generating outcome means. The runtime does not infer those functions from the outcomes. Under these supplied inputs, OR, HT, Hájek and AIPW all produce0.10. This is a designed arithmetic identity, not an empirical competition between methods.

```sh
python -m causal_atlas estimate examples/process_rows.json --nuisance-origin synthetic_oracle
python -m causal_atlas population examples/process_population.json
python -m causal_atlas investigations
```

The sample and population functions are deliberately separate. The first uses observed rows and supplied predictions; the second integrates over a fully authored distribution whose truth is known. A finite sample from a correct model need not reproduce every expectation exactly.

## What could break the real investigation?

If operators decide treatment using a condition not in difficulty, the comparison may remain confounded. If difficult jobs cannot ever receive the existing process, the proposed equal-mix target lacks support. If treatment changes how difficulty is recorded, the stratification is no longer baseline adjustment. If inspection criteria changed, Y itself may not be the same outcome. If only surviving jobs appear in the file, selection needs separate analysis.

A real application should fill the target-study and assumption-ledger templates before using an estimator. At minimum it needs assignment timestamps, intervention versions, baseline-variable definitions, outcome completeness and a reason to believe the adjustment set is sufficient. None is established by this toy table.

## Useful conclusion and forbidden conclusion

The defensible statement is that ignoring a stipulated job-mix difference reverses the contrast in this constructed model, and the declared adjustment recovers its known target. It is not evidence that the user's actual process is beneficial, that every reversal is confounding, or that standardization always fixes a production dataset.

**Evidence:** retained case definitions; original formulas in Chapters2–4; source records HR2006 and AS2015. **Review state:** authored derivation and computation, no external scientific sign-off.
