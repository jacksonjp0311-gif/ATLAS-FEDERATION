# 35. Memory survives when qualifiers survive

A self-improving agent may retain a useful rule after a task, but the stored conclusion must not outrank the evidence that produced it. Memory compactors can remove small qualifications (“in this benchmark,” “for one tool version,” “only at low load”) while preserving the headline, creating a false generalization. Multiple workers may also report incompatible hypotheses. An agent can accumulate more text and become less reliable if its future retrieval retrieves unqualified claims rather than the facts and counterexamples.

## The memory is an assertion with a lifecycle

This edition treats a candidate memory as a scoped and versioned claim: memory ID, claim revision SHA-256, scope ID, supporting and contradicting source IDs, reported evaluation result, candidate state and freshness. The source IDs are pointers to evidence, not proof that the underlying evidence is independent or authentic. The function performs no persistent write.

Decisions respect explicit precedence. Superseded revisions remain archived, not silently erased. Expired or unknown freshness blocks promotion. Contradicting sources trigger review even if the model's latest test claimed success. Reported evaluation failure blocks adoption. Untested or unsupported claims remain pending. Only a current, tested, supported, noncontradicted candidate becomes `eligible_for_external_review`. This says nothing about actual model behavior until a trusted evaluation and admission process verifies the sources.

## Four worked memories

One synthetic rule has support, a reported passing test, no contradiction and current freshness: eligible for review. Another has the same favorable report but a conflicting independent-looking source ID: review conflict. A third failed its reported test: preserve as failed knowledge, not a successful rule. A fourth has expired provenance: block despite its past success. These outputs are useful for designing an agent learning system but are not an experiment showing that its memory improves real performance.

## Contradiction does not equal falsification

Two observations may disagree because they apply to different task conditions, measurement pipelines, APIs or timestamps. A safe ledger retains both and asks for a discriminating experiment. Assigning one positive and one negative role to the **same source ID** is rejected until the claims or evidence are separated; silently using one record to support both sides would make the graph ambiguous.

For a future AI consumer, export not just the memory's proposed lesson but its source chain, evidence status, counterevidence, task/version scope, expiry and uncertainty. An efficient retrieval layer that strips these components would degrade safety and scientific quality. The user-directed Atlas architecture explicitly keeps the router out of this stage; the final system will evaluate whether evidence-aware memory improves unseen-task outcomes after all 30 domain nodes exist.
