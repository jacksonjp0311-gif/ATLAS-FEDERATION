# ATLAS FORGE — Computer Architecture 0.4 reconstruction and audit

Use the exact archived canonical Computer Architecture v0.3.0 full federation ZIP (SHA-256 `c587091c2ad6064c4aeffac9a20a1c210fb737393782c184d37bba1ba30636ed`) and a hash-verified v0.4.0 direct patch. The full archive is reconstructed byte-for-byte, preserving the previous 14 node manifests, all knowledge JSONL historical prefixes, all historic tests, and the original 30-domain queue.

From the resulting clean extracted federation root:

```sh
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /a/new/unique/external/results
```

From the Computer Architecture subfolder:

```sh
python -m unittest discover -s tests -p 'test_v04_*.py' -q
PYTHONPATH=. python evidence/independent_oracle_v04.py
PYTHONPATH=. python evidence/continuity_challenge_v04.py
```

Prior v0.1/v0.2/v0.3 test suites must be replayed against their exact immutable snapshots; no old acceptance assertion may be weakened to match the new node count or record totals. The AT8/0.1 ISA is unchanged. Python standard library is sufficient for core models. Physical fabrication and scientific peer review remain open.
