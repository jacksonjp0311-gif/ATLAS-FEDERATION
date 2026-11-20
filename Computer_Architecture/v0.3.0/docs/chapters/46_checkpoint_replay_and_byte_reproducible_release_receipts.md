# 46. Byte-exact release replay, checkpoint identity and software evidence chains

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`receipt=SHA256(canonical JSON excluding own receipt field); replay results must agree`

**Units and representation:** SHA256 hashes, archive byte identities, immutable revisions. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

Long-term reconstructibility requires more than saving the last program. A release chain should preserve the exact predecessor archive hash, the direct incremental delta, all changed-member hashes, the complete resulting source manifest and a tested recovery script. The release's canonical checkpoint must identify the same revisioned state that its archive reconstructs. The AT8 boot workflow likewise hashes the source bytes, encoded ROM bytes, canonical boot image and canonical serialized input-tape mapping, then records the deterministic state and output digests. The receipt does not include its own hash while calculating its SHA-256, preventing a circular definition.

A replay is successful when a second fresh process recovers exactly the same ROM and observable result under the same bounded inputs, and independently checks its file hashes. Byte equality does not establish scientific truth, security authorization, correct license, fabricated hardware or independent peer review. A recovered file with the wrong registered original identity must be rejected even if it executes. Only an independently trusted publisher signature or other attestation could add authorship confidence.

## Reproduce this investigation offline

Hash the source listing and its assembled ROM, build the version-3 header, and record the empty or explicit input tapes with stable key ordering. Re-execute in an isolated Python interpreter, verify the receipt SHA-256, then deliberately reorder the dictionary keys and confirm canonical input identity is stable. Change one source byte and observe its source SHA change. Run an interrupted dual-slot update and preserve the original slot when the candidate did not commit.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `verify_program, canonical_json_bytes`.

## Counterexamples, failure modes, and model scope

Python and zlib versions may affect ZIP compression and exact full ZIP byte hashes; raw source-file hashes can still prove file equivalence independently. Do not silently claim byte-exact restoration without checking actual target ZIP SHA. Publisher-original full PDFs were not imported into this release; their source cards remain citation/navigation only.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.
