# Atlas Workflow 1.0.0 release candidate 1

**This is a tested release candidate, not the accepted final v1.0.** Measurement is the only active new Atlas. The shared acceptance contract and the no-next-domain guard remain in force. Navigation and Bitwork enhancements stay deferred.

Start with [Measurement scope](MEASUREMENT-ATLAS/docs/V1_RELEASE_SCOPE.md), the [reference guide](MEASUREMENT-ATLAS/docs/REFERENCE_GUIDE.md), [units](MEASUREMENT-ATLAS/docs/UNIT_CONVERSIONS.md), [certificate interpretation](MEASUREMENT-ATLAS/docs/CERTIFICATE_INTERPRETATION.md), and [decision models](MEASUREMENT-ATLAS/docs/CONFORMITY_DECISIONS.md).

## Run

Use Python 3.10 or newer. On Windows, double-click `RUN_CHECKS.cmd` for the existing suite or `RUN_V1_ACCEPTANCE.cmd` for the candidate host checks and final-readiness refusal. Run `START_FORGE.cmd` for the existing local portal. No script installs global packages, creates a remote repository, or changes the existing Atlases elsewhere.

Linux:

```sh
python3 tools/run_candidate_checks.py
python3 tools/v1_readiness.py --require-final
```

The second command exits 2 while final gates are open. This is an expected refusal, not a failed numerical calculation. Host checks write receipts in a fresh `ATLAS-FORGE/output/` directory and do not overwrite previous runs.

## Optional isolated install

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --no-index --no-deps .\wheels\atlas_forge_research-1.0.0rc1-py3-none-any.whl .\wheels\measurement_atlas-1.0.0rc1-py3-none-any.whl
```

The wheel version is the canonical Python spelling `1.0.0rc1`; the display/archive spelling is `1.0.0-rc.1`. Neither is a stable 1.0.0 release.

The library contains 505 common records across Signal, Cymatics and Measurement. Measurement contributes 141 records. Data origin, review status, assumptions and original citations stay attached. The 30-domain queue and approved artwork are retained.

## Acceptance status

No independent human review, native Windows execution, new upstream-byte capture, live Bitwork run or independent held-out model comparison is asserted. See `RELEASE_READINESS.json` and `MEASUREMENT-ATLAS/docs/V1_REVIEW_HANDOFF.md`. Nothing was published to GitHub or installed on your desktop by creating this archive.
