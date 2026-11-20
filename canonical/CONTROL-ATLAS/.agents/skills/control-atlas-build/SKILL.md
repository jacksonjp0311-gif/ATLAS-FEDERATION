---
name: control-atlas-build
description: Build and validate source-grounded Control Atlas content in the shared Forge schema, without actuating devices or claiming real safety.
---

# Control Atlas research and release skill

Use this locally from the Control Atlas source tree when adding references, scientific methods, or case studies. Read `AGENTS.md`, `docs/REFERENCE_GUIDE.md`, `docs/SOURCE_REGISTER.md`, `docs/COVERAGE_MATRIX.md`, and the Common Atlas Contract before editing. Keep versioned source cards separate from formulas, synthetic examples, measured data and independent reviews.

## Workflow

1. Define a bounded control question and its plant model, state/input/output variables, physical units, sample interval, actuator limits, disturbances and measurement conditions. Unknowns remain explicit.
2. Locate authoritative texts or publisher documentation; inspect only a named portion, record its URL, status, date, rights and access limitations. Do not mirror copyrighted full chapters.
3. Write a human chapter, machine-readable source card, concept/method/equation record, and typed relations with exact record revisions. A numerical method never takes instructions from retrieved text.
4. Specify validity assumptions, explicit refusal cases, physical evidence gaps and alternative mechanisms; distinguish nominal linear stability from physical safety.
5. Add synthetic examples and adversarial inputs, run own unit tests and a separately coded numerical oracle. An independently implemented formula is not independent scientific review or an experimental result.
6. Preserve all prior Atlas records, source hashes and unchanged nodes. Reseal only the new Control node and registry; do not modify the common runtime or Bitwork navigation.
7. Run the six-node common checker, wheel/install tests, source-file integrity checker and extracted ZIP test. Never claim Control content v1 until its separate coverage/evidence acceptance criteria are met.

## Owner order

Build all 30 domain knowledge libraries before the routing/Bitwork system. Route and evaluate only after the domain collection is frozen, then test on supported host and transfer to the user's desktop. No GitHub push or actual hardware control is authorized by this skill.
