# 62. Community authority, language documentation and CARE principles

Preservation can cause harm if a researcher publishes restricted speech, cultural knowledge, identities or recordings without permission. Community members are knowledge holders and potential rights holders, not simply annotation providers. The CARE principles for Indigenous data governance emphasize Collective Benefit, Authority to Control, Responsibility and Ethics. Those priorities complement technical FAIR data concerns; a globally downloadable archive is not automatically an ethically acceptable outcome.

## Reconstruction and governance

A documentation accession packet should record language variety, original source and collection identifiers, speaker and community permissions, access classification, license or reuse conditions, original-byte checksum where permitted, reviewer identity, allowed downstream uses, withdrawal procedures and stewardship responsibility. Crucially, a string field saying `community_permission=documented` is *not* proof that valid consent actually occurred; a trusted institution or community authority must confirm and govern it. Cryptographic byte equality is not a license.

The v1 `review_language_document` method accepts a bounded packet and optional raw bytes, computes SHA-256 from supplied bytes without retaining them in its output, and compares a declared expected hash. It blocks public distribution when permission is denied, access is restricted, permission is unknown or source bytes are absent/mismatched. Even when every caller field says approved and local bytes match, it returns only **eligible_for_external_rights_review_only**, never automatically publishable. This distinction prevents a fabricated metadata form from authorizing publication.

## Preservation beyond extraction

Real linguistic preservation requires community co-design, accessible tools for communities, ongoing support for language education and revitalization, multiple dialects, transparent records of interpretation, and a plan for sensitive/restricted sources. Some materials should remain private or within community custody while scientific summaries and general methods stay openly readable. Data may be available only through negotiated access; marking this as `restricted` is more accurate than inventing a free license.

**Sources:** Global Indigenous Data Alliance CARE principles, CLA/UNESCO existing documentation guidance. The CARE document can carry noncommercial/no-derivative licensing; this package does not mirror it or change its rights.
