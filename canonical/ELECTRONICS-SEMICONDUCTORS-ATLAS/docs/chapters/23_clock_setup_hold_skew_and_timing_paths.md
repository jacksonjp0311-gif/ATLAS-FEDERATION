# Chapter 23: Timing inequalities for a synchronous circuit

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
Boolean correctness is insufficient to establish whether a circuit can run at a given clock frequency. Reliable synchronous design requires both longest-path setup and shortest-path hold timing constraints.

## Derivation and sign convention
Let positive capture skew \(s\) mean the capture clock arrives later than the launch clock. For a register-to-register path,

\[T+s\ge t_{CQ,max}+t_{PD,logic}+t_{setup},\]

\[t_{CQ,min}+t_{CD,logic}\ge t_{hold}+s.\]

Here \(t_{PD}\) is the latest propagation delay and \(t_{CD}\) the earliest contamination delay. The setup margin equals \(T+s-t_{CQ,max}-t_{PD}-t_{setup}\); the hold margin equals \(t_{CQ,min}+t_{CD}-t_{hold}-s\). Both must be nonnegative within uncertainty budgets.

## Worked investigation
For period 10 units, \(t_{CQ,min}=1\), \(t_{CQ,max}=2\), \(t_{CD}=2\), \(t_{PD}=3\), setup=1, hold=2, skew=0: setup margin=4, hold margin=1. A +2 capture skew improves setup margin to 6 but changes hold margin to -1: the path fails hold, despite the longer time available to setup.

## Failure modes and scope
Slowing the clock can repair setup but cannot repair a hold violation; modifying minimum path delay or skew is required. The example ignores supply/temperature/process variation, jitter, clock-tree uncertainty, clock-domain crossings, asynchronously asserted reset, real layout extraction and analog metastability. Source reference: MIT 6.004 computation structures official course materials, navigational citation only.

## Reconstruction exercise
Compute both margins for every path, seek the tightest setup and hold constraints, and test positive/negative skew. Explicitly refuse inconsistent delay bounds (earliest greater than latest). Do not infer a safe maximum frequency from a single illustrative path.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `register_path_timing`.
- **Equation/invariant:** `T+skew >= tCQmax+tPD+tsetup; tCQmin+tCD >= thold+skew`.
- **Units:** seconds; GHz=1/seconds.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.
