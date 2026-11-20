# 25. MAST taxonomy: a coded failure label is not task ground truth

The published **MAST-Data / MAD** card identifies 1,642 multi-agent system execution traces from seven frameworks, eight benchmarks and five language-model families. Each full-dataset row includes `mas_name`, `llm_name`, `benchmark_name`, a local `trace_id`, a trace object and a 14-mode annotation map. The dataset is advertised under **CC BY 4.0**; check its primary publication and specific source permissions before redistribution. The card says full-dataset annotations were produced by an **LLM judge**. A separate 19-row inter-annotator file used changing taxonomies across four rounds (18, 17, 17 and 14 modes), so raw mode numbers from different rounds are not interchangeable.

## The denominator is part of the claim

For mode c, define observed positive count `P_c = Σ I(label_i=1)`, known count `K_c = Σ I(label_i∈{0,1})`, and unknown count `U_c=N−K_c`. Report the fraction `P_c/K_c` **only if K_c>0**. If every annotation is unavailable, the fraction is `null`, not 0%. A null label is not a negative observation. Sampling, unlabeled rows and annotation filtering may affect every denominator; a source statement claiming “no failures” from missing codes is invalid.

The `grouped_mast_annotations` method groups by **framework and benchmark**, with a composite identity `(framework, LLM, benchmark, local trace index)`. This prevents deleting distinct traces that reuse a local index. It computes the 14 code counts and conditional proportions for each group. It does not read the raw trace trajectory, make new judgments, infer the reason a real agent failed, or estimate population causal failure rates. Frameworks and benchmarks are not randomly assigned to one another, and observed label prevalence may reflect dataset composition rather than underlying agent quality.

## Structured evidence, not a benchmark claim

The Atlas deliberately includes **zero original full MAST rows** in this v0.3 release: the public dataset card was checked, but the approximately 200 MB source snapshot was not acquired through a verified raw-byte channel. Tests use authorship-identified synthetic fixtures. The source register therefore records the card's public row count and schema with `raw_rows_loaded=0`, preventing a generated example from being confused with an empirical population analysis.

If original data are later acquired with rights and verified hashes, the ingest plan should preserve row-level source paths, corpus revision, full annotation map, missingness, framework/model/task identity, pre-existing task completion ground truth and access restrictions. The code must refuse merging human annotation rounds without a versioned, explicitly evaluated taxonomy mapping. No new LLM judgments should be silently substituted for provided labels.

**Source:** [MAST-Data official dataset card](https://huggingface.co/datasets/mcemri/MAST-Data/blob/main/README.md) and [published NeurIPS 2025 work](https://github.com/multi-agent-systems-failure-taxonomy/MAST). The card supports schema and counts, not independently validated failure probabilities.
