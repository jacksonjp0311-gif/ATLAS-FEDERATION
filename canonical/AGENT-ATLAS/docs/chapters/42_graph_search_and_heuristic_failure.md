# 42. Graph search and the danger of a confident heuristic

A software agent often has a finite set of subtasks or a map of possible actions. Graph search can compute a low-cost sequence if the graph correctly represents real actions and their costs. A graph-theoretic plan is not automatically an executable world plan: tools can fail, environments can change, and some actions have side effects not reflected in edge weights. Search completeness and optimality are mathematical properties *under stated graph assumptions*, not universal guarantees.

## Dijkstra and A*

Let `G=(V,E)` have directed edges with nonnegative costs `c(u,v)`. A path cost is the sum of its edge weights. Dijkstra's algorithm explores by accumulated cost `g`. The A* family uses a priority `f(n)=g(n)+h(n)` where `h` estimates the remaining goal cost. If `h` is **admissible** (never above true remaining cost) and the algorithm handles reopened nodes correctly, optimal path guarantees follow under suitable search conditions. A consistent heuristic is a stronger condition that can simplify implementations. A language-model-generated heuristic should not be declared admissible merely because it sounds plausible.

Hart, Nilsson and Raphael (1968) formalized heuristic graph-search optimality. This edition's `shortest_path_reference` calculates both a Dijkstra witness and an A* candidate for a bounded supplied graph, and reports whether candidate and witness costs match. It refuses negative edge costs or unknown nodes. It can test heuristic admissibility relative to the completely specified finite graph; it does not know the real environment's hidden actions or costs.

## Adversarial example

Construct an entirely synthetic graph. `S→A` costs 1, `A→G` costs 1; `S→B` costs 1, `B→G` costs 4. The true shortest path through A costs 2. Supply the misleading heuristic `h(A)=100`, `h(B)=0`, `h(G)=0`. A* can pop `G` via B with candidate cost 5 while the Dijkstra witness is 2. The code marks this candidate **suboptimal**, rather than silently reporting an optimal plan. A claim that “search was used” would conceal this failure without an admissibility check or independent witness.

## From plans to workflows

An agent task graph is usually a DAG of prerequisites, not merely a path. A child cannot be admitted until its dependencies are independently completed; a worker output with the right name is not a valid dependency receipt if it belongs to a foreign goal revision. The orchestrator should track both causal ordering and independent ownership, budget and permission. A finished path does not imply a completed workflow if its nodes were only planned, not executed.

Heuristic guidance can be useful to prioritize which domain sources to research or which repair to try next. But a heuristic rank is not source reliability or scientific confidence. A more sophisticated search may use more CPU without improving answer correctness. Evaluations must compare latency, effort and verified outcomes on the same tasks and environment.

**Source:** Hart, Nilsson and Raphael, *A Formal Basis for the Heuristic Determination of Minimum Cost Paths*, IEEE Trans. Systems Science and Cybernetics 4(2), 100–107, 1968, DOI 10.1109/TSSC.1968.300136 (publisher abstract inspected). The worked counterexample is original.
