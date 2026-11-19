# ATLAS FORGE — Scientific gap-closure protocol v0.1.0

**An additive, offline verification companion to the ONE original canonical ATLAS FORGE federation.**

**Source checkpoint:** `Computer_Architecture_v0.5.0_continuity` (2026-11-17), exact full archive SHA-256 `ea4b1f70eeaabeec0ea5b553c27bf4b3e094efc1280b1067c3c4754247b3bf8e`.

## The mission and its hard boundary

The goal is to preserve the mathematics, source evidence, executable methods, experiments, errors, and design reasoning that future humans and AI can use to reconstruct technology. A surviving record is valuable, but it is not a demonstrated reconstruction. An executable simulated computer is not a fabricated CPU. A checksum authenticates *content identity against a trusted digest*, not publisher authority or scientific truth. A metadata field saying `peer_reviewed: true` is not independent peer review.

The canonical v0.5.0 collection is proven recoverable as an archive, with a working browser portal and Python reference tools. **It is not a completed thirty-domain encyclopedia or a safety-qualified set of fabrication procedures.**

## Verified baseline (independently reproduced from the Library)

| Measure | Observed result |
|---|---:|
| Canonical Atlas archive | 711,416,573 bytes; 11 SHA-256-verified parts |
| Registered scientific/enabling nodes | 15 |
| Source-linked records | 3,235 |
| Exact-revision relationships | 2,415 |
| File checksums | 9,364 |
| Relation endpoints checked | 4,830 |
| Complete federation regression | 2,706 passed / 34 suites |
| Offline recovery and search-unit tests | 49 passed |
| Original 30 candidate domain IDs with registered nodes | 9 |
| Original candidate domain IDs still missing | 21 |
| Source cards | 547, **none authenticated to complete publisher-original bytes by the offline reader** |
| Independently reviewed scientific/physical reconstruction | Not established |

The archived original queue labels `manufacturing-atlas` queued despite its node already existing. Preserve the queue bytes unchanged; use versioned active overlays to state current work.

## Independent acceptance gates

Every significant claim should have five separately inspectable layers; the outcome of each is distinct.

1. **Archive integrity and revision:** original/derived file bytes, SHA-256, exact node ID and record revision; negative checksum checks; independently retained trusted digest. This is a **digital consistency** test.
2. **Primary source identity and redistribution rights:** publisher/edition, acquisition provenance, original file bytes and hash, precise page/equation locator, verified license or permission, and independent human source comparison. This is **publication evidence**; a URL alone does not satisfy it.
3. **Mathematical and software reproducibility:** derivation, validity conditions, units, uncertainty and independent implementation, negative cases, committed code, pinned environment and comparison with an external oracle. This is **model validation** for a bounded domain.
4. **Physical observation and metrology:** real sample and instrument identities, calibration chain, raw lab data, control/trial design, environmental conditions, standard uncertainties, failure records and physical safety review. This is **experimental evidence**, not achieved by simulation.
5. **Independent scientific adjudication:** qualified reviewer with recorded identity, substantive critique, declared conflicts, revision-specific scope, raw evidence review and authenticated approval of *only the supported claims*. This is **external scientific assessment**. Cryptographic proof of a reviewer's key alone does not prove their expertise or conclusion.

If one required layer is absent, return an explicit **HOLD**. Never collapse all five into a single score, trust a review checkbox, or allow a machine model to certify its own physical fabrication. For hazardous chemical, medical, structural, electrical, life-safety or industrial work, qualified personnel and applicable local regulations remain essential.

## Original domain-completion route

The 30-domain candidate queue is frozen and versioned; its priority numbers are not to be rewritten. The generated `ORIGINAL_30_DOMAIN_CLOSURE_PLAN.json` supplies an exact inventory of present and missing nodes. The first **unrepresented** original slot by recorded priority is **Bioelectric Atlas (priority 9)**. Next are Software Design Patterns (11), Distributed Systems (12), Neural Architectures (13), Cryptographic Protocols (14), OS Internals (15), Network Stacks (16), Database Optimization (17), Compiler Design (18) and Formal Verification (19). The other eleven missing IDs remain in the same generated plan.

For each missing domain, a real content increment requires: original technical chapters, equations and derivations, declared assumptions/units, negative cases, reproducible standard-library reference methods, independent numerical or logical oracles, a rights-aware bibliography, exact-revision records and relationships, and a versioned source archive. Demonstrating real-world applicability requires separate experimental/reviewer evidence. A domain may reach scoped **software-content readiness** without achieving scientific or physical acceptance; label both separately.

### First missing domain: Bioelectric Atlas (recorded priority 9)

**Content proposal only; not a built Atlas node.** Candidate scientific topics: membrane capacitance and equivalent circuits, ionic electrochemical potential/Nernst equation, passive cable dynamics, Hodgkin–Huxley-type excitability models, electrode interfaces and impedance, bioelectric tissue signaling, electrical measurement error, numerical stability, and data/measurement traceability. Candidate software oracles: dimensional unit checks; Nernst limiting cases; RC step response; independent ODE integration and convergence controls; uncertainty propagation; safe synthetic measurement fixtures and negative controls. Clinical practice or device construction must not be implied by models; biosafety and professional review are separate gates.

The **first actual domain release** should be an append-only Bioelectric node within the same canonical federation, not a second Atlas or a silent edit of the original queue. Publish only after historical files, 15 node manifests, complete suite and exact clean restore have been checked. Include a separate acceptance receipt describing unverified experimental scope.

## Receipt intake workflow (provided with this package)

`atlas_evidence_gate.py` offers two read-only commands. It is an **intake validator**, not a source authentication or peer-review service:

```sh
python atlas_evidence_gate.py plan --atlas /path/to/ATLAS_COLLECTION_Computer_Architecture_v0.5.0 --out /new/ORIGINAL_30_DOMAIN_CLOSURE_PLAN.json
python atlas_evidence_gate.py inspect --atlas /path/to/ATLAS_COLLECTION_Computer_Architecture_v0.5.0 \
  --workspace /path/to/lawfully-acquired/evidence --proposal /path/to/proposal.json \
  --out /new/intake_receipt.json
```

Every proposal names the exact record ID and SHA-256 revision. Every linked artifact must exist as bounded local bytes, stay inside the workspace and match its declared SHA-256. Metadata is type-checked for source originals, expert reviews, measurements, negative results or software reproductions. A complete proposal returns `RECORDED_UNVERIFIED_EXTERNAL_REVIEW_REQUIRED`. It **never** auto-returns scientific acceptance or rights clearance.

The template files use placeholders. The example fixture is artificial and must not be presented as new scientific evidence. Store real evidence receipts and raw files in a separately versioned review workspace with appropriate privacy, rights, and safety controls. Do not modify any original Atlas release bytes.

## Release and preservation rules

Preserve the exact v0.5.0 ZIP and its 11 volumes; maintain at least two geographically and administratively independent storage copies; periodically restore and re-run offline tests. Ensure recovery instructions remain printable, text-only and independent of cloud services. Do not publish the entire archive as rights-cleared until third-party material provenance and redistribution rights have been reviewed.

**Bitwork routing remains deferred until the content-domain phase is complete.** Integrated validation and desktop transfer follow routing, as stipulated by the original program. The protocol is an additive verification companion and does not promote the canonical checkpoint or add a fabricated node.
