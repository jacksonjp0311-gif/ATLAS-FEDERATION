# Language Atlas — Constructed Executable Investigations

All 19 cases are author-created input fixtures; no real language corpus, audio, video, speaker interview, model performance or independent translation quality was measured.

## Investigation 01 — canonical_norm

**Observed structure:** `{"schema": "atlas.language-unicode-profile/1", "raw_sha256": "81ef060bcd98adc7824eb5c1ada83c32491b16018e11e79f00ab9d09e04b015a", "utf8_bytes": 6, "code_point_count": 5, "categories": {"Ll": 4, "Mn": 1}, "nfc": "café", "nfkc": "café", "nfc_changed": true, "compatibility_mapping_changed": false, "grapheme_cluster_count": null, "unicode_database_version": "15.1.0", "limitations": ["Python code points are not user-perceived grapheme clusters", "NFKC can erase distinctions; original raw text retained only as a hash here", "This is not an implementation of UAX 29 grapheme, word or sentence boundaries"]}`

**Limitation:** Not grapheme segmentation.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 02 — compatibility_loss_warning

**Observed structure:** `{"schema": "atlas.language-unicode-profile/1", "raw_sha256": "9e96ca1ce18ffb97f67c1230d8282320058da75aa86fc44fb435d25c512a5423", "utf8_bytes": 3, "code_point_count": 1, "categories": {"No": 1}, "nfc": "①", "nfkc": "1", "nfc_changed": false, "compatibility_mapping_changed": true, "grapheme_cluster_count": null, "unicode_database_version": "15.1.0", "limitations": ["Python code points are not user-perceived grapheme clusters", "NFKC can erase distinctions; original raw text retained only as a hash here", "This is not an implementation of UAX 29 grapheme, word or sentence boundaries"]}`

**Limitation:** NFKC loses some distinctions.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 03 — utf8_roundtrip

**Observed structure:** `{"text": "mañana", "bytes_sha256": "f968682da39382523ffa34f7e9e8e84e337eacc30fa2e70435c8ed70e1ff0ff7", "roundtrip": true}`

**Limitation:** No broken UTF-8 accepted.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 04 — invalid_utf8_refusal

**Observed structure:** `{"refused": true}`

**Limitation:** Malformed transport is rejected.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 05 — word_boundary_ambiguity

**Observed structure:** `{"schema": "atlas.language-segmentation/1", "segmentations": [{"tokens": ["therapist"], "cost": 0}, {"tokens": ["the", "rapist"], "cost": 5}], "count_listed": 2, "saturated": false, "complete_count_proven": true, "limitations": ["Results are relative to the supplied lexicon/cost; unknown words have no path", "Cap truncation prevents exact ambiguity counts", "This does not implement script-specific word segmentation"]}`

**Limitation:** Toy lexicon, not UAX 29.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 06 — segmentation_compositional

**Observed structure:** `{"schema": "atlas.language-segmentation/1", "segmentations": [{"tokens": ["un", "seen"], "cost": 1}], "count_listed": 1, "saturated": false, "complete_count_proven": true, "limitations": ["Results are relative to the supplied lexicon/cost; unknown words have no path", "Cap truncation prevents exact ambiguity counts", "This does not implement script-specific word segmentation"]}`

**Limitation:** Not morphological truth.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 07 — morphological_ambiguity

**Observed structure:** `{"schema": "atlas.language-morphology/1", "surface": "flies", "analyses": [{"lemma": "fly", "features": {"Number": "Plur", "POS": "NOUN"}, "source_id": "toy-n1"}, {"lemma": "fly", "features": {"Number": "Sing", "POS": "VERB", "Person": "3"}, "source_id": "toy-v1"}], "status": "found", "disambiguated_by_context": false, "limitations": ["Lexicon is caller-supplied and incomplete", "No universal morphology rules or semantics inferred"]}`

**Limitation:** Analyses are corpus-supplied.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 08 — phonemic_feature_contrast

**Observed structure:** `{"differences": ["voice"], "hamming": 1, "features": 3, "limitations": ["Feature-space differences are a stipulated analytical model, not universal phonetic distance", "Distinctive features and phone inventories vary by analysis and language"]}`

**Limitation:** Not acoustic distance.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 09 — attachment_ambiguity

**Observed structure:** `{"schema": "atlas.language-cyk/1", "accepted": true, "parse_count_cap": 1000000, "parse_count": 2, "saturated": false, "count_is_exact": true, "witness_tree": ["S", ["NP", "robots"], ["VP", ["V", "see"], ["NP", ["NP", "astronomers"], ["PP", ["P", "with"], ["NP", "telescopes"]]]]], "grammar_fragment": "CNF lexical and binary productions only", "limitations": ["No universal/natural-language grammaticality inference", "Specified grammar alone controls ambiguity", "Parse count is not exact if cap saturated", "Unknown tokens are rejected by this grammar, not impossible in human language"]}`

