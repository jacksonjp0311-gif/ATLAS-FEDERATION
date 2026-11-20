# ATLAS FORGE Computer Architecture v0.2 — Offline reconstruction

1. Obtain the exact prior `ATLAS_COLLECTION_Computer_Architecture_v0.1.0.zip` via the official Atlas release chain; its SHA-256 is `527a57f68840b327f6ae1e67b190cb204c6a9513c38770f616f889e1e5dc94f4`.
2. Apply `RESTORE_ATLAS_FORGE_COMPUTER_V02.py` and the versioned delta with embedded/external matching manifests, using no network. Verify all per-file hashes and exact final archive SHA-256. Never replace the historical full ZIP.
3. Extract to a clean directory and run: `python tools/check_manifest.py verify .`; `python tools/survival_audit.py --root . --check-files`; `python tools/check_collection.py --out /separate/nonexistent/destination`.
4. In `COMPUTER-ARCHITECTURE-ATLAS`, run local tests, the independent numerical oracle and `evidence/continuity_challenge_v02.py`.
5. Independently rebuild the source program into ROM, protect/recover ROM through SECDED, compare atomic/microcycle and AST states, and inspect 12 remaining manufacturing evidence requirements. A successful software trace **does not** certify a physical CPU.
6. Preserve `DOMAIN_QUEUE.json` exactly. Routing comes after all content domains, and global validation/desktop transfer afterward.
