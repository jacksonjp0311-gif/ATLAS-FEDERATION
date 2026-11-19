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
