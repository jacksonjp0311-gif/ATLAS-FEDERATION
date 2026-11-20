# Investigation 27 — The shortest path is invisible to an overconfident heuristic

**Origin:** authored nonnegative directed graph, not an execution plan for an outside tool. Vertices S, A, B, G have edges `S→A=1`, `A→G=1`, `S→B=1`, `B→G=4`. The true shortest path costs 2 through A. Assign heuristic `h(A)=100`, `h(B)=0`, `h(G)=0`. A goal-first A* candidate can stop via B with cost 5 because the inflated heuristic postpones A. A separate Dijkstra witness finds cost 2. The reference tool reports `candidate_matches_witness=false` and `heuristic_admissible_for_complete_graph=false`.

The experiment falsifies the incorrect claim that “running A* always produces an optimal path.” The guarantee depends on admissibility, implementation details, and the supplied graph's fidelity to the actual environment. In agent workflows, a suggested plan can also omit expensive external side effects; a mathematically minimal graph path can therefore be operationally invalid.

**Reproduce:** `python -m agent_atlas v1-casebook`. The zero-heuristic variant matches Dijkstra. **Research next:** collect real task and tool costs, distinguish latency from provider cost and allow the parent to recompute a plan after verified state changes. Chapter 42 supplies the source boundary (Hart–Nilsson–Raphael 1968).
