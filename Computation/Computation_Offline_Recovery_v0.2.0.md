# Computation Atlas 0.2.0 — independent offline restoration procedure

**Purpose.** This guide describes how a future custodian can restore and verify the *exact bytes and demonstrated software behavior* of this edition without relying on an AI model, the original authors, or online search. It does not assert that every scientific claim is true or that the bibliography has been archived.

## 1. Keep independent copies

Retain the complete ATLAS Collection ZIP, the Computation Atlas standalone ZIP, their `.sha256` companion files, and the release validation JSON on **independent media**. Retain at least one copy that is physically disconnected from the working machine, and periodically test restoration on separate hardware. Hashes stored alongside an archive detect accidental damage but cannot establish the author's identity or prevent coordinated replacement. Independent signatures, custody records, and trusted distribution channels are additional work.

## 2. Check the archive before extraction

Using Python 3.10+ with no network connection:

```python
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
archive = Path('ATLAS_COLLECTION_Computation_v0.2.0.zip')
print(sha256(archive.read_bytes()).hexdigest())
with ZipFile(archive) as z:
    assert z.testzip() is None
    assert not any(p.startswith('/') or '..' in Path(p).parts for p in z.namelist())
```

Compare the printed hash against an **independently retained** expected checksum before extracting. This script verifies the ZIP's internal CRC but neither the scientific quality nor provenance of its content. Only extract after ruling out absolute paths, `..` path components, and links inappropriate for the target machine.

## 3. Reconstruct and test the library

After extraction, enter the root directory. Run:

```sh
python tools/check_manifest.py verify .
python COMPUTATION-ATLAS/tools/check_manifest.py verify COMPUTATION-ATLAS
cd COMPUTATION-ATLAS
python -m unittest discover -s tests -q
python tools/numerical_oracle_v02.py
```

For collection-wide checks, return to the root and run `python tools/check_collection.py --out /path/to/a-new-external-directory`. The output directory must not be inside a sealed manifest's file inventory. The full suite uses an unmodified seven-node Agent v1 checkpoint stored in the history archive; older test assumptions are not silently reinterpreted as newer federation requirements.

If optional NumPy, SciPy, NetworkX or schema libraries are unavailable offline, report that the corresponding checks were **not run**. The original pure-Python computation models and their local unit tests do not require those optional dependencies. Do not substitute a skipped test with a passing receipt from another system.

## 4. Rebuild an algorithm from the written explanation

Choose a concrete chapter, such as `35` (exact linear algebra), `39` (minimum spanning forest), or `42` (prefix coding). Identify the input contract and refusal behavior, reconstruct the mathematical invariants from the chapter, implement the algorithm in a separate file, and test against the chapter's counterexamples before consulting the supplied implementation. Inspect `computation_atlas/advanced.py` only afterward. Do not assume that copying the provided Python file proves the algorithm; the **invariant, worked trace, and tests** together make reconstruction possible.

## 5. Check original software-source bytes

The captured `TheAlgorithms/Python` files are stored under `COMPUTATION-ATLAS/evidence/licensed_primary_software/TheAlgorithms-Python-30507bbe/`. The exact original snapshot is pinned to commit `30507bbe41397065728167fb09aa820f9fce8dc7` and includes `jump_search.py`, `extended_euclidean_algorithm.py`, their recorded raw SHA-256 and Git blob SHA-1, and the repository's MIT license. The same originals are bundled in the standalone Python wheel. Run the `source_archive_audit` method to verify they are the same expected bytes. Preserve the full license and attribution with any copies of this third-party source.

**Boundary:** This snapshot contains two educational Python implementations and an MIT license. It is **not** a scientific paper, a peer-reviewed correctness proof, or a license to copy the remaining works cited by the Atlas. The other 390 prior source cards remain bibliographic pointers; no original journal-paper source byte preservation has been established here.

## 6. Distinguish integrity from truth

- A checksum answers whether bytes match a claimed digest.
- A schema check answers whether machine-readable relationships have an accepted shape.
- A numerical oracle answers whether a tested implementation agrees on the constructed cases.
- A mathematical proof answers whether a conclusion follows from explicit assumptions, and requires its own review.
- Empirical validation requires measured data, disclosed protocols, controls, and independent replication.

These are different evidence levels and must never be collapsed into one success indicator. Any unknowns must remain visible in derivative knowledge packages.

## 7. What still needs acquisition

Acquire legal primary copies of foundational scientific and mathematical texts; retain immutable revision metadata and rights terms per item; re-run this guide on a second system, including Windows; seek independent domain expert review; and extend content toward scoped Computation v1 before beginning Language Atlas. Do not implement Bitwork routing until all 30 reference domains have been constructed.
