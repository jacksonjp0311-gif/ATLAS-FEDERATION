# 43. Historical sound correspondence: recurrence is evidence, not proof by resemblance

Comparative historical linguistics investigates relationships among languages through systematic sound correspondences, shared innovations, morphology, chronology, and alternative explanations such as borrowing, chance similarity and contact. Similar-looking words do not prove common origin. A table of aligned segment pairs can be an exploratory observation, but it relies on a prior decision about word comparability and alignment. Those judgments must be recorded separately from any inference about language families.

## The constructed alignment model

`aligned_sound_correspondences` accepts stipulated aligned segment sequences for named language IDs, original source IDs and candidate word/item IDs. It counts pairwise segment correspondences except gap columns, rejecting alignment-length mismatches and duplicate item identifiers. It reports language pairs and counts. It never assigns sound-change probabilities, declares cognacy, infers ancestral segments, or constructs a phylogenetic tree.

For toy words /pat/ and /fat/, aligned position counts are p↔f, a↔a, t↔t. That observation alone is insufficient to prove a regular change p→f. The same correspondence should be supported by independently sourced candidate cognate sets, controlled for chronology, lexical borrowing and chance. A relationship of a sound correspondence to a phonological system may vary by environment and grammatical condition. A zero count in an incomplete sample is not evidence of impossibility.

## Reconstruction procedure

Preserve the original orthographic form and source recording or transcription scheme. Normalize IPA only with an explicitly defined mapping; never silently discard diacritics or tone. Build a candidate cognate set, record hypotheses and reasons for accepting or rejecting each alignment, compare recurring correspondences across multiple lexical items and grammatical environments, examine borrowing and geographic contact, and test whether a proposed sound-change system predicts unseen forms.

A robust corpus needs provenance for each source and language classification version. The content should distinguish field observation, transcription, analytical alignment and reconstructed historical claim. The model must permit disagreement and uncertainty rather than synthesizing a confident ancestral form from insufficient data.

**Sources:** Glottolog bibliography and WALS linguistic classification for context, with existing phonetics/phonology chapters. This version implements correspondence counting only, not a scientific reconstruction of any real language.
