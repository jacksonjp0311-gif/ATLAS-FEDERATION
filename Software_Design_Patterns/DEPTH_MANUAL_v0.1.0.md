# ATLAS FORGE — Software Design Patterns v0.1.0

**Domain priority #11 of the original 30-domain roadmap, node #17 of the ONE canonical scientific federation.** Original standalone technical reference and finite offline reference implementations. All physical assurance, original publisher-file authentication and independent peer review are open requirements.

# 01. Design patterns as reconstructible engineering contracts

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A pattern is a repeatable relationship between a problem, competing constraints, and a proposed structure; it is not a command to use a particular class or framework. For technological continuity, the important question is whether a future maintainer can reconstruct behavior without the original author's assumptions. Each pattern must therefore specify external state, inputs, outputs, version boundaries, failure semantics, and a finite test fixture. Design-pattern labels like Factory, Strategy, Adapter, or Unit of Work refer to established architectural ideas; the Atlas implements its own small educational variants. Concrete mechanisms matter more than names: for example, an idempotency key prevents duplicate *database* commands only when storage enforces uniqueness in the same transaction.

## Formal contract and executable reference

**Invariant:** `Pattern=(problem,context,forces,solution,invariants,negative_cases,evidence)`.

**Implementation:** `README.md and tests`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Select a failed local sensor-processing workflow. State its normal flow, the assumption that a value arrives in millivolts, the alternate value in volts, and the failure when units are confused. Identify which boundary a PortAdapter could normalize and how to verify it through a replayable sample. Require source-level hashes, pass/fail test, and evidence maturity for each claim.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Do not infer implementation quality from an architectural diagram. Patterns can increase complexity and centralize failure. A local reference can demonstrate finite behavior but not reliability across unknown operating systems, storage hardware, attackers, or physical devices.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 02. Canonical data, strict schemas, and versioned contracts

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A recoverable exchange format must be decodable after its generating software changes. A versioned envelope explicitly identifies a kind, integer version, stable record ID and payload, with a deterministic SHA-256 of canonical JSON. Sorting object keys and refusing nonfinite numbers eliminates many accidental differences between processes; restricting sizes and nesting bounds prevents unbounded parsing. The parser must reject extra fields rather than silently assigning new semantics. A content digest checks equivalence to an expected value, but an attacker who controls the document and hash can change both. Real authentication requires separately trusted signing or attestation, which is absent here.

## Formal contract and executable reference

**Invariant:** `H=SHA256(canonical(kind,version,id,payload)); digest equality ≠ authentication`.

**Implementation:** `contracts.envelope, contracts.parse_envelope`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Create the mapping {b:2,a:1}, wrap it as a version-one command, serialize and decode it. Reverse the order of input keys: the payload digest must not change. Modify a value without recomputing SHA-256: decoding must refuse. Supply a NaN, an unexpected schema field, an invalid ID, and excessive nesting: reject each. Record exact byte-length bounds and the trusted provenance of any external envelope.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

