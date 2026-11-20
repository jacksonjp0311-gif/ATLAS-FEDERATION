# 59. Scripts, orthographies, bidirectionality and identifier hazards

A language is not a script, and a script is not a full orthography. One language may have multiple writing systems, and one script may serve multiple languages. Writing direction, combining marks, shaping, font behavior and line breaking require separate models. A visually correct string can have a different sequence of code points from another rendering, which matters for text search, citations, passwords and program identifiers.

## Reconstruction

Store code-point-level raw text and declared encoding, writing direction, script(s), language variety and normalization status. If a string contains mixed right-to-left and left-to-right spans, the Unicode Bidirectional Algorithm governs display order under its context and formatting controls; do not assume visual order equals logical character order. A typed language tag (e.g. BCP 47 with a script subtag) is metadata, not proof that the text was written in that language. For historical scripts, preserve photographs/scans where rights permit and a faithful transliteration with editorial provenance.

A security-sensitive system must also recognize visually confusable symbols, invisible joiners and mixed-script identifiers. However, a risk flag is not a universal prohibition: multilingual text regularly combines scripts legitimately. A text inspector should report code-point identity, script and policy context before a human decides whether something is deceptive. A language preservation tool should not erase diacritics, standardize culturally specific orthography, or replace source glyphs without preserving the original.

## Limits

The v1 package includes basic Unicode normalization and a bounded code-point n-gram score. It does not implement full Unicode bidirectional shaping, script identification, collation, identifier security or UAX29 segmentation. Those are separate conformance tasks requiring version-locked Unicode data and official test suites. A visually plausible screenshot is not a byte-level source artifact.

**Sources:** Unicode 18 UAX #15 and #29 and existing Language Atlas writing-system and BCP47 source cards.
