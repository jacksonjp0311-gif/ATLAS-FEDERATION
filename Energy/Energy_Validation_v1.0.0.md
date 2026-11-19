# Energy Atlas v1.0.0 — software and scientific validation

**Content edition:** scoped reconstruction-ready v1. **Independent science and physical implementation:** HOLD.

## Reproduced engineering evidence

- **1,743 tests passed, zero failures, errors and skips** in the source-tree ten-node suite (Forge, Measurement, Causal, Materials, Control, Agent, Computation, Language, Language V1, Energy V0.1 historical, Energy V0.2 historical, Energy V1).
- The v0.2 suite runs unchanged against a content-addressed historical test snapshot copied byte-for-byte from the immutable v0.2 archive; v0.1 tests still run against its own original release snapshot.
- **8,670 independent NumPy comparisons** of authored synthetic energy budgets and refusal cases, with maximum absolute arithmetic discrepancy 4.54747e-13 in tested inputs. This is code verification, not physical measurement accuracy.
- Shared registry: 10 nodes, 2,052 records, 1,245 relationships, 466 source cards. All **64** representative source-linked contexts and compiled JSON schema validations pass. The slower Draft 2020-12 validator ran on bounded samples, not each large corpus context.
- Clean wheel installation in an isolated Python environment: nine installed packages, including Energy v1.0.0; standalone retrieval exposes 301 source-closed Energy records and 256 local relations. Five additional Energy cross-domain relations live only in the full federation.
- **2,327 files unchanged byte-for-byte** from the v0.2 source archive (including earlier nine node packages and historical baseline); all 241 previous Energy record revisions and 205 prior full-node relation revisions remain exact.
- 64 original research chapters, 51 worked investigations; manuscript approximately 39,085 words, with proof assumptions, source links and safety exclusions.

## Source and life-safety gaps

- **0 of 466 bibliographic source cards** carries an original publisher file authenticated under the strict local original-byte audit. Direct NIST CODATA ASCII acquisition failed and was not misrepresented as archived source material. Authenticated primary materials must be collected later under appropriate rights.
- No live battery, generator, water system, grid, heating plant, or physical instrument was operated or tested; there is no independent peer review of all claims.
- A static energy balance does not validate electrical protections, power quality, islanding, emergency power, medical continuity, generator CO hazards or potable water. NFPA 855's restricted text was not mirrored.
- Scenario-weighted outcomes use *stipulated weights* rather than a validated weather/outage probability model.

## Reconstruct offline

From a fresh extracted release tree run `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, and `python tools/check_collection.py --out /external_results/unique_directory`. From Energy-Atlas run `python -m energy_atlas v1-casebook`; the optional oracle `python ENERGY-ATLAS/tools/v1_oracle.py` requires NumPy.

The final external release receipt will attest archive checksums and the **extracted** full regression after sealing; the presence of this text alone does not assert that the latter has happened.
