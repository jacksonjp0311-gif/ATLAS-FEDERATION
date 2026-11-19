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
