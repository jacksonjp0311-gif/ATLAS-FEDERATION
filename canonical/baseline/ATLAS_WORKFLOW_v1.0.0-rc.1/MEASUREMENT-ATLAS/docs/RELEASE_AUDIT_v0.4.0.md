# Measurement Atlas 0.4.0 release audit

Engineering checkpoint, not scientific v1 acceptance. November 12, 2026.

55 tests passed with the companion Forge runtime available. Without Forge, six reference tests explicitly skip; the numerical functions remain dependency-free. The original 31 tests are retained. A confirmed v0.3 invalid-covariance acceptance defect is reproduced in `receipts/baseline_v03/covariance_defect.json` and repaired in the current suite.

The optional NumPy comparison passed 600 seeded positive-definite covariance cases across five scales and rejected five invalid cases. Maximum relative variance disagreement was 2.318e-15. Five worked examples are synthetic teaching inputs, not instrumented observations. This is arithmetic cross-checking, not independent scientific review.

The common Measurement node contains 35 records: five older navigation packets, ten source cards, and twenty new bounded assistant primary-portion checks. These match the current Forge node. Exact locators and qualifications are in PRIMARY_SOURCE_REGISTER.md and the common records.

Clean local wheel installation with the companion Forge wheel passed on Linux Python 3.13.5. Windows is not tested here. Source ZIP extraction and final manifests are reported at the delivery level.

Measurement remains the active domain. Scope/evidence expansion, real Bitwork routing, actual AI consumption, frozen independent evaluation and supported-platform verification are outstanding. No physical calibration was certified, no study replicated, and no model quality or compute saving established. The common protocol version 1.0 is not a scientific readiness claim.
