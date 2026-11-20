# ATLAS FORGE — OS Internals Atlas v1.0.0 (original federation node #15)

> Reconstructible foundations, explicit assumptions, independent finite tests, and honest hardware holds. **Not an operating system distribution or boot image.**

## Reader entrypoints

- `docs/DEPTH_MANUAL_v1.0.0.md`: 22 original technical chapters and negative cases.
- `docs/chapters/`: standalone research chapters.
- `os_atlas/`: dependency-free Python reference models; `python -m os_atlas`.
- `tests/test_reference.py`: regression, negative conditions and determinism.
- `evidence/independent_oracle.py`: separate finite comparators including brute dynamic programming.
- `atlas_manifest.json`, `data/*.jsonl`: immutable exact-revision Atlas records, relations and scientific bibliographic pointers.

## Replay offline

```sh
python -m unittest discover -s tests -q
python evidence/independent_oracle.py
python -m os_atlas
```

## What it is not

This is not Linux, a driver, an ELF execution environment, secure filesystem, physical firmware, production virtual memory or a crash-consistency guarantee. Compiler, emulator and hardware replication are future separately authorized milestones. Publisher source files are pointers, not authenticated local originals.

Next original priority: Network Stacks #16. All 30 content domains before routing.
