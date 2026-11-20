# Causal Atlas validation and limits

**Content checkpoint 0.1.0 · 12 November 2026**

The actual source suites ran on Python 3.13.5 / Linux: 188 Forge, 218 Measurement, and 75 Causal tests passed without skips (481 total). The inherited Forge aborted-client tests can log BrokenPipeError while passing; this checkpoint makes no repair claim. Source checks use the actual package paths rather than an assumed global installation.

## Scientific-tool checks

The 75 Causal tests cover exact finite probability models, graph structure and d-separation, the sufficient single-exposure back-door criterion, restricted observed adjustment sets, grouped standardization, invalid inputs, source closure and common-node integration. Five original synthetic cases pass. They are controlled teaching examples, not independent experiments or a test of causal discovery on real observations.

A separate NetworkX 3.6.1 `is_d_separator` comparison agrees on **2,536 cases**: all 64 forward-order four-node DAGs with 1,536 endpoint/conditioning comparisons, plus 1,000 seeded comparisons in seven-node DAGs. The local algorithm uses an ancestral moral graph; this checks agreement of computational algorithms, not physical validity of any graph. Seed: 121126. No failures were observed in this finite comparison.

## Shared-node and installation checks

All 34 Causal records and ten relations conform to the same schema used by the preserved Signal, Cymatics and Measurement nodes. The existing shared engine loads 539 records across four nodes and validates context examples for all four without any retrieval-kernel change. Required source/qualification relationships are retained in context assembly.

The new Causal wheel was installed with the baseline Forge and Measurement wheels in an isolated virtual environment using `--no-index --no-deps`. Causal's installed casebook and reference CLI worked; all modules resolved from site-packages rather than the source tree. Causal mathematics has no third-party runtime dependency. Reference retrieval requires the existing shared Forge runtime.

## Reproduce

From Causal's source directory, `python -m causal_atlas casebook` runs the five cases. `python tools/graph_oracle.py` runs the optional NetworkX comparison. The parent collection's `python tools/check_collection.py` sets source paths, runs all three suites, validates the four nodes/context examples and checks that every one of the 771 original baseline members is unchanged. Detailed receipts are in the collection's `receipts/` directory.

## Open checks

This is not final scientific v1 acceptance. No native Windows run, independent human source review, independently authored held-out AI evaluation, empirical causal study, full causal identification implementation, or live Bitwork/AI connection is claimed. The review questions are author-created. Seven source portions were checked; the What If landing page remains navigation-only. Scientific assumptions, semantic interpretation of graphs and observational causal identification must be justified outside these algorithms.
