# Control Atlas 0.4.0 — executable release audit and scientific boundaries

**Status:** software/model research checkpoint, **not** Control scoped content v1 or hardware certification.

## What was tested

- Forge 188, Measurement 218, Causal 233, Materials 122, Control 164: **925 automated tests passed with zero skips** in the source checkout.
- Shared six-node common contract: 975 records and 278 typed relations; source closure, exact record revision and context integrity validated.
- Separate SciPy/NumPy oracle: **4,630 numerical comparisons** of independently implemented algorithms on seeded *synthetic mathematical inputs* (2×2 singular values/inverse, 16 uncertainty-box vertices per sample, finite-horizon quadratic optimization, exhaustive scalar input-grid comparison, correlated two-sensor NIS and time-split ARX regression).
- A clean offline environment installed Forge/Measurement/Causal/Materials and the new Control 0.4 wheel, ran the new nine-case reference and validated the packaged 173-record Control node and context assembly.
- All **145 earlier Control record revisions and 81 relationship revisions** are preserved. The original 771 baseline entries and the unrelated domain/node source files are unchanged. The inherited common routing logic was not modified.
- Final archive members and a test rerun after extraction are included in the sibling release report; archive hashes establish byte identity, not scientific truth.

## What passing does not mean

None of the computations uses real hardware, independent plant measurements or actual sensor covariance calibration. A verified Riccati cost is not a safe actuator command; a common-P box certificate requires physically justified uncertainty bounds; a finite-grid plan is not continuous MPC; NIS can neither isolate fault cause nor prove a safe state. The NIST Rev4 document referenced is an **initial public draft**, not an adopted final standard. No independently authored held-out AI evaluation, live Bitwork routing, Windows host verification, peer review or real industrial commissioning was performed.

## Reproduction

```sh
PYTHONPATH=CONTROL-ATLAS python -m control_atlas advanced-casebook
PYTHONPATH=CONTROL-ATLAS python CONTROL-ATLAS/tools/advanced_v04_oracle.py
python tools/check_collection.py --out receipts/new-unique-output-folder
python tools/check_manifest.py verify .
python CONTROL-ATLAS/tools/check_manifest.py verify CONTROL-ATLAS
```

Use unique receipt directory names; running generated source code from retrieved knowledge is forbidden. The known inherited HTTP BrokenPipe test log does not mean a reliability repair occurred.

**Owner ordering:** develop all thirty domain reference contents first, then routing/Bitwork last, then integrated testing and transfer. Control content v1 still needs broader robust multivariable/empirical coverage and independent review.
