# 48. Unicode 18 and the requirement to version text segmentation

Text systems often count code points but present grapheme clusters to users. The Unicode Consortium's Standard Annex #29 defines default grapheme, word and sentence boundaries, and its rules change as the standard evolves. A single displayed grapheme may contain multiple scalar values, such as a letter plus a combining mark, an emoji sequence using a joiner, or a regional-indicator flag sequence. Counting code points with `len(text)` is not equivalent to counting perceived characters or word boundaries.

## Version evidence

The published UAX #29 revision 49, associated with Unicode 18.0.0 (1 September 2026), describes legacy and extended grapheme clusters and includes rules governing Indic conjunct linking, emoji joiners and regional indicators. The exact Unicode property databases and rule versions matter. Python's `unicodedata` carries its own version, which may lag the latest Unicode Standard. A language archive must record both the text's original Unicode code points and the segmentation implementation/version used to derive boundaries.

Neither the original v0.1 `unicode_profile` nor the new v0.2 methods implement normative UAX 29 extended grapheme segmentation. The profile deliberately returns `grapheme_cluster_count=null` instead of pretending that code-point count is correct. That refusal remains important for accessibility, UI cursor motion, text comparison and cross-script evaluation.

## Reconstruct without data loss

Keep original source bytes, encoding, normalization form, segmentation library/version, and token boundary offsets. Normalization forms NFC and NFKC differ: compatibility normalization can deliberately collapse distinct glyph semantics. If normalized strings are used to detect benchmark leakage, preserve the raw-to-normalized transformation and do not claim that exact string comparison detects all paraphrases or cross-language translations.

A future implementation should use a properly versioned Unicode property database and a conformance test suite, not a handmade approximation of emoji/Indic rules. Only then can the archive claim UAX 29 conformity for a specific version. Code that works on English text may silently fail on Thai, Khmer, Devanagari or emoji clusters.

**Source:** Unicode UAX #29 revision 49, v18.0 (2026-09-01) and the Unicode Standard; inspected published overview and boundary-rule sections, not original test-vector bytes.
