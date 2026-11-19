# 05. Strategy pattern and deterministic policy substitution

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Strategy separates the algorithm used from the context invoking it. A reproducible Atlas evaluator can test multiple algorithms on identical inputs without changing transport, instrumentation or storage. Registering each strategy under a unique bounded name makes selection inspectable and rejects accidental replacement. Compare algorithms against a common oracle, preserve both successful and failing cases, and include the policy-selection name with each result. When policy changes, the same input may produce different outputs, so a receipt must record the selected strategy and source revision.

## Formal contract and executable reference

**Invariant:** `result=StrategyRegistry[name](payload) with explicit named policy`.

**Implementation:** `composition.StrategyRegistry`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Register an integer doubling strategy and an independent identity strategy. Evaluate the same integer and compare results to the reference definition. Attempt to register another function under the existing name; the registry must refuse the conflict. Attempt an unknown name and verify it fails rather than silently returning a default result.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A callable policy is trusted local code. This is not a plugin sandbox or secure environment for arbitrary third-party Python. Strategies can have hidden side effects; full scientific reproducibility requires pure implementations, versioned inputs and independently checked outputs.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
