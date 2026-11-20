# Bitwork bridge and integration boundary

## Inspected implementation

Perci main was inspected on November 12, 2026 at `0811f45a5c7322f77a17c75856eabc9a7a620870`:

- https://github.com/jacksonjp0311-gif/Perci/blob/0811f45a5c7322f77a17c75856eabc9a7a620870/README.md
- https://github.com/jacksonjp0311-gif/Perci/blob/0811f45a5c7322f77a17c75856eabc9a7a620870/docs/BITWORK_WHITEPAPER.md

The documented Bitwork `route` classifies requests into task/category labels. The observed contract is not an exact Atlas record-ID resolver. The whitepaper describes hashed lexical/structural 4,096-bit representations; it does not make an arbitrary text hash into a verified semantic embedding. Its published limitations and benchmark caveats are retained rather than transplanted as Forge performance claims.

## Implemented bridge

`python -m atlas_forge acs route-request "expanded uncertainty" --node measurement-atlas` exports a request digest, registry revision and candidate text/record map. An external integration may supply an `atlas.route-receipt/1` object containing runtime/version/implementation commit/execution evidence, encoder revision, index revision, status and exact candidate IDs/revisions with finite scores and named score scales.

`acs context ... --route-receipt receipt.json` checks that the request, registry, selected nodes and every candidate revision match. Unknown IDs, stale revisions, duplicate entries, unlabelled scores and extra executable fields are rejected. An invalid, error or abstaining router falls back to BM25 with an explicit reason.

The bridge does not launch a subprocess, fetch weights, build prototypes or execute remote code. It does not attest the claimed runtime identity. Accepted receipts remain `self_reported_not_attested` and `live_bitwork_run: false`. Unit fixtures are marked `test-fixture-not-bitwork`. No fixture is integration evidence for G6.

## What G6 still needs

The real Perci/Bitwork implementation must be pinned, its Atlas-specific encoder/prototype mapping built and tested, its emitted candidates bound to the same records, and a real consuming model must use the assembled context. Retain successes, failures, fallback and abstentions. Then compare against same-corpus/same-budget baselines. These are not simulated by the current bridge, and no Perci code or user installation was changed.

This checkpoint can produce a valid input request and verify an output receipt. It cannot truthfully label that path a live integrated Bitwork retrieval engine yet.
