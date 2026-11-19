# Language Atlas — Scientific Reading Directory v0.1.0
**Observed form → Feature/word analysis → Structural hypothesis → Semantic interpretation → Pragmatic context → Qualified evidence.**
All reconstructions and casebooks are original constructed fixtures, not human-subject experiments or source language corpora.
## Chapters
- [01. What a human language is and what a language model is not](chapters/01_what_a_human_language_is_and_what_a_language_model_is_not.md)
- [02. Speech articulation and the production of linguistic sound](chapters/02_speech_articulation_and_the_production_of_linguistic_sound.md)
- [03. Acoustic phonetics, speech signals and uncertainty](chapters/03_acoustic_phonetics_speech_signals_and_uncertainty.md)
- [04. Signed languages, gesture, and visual linguistic form](chapters/04_signed_languages_gesture_and_visual_linguistic_form.md)
- [05. Phonemes, phones, and allophonic distribution](chapters/05_phonemes_phones_and_allophonic_distribution.md)
- [06. Prosody: stress, tone, timing, and intonation](chapters/06_prosody_stress_tone_timing_and_intonation.md)
- [07. Phonotactics, syllables, and sound-pattern restrictions](chapters/07_phonotactics_syllables_and_sound_pattern_restrictions.md)
- [08. Morphology: words, lexemes, morphemes and segmentation](chapters/08_morphology_words_lexemes_morphemes_and_segmentation.md)
- [09. Inflection, derivation, and nonconcatenative morphology](chapters/09_inflection_derivation_and_nonconcatenative_morphology.md)
- [10. Grammatical categories and cross-linguistic typology](chapters/10_grammatical_categories_and_cross_linguistic_typology.md)
- [11. Lexemes, polysemy and lexical semantic networks](chapters/11_lexemes_polysemy_and_lexical_semantic_networks.md)
- [12. Word boundaries are analytical choices, not whitespace](chapters/12_word_boundaries_are_analytical_choices_not_whitespace.md)
- [13. Writing systems, orthography, scripts and transliteration](chapters/13_writing_systems_orthography_scripts_and_transliteration.md)
- [14. Unicode scalar values, UTF-8, and exact source bytes](chapters/14_unicode_scalar_values_utf_8_and_exact_source_bytes.md)
- [15. Canonical and compatibility normalization are different](chapters/15_canonical_and_compatibility_normalization_are_different.md)
- [16. Grapheme clusters and segmentation across scripts](chapters/16_grapheme_clusters_and_segmentation_across_scripts.md)
- [17. Interlinear glossing, transcripts and scientific accountability](chapters/17_interlinear_glossing_transcripts_and_scientific_accountability.md)
- [18. Formal grammars, constituency and derivation](chapters/18_formal_grammars_constituency_and_derivation.md)
- [19. Dependency syntax and Universal Dependencies](chapters/19_dependency_syntax_and_universal_dependencies.md)
- [20. Word order, head direction and cross-language diversity](chapters/20_word_order_head_direction_and_cross_language_diversity.md)
- [21. Ambiguity in attachment, ellipsis and scope](chapters/21_ambiguity_in_attachment_ellipsis_and_scope.md)
- [22. Compositional semantics and structured meanings](chapters/22_compositional_semantics_and_structured_meanings.md)
- [23. Reference, deixis, anaphora, and shared context](chapters/23_reference_deixis_anaphora_and_shared_context.md)
- [24. Quantification, negation and unknown propositions](chapters/24_quantification_negation_and_unknown_propositions.md)
- [25. Pragmatics, implicature, and cooperative inference](chapters/25_pragmatics_implicature_and_cooperative_inference.md)
- [26. Speech acts, commitments, and conversation structure](chapters/26_speech_acts_commitments_and_conversation_structure.md)
- [27. Discourse coherence, information structure and repair](chapters/27_discourse_coherence_information_structure_and_repair.md)
- [28. Language acquisition, developmental change and learning](chapters/28_language_acquisition_developmental_change_and_learning.md)
- [29. Dialect, register, social variation and linguistic equality](chapters/29_dialect_register_social_variation_and_linguistic_equality.md)
- [30. Historical change, sound correspondence and reconstruction](chapters/30_historical_change_sound_correspondence_and_reconstruction.md)
- [31. Language documentation, endangerment and community control](chapters/31_language_documentation_endangerment_and_community_control.md)
- [32. Corpora, sampling and annotation disagreement](chapters/32_corpora_sampling_and_annotation_disagreement.md)
- [33. N-gram language models, smoothing and perplexity](chapters/33_n_gram_language_models_smoothing_and_perplexity.md)
- [34. Neural language models, transformers and inference limits](chapters/34_neural_language_models_transformers_and_inference_limits.md)
- [35. Translation, equivalence and culturally grounded evaluation](chapters/35_translation_equivalence_and_culturally_grounded_evaluation.md)
- [36. Language identification, tags and multilingual metadata](chapters/36_language_identification_tags_and_multilingual_metadata.md)
- [37. Linguistic uncertainty, misinformation and tool instruction boundaries](chapters/37_linguistic_uncertainty_misinformation_and_tool_instruction_boundaries.md)
- [38. Human knowledge survival: rebuilding language science offline](chapters/38_human_knowledge_survival_rebuilding_language_science_offline.md)

## Working offline

```sh
python -m language_atlas
python -m unittest discover -s tests -q
python tools/check_manifest.py verify .
```
Read `SOURCE_REGISTER.md`, `COVERAGE_MATRIX.md` and `VALIDATION_v0.1.0.md` before using any examples outside a constructed setting.
The exact and complete Unicode UAX 29, BCP 47, full UD parser, natural-language reasoning, real audio analysis and translation are **not** implemented.
All thirty domain content libraries precede Bitwork routing, integrated evaluation and desktop transfer.

## Worked investigations (19)

- [01. Canonical equivalent strings](investigations/01_canonical_norm.md)
- [02. Compatibility normalization is not reversible](investigations/02_compatibility_loss_warning.md)
- [03. Preserve every source byte](investigations/03_utf8_roundtrip.md)
- [04. Reject silent Unicode corruption](investigations/04_invalid_utf8_refusal.md)
- [05. A lexicon creates alternatives](investigations/05_word_boundary_ambiguity.md)
- [06. Segmentation versus morphology](investigations/06_segmentation_compositional.md)
- [07. One surface can have two analyses](investigations/07_morphological_ambiguity.md)
- [08. A feature distance is not acoustic similarity](investigations/08_phonemic_feature_contrast.md)
- [09. Two parse trees, one token sequence](investigations/09_attachment_ambiguity.md)
- [10. Reject under this grammar only](investigations/10_grammar_rejection_not_human_rejection.md)
- [11. A counterexample can refute a universal proposition](investigations/11_finite_quantifier_false.md)
- [12. Unknown is not a negative label](investigations/12_unreported_fact_unknown.md)
- [13. Tree structure is weaker than annotation correctness](investigations/13_ud_basic_dependency_shape.md)
- [14. A tree cannot parent itself](investigations/14_dependency_cycle_refusal.md)
- [15. Predictive likelihood is not language understanding](investigations/15_smoothing_and_probability.md)
- [16. Explicit task exposure breaks the split](investigations/16_training_id_leakage_refusal.md)
- [17. A plausible tag is not registry validation](investigations/17_language_tag_skeleton_only.md)
- [18. Equivalent Unicode can conceal exact duplicates](investigations/18_canonical_text_leakage.md)
- [19. Absence of overlap evidence is not independence](investigations/19_clean_does_not_prove_holdout.md)
