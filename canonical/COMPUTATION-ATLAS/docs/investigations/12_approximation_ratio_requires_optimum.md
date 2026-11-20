# Investigation 12 — A feasible solution does not establish an approximation ratio

**Origin:** original optimization scenario. An algorithm returns a feasible network design costing 15 units. A developer describes it as a 1.5-approximation, but the optimal cost is unknown. Feasibility alone cannot verify the multiplicative factor. For a minimization problem, a ρ-approximation means ALG(I)≤ρ·OPT(I) on every instance in the declared class, with ρ≥1. A proven lower bound L≤OPT gives ALG/L as a computable *upper bound* on the instance ratio, if L>0.

**Counterexample:** without L or a proof of OPT, any flattering claim about ratio is unsupported. A finite brute-force optimum on a small instance can check a particular input, but not a universal performance guarantee. Mathematical proof and input-domain restrictions remain required.

**Source scope:** MIT 6.046J approximation-algorithm lectures; no original primary file in the archive.
