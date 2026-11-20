# Measurement-first Atlas build workflow

This checkpoint turns the shared standard into an executable local workflow. It does not complete Measurement v1.

## Starting from the combined workspace

The workspace contains `ATLAS-FORGE/`, `MEASUREMENT-ATLAS/`, and local Python wheels. From Forge, run:

```powershell
py -3 tools/run_workflow.py --measurement ..\MEASUREMENT-ATLAS --out output\check-001
```

Choose a new output directory for each run. The runner invokes both unit suites, common conformance, skill-header validation, source-intake structure validation, authored context diagnostics and the synthetic Measurement casebook. It also confirms that advancing to Causal Atlas is blocked. It writes command lines, exit codes, elapsed time and log hashes. A successful runner result is software-check evidence, not v1 acceptance.

## One active Atlas

`workflow/state.json` identifies Measurement. `workflow/acceptance.json` holds candidate G1–G8 criteria and proposed thresholds. These are not yet owner-approved/frozen. `workflow/gate_decisions.json` records only supported outcomes.

A passed gate must point to a structured actual-execution receipt of the required kind, bound to the release-input subject digest and criteria digest, plus a recorded review identity/date. Fixture and unrun receipts cannot pass a gate. The review identity is a local assertion, not independently authenticated. Do not treat this administrative guard as tamper-proof access control against an operator who edits the entire repository.

The runtime will not mark v1 ready until all gates pass and criteria are explicitly frozen/approved. `advance` checks the gate and does not itself create a new domain or mutate state. The new scaffold builder enforces the same rule.

## Intake and migration

1. Read the source-curation skill. Inspect the original primary passage; record the exact portion, date, uncertainty, rights and limitations. A page index is navigation, not full review.
2. Author bounded records in the Measurement evidence additions file. Run `python tools/check_curation.py ../MEASUREMENT-ATLAS/evidence/primary_reference_additions.json`.
3. Run `python tools/build_common.py --help` for the offline rebuild interface. Preserve prior snapshots; do not edit release hashes to hide a failed import.
4. Run common conformance and schema validation. Domain assumptions must survive migration exactly.
5. Run context diagnostics and inspect the actual rendered package. Search scores do not approve a scientific claim.

## Skills and host integration

The five project-local `SKILL.md` files use the Agent Skills name/description convention. A compatible coding host may discover `.agents/skills`; otherwise explicitly point the host to `AGENTS.md`. No host installation, global plugin activation or account Memory update occurred here.

Format references: https://agentskills.io/specification and https://developers.openai.com/codex/skills/ . The skill instructions call the included tools; they do not create additional privileges.

## Release order

Finish Measurement scope and evidence, test the actual Bitwork mapping and model consumption, freeze the independent evaluation, run the platform matrix, then judge v1. Until then, publishable checkpoints must keep the `v1_ready: false` status and the outstanding gates visible. The ten-domain roadmap does not authorize starting them early.
