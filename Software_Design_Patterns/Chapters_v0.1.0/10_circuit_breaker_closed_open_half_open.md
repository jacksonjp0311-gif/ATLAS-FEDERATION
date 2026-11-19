# 10. Circuit breaker states and recovery under unreliable dependencies

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A circuit breaker protects a failing dependency from repeated calls that waste limited resources. Its closed state admits normal requests, its open state rejects new attempts, and its half-open state cautiously admits a probe after a cooldown interval. Recovery is conditional: a successful probe closes the circuit, and a failed probe opens it again. The Atlas reference uses a caller-supplied monotonic logical tick instead of a wall clock or network; this makes tests deterministic. A call must not be recorded as successful when the breaker never admitted it.

## Formal contract and executable reference

**Invariant:** `closed --threshold failures--> open --cooldown--> half_open --probe--> closed/open`.

**Implementation:** `resilience.CircuitBreaker`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

With threshold two and reset interval five, record failures at ticks 0 and 1. An attempt at tick 2 is rejected. At tick 6 the breaker admits one half-open probe; a simultaneous second probe is rejected. Record a successful probe and confirm the breaker closes. Repeat with a failed probe: it must reopen. Try a backward clock tick and verify refusal.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A circuit breaker does not guarantee service availability, safety, or failover. Network and resource errors may require human intervention; an overly aggressive breaker can block recovery. State in this model is in memory unless independently persisted.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-CIRCUIT` — Microsoft Learn, Circuit Breaker Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.
