# Control Atlas v0.2.0 release audit

**Content-development checkpoint, not scientific v1 or control safety validation.** Date 12 November 2026.

Two distinct v0.1.0 research lineages were found: the first already in the persistent Library and a different additional local research build. Rather than overwrite the prior release, this v0.2.0 merge preserves the older **60 record revisions, 36 relationship revisions, models.py, cases.py and numeric model tests unchanged**, and imports **57 additional records and 28 additional relations** with explicit `merged_into` provenance. Two MIT source-ID collisions are remapped, not silently deduplicated. The current Control node has **117 records (27 source cards), 64 relations** and 26 original chapters with 18 constructed investigations.

**Software tests:** Forge 188, Measurement 218, Causal 233, Materials 122, Control 92 = **853 passed, zero skipped** on Linux. The generic Forge schema and 6-node exact source closure passed, with **919 total source/research records**. A separate SciPy/NumPy numerical oracle agreed on **7,280 synthetic authored comparisons**, using seed 261112. This checks mathematical software only.

**Clean install:** The versioned Control 0.2.0 wheel installed with unchanged Forge/Measurement/Causal/Materials wheels in an isolated Python virtual environment. Both models.py and methods.py, both synthetic casebooks, 117 standalone records and evidence-limited context validation worked without importing source tree.

**Explicit non-claims:** No physical plant, industrial controller, HIL, system-identification dataset, safe controller tuning, independent engineering review, live Bitwork/AI answer evaluation, native Windows or desktop installation. A high test count is not evidence that real control systems are stable or that this content constitutes a safety standard. Source scopes vary and some are only author/publisher overview pages. Full v1 content and independent review remain unfulfilled.

**The original Library Control v0.1 release is not overwritten.** The owner requires all thirty domain libraries first, Bitwork/routing last, desktop transfer after routing.
