# Investigation 23 — A learning record with contrary observations

The memory gate receives four constructed candidate records with explicit revision hashes and source identifiers. One is current, tested, supported and uncontradicted; it becomes `eligible_for_external_review`. The second has one supporting and one contradictory source and becomes `review_conflicting_evidence`. The third failed its reported evaluation and becomes `preserve_failed_candidate_do_not_adopt`. The fourth has expired freshness and remains on hold.

No source text is included, executed or rewritten. The function does not silently choose the newest source, boost a candidate's confidence after failed verification or equate one source ID with independent evidence. Contradictory evidence is retained as an investigative lead.

Suppose a learned fix to a provider error improves a synthetic task but the provider's SDK changes. Its source revision and freshness become important: the old rule may be inapplicable even if previously tested. That is why content-addressed histories and scope are prerequisites for future continual learning. A live PEGASUS/SYMBIOTE integration would need separate trusted admission, rollback and repeated unseen-task comparisons. None is executed in this edition.
