# Investigation 19 — A matching hash does not authenticate a worker result

A synthetic worker returns an expected artifact SHA-256 identical to the reported observed hash. Its parent dispatch ID, task ID and goal revision match, and its evaluator revision and reported passing state are present. The `audit_artifact_proof` classifier returns `structurally_eligible_given_trusted_host_facts`.

This label is intentionally weaker than verified success. The packet fields were **supplied by the caller**, and the function did not read an artifact, compute a digest from its bytes, verify a host signature, or independently run acceptance tests. An attacker could copy the same fabricated hash into two fields. No agent learning can safely be admitted on the strength of that string comparison alone.

Change only the worker receipt dispatch ID to another value: classification becomes `deny_missing_or_mismatched_parent_dispatch`. Change the goal revision: `deny_foreign_goal_revision`. Change the observed artifact hash: `deny_artifact_hash_mismatch`. Set the operator Stop flag and an uncertain side effect: `respect_operator_stop` dominates every favorable other signal. With Stop unset but the tool marked `submitted_unknown`, the classifier returns `reconcile_external_effect_first` even when an artifact appears complete.

For a real trustworthy result, the host would have to supply an independently authenticated dispatch receipt, actual artifact-byte hash or equivalent trusted storage guarantee, provider-side effect observation, and a separate evaluator that truly measures task success. These are not simulated here. All nine v0.4 casebook fixtures are constructed and contain no real authenticated host events.
