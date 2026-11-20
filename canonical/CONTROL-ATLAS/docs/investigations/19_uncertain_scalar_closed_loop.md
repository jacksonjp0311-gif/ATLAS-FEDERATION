# Investigation 19 — Nominal and interval robustness cannot be conflated

Given the *invented* scalar discrete plant `x[k+1]=a x[k]+b u[k]` with `u=-x`, compare two coefficient boxes. In the first, a∈[0.9,1.1] and b∈[0.25,0.45]. The four closed-loop poles range between 0.45 and 0.85 and the entire independent interval box satisfies |a-b|<1. The exact vertex argument works only because the scalar pole is affine and the set is a rectangle. In the second, a∈[1.35,1.8] and b∈[0.05,0.25], the worst case pole is 1.75. The model uncertainty set contains an unstable member.

A failed interval bound is not a physical failure report. The box boundaries must be justified independently: identification confidence intervals are not strict guaranteed parameter bounds, unknown actuator nonlinearities are not represented by a or b, and a larger unmodeled state can destabilize a nominally stable scalar projection. An engineer should design an experiment that measures the actual dynamics, actuator constraints, sensor timestamps and relevant operating regions.

**Run:** `python -m control_atlas robust-casebook`. **Result:** the node reports exact bounded mathematical classifications with assumptions and refusals; no equipment was controlled. Source scope: [Åström–Murray](https://fbswiki.org/) mathematical robustness topics.
