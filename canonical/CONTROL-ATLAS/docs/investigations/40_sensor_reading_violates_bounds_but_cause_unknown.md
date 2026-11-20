# Investigation 40 — A residual contradiction does not isolate a failed sensor

**Origin:** authored scalar consistency test, no real process log. Assume the estimated state h=0.1, absolute error radius E=0.04 and sensor noise absolute maximum V=0.02. The predicted measurement lies within **[0.04,0.16]**. A reported y=0.13 is consistent with those assumptions. A reported y=0.30 lies 0.14 model units above the interval and is inconsistent.

This evidence does **not** establish whether a sensor broke. The process may have experienced a disturbance outside W, the actuator may not have followed the command, the plant model might be wrong, or the timestamp may be stale. A sensor bias could also explain the residual. Each possibility requires a distinct observation or controlled study to discriminate.

A useful diagnostic next step is to inspect independent actuator feedback and a calibrated secondary measurement, verify time alignment, check software data handling, and review process changes against the model's parameter range. Those steps are a research protocol, not instructions for unattended shutdown, bypass, override or repair. No physical action is performed in this reference system.

**Sources:** NIST OT Security Guide SP 800-82 Revision 3 (final, September 2023), on unique reliability and safety requirements of OT; MIT state-estimation notes. NIST Revision 4 remained a draft in November 2026. Bound equations are original and system-specific validity is untested.
