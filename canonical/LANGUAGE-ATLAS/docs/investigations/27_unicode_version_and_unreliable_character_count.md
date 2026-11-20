# Investigation 27: Counting code points is not Unicode grapheme segmentation

**Origin:** constructed offline study unless otherwise stated. No human participant or original media data was acquired.

A string with a combining acute accent may use two Unicode scalar values but display as one grapheme cluster. A family emoji may use multiple scalars and joiners. The baseline `unicode_profile` correctly reports `grapheme_cluster_count=null` rather than pretending the code-point count equals user-perceived characters.

Unicode UAX #29 v18 revision 49 includes rules governing Indic conjunct sequences and emoji/flag boundaries. A parser whose Unicode property database lags that revision cannot claim exact conformance merely because it normalizes to NFC. The underlying Python Unicode database version must be recorded separately.

**Needed later:** acquire rights-cleared official Unicode test vectors with exact version and hashes, then implement and validate a complete extended-grapheme segmenter. Handwritten shortcuts that work for Latin accents can fail on Indic scripts or emoji.

**Evidence status:** This is a reproducible bounded algorithm/method example. Human-language validity and independent review are not established.
