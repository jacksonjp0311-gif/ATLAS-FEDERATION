# 55. Acquisition intervals and asynchronous measurement alignment

Control algorithms are sensitive to the difference between sampling time, communication latency and the timestamp of a physical reading. The OpenMCT article records measured loop interval `DT_ms` and a separate asynchronous DMM timestamp, sample age and ID. Those fields are deliberately different. For a log with entries `0..N-1`, this Atlas constructs `t[0]=0` and `t[k+1]=t[k]+DT_ms[k]/1000`, preserving the experiment's interval recordings instead of imposing the nominal sampling period. The reconstruction establishes relative acquisition time **conditional on correct firmware logging**, not an absolute synchronized laboratory clock.

A multimeter may produce one reading every several control-loop iterations. Consecutive GUI records can repeat a single `DMM_SAMPLE_ID`, so repeated rows must not be interpreted as independent current samples. `parse_openmct` keeps explicit counts for absent, duplicate, stale and first-accepted DMM IDs; it refuses partial asynchronous records and does not interpolate missing values. A duplicate ID is not an independent replicate even if its sample age appears low. In the strict loader all required speed, timing and PWM fields must be finite; blank or NaN DMM records are permitted only as a whole missing group. These are software schema choices based on the published column description, **not yet verified against all raw v2 logs**.

For a discrete model `y[k+1]=a*y[k]+b*u[k]+c`, the input should be the **PWM recorded as applied** at sample k. Substituting `REF` would model the command rather than the actuator. Strong sample-interval jitter can invalidate one constant discrete coefficient matrix; this implementation rejects logs exceeding a chosen relative jitter tolerance. It does not resample automatically, infer time delays, identify sample-drop patterns, or align independent instrument clocks after the fact.

## Failure situations to retain

- Negative, zero or nonfinite acquisition interval: refuse, because time ordering is not physically defined.
- Repeated DMM ID: count once per unique meter reading, not once per GUI sample.
- Partial DMM fields: explicitly flag malformed/missing cross-channel data instead of treating them as a measurement of zero current.
- Large time jitter: a constant-sample ARX equation has an unverified premise; refuse or use an actual variable-step model.
- Reference command differs from applied PWM: log both, and identify which is an observed command versus physical actuation.

Preserve these statuses with any downstream record. NIST SP 800-82 Rev. 3's operational-technology guidance additionally emphasizes security, safety and operational reliability as distinct requirements for real equipment; the **September 2026 Rev. 4 is still a draft**, not a final replacement at this release date. [NIST final Rev3](https://csrc.nist.gov/pubs/sp/800/82/r3/final), [Rev4 initial draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd).
