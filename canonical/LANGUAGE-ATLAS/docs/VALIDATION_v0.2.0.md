# Language Atlas v0.2.0 — Verified Engineering and Scientific Boundaries

**Status:** research reference development, not scoped v1.0 or independently validated linguistic knowledge. No live translation model, speech recognition, field recording, sign-language video, or speaker interview was used.

## Executed verification in source tree

- **1,519 tests passed, zero failures/errors/skips**, across Forge 188, Measurement 218, Causal 233, Materials 122, Control 244, Agent 251, Computation 128 and Language 135.
- **4,407 independent constructed numerical comparisons**: token alignment vs independent edit recursion, BLEU precision and brevity arithmetic, family-weighted vs NumPy aggregations, tiny PCFG inside/Viterbi derivation, and multimodal annotation timing.
- **43 qualified full-collection retrieval contexts**, seven earlier domain suites and complete JSON schema checks passed. Standard Draft 2020-12 was sampled on bounded examples while fast-compiled schema validated the corpus, consistent with previous releases.
- Clean offline installation of the standalone Language 0.2 wheel succeeds with exactly **224 records and 222 local relationships**. The full nine-node federation includes five additional cross-domain relationships, for 227 Language edges total and 934 relationships in the corpus.
- Historical preservation audit: **1,884 protected files byte-identical** against the immutable Language v0.1 source archive; all 167 old Language record revisions and 167 old full relations retained exactly.

## Scientific limits

- No original UNESCO, WALS, Unicode, CLDF, ACL paper, or language corpus bytes were acquired into this package; source cards remain bibliography and scoped summaries. Unicode 18 GraphemeBreakTest original download was attempted but blocked, and is **not claimed acquired**.
- BLEU here is unsmoothed and caller-tokenized, **not SacreBLEU**. A perfect lexical match is not semantic truth or cultural adequacy.
- A PCFG score is conditional on a stipulated grammar and is not a human grammaticality judgment. A structural correspondence is not cognacy.
- Permission labels in rights audit cannot authorize redistribution or override community/speaker restrictions.
- Multimodal annotation timestamps are synthetic and no real sign video was inspected.
- No independent linguistic expert, native-speaker panel, licensed primary-source mirror, formal Unicode UAX 29 conformance, held-out multilingual benchmark or Bitwork routing quality experiment was conducted.

## Reproduce

```sh
python -m language_atlas advanced
python -m unittest discover -s tests -q
python tools/numerical_oracle_v0.2.0.py
python ../tools/check_collection.py --out /tmp/new-receipt
```

Final archived ZIP checksum and extracted replay are recorded in the separate full-release audit, **only after verification**.
