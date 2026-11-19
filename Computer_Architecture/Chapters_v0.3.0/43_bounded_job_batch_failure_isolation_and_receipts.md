# 43. A minimal job monitor with explicit failure isolation and durable receipts

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`Batch pass = AND_i(valid_software_receipt_i); failures must not be dropped`

**Units and representation:** job counts, deterministic hashes, bounded instruction budgets. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

Operating systems eventually provide scheduling, process isolation, I/O and persistent state, but those features cannot simply be assumed in a four-register educational CPU. The AT8 v0.3 batch monitor is therefore an external **software harness** that runs up to eight bounded, independently reset AT8 programs. Every job has a source listing, an optional finite input tape and an instruction budget. The monitor compiles, verifies and executes jobs separately using the three comparison pathways; it records an individual pass or explicit failure record for each.

The batch acceptance condition is an AND of all job statuses. One failed program does not silently disappear because neighboring jobs passed. The monitor continues with remaining jobs to preserve diagnostic evidence, then reports `software_acceptance=False`. It cannot allocate asynchronous process address spaces or preempt a running hardware core; its isolation is achieved by constructing separate Python machine states and bounded execution, not by an MMU. The hashes are deterministic reproducibility receipts, not cryptographic attestations of a physical device.

## Reproduce this investigation offline

Submit two jobs: a finite arithmetic program expected to output 15, and an IN program with no input bytes. The first must carry a verified software receipt; the second must report a failed-closed `ValueError`, and the aggregate must be false. With two valid jobs, the aggregate becomes true. Reorder JSON dictionary keys representing the same input tape and check the canonical digest remains unchanged. Reject unsupported job fields and more than eight submitted jobs.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `verify_job_batch, canonical_json_bytes`.

## Counterexamples, failure modes, and model scope

No OS scheduler, interrupts, privileged mode, memory protection, fault-tolerant physical storage, file system, virtual memory or real concurrency are implemented. Failure isolation within a Python list is not hardware containment. A later Operating Systems Atlas must test true process scheduling and protection on independently characterized hardware or appropriate validated emulation.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
