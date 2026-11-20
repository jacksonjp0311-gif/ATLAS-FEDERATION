# How to reconstruct and extend Computation Atlas

1. Begin with `README.md`, then `docs/DEPTH_MANUAL_v0.1.0.md`. The 34 chapters preserve definitions, preconditions, derivations, worked cases, limitations and bibliographic locators.
2. Validate the original repository bytes with `python tools/check_manifest.py verify .` (after a release archive has been sealed). A matching checksum does not authenticate the author.
3. Use a local Python 3.10+ runtime. `python -m unittest discover -s tests` and `python -m computation_atlas` operate offline with no provider or cloud keys.
4. The machine-readable records live in `computation_atlas/resources/common/`; the root collection also has a new eighth node. Consumer systems MUST keep the source refs and qualifiers.
5. Read the survival charter and the source-acquisition ledger. Links are not archived source bytes. Do not erase missing-source flags.
6. Run a separate independently coded oracle before claiming a method is numerically checked. No finite oracle run proves a universal theorem.
7. Repair suspected errors by appending a new revision, preserve old archive, record the failed input as a regression, and seek independent scientific review.

For a future survivor without Python: follow each chapter's hand algorithm and verify a short exact example, then implement from the published pseudocode and input contracts.
