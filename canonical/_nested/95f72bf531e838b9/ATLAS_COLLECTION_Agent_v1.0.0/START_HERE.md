# Start here — offline ATLAS FORGE reading

The core files are original plain-text knowledge references and structured JSONL records; they do not require a cloud model to read. Start with `docs/HUMAN_KNOWLEDGE_SURVIVAL_CHARTER_v1.md`, then select a domain through its `README.md` and reference guide. To reconstruct the mathematical foundations of agents, read `AGENT-ATLAS/docs/DEPTH_MANUAL_v1.0.0.md` and its worked investigations.

If Python 3.10+ exists, use `python tools/survival_audit.py --root .` to check references and show missing authenticated source documents. When the release is sealed, `python tools/check_manifest.py verify .` checks file integrity. Run `python tools/check_collection.py --out output/check-new-unique-name` for complete engineering tests. These are not scientific peer review.

**Owner instructions:** complete all thirty scientific domain libraries; build the Bitwork router only after domain content is finished; then conduct system-wide evaluation and transfer to the desktop. No Windows installation is implied by the existence of this archive.
