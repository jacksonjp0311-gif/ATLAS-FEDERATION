# Final acceptance handoff

This checklist is for the same Measurement milestone, not permission to start Causal Atlas.

## Scientific reviewer

Review the eight scope families and the source register. For each record, check whether its precise claim, qualifiers, units and applicability are supported by the named source portion or derivation. Mark disagreements and gaps. Review synthetic examples separately from the published Pontius observations and from publisher illustrations. The source discrepancies must remain visible.

Record reviewer identity, relevant competence, date, examined input hashes, decisions and limitations. An assistant-generated form, a source-structure check, another run of the same tests or the author's self-review is not an independent human review. No reviewer has been invented for this candidate.

## Windows validation

On the ROG, extract the complete workspace and run `RUN_V1_ACCEPTANCE.cmd`. It executes the actual tests and writes a fresh host receipt, identifying Python and the native platform. Its final preflight deliberately returns exit code 2 when final gates remain incomplete. Keep the test-stage outcome distinct from the final acceptance outcome. Merely shipping this launcher is not a Windows test pass.

## Deferred integration and evaluation

After the knowledge stage, inspect and pin the actual Bitwork runtime, implement the exact prototype-to-record mapping, run it against the same immutable corpus, and retain real route/failure traces. Supply the resulting context to a named model and record its actual outputs. Do not substitute fixture receipts or a hand-authored model answer.

Before final testing, freeze the independent question set, retrieval arms, corpus and budget, model identifiers, sample-size rationale, scoring rubric and uncertainty analysis. Keep development diagnostics separate from held-out results. Performance and cost benefits require measured comparisons, not the release number.

## Final promotion

Run `python tools/v1_readiness.py --require-final` from the workspace root. Every required gate must be supported for the exact release inputs, and the criteria must be owner-approved and frozen. Only then prepare a final 1.0.0 package, signed-off release notes and separately authorized publication. A candidate package cannot authorize its own final promotion.
