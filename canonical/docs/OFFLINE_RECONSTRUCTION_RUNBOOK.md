# ATLAS FORGE — Read the knowledge after the network goes dark

**This guide is deliberately readable using only an ordinary text viewer.**

## First hour

1. Make a read-only copy of the archive if storage is available. Do not edit the only copy. Find `README.md` at the collection root, then `docs/HUMAN_KNOWLEDGE_SURVIVAL_CHARTER_v1.md` and `DOMAIN_QUEUE.json`. Those documents explain the collection's scope and what is missing.
2. Open any domain's `README.md`, `docs/REFERENCE_GUIDE.md`, and full scientific Markdown manual. These are original summaries, mathematical explanations and examples; **not** substitutes for missing primary-source publications.
3. Inspect `common/registry.json`, then `common/nodes/<node-id>/atlas_manifest.json`. Its record collections are text lines in JSON format. A record's `record_id` and `revision` identify the exact statement, and its `sources[]` point to source cards. A source URL may be unreachable; its absence is an evidence gap.
4. If Python 3.10+ exists, run `python tools/survival_audit.py --root . --out SURVIVAL_AUDIT.json` and `python tools/check_manifest.py verify .` in the unpacked directory. These scripts are standard-library only where possible. Read failures, especially missing or changed files, before trusting any package.
5. Do not install from the network or execute retrieved third-party papers. Optional virtual-environment installation and tests are engineering convenience, not a prerequisite for reading formulas and notes.

## Reconstruct a concept

Start with the prerequisites and definitions. Record all variables and their dimensions. Trace every quoted empirical result to its source card and mark whether original data bytes are present. Read the derivation and its assumptions. Recalculate the smallest worked example by hand if feasible; only then run the Python reference model. Confirm where the numeric result stops short of a scientific or engineering conclusion. Read contradictory or qualifying records rather than selecting a single attractive answer. If the source is not recoverable, write the missing evidence in a local audit note rather than inventing its contents.

## Restore or migrate a release

Keep the original release archive unchanged and make a new workspace. Check the ZIP integrity and SHA-256 before extraction if its digest was recorded separately. Use a tool that preserves UTF-8 names. Verify every relative file against its `FILE_MANIFEST.json`, if present. For a new format or system, convert only into an openly documented representation and retain the prior bytes and a conversion report. Never overwrite prior record revisions. Run the source and test suites if an interpreter exists; record the exact operating system, interpreter version, tests run and unresolved failures.

## What is *not* included yet

A complete collection of all primary research articles, a durable global legal source mirror, raw scientific instruments and samples, reliable regional backups, access to active proprietary AI providers, or an authenticated real-world agent evaluation set. Those absences may matter critically. Future work must track and reduce them without exaggerating archive coverage.

## Human curriculum

Read `Measurement` first to learn uncertainty and units; use `Causal` for identification and counterexamples; use `Materials` to see how claims depend on specimen and measurement conditions; use `Control` for dynamic systems and estimation limits; use `Agent` for planning, tools, trace evidence and reliability. Signal and Cymatics remain companion knowledge nodes. The queue identifies upcoming topics. A reader with no software can still follow the conceptual explanations and worked arithmetic.
