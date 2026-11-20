# 58. Unicode 18: normalization, grapheme clusters, and exact reproducibility

A Unicode code point is not always what users perceive as a written character; grapheme clusters may combine several code points, and writing systems use context-sensitive rules. The Unicode 18.0 version of UAX #29, published as revision 49, specifies default extended grapheme, word and sentence boundary algorithms. UAX #15 revision 58 specifies normalization forms. These are distinct transformations. A computer program that counts Python string elements is generally counting Unicode code points, not extended grapheme clusters, letters, words, phonemes or morphemes.

## Reconstruction

For a decomposed 'e' + COMBINING ACUTE ACCENT, NFC normalization yields a composed 'é' if the relevant mapping exists. For text `café`, canonical normalization changes the code-point sequence without changing intended written word identity in many applications. NFKC performs *compatibility* operations that may erase distinctions such as circled digits. For auditing, retain both the original source bytes and the normalization method/version; never silently overwrite original orthography and declare the normalized bytes equivalent for cultural, historical or forensic purposes.

A complete extended-grapheme algorithm needs the specific Unicode Character Database property tables, the UAX29 rule sequence, tailoring decisions and a versioned conformance test file. The v1 source register gives exact links to Unicode 18 UAX29 and UAX15, but **the original GraphemeBreakTest.txt was not downloaded in this environment**, and the core package does **not** claim UAX29 conformance. The existing Unicode profile is a limited Python Unicode-normalization illustration; the installed `unicodedata.unidata_version` should be recorded before describing a code-point transformation as Unicode 18.

## Failure boundary

UTF-8 decoding, normalization, script identification, grapheme segmentation, orthographic words and natural-language tokenization are separate layers. A combining sequence, emoji ZWJ sequence or Indic conjunct can defeat simplistic character counting or boundary rules. The preservation goal is to store raw bytes, algorithms, property versions and tests in openly documented formats—not just the rendered text as one system displayed it.

**Primary sources:** Unicode UAX #29 revision 49 (2026-09-01), Unicode UAX #15 revision 58 (2026-08-12), and Unicode v3 data/software license. None of those original files is mirrored by this edition.
