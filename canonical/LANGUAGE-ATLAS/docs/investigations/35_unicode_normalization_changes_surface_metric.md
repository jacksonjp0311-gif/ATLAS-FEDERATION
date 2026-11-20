# Investigation 35 — A visually similar word receives a different score

The strings `café` (decomposed) and `café` (composed) can render similarly. A literal Unicode code-point n-gram scorer sees different sequences, so its score is below 1. Comparing composed text to itself yields 1. This is expected for an exact-code-point metric and not evidence that the spellings differ in communicative meaning.

The v1 scorer intentionally **does not implement official chrF or Unicode 18 grapheme cluster segmentation**. Normative UAX #29 conformance would require Unicode 18 property tables and the original GraphemeBreakTest.txt, which were not acquired here. A result must retain its normalization, code-point/grapheme unit, and Unicode-data version.

No actual translation was scored or evaluated by a human.
