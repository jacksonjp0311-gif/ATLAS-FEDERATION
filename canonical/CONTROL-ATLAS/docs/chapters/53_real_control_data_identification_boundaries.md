# 53. Real control data: identify the recorded experiment before fitting

A real-data source is useful only when the variables actually record the intervention and observations required by the model. An experiment reporting elapsed time and motor RPM is not automatically a record of actuator inputs, even when its filename names a PWM setting. Conversely, a log containing both requested REF and actually applied PWM must not use REF as if it were the plant input. The mathematical relationship to be identified is conditioned on the physical actuation, measurement timestamps, transport delay, sensor quantization, and unobserved disturbances.

## OpenMCT laboratory data: publisher-grounded source scope

A 2026 open-access dataset by Alejandro Von Chong and Dorindo Cárdenas, deposited as **Mendeley Data v2, DOI 10.17632/5xvg43r9r8.2**, contains 14 acquired logs and more than 60,000 sample rows from a documented DC-motor educational platform. The version-2 description reports 10 columns: reference command (`REF`), measured speed (`MEAS`), measured loop interval (`DT_ms`), raw and averaged current-sense signals (`CURRENT_RAW`, `CURRENT_AVG`), applied PWM, and asynchronous digital-multimeter reading, time, age and ID. The article *Data in Brief* 69 (2026) 113274 provides the apparatus and analysis context and its authors. [Dataset publisher](https://data.mendeley.com/datasets/5xvg43r9r8/2). [Article DOI](https://doi.org/10.1016/j.dib.2026.113274).

The *published file descriptions and fields were inspected*, and the dataset page states **CC BY 4.0**. The original raw log bytes could not be retrieved through the available environment; accordingly **no v1 model fit, RMSE, current calibration or sampling statistic is presented as derived from OpenMCT's actual files**. The Atlas provides a strict local parser and chronological validation module ready to run on an explicitly supplied, authentic log. This is a reproducibility pipeline, not a performed empirical reproduction. The source list and checkout procedure record this distinction.

## Why metadata is a scientific prerequisite

A recorded error requires knowing when reference and observed speed were aligned. A plant could have fast dynamics at 2-ms sampling but a different effective response when a controller is deployed at 50 ms. Firmware filters can shift current measurements, and an asynchronous digital multimeter can repeat the same reading across many GUI rows. Counting repeated sample IDs as independent instrument measurements would artificially inflate apparent precision. `CURRENT_AVG` may contain provisional calibration; the original data article explicitly warns that final current calibration relied on the raw current data and the DMM.

The parser rebuilds acquisition times from the preceding recorded `DT_ms` values, refuses nonpositive intervals or malformed records, and counts unique digital-meter sample IDs. It does **not** invent absolute clock synchronization, replace missing DMM readings with zero, or infer that nominal PWM filename labels equal the applied time-series input. An observer model cannot be validated merely by possessing a CSV with thousands of rows.

## Future real-data gate

For any external data-based result, preserve upstream source UUID and release version, byte hash, acquisition method, raw log count, exact parser/fit version, sampled time axis, training/validation separation, potential closed-loop identification bias and all failed checks. Fit-performance numbers derived from the same identification record are not independent out-of-sample accuracy estimates. A successful numerical fit is not a physical safety certificate.
