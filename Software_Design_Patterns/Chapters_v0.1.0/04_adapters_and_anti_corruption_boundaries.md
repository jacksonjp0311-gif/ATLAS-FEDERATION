# 04. Adapters and anti-corruption layers for incompatible information

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

An adapter translates one interface into another without changing its intended meaning. An anti-corruption layer is broader: it prevents an outside system's naming, units or conceptual model from silently contaminating internal invariants. When reconstructing legacy technology, units, byte ordering, error conventions, integer widths and missing-value semantics must each be explicit. Normalize to a small canonical internal representation and preserve the source-unit label in provenance. Translation should fail on unknown inputs, not clamp them to a plausible physical value.

## Formal contract and executable reference

**Invariant:** `V_SI = V_mV/1000; raw_data != certified_calibration`.

**Implementation:** `composition.PortAdapter.normalize`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Convert a synthetic reference signal of 2500 mV to 2.5 V and compare it with a 2.5 V reference using the same canonical field. Try an unrecognized Celsius unit for a voltage field: reject it before downstream use. Include a negative control where the same numeric '2500' is supplied with the wrong unit; the results must differ and the source identity must accompany the example.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Structural interface compatibility does not verify physical equivalence, measurement uncertainty or safety certification. Cross-domain integration also requires calibrated instruments, correct sampling, environmental constraints and human expert review.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
