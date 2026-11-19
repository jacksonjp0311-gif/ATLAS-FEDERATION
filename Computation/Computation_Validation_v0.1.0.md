# Computation Atlas 0.1.0 — evidence and release limitations

## Exact assertions tested

- The source-tree collection runner completed **1332 tests** across Forge, Measurement, Causal, Materials, Control, Agent (on its original seven-node snapshot), and Computation. **Zero failures and zero skips.**
- The independent author-generated numerical corpus generated **8910 comparisons**, compared with NumPy 2.3.5, SciPy 1.17.0 and NetworkX 3.6.1, plus brute-force subset enumeration.
- Eight-node source closure validates **1403 records, 626 relationships and 390 source cards**. 27 source-linked context checks and JSON schema validation passed.
- **2106 prior files** are byte-identical to archive SHA-256 `57a2db9daea62f9cfcc0728e2b2ff61d7d2020ad1d423d93ba87f2177969d505`. All previous node data, manifests, and tests remained unmodified.
- The standalone computation bundle deliberately omits five cross-domain edges whose targets are in the seven older nodes; it retains 170 local edges and the same 162 record hashes. The full eight-node package retains all 175 edges. Clean installation, local casebook and context retrieval pass.

## Scientific limitations that remain

- **No authenticated, local original publisher source files** among 390 source cards. These are 375 earlier + 15 new bibliographic pointers. The survival charter treats link-only primary sources as unresolved loss risk.
- **No independent domain-expert review**, verified formal theorem-prover proof, hardware benchmarking, physical experiment, live agent evaluation, or user-desktop execution.
- Runtime and memory complexity in the manual are theoretical claims under described models, not measured energy savings or engineering certification.
- Tests are finite and case-specific. An oracle using an independent implementation increases confidence but does not prove algorithms correct for every possible input.
- The earlier Agent suite asserts that Agent v1 had seven nodes; the suite is executed unchanged against the exact archived Agent v1 release, while the new eight-node data and contexts undergo independent live validation. This distinction is permanent evidence, not an exception swept under the rug.

## Release procedure

1. Verify standalone and root file manifests against their sealed archives.
2. Extract the complete ZIP into an empty folder, run `python tools/check_manifest.py verify .` and `python tools/survival_audit.py --check-files`.
3. Run `python tools/check_collection.py --out /path/outside/the/archive`. The runner also restores and re-tests the embedded previous Agent v1 snapshot.
4. Install Python wheels from `wheels/` and baseline wheels without internet; execute `python -m computation_atlas` and standalone source-linked retrieval.
5. Record the final external archive SHA256 and extracted replay receipt without modifying the sealed archive.

**Status:** scoped computation research foundation v0.1.0; not scientific content v1.0. The user project will complete 30 domain libraries before any Bitwork routing and integrated evaluation or desktop transfer.