JSON key ordering alone is not a complete cross-language canonical-JSON standard: numeric formatting, Unicode normalization and large integers must be specified before interoperability can be certified outside this Python reference. No signed origin or network protocol is provided.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `NIST-SSDF` — NIST SP 800-218 Secure Software Development Framework (https://csrc.nist.gov/pubs/sp/800/218/final). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

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


---

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


---

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


---

# 06. Decorator pattern for explicit audit boundaries

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A decorator adds consistent behavior around an existing operation while preserving its primary interface. Logging and audit are common examples, but an audit event should not claim success if the wrapped operation throws an exception. A purely functional digest of the returned value can record which result was observed; it does not prove the operation caused or avoided any external side effect. Error states, retry attempts and interrupted outcomes should be represented in separate durable events when a production system needs them.

## Formal contract and executable reference

**Invariant:** `record(receipt)=digest(output) only AFTER successful invocation`.

**Implementation:** `composition.audited`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Wrap a function mapping x to {out:x+1} with an audit decorator and inspect the result SHA-256. Invoke the wrapper twice on the same input; the output digests should agree, although two audit entries exist. Wrap a function that raises: verify no false completed entry appears. Keep detailed failure information separately if the surrounding workflow requires it.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

An audit decorator does not make a distributed operation transactional. A crash after external action but before logging can leave missing evidence; a crash after logging but before completion can produce misleading partial records unless state transitions are separately modeled.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `NIST-SSDF` — NIST SP 800-218 Secure Software Development Framework (https://csrc.nist.gov/pubs/sp/800/218/final). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 07. Pipes and filters with verifiable intermediate results

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Pipes and filters break a transformation into bounded, independently understandable steps. For technological reconstruction, this allows a researcher to inspect each stage of a source-to-output process: parse a measurement, normalize units, validate constraints, calculate a model prediction, and serialize a result. Trace intermediate content hashes so a failure can be localized. The pipeline must not silently continue after a failed filter or substitute a guessed value. Finite pipeline length also guards against accidental unbounded composition.

## Formal contract and executable reference

**Invariant:** `x_(i+1)=f_i(x_i); each intermediate SHA256 is part of the receipt`.

**Implementation:** `composition.Pipeline.run`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Build a two-stage pipeline where the first stage converts an integer into {v:x+1}, and the second multiplies that field by three. With x=2, output {v:9} and two intermediate receipts. Mutate the second stage to a different calculation and verify its result digest changes. Reject an empty pipeline and a noncallable stage.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Pipelines do not guarantee transactional side effects or identical behavior under parallel execution. A physical sensor or network source requires separate timing, provenance and replay controls. The full chain's correctness is not established solely by intermediate hash equality.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-PUBSUB` — Microsoft Learn, Publisher-Subscriber Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 08. State machines with explicit forbidden transitions

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Finite state machines make operational modes and transitions explicit. A recovery action has different meaning depending on whether a system is idle, prepared, validated, committed or held for review. A transition table prevents a 'commit' event from succeeding before validation. For reliable offline operation, illegal transitions should be refused without modifying the prior committed state. State history can be hashed and replayed, but a hash is only evidence of the recorded logical state, not of a corresponding hardware actuator position.

## Formal contract and executable reference

**Invariant:** `next = T(current,event), undefined T is a failure not a self-loop`.

**Implementation:** `state.StateMachine, state.recovery_machine`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Start idle; prepare -> prepared; validate -> verified; commit -> committed. From idle try commit directly: refuse, state and trace unchanged. From prepared reject -> hold; reset -> idle. Execute identical sequences in separate instances and compare history digests. Deliberately declare duplicate transitions to show that an ambiguous graph is refused at initialization.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A discrete state machine does not prove physical interlocking or enforce electrical disconnection. Devices, mechanical actuators, and power supplies require external sensors, fail-safe hardware, verified timing and qualified operators.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 09. Retry with bounded attempts and explicit idempotency preconditions

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Retry is useful when a failure may be temporary, but automatic repetition is dangerous when an operation may have succeeded before its response was lost. A finite retry wrapper should accept a bounded attempt count and a deliberate classification of retryable exceptions. It must not catch every error, blindly replay irreversible physical commands, or change result ownership silently. Idempotency keys and durable knowledge of prior completion are prerequisites for safely retrying many mutations. Timeouts and backoff should also be explicit in a real system; this offline model deliberately does not sleep or call networks.

## Formal contract and executable reference

**Invariant:** `attempts<=1+retry_budget; retry only if chosen exception is transient`.

**Implementation:** `resilience.bounded_retry`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Make an operation fail twice with a designated transient OSError, then succeed on its third call. The retry wrapper returns attempt count three. Next make an operation fail with a ValueError that is not designated transient; it must be raised immediately. Repeat with retries set to zero and prove exactly one attempt. Do not use this simple wrapper to send repeated machine commands without durable command identification.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The reference does not know whether a prior external operation committed. A local retry success does not imply exactly-once delivery to a robot, industrial controller, database on another host or medical instrument. Classification is policy, not an objective property proven by exception type.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-RETRY` — Microsoft Learn, Retry Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/retry). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

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


---

# 11. Bulkhead capacity partitioning and blast-radius limits

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A bulkhead partitions finite capacity so a failing subsystem cannot consume all resources shared by others. In a local recovery tool, domain indexing and file restoration might use separate worker budgets; a hung search should not exhaust the entire runtime. The Atlas bulkhead model accepts named lanes with bounded positive capacities, refuses a lease when a lane is full, and requires explicit balanced release. This demonstrates numerical isolation of allocations, not operating-system process isolation or protection against a malicious plugin.

## Formal contract and executable reference

**Invariant:** `allocated[lane] <= capacity[lane] independently for every lane`.

**Implementation:** `resilience.Bulkhead`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Set lane search capacity one and restore capacity two. Acquire search once and verify a second search acquisition is refused while restore can still acquire twice. Release the search lease and verify it becomes available. Try releasing an unacquired lease or allocating a boolean-sized capacity: reject. The result must include independent per-lane counts.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A thread counter does not preempt a deadlocked task, enforce CPU memory limits, or isolate crashes in separate processes. Real isolation requires worker supervision, timeouts, process/container boundaries and instrumented resource limits.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-BULKHEAD` — Microsoft Learn, Bulkhead Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 12. Queues, backpressure, duplicates and delivery guarantees

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A queue decouples producers from consumers, but an unchecked queue can grow until storage or memory fails. Backpressure requires a bounded backlog, a refusal or deferral policy, and explicit handling of overflow or poison tasks. Delivery semantics matter: at-most-once may lose data, at-least-once may duplicate messages, and claimed exactly-once effects require carefully scoped coordination. An idempotent consumer can make a repeated database command produce one stored logical result, but this does not ensure the same for an external machine. The offline reference splits capacity admission from durable processing for that reason.

## Formal contract and executable reference

**Invariant:** `admitted_work <= declared_capacity; at-least-once != exactly-once effect`.

**Implementation:** `resilience.Bulkhead and ledger.CommandJournal`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Model a queue lane with two available slots and attempt a third acquisition. The third must be refused without increasing the recorded allocation. Process a command with a stable id in the SQLite journal, then submit the same id and payload again; the reducer must not run a second time. Change the payload under the old id: fail closed rather than reusing a conflicting result.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The package does not include a production broker, distributed consensus, network partitions, poison-message dead-letter storage, or a measured throughput guarantee. This chapter records the missing contracts for the eventual Distributed Systems Atlas.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-PUBSUB` — Microsoft Learn, Publisher-Subscriber Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 13. Command identity and database-local idempotent effects

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A command is a request to perform a specific change; an event is a record that something occurred. Their distinction is fundamental to recovery after an interrupted response. A stable command ID and exact canonical payload digest allow a local journal to identify duplicate submissions. Within one serialized SQLite transaction, the first submission computes a result and stores it; an identical later submission reads that result without invoking the reducer again. The uniqueness constraint belongs in the database, not only in application memory, otherwise restarting could forget it.

## Formal contract and executable reference

**Invariant:** `same ID + same payload -> same committed row; same ID + different payload -> error`.

**Implementation:** `ledger.CommandJournal.execute`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Insert command ID c1 with {a:5,b:7}, using a pure reducer that returns {sum:12}. Submit the same command again and assert the reducer ran once; the replay returns the exact stored result with new_commit=False. Now reuse c1 with {a:5,b:8}: refuse. Close SQLite, reopen the database and verify c1 persists with a valid hash chain.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The reducer must be pure and deterministic. If it sends a command to a printer before database COMMIT, a later retry can send it again after a crash. A local unique ID does not establish exactly-once actuation, distributed exactly-once effects, or physical safety.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-RETRY` — Microsoft Learn, Retry Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/retry). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 14. Unit of Work, SQLite transactions and rollback boundaries

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

The Unit of Work pattern coordinates related changes as a single logical transaction. An offline SQLite database offers an explicit transaction boundary with BEGIN IMMEDIATE, protected uniqueness constraints, a deterministic reducer and COMMIT or ROLLBACK. The journal chooses WAL mode with synchronous FULL to improve software durability under supported filesystem semantics. It is important to describe the database boundary precisely: separate filesystem snapshots and external machines do not automatically join this transaction. A crash after the database commits but before another action can leave derived state stale.

## Formal contract and executable reference

**Invariant:** `BEGIN IMMEDIATE; validate->reduce->insert->COMMIT or ROLLBACK`.

**Implementation:** `ledger.CommandJournal`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Make a reducer raise after a transaction has begun. The database must roll back and contain zero committed commands for that ID. Submit a valid command afterward; the sequence must begin at one. In a separate test mutate a stored result directly using SQLite and verify the journal's independent hash-chain audit reports corruption. Read SQLite's official WAL and atomic-commit documentation for host/storage caveats.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

SQLite durability depends on the operating system, filesystem, disk controller, flush implementation and power conditions. A passing unit test on a desktop cannot substitute for controlled power-cut experiments. Do not claim transactional consistency between SQLite and a printer, actuator, or independently committed external database.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 15. Hash-chained command history with independent replay checks

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

An ordered journal needs evidence that sequence gaps, payload mutation and result tampering are detectable relative to an independently trusted head. Each committed row stores a sequence number, command ID, canonical payload and result, previous row hash and current row hash. Replaying validates consecutive sequences, recalculates payload identity, checks canonical serialization and recomputes each link. A mutation of an early row should invalidate that row and subsequent chain verification. This protects against accidental corruption of locally stored entries; an adversary with control of every row and head may rewrite the chain consistently.

## Formal contract and executable reference

**Invariant:** `H_i=SHA256(seq,id,payload_sha,payload,result,prev=H_(i-1))`.

**Implementation:** `ledger.CommandJournal.verify_replay`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit two commands and capture the final head hash. Reopen SQLite and confirm the same head. Use a separate SQLite connection to alter result_json without updating the recorded hash: replay must fail. Test a changed payload and a broken previous-hash link. A recovered journal that fails a hash audit must enter a HOLD state instead of silently deriving new snapshots from untrusted history.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Hash chains are not digital signatures or tamper-proof logs when the attacker controls the entire file. Reliable audit needs separately anchored head values, trusted timestamps, key management or independent replicas, as appropriate. Crash durability also needs physical storage testing.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `SQLITE-WAL` — SQLite, Write-Ahead Logging (https://www.sqlite.org/wal.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 16. Event sourcing with immutable blobs and a versioned head pointer

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Event sourcing records successive state-changing facts rather than only the newest current state. A content-addressed event graph allows replay from a head pointer to earlier immutable event blobs. Each event includes its sequence number and predecessor digest; the head identifies the newest entry, so a new blob created but not published can remain an orphan without becoming visible history. The reader verifies every referenced blob hash and contiguous sequence numbers. A missing or altered head must not silently reset the chain to empty.

## Formal contract and executable reference

**Invariant:** `entry_i={event_i,prev:H_(i-1),sequence:i}; head points to last hash`.

**Implementation:** `events.EventChain, atomicfiles.ContentStore`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Append events {n:1} and {n:2}, close the process and construct a new reader from the same directory. Replay must return both in order with the same head hash. Corrupt the head pointer to an unknown digest: the next append and replay must refuse. Limit replay length to a declared bound and test rejection when the event chain exceeds it.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The sample is single-writer only; two concurrent writers can race on the same head and one update may be lost. A hash chain whose pointer is not independently anchored does not resist an attacker rewriting all content. Event sourcing can also expose sensitive information unless retention and access controls are engineered separately.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `AZURE-PUBSUB` — Microsoft Learn, Publisher-Subscriber Pattern (https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 17. Content-addressed immutable artifacts and integrity checks

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A content-addressed store names an artifact by a digest of its bytes. Identical inputs have identical names, and accidental byte changes should be detected during retrieval. This is useful for technical continuity because recovery depends on exact binaries, test data, CAD source files and manifests, not just human-readable filenames. The reference restricts individual blobs to one MiB to keep tests finite. It writes a temporary file and atomically replaces the digest-named leaf within a controlled local directory, then verifies content hashes on every read.

## Formal contract and executable reference

**Invariant:** `blob_name=SHA256(blob_bytes); retrieval recomputes the digest`.

**Implementation:** `atomicfiles.ContentStore.put/get`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Store the bytes of a small offline instruction file. The returned name must equal SHA-256 of those bytes. Store the same bytes again and verify the name is unchanged. Corrupt the stored blob through a separate test tool and require the next retrieval to fail. Submit a malformed hash or too-large file: reject it before writing.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Content-addressed naming is not secure provenance without a separately trusted digest. One local copy is also vulnerable to physical media failure. Multi-disk backups, verified redundancy and lawful redistribution are required for meaningful long-term survival.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `PY-OS` — Python Software Foundation, os.replace Documentation (https://docs.python.org/3/library/os.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 18. Atomic same-filesystem pointer replacement and rollback design

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A recoverable system should not leave readers observing a partially written pointer. The reference creates a temporary file in the same directory as the target, writes its full digest and flushes it, then uses os.replace to make the head switch visible in one supported local operation. It retains old content-addressed blobs so an operator can inspect historical versions after a head update. The reference attempts parent-directory fsync where supported, but the physical durability of a filesystem operation depends on platform semantics and storage behavior.

## Formal contract and executable reference

**Invariant:** `write temp->fsync(file)->os.replace(temp,head)->best_effort_fsync(parent)`.

**Implementation:** `atomicfiles.ContentStore.publish`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Publish an initial head pointing at blob A, then update it to blob B. A fresh reader must see the complete digest for B, while blob A remains retrievable by hash. Attempt a path traversal tag or symlink head: the operation must fail. A power interruption simulation can test the software's handling of stale/missing pointers, but cannot certify actual Windows or Linux storage devices under a power cut.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

os.replace provides atomic rename semantics on appropriate platforms and filesystems; it does not by itself guarantee power-loss atomicity or synchronous commit across SQLite and filesystem storage. Not all filesystems safely support directory fsync or network shares. Test on the actual device before a blackout-readiness claim.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `PY-OS` — Python Software Foundation, os.replace Documentation (https://docs.python.org/3/library/os.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 19. Recovering a derived snapshot after a committed journal update

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

An application often updates more than one storage resource: a primary database and a derived file snapshot, for example. They cannot simply be described as one transaction. A safer design identifies the authoritative source and treats the secondary artifact as rebuildable. The Atlas recovery workflow commits a bounded pure command to SQLite and then publishes a derived content-addressed snapshot of all committed results. If an interruption occurs between these steps, a restarted process compares the journal head with the snapshot head, rebuilds the derived view if necessary, and records the new digest.

## Formal contract and executable reference

**Invariant:** `authoritative_journal_head != snapshot_head -> reconstruct derived view`.

**Implementation:** `workflow.RecoveryWorkflow.apply/recover`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit command A normally. Commit command B but deliberately raise a simulated interruption before publishing its snapshot. Close the process. Reopen the journal, validate every hash-chain link, and call recover(): it should detect that the snapshot head is stale and reconstruct a two-command view. A second recover should return recovered=False because the views now agree. Corrupt the existing snapshot pointer: refuse silent repair and require an operator to establish a trusted recovery basis.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A real controller can have other nonrebuildable state, including motor movements, heat, physical stock or remote financial transactions. Such effects are not rolled back by rebuilding a database view. The demonstration only certifies deterministic software-level derived state under its explicit model.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `SQLITE-WAL` — SQLite, Write-Ahead Logging (https://www.sqlite.org/wal.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 20. CQRS-style separation of command authority and read projections

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Command Query Responsibility Segregation separates the authoritative mutation path from a potentially cached or delayed read model. In an offline recovery workflow, the SQLite command journal is authoritative for accepted local operations. A content-addressed JSON snapshot is only a derived projection that can be reconstructed at any time. This simplifies restart logic: before relying on a read view, compare its source head to the journal's verified head. A stale projection is not evidence that a command failed; it may mean the secondary update was interrupted. A corrupted projection is an integrity failure that should be made visible.

## Formal contract and executable reference

**Invariant:** `read_view = f(verified_committed_journal); commands do not trust stale projections`.

**Implementation:** `workflow.RecoveryWorkflow`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit two journal entries while intentionally interrupting publication after the second. The old snapshot contains one entry, while the verified authoritative ledger contains two. Calling recover reconstructs the projection; repeat without new commands to verify idempotent read results. The projection should not cause a second execution of the reducer or any physical device output.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A read-projection pattern does not guarantee freshness without a defined synchronization protocol. This reference is single-host and local; distributed replicas, interleaved writers and conflict resolution belong to the Distributed Systems Atlas, not to an unproven local transaction claim.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 21. Cache-aside, invalidation and the limits of stale knowledge

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A cache increases read speed by retaining previously computed values, but its content may become stale when the underlying source changes. The Cache-Aside pattern makes the source authoritative and loads cached values on demand. In the Atlas, a version hash or exact record revision offers a concrete invalidation key; an old context assembled from earlier records should not silently replace new evidence. The Computer Architecture node includes a separate direct-mapped write-through cache at the byte level. The Software Design Patterns domain focuses instead on application-level reconstruction of derived results.

## Formal contract and executable reference

**Invariant:** `cache_valid iff cache_revision == authoritative_revision`.

**Implementation:** `workflow snapshot revision comparison; Computer Architecture cache reference`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Commit a new journal entry and deliberately leave the derived snapshot stale. The read-side recovery compares hashes, detects revision mismatch, and reconstructs a fresh projection. A second read returns the same digest without rebuilding. Contrast that with deliberately modifying a cached byte without its source update: retrieval must detect corruption or refuse inconsistent evidence rather than returning it as authoritative.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Cache coherence across multiple machines is not solved by local SHA-256 comparisons alone. Read stale values can be dangerous for control systems and medicine; real service deadlines, network partitions and consistency models require explicit designs and external validation.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `FOWLER-CATALOG` — Martin Fowler, Patterns of Enterprise Application Architecture Catalog (https://martinfowler.com/eaaCatalog/). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 22. Software supply-chain evidence, rights, and untrusted inputs

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Rebuildable software needs more than a ZIP. Its source, build commands, interpreter/compiler version, dependencies, tests, expected outputs, licenses and security boundaries must be recorded. NIST's Secure Software Development Framework offers guidance on organizational practices, but the existence of this Atlas code does not establish conformance. Hashes show byte equivalence to a claimed value; they do not authenticate a publisher, prove the absence of vulnerabilities, or grant redistribution rights. The complete Atlas requires authenticated original files and independently reviewed claims before any domain can be considered scientifically accepted.

## Formal contract and executable reference

**Invariant:** `release_acceptance = artifact_integrity AND scoped_tests AND independent_provenance`.

**Implementation:** `contracts.parse_envelope, evidence receipts`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Build a compact release with a source manifest, test receipt and exact restore instructions. Modify a single source byte and verify that the file digest no longer matches. Feed an oversized JSON message and a nested malicious-looking path to the strict parser, which must reject them. Document each failure and its source revision. Ensure original third-party publications are only linked, not copied without rights clearance.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

The reference parser is not a comprehensive hostile-data sandbox; pure Python strategies are not safe to execute from untrusted sources. Production threat modeling, independent code review, dependency scanning and patch management remain open work.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `NIST-SSDF` — NIST SP 800-218 Secure Software Development Framework (https://csrc.nist.gov/pubs/sp/800/218/final). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 23. Property-based, differential and interruption-oriented test design

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

A test suite that merely checks success on expected inputs can miss the failure cases that matter during reconstruction. Property-based testing exercises invariants across many finite inputs; differential testing compares structurally distinct implementations; fault injection checks behavior when a dependency fails between transitions. The Atlas independent oracle compares canonical JSON digests, thousands of state-machine transitions, circuit-breaker state sequences, a SQLite journal against a separate mapping, content-addressed snapshots, and explicit crash recovery. It records the seed and count of comparisons so another process can reproduce the same finite experiment.

## Formal contract and executable reference

**Invariant:** `oracle(inputs) == implementation(inputs) for explicit finite test set`.

**Implementation:** `evidence/independent_oracle.py and tests`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Generate 2,048 synthetic versioned envelopes with shuffled key order, verify canonical digest agreement and reject unauthorized modification. Generate 1,280 valid state-machine sequences and compare each transition with an independent hand-coded table. Run 500 circuit-breaker traces with a separately coded reference model. Inject a crash after journal commit and verify recovery from a fresh process. Report the exact number of comparisons, categories and test failures, not a vague claim of formal proof.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

Finite testing cannot establish correctness for all programs or operating conditions; models can share a mistaken requirement. Independent audit, deterministic build reproducibility and tests on target operating systems are needed before life-safety or critical infrastructure adoption.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `NIST-SSDF` — NIST SP 800-218 Secure Software Development Framework (https://csrc.nist.gov/pubs/sp/800/218/final). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.


---

# 24. Reconstructing resilient software without network services

**ATLAS FORGE — original canonical scientific federation / Software Design Patterns v0.1.0**

**Evidence level:** original authored engineering reconstruction and finite standard-library software tests. Bibliographic source pointers are not authenticated publisher-original bytes. No claim of certified safety, physical power-failure testing, or independent expert review.

## The reconstruction problem and why the pattern exists

Technological continuity depends on an executable path from known instructions to independently reproducible behavior. Start with a clean Python environment and the standard-library-only reference package. Decode a versioned contract, construct a named policy/adapter, use an explicit state machine, commit a bounded pure command under SQLite, build a content-addressed snapshot and verify its hash. Simulate a crash after another command is committed but before a snapshot is updated. Restart from the stored file and database, verify the journal's hash chain, rebuild the derived projection, and compare a deterministic receipt. This creates a small but meaningful end-to-end recovery proof without internet access or an AI model.

## Formal contract and executable reference

**Invariant:** `source + tests + schema + journal + snapshots + evidence -> reproducible bounded recovery`.

**Implementation:** `python -m patterns_atlas; workflow.RecoveryWorkflow`. The reproducible reference is scoped to local, finite, deterministic operations with explicit failure outcomes. The test suite must check state or output as well as the refusal behavior for invalid inputs. A source-linked claim does not become true merely because a Python function returned the expected value once.

## Worked reconstruction investigation

Run `python -m patterns_atlas` from a clean extracted package. It should report a committed result of 12 for a 5+7 calculation, simulate an interrupted later command, reopen its SQLite journal, and reconstruct a two-entry snapshot without repeating a pure reducer. Repeat the test on the target Windows machine. Compare actual file hashes, SQLite journal-mode behavior, filesystem flush semantics and USB storage recovery. Preserve a short README with command syntax and negative cases.

The verification record must include the exact input, algorithm/code edition, result or state digest, negative case, environmental assumptions, and whether an external effect occurred. A future human or offline AI should be able to regenerate the result from the archived executable source, not guess from the prose alone.

## Known failure mechanisms and evidence boundaries

A successful offline software run does not certify local power backup, filesystem crash consistency, hardware control, or 3D printer functionality. An independent technician must test actual recovery hardware, battery conditions, source authenticity and safe operating procedures. The next original Atlas domain is Distributed Systems (#12), where multi-host consensus, retries and network partitions can be studied separately.

For a critical recovery application, power continuity, storage hardware, timekeeping, synchronization, trusted code origin, and adversarial inputs must each be independently evaluated. Software integrity checks do not replace those measurements or a qualified risk assessment. Explicitly record unsatisfied prerequisites rather than promoting a test pass into a safety or reliability certificate.

## Source provenance and federation interfaces

- **Publisher navigation:** `PY-SQLITE` — Python Software Foundation, sqlite3 Library Documentation (https://docs.python.org/3/library/sqlite3.html). The original publisher file bytes, licensing, exact edition and page-specific claims have **not** been independently authenticated or mirrored.
- **Existing exact-revision prerequisites:** Computation, Agent, Control, Language, Computer Architecture & Digital Hardware, and the original Atlas persistence/reader infrastructure.
- **Scope:** This Software Design Patterns node implements small educational, offline pieces. Distributed consensus, full operating-system failure recovery, secure firmware and actual manufacturing controls remain work for other named domains.

**Original roadmap rule:** The canonical 30-domain queue remains byte-identical; Bioelectric (#9) and Manufacturing (#10) are predecessors; this domain is #11. Bitwork routing remains deferred until content-domain completion.

