# 03. Factory construction and explicit dependency injection

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A factory chooses a concrete implementation from a declared configuration while allowing calling code to depend on an interface. In an offline diagnostic tool, an instrument record may use volts or millivolts; choosing the correct adapter at the boundary avoids scattering conversion conditionals across the rest of the system. Dependency injection also makes independent tests possible: a deterministic dummy port can replace an unavailable physical instrument. Configuration must be validated, not guessed from a convenient default or inferred from the numeric magnitude of a sample.

## Formal contract and executable reference

**Invariant:** `implementation = Factory(checked_configuration), not global hidden state`.

**Implementation:** `composition.build_adapter, composition.PortAdapter`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Call build_adapter({source_units:mV}) and normalize a record containing 1234 mV; the output is 1.234 V. Construct the same adapter from source_units:V and input 1.234; both agree to floating-point precision. Reject an unknown unit or undeclared configuration field. This makes a missing calibration explicit rather than implicitly assigning SI units.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Factory construction does not imply that a real sensor is calibrated. An adapter can translate units while preserving a systematically wrong voltage. Do not use a software conversion test to certify electrical safety, instrument isolation or clinical devices.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
