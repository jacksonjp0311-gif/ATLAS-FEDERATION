# Language Atlas v0.1.0 — Scientific and Engineering Release Receipt

**Scientific status:** first source-linked, offline-readable reference edition. Not independently reviewed or scoped content v1.0. No real speaker or language-model evaluation has occurred.

## Executed software evidence

- All nine-node regression suites: **1457 passed, zero failures, zero skips**, including the Language node's 73 tests. Historical Agent and Computation tests run against their exact archived prior-version node counts.
- **2640 independent finite/constructed comparisons**: independent_segmentation_enumeration 350, independent_recursive_CYK_counts 390, independent_bigram_probability 450, independent_three_valued_quantifiers 840, unicode_canonical_and_raw_byte_integrity 360, conllu_independent_tree_shape 250. These are **not** actual human-language corpora, universal proofs or live multilingual model benchmarks.
- Entire new common registry: nine nodes, **1,642 records, 874 qualified relations**, **421 source cards**. All 37 representative source-linked context queries and the schema validation passed.
- **2,280 files from the previous eight-node release verified byte-identical**; all 1,475 earlier record revisions and 707 relationship revisions remain unchanged.
- Clean offline wheel installation passed for Language v0.1, exposing 167 standalone records, 162 internal relations and 19 constructed casebook cases. The five cross-domain relations remain in the full federation only.

## Scientific and source limits

- Bibliographic source cards include Unicode UAX15/29, IPA, WALS, PHOIBLE, Universal Dependencies, Leipzig rules, Stanford formal semantics, Jurafsky/Martin and others. No original publisher texts, data, recordings, sign-language videos or community field notes were copied into this archive.
- **Zero authenticated original primary-source files** under the strict survival audit. Some primary resources are CC BY/CC BY-SA; others are proprietary or depend on specific community permissions. The source register differentiates them.
- No full Unicode 18.0 segmentation implementation or normative test suite. Python's runtime Unicode database may be older than published Unicode annexes.
- No universal parser, complete CoNLL-U v2 validator, real morphology/phonology discovery, normative BCP47 registry validation, human-subject study or independent model evaluation.
- Full source schema validation uses fast compiled JSON Schema for all records/relations/contexts plus selected Draft 2020-12 samples and the exact source-closure runtime. It is not a peer review of the scientific claims.

## Reproduction

`python -m language_atlas` in `LANGUAGE-ATLAS`, `python -m unittest discover -s tests -q`, `python tools/numerical_oracle.py`; then from the collection root `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, and `python tools/check_collection.py --out /unique/external/path`. The separate external release JSON records the extracted ZIP replay after it actually runs.
