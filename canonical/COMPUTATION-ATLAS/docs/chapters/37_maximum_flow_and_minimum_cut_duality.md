# Chapter 37 — Maximum flow and minimum cut duality

**Area:** Optimization. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

In a directed network, each edge has a nonnegative capacity. A feasible flow respects capacity constraints and flow conservation at intermediate vertices. The objective maximizes net flow from source to sink. A cut partitions vertices into a source side and sink side; its capacity is the sum of forward capacities crossing the cut. The max-flow min-cut theorem equates the optimum flow value with the minimum cut capacity. This provides a powerful independent certificate: one feasible flow and one matching cut prove optimality for the declared network.

## Mathematical contract

For all e: 0≤f_e≤c_e; for v≠s,t, inflow(v)=outflow(v). For every feasible flow and s-t cut C, |f|≤capacity(C). At optimum, max |f|=min capacity(C).

## Derivation and reasoning

An augmenting-path algorithm builds a residual graph representing additional permissible changes, including reversal of prior choices. If no residual path connects s to t, the vertices reachable from s define a cut. Every forward edge crossing that cut is saturated while reverse residual behavior accounts for cancellations, so its capacity equals the current flow. The upper-bound inequality and matching witness establish optimality.

## Worked reconstruction and independent check

Use edges (0,1,3), (0,2,2), (1,2,1), (1,3,2), (2,3,4). Maximum flow equals 5. Our bounded Edmonds–Karp implementation reports flow, cut capacity, source side, and augmentation count; independent NetworkX tests compare many small networks.

## Limitations, falsification, and invalid use

The implementation aggregates parallel arcs and uses floating-point residual capacities. Extreme tiny capacities and numerical cancellation warrant exact-rational or verified tolerance implementations. A flow calculation cannot establish real data-center throughput or internet reliability from unmeasured capacities.

## Cross-domain meaning

Network throughput and agent task quotas can use a flow abstraction, but the actual resource and queue semantics must first be measured and identified.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT 6.006 Introduction to Algorithms, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
