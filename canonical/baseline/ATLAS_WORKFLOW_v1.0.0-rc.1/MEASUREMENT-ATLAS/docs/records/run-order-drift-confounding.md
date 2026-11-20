# Run order can confound calibration drift with load

**Record:** `run-order-drift-confounding` · **Type:** claim · **Origin:** source_reported

Because both Pontius runs progress through increasing loads, the source warns that load dependence and time-dependent drift cannot be cleanly separated from the run order alone.

## Source and inspected portion

[Load-cell calibration collection design](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd611.htm) · §4.6.1.1 Description of Data Collection

## Assumptions

- The same recorded order is relevant to the fitted calibration case.

## Limitations

- A good polynomial fit does not establish absence of drift.
- No time stamps or independent drift controls are supplied.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
