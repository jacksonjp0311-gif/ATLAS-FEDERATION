# ATLAS FORGE — Complete recovery and evidence gap-closure handoff

**This is a small companion toolkit, NOT the whole scientific Atlas and NOT a new canonical release.** The full canonical federation remains `Computer_Architecture_v0.5.0_continuity` in `/ATLAS FORGE/Releases/Computer_Architecture_v0.5.0_continuity/`.

## Recover the complete Atlas

Retrieve all 11 `ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip.partNNN` files from `FullArchiveParts/`, `FULL_ARCHIVE_PARTS_MANIFEST.json`, and `RESTORE_FULL_ATLAS.py`. With Python 3.10+ (offline) run:

```sh
python RESTORE_FULL_ATLAS.py --parts-dir . --output ./ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip
```

Expected SHA-256: `ea4b1f70eeaabeec0ea5b553c27bf4b3e094efc1280b1067c3c4754247b3bf8e`. Expected bytes: `711416573`. The restorer must verify 11 volume hashes, 9,365 ZIP member entries, safe ZIP paths and full digest. Extract the ZIP into a clean folder. Open `SURVIVAL/ATLAS_OFFLINE_PORTAL.html` locally or use Python:

```sh
python tools/atlas_offline.py catalog
python tools/atlas_offline.py audit
python tools/atlas_offline.py gaps
python tools/atlas_offline.py challenge
python tools/check_collection.py --out /separate/outside/regression
```

## Understand the gaps and accept new evidence safely

Run the companion `atlas_evidence_gate.py plan --atlas /path/to/extracted/federation --out /new/path/plan.json`, then read `SCIENTIFIC_GAP_CLOSURE_PROTOCOL.md`. Work through missing original domains in the preserved priority queue, beginning with `bioelectric-atlas` (priority 9). Independent evidence intake uses `inspect`; *metadata acceptance is never equal to scientific certification*.

## Verified 2026-11-17

The full v0.5.0 archive was recovered directly from its 11 Library parts, with matching canonical SHA-256. All 9,364 individual file hashes and 4,830 exact relation endpoints validated; fresh full regression reproduced 2,706 passing tests across 34 suites and matched the historical test-receipt SHA-256. Forty-nine offline reader/recovery tests passed. The companion evidence gate passed 20 standalone tests. No independent physical manufacture, publisher-original authentication, licensed public redistribution or peer-review is claimed.
