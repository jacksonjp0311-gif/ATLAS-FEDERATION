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
