# Investigation 25: Community or speaker denial blocks public release

**Origin:** constructed offline study unless otherwise stated. No human participant or original media data was acquired.

A constructed language-archive record has community permission explicitly denied. The metadata-only rights gate returns `do_not_release` even if a license field and a plausible SHA-256 string are provided. A second record claims both permissions documented, public access and bytes/hash present; it returns only `conditionally_eligible_for_human_rights_review`.

**Crucial limit:** the gate has not contacted a speaker or community, authenticated consent, inspected an agreement, recomputed a hash or verified publication rights. A self-reported “documented” flag cannot grant permission. A false hash can be manufactured as easily as a false statement.

**Preservation rule:** retain public metadata and access procedures when materials are restricted; do not treat a denial as a technical defect to bypass. This approach follows community autonomy described by the California Language Archive and UN DESA language policy.

**Evidence status:** This is a reproducible bounded algorithm/method example. Human-language validity and independent review are not established.
