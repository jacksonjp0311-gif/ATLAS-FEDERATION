---
name: atlas-release-gate
description: Validate an Atlas release and prevent v1 promotion or next-domain work without the required evidence.
compatibility: Requires Python 3.10 or newer and access to the Atlas Forge checkout.
---

# Release gate

Read `workflow/acceptance.json` before testing. Never change criteria because a final evaluation failed. Run the complete suites, JSON Schema checks, common-node checks, numerical casebook, authored retrieval diagnostics, clean-wheel install smoke checks, and archive extraction checks.

Use `python tools/workflow.py status` to inspect G1 through G8. A gate marked passed must bind to the current release inputs and criteria, with hashed evidence and a recorded review decision. G6 requires real pinned Bitwork and actual AI consumption. G7 requires frozen independent held-out evaluation. Mock data cannot satisfy those gates.

Run `python tools/workflow.py advance --node causal-atlas`. While Measurement v1 is incomplete, exit 2 is the expected protection. Do not bypass it by relabeling an intermediate version v1.

Generate manifests only after content is finalized. Verify archives after extraction, then report actual local results and unrun platforms. Never state that CI passed or a repository was pushed unless the remote state was checked.
