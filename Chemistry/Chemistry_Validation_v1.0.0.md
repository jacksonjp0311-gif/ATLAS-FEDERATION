# Chemistry Atlas v1.0.0 — executed software verification and scientific limits

**Status:** scoped content milestone; independent laboratory science, original-source archival completeness, semiconductor fabrication and qualified safety review remain **HOLD**.

## Executed release-source tests

- **1,923 tests passed, zero failures, errors and skips** across the eleven-node Atlas federation. The unchanged 68-test Chemistry v0.1 and 60-test Chemistry v0.2 suites run against their original historical source/registry snapshots; Chemistry v1 tests are separate and do not weaken prior expectations.
- **5,780 independent numerical comparisons** passed on constructed Shomate analytic/numerical integration, intrinsic carriers, band gaps, diode current, ideal electrochemical work, Faraday conversion, XRD geometry and covariance.
- All **83 qualified source-linked context packages** pass exact version-linked retrieval; fast compiled schema validation plus bounded Draft 2020-12 sample checks pass. Exhaustive Draft 2020-12 checking of every large source context is not claimed.
- Federated **11 nodes, 2,357 records, 1,519 typed relationships**, including 305 Chemistry records and 274 full Chemistry relations (268 standalone source-closed).
- **3,357 protected earlier archive files** remain byte-identical against Chemistry v0.2, including the previous ten node packages; all 237 earlier Chemistry record and 210 previous full Chemistry relation revisions retained exactly.
- Standalone Chemistry 1.0 Python wheel installs offline with the previous nine Python distributions and returns exact source-closed reference data without relying on source checkout.

## Scientific and primary-source limitations

- Of the **487 bibliographic source cards**, **zero publisher-original source files** have been locally authenticated under the strict survival audit. The attempted IUPAC Gold Book JSON acquisition failed; no authentic original was invented. The original NIST WebBook/Shomate coefficient data, real spectra and materials property rows remain external.
- This edition generated no original experimental measurements or physical semiconductors, cell tests, XRD patterns or actual manufactured materials.
- Shomate and Varshni models require independently verified coefficients and original source temperature limits; ideal diode response and carrier statistics do not establish usable device design.
- All numerical tests use authored synthetic inputs, so they establish software/arithmetic consistency under assumptions, **not** general scientific truth, novelty, or real-world safety.
- No Bitwork routing, training of real chemistry AI, or desktop installation occurred.

## Recoverability

Extract the signed-by-manifest (not cryptographically signed by publisher) archive, verify `FILE_MANIFEST.json`, run `tools/survival_audit.py --check-files`, execute `tools/check_collection.py` in an external receipts directory, then rerun the pure-Python casebooks. The exact delta restoration proof belongs to the final external release receipt generated after the sealed archive is reconstructed and checked; it is not assumed here.
