# Control Atlas v1.0.0-rc.1 — validation and open scientific gates

**Status: a substantive scoped content release candidate, not final scientific v1, qualified real-world control, or independent expert review.**

## Engineering validation executed

- All **1005 automated tests passed**, zero skips, across six-node collection: Forge 188, Measurement 218, Causal 233, Materials 122, Control 244. Full source-tree `tools/check_collection.py` passed; it checks the contract, context closure, pinned existing nodes, casebooks, manifest/schema and source references.
- **249 Control records** including **51 source cards**, **147 Control relations**, and **1,051 total Forge records** across six nodes; all old **214 Control record revisions** and **124 relations** unchanged.
- NumPy separately computed **19380** numerical comparisons and matched the new 2×2 observer and identification arithmetic within reported tolerance. The oracle is author-coded, synthetic and not independent control experimentation.
- A clean install of Forge, Measurement, Causal, Materials and Control wheels passed. The Control wheel exposes all 249 records with valid budgeted source-linked context and runs the v1 casebook without using source-tree imports.
- **1190 protected files** from the previous collection are byte-for-byte unchanged by SHA-256, including the original 771 baseline files and all prior non-Control node snapshots.

## Evidence that is authentic and work still blocked

- OpenMCT Mendeley v2 is a recent CC BY 4.0 study with controller experiments, but actual source log bytes could not be downloaded here. The strict parser, duplicate DMM handling and chronological ARX test were exercised only on synthetic fixtures. **Do not claim a numerical OpenMCT model fit or its held-out prediction accuracy**.
- A second educational public repository supplied three 49-row (`time,rpm`) traces at nominal PWM labels 30, 50, 70; we calculated descriptive metrics from public raw text and retained Git blob/source pointers. Per-sample applied PWM is absent, so **dynamic plant identification is not supported** from those files. The raw CSVs are not redistributed without established rights.
- The new 2x2 observer bounds require known matrices and bounded process/sensor disturbances. Consistency exceptions and intervals do not attribute sensor fault cause, establish measured hard bounds or justify automated action.
- NIST OT r3 final and r4 initial-draft differences remain labelled by publication status, not flattened into a supposed certification standard.

## Outstanding v1 gates

Raw-data replay and independently reviewed source passages; realistic apparatus/calibration and actuator/sensor bounds; robust multivariable model-error validation on authentic experiments; uncertainty and closed-loop identification bias; physical/hardware-in-the-loop investigation; signed engineering review; Windows host confirmation. All 30 Atlas content domains are to be built before the routing system, and the computer transfer follows routing/integrated evaluation.

**Software success does not transform synthetic control algebra into physical safety evidence.** The content version remains `1.0.0-rc.1` until the specific scientific evidence blockers are resolved.
