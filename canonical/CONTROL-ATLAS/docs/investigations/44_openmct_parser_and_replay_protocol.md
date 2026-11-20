# Investigation 44 — OpenMCT v2 raw-log replay, pending source-file acquisition

The publisher's version-2 OpenMCT dataset, DOI `10.17632/5xvg43r9r8.2`, is licensed CC BY 4.0 and contains more than 60,000 rows across 14 acquisition logs. The data article describes 10 CSV columns and two metadata lines preceding the header. This investigation is a **reproducibility protocol**, not a completed reanalysis. Dataset metadata and article were checked, but direct raw download was blocked in the execution environment, so no real OpenMCT model coefficients or RMSE are reported.

Once an authorized copy is available, preserve all original file bytes and publisher SHA-256 where supplied; record dataset version, hardware and firmware metadata, file path, checksums and licence. Run `parse_openmct` on a locally supplied acquisition log, inspect the reported sample count, `DT_ms` distribution, and DMM duplicate/stale IDs, and validate that the measured PWM—not REF—was used as the plant input. A chronological split then estimates a bounded ARX one-step model, compares against persistence and computes free-run error.

The program refuses a non-monotone or unsupported sample interval, missing required fields, too few records, constant or collinear PWM excitation, and high sample-period jitter. An actual controller validation should also compare *across* acquisition runs and physical regimes rather than only within one log. A winning one-step RMSE does not establish transfer, independence of residual noise, safe actuation or instrument calibration.

**Status:** source available publicly, data acquisition not completed here; original-byte hash and real-data metrics remain `null`. Synthetic parser and numeric-oracle tests are reported separately and cannot be relabeled as experiments.
