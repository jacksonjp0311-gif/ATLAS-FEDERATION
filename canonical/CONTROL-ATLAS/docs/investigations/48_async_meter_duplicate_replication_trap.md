# Investigation 48 — Repeated digital-meter readings are not replicates

In a constructed ten-column motor log, a multimeter produces one physical current sample for every four control-loop rows. Each of the four GUI records carries the same `DMM_SAMPLE_ID`. A careless analyst computes standard error as though there are four times as many independent current measurements, overstating precision. The correct parser reports 45 distinct DMM readings and 135 repeated IDs across 180 synthetic rows; it does not count all 180 as independent current observations.

The real OpenMCT article describes asynchronous DMM measurements and explicitly provides `DMM_TIME_s`, `DMM_AGE_ms` and `DMM_SAMPLE_ID` to support synchronization. The actual v2 raw data have not been downloaded, so no source-specific repeated-ID count is claimed. A stale DMM sample is not repaired by averaging, and a blank current field is not zero current. The new parser rejects partial meter records and records missing/stale cases.

A rigorous current calibration must reconstruct paired acquisitions from independent multimeter timestamps, account for repeated IDs and age thresholds, track the provisional versus final current calibration, and retain uncertainty at the level of independent DMM readings. The software checks establish only that the parser follows its declared policy on synthetic rows.
