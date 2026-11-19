# ATLAS FORGE — Language Atlas v1 primary-source preservation plan

**14 November 2026 · Scientific-content edition v1.0.0**

The program's preservation criterion is unusually demanding: human beings and future AI systems must be able to *reconstruct* concepts, observations, assumptions, derivations and counterarguments without depending on their original cloud providers. The current nine-node federation is not at that standard for source originals. It has **435 bibliographic source cards but zero original publisher files authenticated locally** by its strict byte-provenance audit. Original Atlas explanations and algorithms remain available offline; the missing authentic primary sources are a separate risk.

## Priority A — Unicode conformance and orthographic continuity

Obtain the **Unicode 18.0** version-pinned UAX #29 extended grapheme, word and sentence segmentation test files, Character Database properties, and UAX #15 normalization test files from official Unicode distribution directories. Record URL, publication version, HTTPS retrieval/redirect history, exact original bytes, acquisition time and SHA-256. Preserve a copy of the **Unicode License Version 3** notice with the acquired data, satisfying its license conditions. The UAX #29 revision 49 page and UAX #15 revision 58 page are documented source references, not locally authenticated original normative test bytes. An attempted direct download in this runtime did not complete; do not mark those files acquired.

Separate four states: original bytes available; correct Unicode-version data installed; a conformant tested implementation; and actual linguistic grapheme/word interpretation. Only the first three can be established by the normative files and a conformance suite; language-specific tailoring and cultural orthography require independent analysis. Current Python `unicodedata.unidata_version` is **15.1.0** in the verified runtime, not Unicode 18. Never treat its code-point operations as proof of Unicode 18 segmentation.

**Official references:** https://www.unicode.org/reports/tr29/tr29-49.html ; https://www.unicode.org/reports/tr15/tr15-58.html ; https://www.unicode.org/license.txt .

## Priority B — Open linguistic datasets with precise licensing

Prefer public, source-identified and reproducible subsets of CLDF, Universal Dependencies, WALS, PHOIBLE and carefully selected lexical corpora with verified reuse permission. Pin upstream repository commits or official publication releases, including treebank-specific licenses, annotation schemes, original byte hashes, parser transformations and missing-value semantics. Do not use a general site-level license to override a restricted dataset's rights. Normalize only into a distinct derived copy; preserve authentic Unicode and original metadata separately.

The v1 reference includes no authentic WALS/CLDF/UD corpus rows and no human-validated translation or language-model benchmark. These are not simply test failures to patch with synthetic rows. They require actual source acquisition and independent linguistic judgment.

## Priority C — Community-governed endangered and signed languages

Access is not synonymous with the right to redistribute. Indigenous and other communities may control culturally sensitive words, recordings and stories; speakers and signers may require independent consent. Adopt CARE data-governance principles—Collective Benefit, Authority to Control, Responsibility and Ethics—alongside technical reproducibility. A restricted item can be *successfully preserved under controlled custody* without becoming public. Maintain permissions, allowed uses, withdrawal and consent status, custodians, retention policy, translations, annotation rights, and a way to maintain community governance after a change in archive operator.

The v1 `review_language_document` function calculates SHA-256 only on caller-provided bytes and never authenticates community consent. Even its most favorable output is eligibility for external review, **not publication approval**. No authentic speaker, signer or consent records were acquired in this edition.

## Priority D — Scientific verification and pedagogical reconstruction

For each major chapter, preserve sources and peer-review status, an original human-readable derivation, a worked counterexample, an exact or separately coded mathematical oracle, and a corrected/superseding revision trail. Validate speaker judgments, historical comparisons, translation adequacy and typological sampling separately from software. A constrained finite-state recognizer that accepts a token sequence proves nothing universal about human grammaticality. An exact BLEU or character n-gram score is not translation comprehension.

## Restore drill and pass/fail standard

After acquiring rights-cleared source files, rebuild the evidence inventory and re-seal the release. Restore on a disconnected second host; verify all source-byte hashes, original licensing notices and complete schema/reference closure, reconstruct one phonological analysis and one formal semantic interpretation from the manual, run the relevant Unicode conformance suite, and record any missing original. Independent community representatives must participate where their knowledge and rights are implicated. Only then upgrade individual source records from L0/L1 bibliography to authenticated local-byte status. The entire knowledge vault remains incomplete until every relevant domain's source and content gates are met.

**Work order is fixed:** finish all thirty domain content libraries, then build Bitwork routing, then run independent integrated evaluations and complete desktop transfer. The preservation debt should remain visible throughout that process.
