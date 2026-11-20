# ATLAS FORGE — Software Design Patterns, Priority #11

**One canonical original federation, not a new ATLAS.** This v0.1.0 reference adds offline standard-library recovery and resilient software engineering models to the original scientific archive.

## Navigate the reference

- `docs/DEPTH_MANUAL_v0.1.0.md`: 24 technical chapters; exact invariants, worked examples and failure/assurance limitations.
- `docs/CASEBOOK_v0.1.0.md`: 24 constructed investigations and negative controls.
- `docs/SOURCE_REGISTER_v0.1.0.md`: official bibliography, rights and source-authentication queue.
- `patterns_atlas/contracts.py`: canonical JSON, versioned envelopes, strict schema and migrations.
- `patterns_atlas/state.py`: finite state machine, no invented transitions.
- `patterns_atlas/resilience.py`: circuit breaker, bounded retry and capacity bulkheads with simulated clock.
- `patterns_atlas/composition.py`: Strategy, Factory, Adapter, Decorator, Pipeline.
- `patterns_atlas/ledger.py`: SQLite WAL journal with local ID deduplication and hash-linked replay.
- `patterns_atlas/atomicfiles.py`: bounded content-addressed immutable blobs and filesystem pointer changes.
- `patterns_atlas/events.py`: single-writer event-chain replay and fail-closed corrupt-head handling.
- `patterns_atlas/workflow.py`: SQLite→derived snapshot recovery after simulated interruption.
- `evidence/independent_oracle.py`: independent finite reference calculations and constructed restarts.

## Run offline

Requires Python 3.10+ and its standard library. From this node directory:

```sh
python -m patterns_atlas
python -m unittest discover -s tests -q
PYTHONPATH=. python evidence/independent_oracle.py
```

From the **entire original federation root**:

```sh
python tools/check_manifest.py verify .
python tools/survival_audit.py --root . --check-files
python tools/check_collection.py --out /unique/outside/federation_checks
```

## The real reconstruction boundary

A local SQLite COMMIT and a separate file pointer update are **not** one atomic transaction. The reference makes the journal authoritative and the file snapshot rebuildable, then demonstrates restoration after a simulated interruption. Its idempotency keys prevent repeated pure reducer execution inside one local database transaction; they do **not** guarantee exactly-once effects on a real actuator, printer, generator, vehicle, remote database or human.

Python's standard library being available is itself a dependency. This package does not demonstrate disk durability under physical power loss, file system guarantees on the user's target hardware, network consensus, secure trusted data origin, life-safety control or independent expert validation.

## Program sequencing

Original 30-domain roadmap remains byte-identical. Bioelectric priority 9 is complete as an educational reference; Manufacturing priority 10 is already represented, Software Design Patterns priority 11 is the current node, and Distributed Systems priority 12 is next. No Bitwork router work before completing content-domain libraries.
