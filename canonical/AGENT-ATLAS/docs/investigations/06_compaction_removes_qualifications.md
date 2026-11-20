# Investigation 06 — A memory without its qualifier becomes a false credential

**Origin:** fabricated memory entries. One memory claims “analysis completed” but carries the qualifier “source not expert reviewed.” Another describes a provisional finding with an untested model assumption. Their full memory records have explicit token costs, source IDs and status. A six-token illustration budget admits only the highest-ranked qualified unit.

If a context builder strips the qualifier while preserving the claim, it can create an apparent proof of scientific or engineering readiness. This is particularly dangerous when later agents aggregate summaries across multiple parents or model configurations. Our `select_qualified_memories` only selects whole memory units, retaining the source ID and qualifier. If a whole unit cannot fit, it is excluded and marked as such.

The rank is an original arithmetic heuristic; it is **not** a calibrated truth probability, semantic matching model or live Atlas routing layer. The score can be wrong, a fresh source may be less relevant than an old one, and the token counts are caller-supplied. Real data require an auditable source store with corrections, privacy controls, decay and tests of retrieval usefulness.

**Verification plan:** construct task questions that deliberately require the excluded caveat, evaluate whether the agent admits uncertainty when it cannot retrieve the full evidence, compare with a retrieve-all and summary-only baseline, and record cost. Implement later in the common Bitwork stage only after the full corpus exists.

**Sources:** Reflexion and Generative Agents architectures, plus Forge contract's existing whole-evidence selection policy.
