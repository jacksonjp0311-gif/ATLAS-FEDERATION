# Chapter 28: Combinational timing from acyclic gate networks

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Reconstructible directed acyclic graph
A combinational circuit is represented as a directed graph whose leaf pins have arrival intervals and whose gates have bounded contamination/minimum and propagation/maximum delays. Each node is evaluated after all its predecessors. Reject disconnected pins, duplicate drivers, negative bounds and directed cycles. The independent oracle enumerates all input–output paths on small acyclic graphs, instead of repeating the topological dynamic-programming algorithm.

The min/max recurrence gives a **conservative envelope** of possible arrival times, not a functional sensitization proof: Boolean conditions may prevent some structural paths from switching. It also omits interconnect parasitics, transition-dependent timing, glitch energy, correlated process corners, and reconvergent path complexity.

## Worked investigation
Two primary inputs have arrivals A=[0,1] ns and B=[0,2] ns. Gate G1(A) delay [1,1] ns, G2(B) delay [2,4] ns, G3(G1,G2) delay [1,2] ns. The output earliest is 2 ns (A→G1→G3), and latest is 8 ns (B→G2→G3). The reported longest structural path is B–G2–G3. A negative delay or a feedback loop is not made magically schedulable by the reference implementation.

## Build and measurement handoff
A physical timing library would supply characterized delays indexed by voltage, input slew, output load and process corner. Future Manufacturing must preserve layer stacks and parasitics, while Computer Architecture must connect the path to register-to-register timing. This chapter does not claim to contain a transistor-extracted design or signoff-grade static timing analysis.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `logic_dag_arrival`.
- **Governing relation:** `t_earliest(out)=min_i t_earliest(in_i)+d_min; t_latest(out)=max_i t_latest(in_i)+d_max`.
- **Units:** seconds.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
