# 64. Linguistic datasets: lineage, sampling, contamination, and independent assessment

A multilingual dataset is an observed sample constructed through decisions about what counts as a language, variety, text, speaker, sentence and annotation. It is not a transparent representation of the world's languages. Data can be concentrated in well-documented language families, regions, writing systems and institutions; a global score weighted by number of texts can misrepresent cross-linguistic coverage. Family and areal dependencies violate naïve independence assumptions in many comparisons.

## Reconstruction

For each dataset version preserve publisher/collector, date, rights, original bytes and hash where allowed, normalization/tokenization decisions, language and variety identifiers, family/area metadata, data splits, annotation schemas, label provenance, missing-value policy and evaluation code. CLDF provides CSV/metadata conventions for cross-linguistic datasets, while UD uses CoNLL-U for dependency-annotated sentences. Neither format inherently certifies annotation validity or representative sampling. Enhanced UD graphs may contain additional relations and empty nodes; a simple tree parser is not a full standard-conformance checker.

When evaluating a model, split by language family or source where appropriate to test generalization rather than memorization. Prevent exact and near-duplicate document leakage between training and evaluation; a few different IDs do not establish independence if both refer to the same sentence or translation. Record missing outcomes rather than treating unknown as negative.

## Survival boundary

Source card counts are not enough for an archive intended to survive infrastructure collapse. Without original, permitted source bytes, data dictionaries and transformation code, a future researcher cannot reproduce many claims. The v1 release therefore reports selected public documentation and newly authored examples; **no real WALS, UD, CLDF or linguistic media datasets were downloaded**. Community-controlled sources may require access restrictions that a generic open archive cannot override.

**Sources:** CLDF specification, Universal Dependencies v2, WALS methodology, and existing source-acquisition ledger.
