# Synthetic coverage stress test

**Checkpoint 0.7.0. This is generated teaching data, not a physical experiment.**

A fixed-seed simulation uses 20,000 trials of five independent normal readings with unit noise standard deviation and a true mean of zero. The same samples compare the t-based mean interval with a k=2 shortcut. A third condition adds a per-trial shared offset with standard deviation 0.75 and deliberately omits it from the reported standard-error budget. It is a counterexample, not an endorsed method.

| Procedure | Coverage count | Observed rate | 95% Wilson interval for simulation rate |
|---|---:|---:|---|
| iid_normal_student_t | 19017/20000 | 0.95085 | [0.94777, 0.95376] |
| iid_normal_k_equals_2 | 17686/20000 | 0.88430 | [0.87979, 0.88866] |
| shared_offset_omitted_from_budget | 15548/20000 | 0.77740 | [0.77158, 0.78311] |

The first rate is consistent with its nominal 95% under the model. The other conditions show undercoverage under the selected synthetic setup. The offset comparison is not a test of an improved method and supplies no new empirical discovery.

The seed is 7132026. The declared acceptance band for the first procedure was [0.938, 0.962]. Monte Carlo uncertainty is not measurement uncertainty in a real instrument. Repetition of the same seed is reproducibility, not independent evidence.

Run `python tools/coverage_simulation.py` with NumPy available. The full JSON includes counts, rates, standard errors, dependency versions and limitations. See [the method supplement](COVERAGE_METHODS.md).
