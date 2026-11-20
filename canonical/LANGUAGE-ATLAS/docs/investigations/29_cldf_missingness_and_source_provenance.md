# Investigation 29: Source-aligned tables must distinguish unknown from absent observations

**Origin:** constructed offline study unless otherwise stated. No human participant or original media data was acquired.

An imaginary CLDF-style feature table records two languages with an observed feature value and a third whose source does not report the feature. The third case must remain unknown rather than negative. Another source can explicitly say the observed value is unknown; CLDF's metadata/rows allow those two types of absence to be represented distinctly.

**Failure:** concatenate tables with the same `Language_ID` but different classification editions or mismatched source references. Aggregated rates can become plausible yet invalid. Reference integrity requires stable IDs, schema version, field definitions, source bibliography, transformation code, null semantics and hash-linked original data where permitted.

This package has no full CLDF validator and does not claim original CLDF dataset conformance. It preserves an original methodological explanation and source links for future implementation.

**Evidence status:** This is a reproducible bounded algorithm/method example. Human-language validity and independent review are not established.
