# Compiler Design v0.1.0 reconstruction procedure

1. Verify the full predecessor archive SHA256 `13d8f5d19ed98d052dad9c424b22295599722b82a2938ec6f94f2a95122fe8c2` against the independently trusted manifest.
2. Apply the direct deterministic Compiler v0.1.0 incremental patch using `RESTORE_ATLAS_FORGE_COMPILER_V01.py` from the matching release folder; fail closed on mismatched member, changed original file or wrong final ZIP hash.
3. Independently check all final files against `FILE_MANIFEST.json`; preserve historical exact-revision source records and the original 30-domain queue byte-for-byte.
4. Extract the release in a fresh directory and use `python tools/check_manifest.py verify .` and `python tools/survival_audit.py --root . --check-files`.
5. Run `python tools/check_collection.py --out /new/empty/check_output` on source and fresh extracted archives; compare exact checks JSON bytes and test counts.
6. In `COMPILER-DESIGN-ATLAS`, run `python -m unittest discover -s tests -q`, then `python -m evidence.independent_oracle`. Execute the example; compare compiled output against an independent tree evaluator, including traps.
7. Only after Library upload, readback, SHA comparison and preserved release receipt may `/ATLAS FORGE/CURRENT_CHECKPOINT.json` advance. No step is a physical or independent scientific certification.
