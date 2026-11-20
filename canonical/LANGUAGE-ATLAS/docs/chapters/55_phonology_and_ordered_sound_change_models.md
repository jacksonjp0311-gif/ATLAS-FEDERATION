# 55. Phonological representations and ordered sound changes

Phonetics describes measurable articulatory and acoustic events; phonology describes how sounds pattern in linguistic systems. A phonetic segment, phoneme, feature bundle and written letter need not correspond one-to-one. Phonological alternations can be conditioned by surrounding segments, syllable structure, stress, morphology and social variation. Historical sound-change hypotheses must also consider chronology, loanwords, dialect mixture and irregular processes. A computational transformation rule can demonstrate a hypothesis without showing it actually occurred.

## Reconstruction

Take a supplied segment sequence and a sequence of explicitly ordered local rules. A rule includes a target segment, replacement, optional immediate left and right context, and stable rule identifier. For each stage, examine the entire pre-stage sequence and perform simultaneous matches. Carry the result into the next stage. This prevents unintended within-stage cascading and makes chronological ordering inspectable. With input [p,a,t], a rule p→f before a, followed by t→s after a, produces [f,a,s]. Reversing a relevant pair of rules can change results. These strings are *invented*, not a historical reconstruction of a documented language.

The `ordered_sound_changes` method returns each stage's original and resulting sequences plus changed positions. It cannot infer phonemes, assign real dates, prove regular correspondences, or reconstruct a protolanguage. Noninvertibility is common: two distinct inputs can map to one surface sequence. The output therefore declares that reversibility and historical correspondence were not established. The `weighted_segment_alignment` model supplies a separate explicit-cost edit path for proposed segment correspondence, but its scores are not calibrated acoustic or perceptual distances.

## Scientific boundary

A serious comparative study needs a documented corpus, independently judged cognates, language-family sampling, careful separation of sound correspondences from borrowing and chance resemblance, and annotations by speakers or qualified linguists. A neat output string is a useful prediction to test, not evidence the historical event occurred. This is why source, segmentation choices and limitations travel with the result.

**Sources:** IPA and comparative-linguistics material already in Language Atlas's source register; rule-ordering examples are original.
