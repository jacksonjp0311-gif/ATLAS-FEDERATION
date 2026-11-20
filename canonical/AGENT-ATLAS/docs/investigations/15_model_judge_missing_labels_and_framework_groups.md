# Investigation 15 — A missing MAST annotation must not become “no failure”

**Origin:** constructed metadata with the 14-code published MAST-Data schema; no original corpus rows are included. A toy trace has `1.1=1` for a model-judge warning, `3.2=0`, and all other codes `null`. The grouped summary reports a one-of-one positive proportion for code 1.1, zero-of-one for 3.2, and **no known denominator** for the other 12 codes. It never emits 0% for an entirely unknown code.

Two frameworks can reuse the same local trace index without being duplicate records; composite identifiers must include the context. Rows are grouped by framework and benchmark, but even a precise proportion among the known labels cannot be read as the objective failure probability of a deployed system. The dataset mixes frameworks, models and tasks and uses LLM-judge annotations rather than independent end-state ground truth.

**Reproduction:** `python -m agent_atlas v03-casebook`. **Original study:** MAST-Data source card describes 1,642 traces under CC BY 4.0; the present release has read **zero original rows**. It does not present a toy label as a finding from the published data.
