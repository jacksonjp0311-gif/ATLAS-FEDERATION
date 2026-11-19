# Berkeley 1973 admissions — attributed real-data descriptive reproduction

## Provenance and rights

Source: R base `datasets::UCBAdmissions`, published CRAN reference manual (https://cloud.r-project.org/doc/manuals/r-release/packages/datasets/refman/datasets.html), reflecting applicant counts in the six largest Berkeley graduate departments in 1973. The 24 aggregate numbers are transcribed from public teaching references (the source full paper and original R CSV bytes are not bundled). The historical table is not sampled randomly, has no randomized treatment, and does not establish a causal interpretation of the recorded-sex grouping.

The Rdatasets collection explicitly says its maintainer was unable to establish definitive reuse rights for all included datasets: https://github.com/vincentarelbundock/Rdatasets. The Atlas therefore does not mirror that upstream CSV or its documentation. The original upstream-byte hash is null. The local numeric transcription has its own release manifest hash; that hash does not establish upstream authorship. All calculations are reproducible from `examples/ucb_admissions.json`.

## Numerical reproduction

| Recorded group | Admitted | Total applications | Crude admit rate | Pooled-department standardized rate |
|---|---:|---:|---:|---:|
| Male | 1198 | 2691 | about 44.52% | about 38.73% |
| Female | 557 | 1835 | about 30.35% | about 43.00% |

All 4,526 applications are classified in the 24-cell six-department table. The female-minus-male crude difference is roughly **−14.16 percentage points**. When both groups' department-specific rates use the combined application distribution as weights, the difference is about **+4.26 points**. No significance test or causal model is implied by this simple standardization. A separate source lists the published numeric table: https://utstat.utoronto.ca/~brunner/oldclass/312f22/lectures/312f22ContingencyTables-R.pdf (linked only; not mirrored).

Run `python -m causal_atlas ucb-admissions examples/ucb_admissions.json` or the installed `advanced-casebook` command. The output explicitly contains `causal_identification_verified: false`. Department choice and omitted qualifications are scientifically important, and this table does not establish causes of admission decisions or adjudicate discrimination. It covers only six departments in 1973.

**Reproduction class:** source-attributed historical observational *descriptive* analysis. **Not:** randomized trial, cause identification, peer review, complete raw-file archival replication, or independent experimental result.
