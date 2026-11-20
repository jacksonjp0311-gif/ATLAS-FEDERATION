![Approved ATLAS FORGE artwork](assets/atlas_forge_knowledge_hub.png)

# CONTROL ATLAS — v1.0.0-rc.1

**Scoped scientific reference release candidate** by the James Paul Jackson research program. **Read-only offline mathematical and evidence reference; no device control.**

[**Full scientific manual**](docs/DEPTH_MANUAL_v1.0.0-rc.1.md) · [**Reference guide**](docs/REFERENCE_GUIDE.md) · [Source inspection](docs/SOURCE_REGISTER.md) · [Open scientific gates](docs/COVERAGE_MATRIX.md) · [Casebook](docs/CASEBOOK.md)

## Included

- 61 reference chapters, 49 worked investigations and machine-verifiable source-linked claims with immutable versioned records.
- Classical and robust control models, sensor/actuator uncertainty, sampled dynamics, constrained planning and error/fault-ambiguity counterexamples.
- New bounded 2-state/2-sensor observer-error and measured-value consistency tools.
- Offline OpenMCT v2 ten-column CSV ingestion and chronological ARX validation for an **operator-supplied** authorized raw log. The 2026 CC BY dataset is linked, but **the original raw records could not be downloaded in this environment**: no actual source-specific fit or held-out RMSE is claimed.
- An attributed three-file public student motor RPM descriptive case (49 observations per file), with source Git blob IDs and no raw CSV redistribution. These files do not contain rowwise applied PWM and cannot identify plant response on their own.

## Commands

```
python -m control_atlas v1-casebook
python -m control_atlas openmct-review path/to/raw_log.txt
python -m control_atlas openmct-fit path/to/raw_log.txt
```

The local runtime uses only Python standard library. Separate numeric-oracle tests use NumPy and do not prove physical model validity. Each command returns explicit assumptions, limitations or refusals; none opens network connections or sends hardware commands.

## Acceptance and future routing

This is **v1.0.0-rc.1**, not an independently certified content v1.0.0. Actual publisher-raw motor model reproduction, physical hard bound tests, independent source/engineering review, real hardware-in-the-loop tests and AI model evaluations remain open. The existing shared Forge retrieval system is unchanged. **Complete all 30 domain content libraries first, build Bitwork routing last, then integrate/test and transfer to the user’s computer.** Agent Atlas is next, but Control remains active until content acceptance is justified.

**Hardware boundary:** no actuator drivers, no PLC connections, no device credentials and no control output dispatched by this research package.

**No real equipment was controlled, observed through hardware, or safety-tested by this release.**
