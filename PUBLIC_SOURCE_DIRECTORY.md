# Public source directory

> Supplementary navigation for the cleared public derivative. Source identities remain traceable. Omissions, redacted source files, and rebuilt manifests are documented separately; transformed files are not byte-identical originals.

The [`canonical/`](canonical/) directory retains the federation archive's original internal layout for the cleared public export. This path contains the **public derivative**, with explicit omissions and documented redactions. The complete original remains unchanged privately. Read the [browsable notice](canonical/PUBLIC_BROWSABLE_NOTICE.md), [browsable file manifest](canonical/BROWSABLE_FILE_MANIFEST.json), [omission inventory](canonical/PUBLIC_OMISSION_MANIFEST.json), and [publication verification receipt](evidence/publication/PUBLIC_DERIVATIVE_VERIFICATION.json) first.

## Browse the 24 checkpoint nodes

The first column follows the original 18 represented roadmap domains, then the supporting nodes outside that candidate list. These links establish navigation, not scientific acceptance or complete restoration. The familiar publication directories remain available alongside the preserved archive layout.

| Domain | Original layout in public derivative | Earlier publication directory |
| :--- | :--- | :--- |
| Measurement | [Browse](canonical/baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/MEASUREMENT-ATLAS/) | [Guide / source](Measurement/) |
| Causal reasoning | [Browse](canonical/CAUSAL-ATLAS/) | [Guide / source](Causal/) |
| Materials | [Browse](canonical/MATERIALS-ATLAS/) | [Guide / source](Materials/) |
| Control | [Browse](canonical/CONTROL-ATLAS/) | [Guide / source](Control/) |
| Agents | [Browse](canonical/AGENT-ATLAS/) | [Guide / source](Agent/) |
| Computation | [Browse](canonical/COMPUTATION-ATLAS/) | [Guide / source](Computation/) |
| Language | [Browse](canonical/LANGUAGE-ATLAS/) | [Guide / source](Language/) |
| Energy | [Browse](canonical/ENERGY-ATLAS/) | [Guide / source](Energy/) |
| Bioelectricity | [Browse](canonical/BIOELECTRIC-ATLAS/) | [Guide / source](Bioelectric/) |
| Manufacturing | [Browse](canonical/MANUFACTURING-ATLAS/) | [Guide / source](Manufacturing/) |
| Software design patterns | [Browse](canonical/SOFTWARE-DESIGN-PATTERNS-ATLAS/) | [Guide / source](Software_Design_Patterns/) |
| Distributed systems | [Browse](canonical/DISTRIBUTED-SYSTEMS-ATLAS/) | [Guide / source](Distributed_Systems/) |
| Neural architectures | [Browse](canonical/NEURAL-ARCHITECTURES-ATLAS/) | [Guide / source](Neural_Architectures/) |
| Cryptographic protocols | [Browse](canonical/CRYPTOGRAPHIC-PROTOCOLS-ATLAS/) | [Guide / source](Cryptographic_Protocols/) |
| OS internals | [Browse](canonical/OS-INTERNALS-ATLAS/) | [Guide / source](OS_Internals/) |
| Network stacks | [Browse](canonical/NETWORK-STACKS-ATLAS/) | [Guide / source](Network_Stacks/) |
| Database optimization | [Browse](canonical/DATABASE-OPTIMIZATION-ATLAS/) | [Guide / source](Database_Optimization/) |
| Compiler design | [Browse](canonical/COMPILER-DESIGN-ATLAS/) | [Guide / source](Compiler_Design/) |
| Chemistry | [Browse](canonical/CHEMISTRY-ATLAS/) | [Guide / source](Chemistry/) |
| Mathematics and fundamental physics | [Browse](canonical/MATHEMATICS-PHYSICS-ATLAS/) | [Guide / source](Mathematics_Physics/) |
| Computer architecture and digital hardware | [Browse](canonical/COMPUTER-ARCHITECTURE-ATLAS/) | [Guide / source](Computer_Architecture/) |
| Electronics and semiconductors | [Browse](canonical/ELECTRONICS-SEMICONDUCTORS-ATLAS/) | [Guide / source](Electronics_Semiconductors/) |
| Signal reference records | [Browse](canonical/common/nodes/signal-atlas/) | [Guide / source](Signal/) |
| Cymatics reference records | [Browse](canonical/common/nodes/cymatics-atlas/) | [Guide / source](Cymatics/) |

Signal and Cymatics are frozen reference subsets within the federation. Their upstream application repositories have separate versions and provenance. Browse the [Signal snapshot](canonical/baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src/atlas_forge/resources/federation/nodes/signal-atlas/1.0/) and [Cymatics snapshot](canonical/baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src/atlas_forge/resources/federation/nodes/cymatics-atlas/1.0.0/) for preserved notices and reference records.

## Shared context and history

| Directory or record | Purpose |
| :--- | :--- |
| [Common records and registry](canonical/common/) | Cross-domain manifests, typed records, and exact revision relationships |
| [Expanded nested sources](canonical/_nested/README.md) | Distinct nested source payloads exposed for browsing; [provenance](canonical/_nested/PROVENANCE.json) links their archive/member origins |
| [Historical source snapshots](canonical/history/) | Preserved earlier editions with explicit public omissions where required |
| [Baseline](canonical/baseline/) | Original collection baseline layout and frozen references |
| [Original shared documentation](canonical/docs/) | Scientific contract, reconstruction context, and historical release notes |
| [Original roadmaps](canonical/roadmaps/) | Preserved priority records; the original 30-domain plan remains unchanged |
| [Preservation resources](canonical/knowledge_preservation/) | Original source and evidence continuity material |
| [Survival reference](canonical/SURVIVAL/) | Original preservation and access context, with its historical limitations |
| [Historical receipts](canonical/receipts/) | Evidence from the edition/run identified inside each receipt |
| [Source tools](canonical/tools/) | Preserved utilities; inspect before execution and account for omitted inputs |
| [Browsable file manifest](canonical/BROWSABLE_FILE_MANIFEST.json) | Hashes for repository source and supplementary navigation; excludes archive containers |
| [Release-archive file manifest](canonical/FILE_MANIFEST.json) | Hashes for the release package, including eligible nested archive containers |
| [Original file manifest, historical only](canonical/FILE_MANIFEST.original-historical.json) | Preserved checksum context for the original edition; does not certify this derivative |
| [Public omission inventory](canonical/PUBLIC_OMISSION_MANIFEST.json) | Excluded paths and documented review reasons |

Historical documents can refer to omitted files, original archive hashes, or environment-specific commands. Such references are retained as provenance. Use the current public manifests and verification receipt to determine what this derivative actually contains. ZIP and WHL containers are excluded from Git; distinct eligible nested source payloads are exposed under `_nested/`, while identical payloads link to existing files. The browsable and release-archive manifests describe different file sets.

See [restoration and verification](RESTORATION.md), [publication status](PUBLICATION_STATUS.md), and [rights and reuse](README.md#rights-and-reuse).
