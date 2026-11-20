# Investigation 18 — Untrusted trace content masquerades as an instruction

**Origin:** authored malicious-looking string in a structured metadata fixture. A test adds `gen_ai.input.messages` containing an instruction to a tool span's attributes. This attribute is outside the research adapter's permitted metadata allowlist, so the entire span is rejected. The text is neither interpreted as authority nor copied into the output.

That is a local input-validation result, not a guarantee against prompt injection in an actual agent. A privileged system that reads the raw trace elsewhere might still be exposed. A well-designed real trace pipeline therefore separates source content from instructions, uses minimal data collection, enforces host tool policies, and audits the effects rather than granting capability through source text.

The method deliberately does not attempt to detect all malicious content semantically. Even benign text may contain personal data. Separate retention and rights rules are necessary for actual MAST or user-specific agent trace ingestion. The casebook contains no real credentials or sensitive user messages.