**Limitation:** Grammar is constructed CNF.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 10 — grammar_rejection_not_human_rejection

**Observed structure:** `{"schema": "atlas.language-cyk/1", "accepted": false, "parse_count_cap": 1000000, "parse_count": 0, "saturated": false, "count_is_exact": true, "witness_tree": null, "grammar_fragment": "CNF lexical and binary productions only", "limitations": ["No universal/natural-language grammaticality inference", "Specified grammar alone controls ambiguity", "Parse count is not exact if cap saturated", "Unknown tokens are rejected by this grammar, not impossible in human language"]}`

**Limitation:** Unknown under this grammar, not universally ungrammatical.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 11 — finite_quantifier_false

**Observed structure:** `{"schema": "atlas.language-three-valued/1", "truth": "false", "operations": 3, "world_truth_grounded": false, "limitations": ["Finite three-valued first-order fragment only", "Unknown is not equivalent to false", "Predicate assignments are supplied, not observations verified from real world", "Natural language interpretation and quantifier scope must be supplied separately"]}`

**Limitation:** Depends on provided domain and facts.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 12 — unreported_fact_unknown

**Observed structure:** `{"schema": "atlas.language-three-valued/1", "truth": "unknown", "operations": 3, "world_truth_grounded": false, "limitations": ["Finite three-valued first-order fragment only", "Unknown is not equivalent to false", "Predicate assignments are supplied, not observations verified from real world", "Natural language interpretation and quantifier scope must be supplied separately"]}`

**Limitation:** Missing is not false.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 13 — ud_basic_dependency_shape

**Observed structure:** `{"schema": "atlas.language-conllu-basic-subset/1", "sentences": [{"forms": ["Ada", "reads", "."], "heads": [2, 0, 2], "root_index": 2, "comments": ["# sent_id = toy1", "# text = Ada reads."]}], "sentence_count": 1, "conllu_full_conformance_certified": false, "limitations": ["Not a complete CoNLL-U validator: no multiword tokens, empty nodes, enhanced dependencies or full feature validation", "Valid dependency shape does not imply correct linguistic annotation or grammaticality"]}`

**Limitation:** Not full UD conformance.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 14 — dependency_cycle_refusal

**Observed structure:** `{"refused": true}`

**Limitation:** No semantic annotation assessment.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 15 — smoothing_and_probability

**Observed structure:** `{"schema": "atlas.language-bigram-score/1", "evaluation_id": "heldout-c", "tokens_scored": 3, "log2_probability": -4.614709844115208, "perplexity": 2.904392866781852, "train_id_disjoint": true, "independent_language_understanding_verified": false, "limitations": ["This is a small-order surface distribution; low perplexity is not semantic understanding", "Exact-sequence training leakage checks cannot detect paraphrases or other contamination", "OOV mapping and caller-provided tokens determine all scores"]}`

**Limitation:** Perplexity is not understanding.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 16 — training_id_leakage_refusal

**Observed structure:** `{"refused": true}`

**Limitation:** Paraphrase leakage not checked.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 17 — language_tag_skeleton_only

**Observed structure:** `{"schema": "atlas.language-tag-skeleton/1", "canonical_casing_only": "sr-Latn-RS", "language": "sr", "script": "Latn", "region": "RS", "registry_validated": false, "normative_BCP47_validated": false, "limitations": ["No IANA language-subtag registry lookup, variants, extensions, private use, grandfathered tags or language matching", "Well-formed skeleton does not guarantee actual language-tag registration"]}`

**Limitation:** Not full BCP47.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 18 — canonical_text_leakage

**Observed structure:** `{"schema": "atlas.language-leakage-audit/1", "overlapping_ids": [], "exact_nfc_text_hashes": ["850f7dc43910ff890f8879c0ed26fe697c93a067ad93a7d50f466a7028a9bf4e"], "clean_under_exact_tests": false, "semantic_leakage_ruled_out": false, "limitations": ["NFC exact hashes do not detect paraphrases, translations or answer exposure", "A split that passes this test is not independently verified as held out"]}`

**Limitation:** No semantic duplicates checked.

**Reproduce:** `python -m language_atlas` in the standalone package.

## Investigation 19 — clean_does_not_prove_holdout

**Observed structure:** `{"schema": "atlas.language-leakage-audit/1", "overlapping_ids": [], "exact_nfc_text_hashes": [], "clean_under_exact_tests": true, "semantic_leakage_ruled_out": false, "limitations": ["NFC exact hashes do not detect paraphrases, translations or answer exposure", "A split that passes this test is not independently verified as held out"]}`

**Limitation:** Cannot certify independent benchmark.

**Reproduce:** `python -m language_atlas` in the standalone package.
