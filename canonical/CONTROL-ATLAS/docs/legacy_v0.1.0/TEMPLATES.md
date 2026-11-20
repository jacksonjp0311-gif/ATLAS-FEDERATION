# Control Atlas experiment templates

## Plant and safety record
- Physical system, exact model, units and state limits:
- Operating point, expected disturbances and validated domain:
- Sensor/actuator identity, calibration, delay, rate/saturation, safety interlocks:
- Data-acquisition clock and control computation jitter:
- Operator approval, test plan, rollback, monitoring and stop conditions:

## Control algorithm record
- Design objective, target, performance metric, state-space/transfer model:
- Parameters and identification/uncertainty provenance:
- Continuous/discrete hold convention, sample time, gain limits:
- Test cases for disturbances, reference changes, noise, saturation and failures:
- Formal sufficient conditions versus observed traces; unexplored failure modes:
- Independent reviewer, source revisions and bounded decision:

## State estimation record
- Sensor model, bias, noise covariance, process noise and origin:
- Filter structure and measurement ordering:
- Residual/innovation statistics, missing values, outlier policy:
- Estimation uncertainty model versus actual calibration evidence:
- Response to sensor failure, fallback mode, and operator review:

## Evidence/revision ledger
- Record ID and revision, source URL and inspected scope, model/software release:
- Inputs and state conditions, physical units, certified versus synthetic origin:
- Alternate explanation, source contradiction, missing evidence:
- Updated corpus dependencies and context invalidation:
