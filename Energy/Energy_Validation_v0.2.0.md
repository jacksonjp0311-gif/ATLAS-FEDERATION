# Energy Atlas v0.2.0 — reproducibility and source limits

**Status:** substantive survival-energy reference under development, NOT independently certified real-world energy resilience.

## Executed verification

- **1,702 full-collection automated tests passed, zero skipped or failed**, including original Energy v0.1 (79 tests in immutable scope) and Energy v0.2's 46 new tests.
- **4,670 independent NumPy comparisons passed** on invented water, heat, fuel, battery reserve, load-priority and multi-interval energy scenarios. Maximum absolute arithmetic discrepancy: 5.68e-14 in tested units.
- Current ten-node Atlas contract contains **1,992 exact-revision records, 1,189 relationships and 463 source cards**; all 59 assembled source-linked contexts and compiled JSON schemas validated.
- **2074 older files** directly byte-matched against the immutable Energy v0.1 full archive. All **176 original Energy record revisions and 149 full-collection Energy relationship revisions** are identical.
- Clean isolated Python wheel installation loads nine distributions, standalone Energy v0.2 with 241 records, 200 locally closed relationships, and the 11-case survival casebook.
- The full file-inventory and extracted-release rerun are separate final checks after sealing, not assumed from this preflight.

## Evidence not acquired

- No original transport bytes for the cited NIST, DOE, EPA, CDC, NFPA or BIPM publications were obtained and authenticated. All 463 source cards are source locators/selected summaries under the strict offline audit, not a locally authenticated original library.
- No real electrical, battery, nuclear, fuel, water or microgrid hardware was operated or inspected by this package. No independent expert or experimental verification was completed.
- The v0.2 models omit AC voltage/frequency, grid-forming and anti-islanding controls, breaker/transfer protections, battery fire hazards, motor startup, water treatment efficacy and other essential safety requirements.
- The worst modeled shortage among authored scenarios is not a probabilistic worst-case outage bound. No live survivability, medical continuity, potable-water purity, or fuel safety is established.
- NFPA 855 2026 is a referenced copyrighted standard, not a set of full clauses mirrored or interpreted as installation approval.

## Reconstruct without internet

1. Open `docs/DEPTH_MANUAL_v0.2.0.md` and `docs/SURVIVAL_RECONSTRUCTION_PATH.md`; inspect sources and counterexamples.
2. Run `python -m energy_atlas survival-casebook` and the tested pure-Python methods; compare dimensional results by hand.
3. Run `python tools/survival_oracle.py` if NumPy is available; this still only compares synthetic mathematical models.
4. Verify the standalone/federation manifests and `tools/survival_audit.py`, then replay the full ten-node test runner from a fresh archive extraction.
5. Preserve the archive and original v0.1 scope snapshot. Maintain the complete Library multipart recovery manifest for the full federation.

## Next scientific gates

Field-calibrated resource/weather data, authenticated rights-cleared original sources, battery and electrical safety standards review, physical control/protection validation, water-source public-health verification, and independent energy-service performance measurements. All 30 domain libraries before Bitwork routing and desktop transfer.
