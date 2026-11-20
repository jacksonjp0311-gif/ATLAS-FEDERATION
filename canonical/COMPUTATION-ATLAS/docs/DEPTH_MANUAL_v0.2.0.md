# Computation Atlas — Scientific Reconstruction Manual v0.2.0

James Paul Jackson research program · 14 November 2026 · Atlas Common Contract 1.0

**Survival standard:** explanations, mathematical assumptions, original examples, counterexamples, source references and rights boundaries should remain readable with only a UTF-8 text viewer. Numerical code is a supplemental check, not a substitute for proof or experiment.

**Scope and truth:** 50 original teaching chapters and two generations of deterministic examples. Primary source articles remain link-only. No live model, physical experiment, independent peer review, production cryptographic deployment, or Bitwork router was run.

## Reading order

- 01_computation_is_a_rule_governed_transformation.md

- 02_counter_machines_and_explicit_instruction_semantics.md

- 03_the_church_turing_thesis_and_its_limits.md

- 04_the_halting_problem_and_undecidable_specifications.md

- 05_asymptotic_complexity_concrete_cost_and_evidence.md

- 06_recurrences_and_divide_and_conquer_algorithms.md

- 07_machine_models_ram_cache_memory_traffic_and_energy.md

- 08_binary_search_and_the_invariant_of_an_ordered_interval.md

- 09_stable_sorting_and_comparison_lower_bounds.md

- 10_heaps_priority_queues_and_ordering_versus_identity.md

- 11_hashing_collision_resolution_and_adversarial_keys.md

- 12_graph_representations_and_traversal_semantics.md

- 13_dijkstra_s_algorithm_and_shortest_path_certificates.md

- 14_negative_edges_bellman_ford_and_cycle_detection.md

- 15_directed_acyclic_graphs_and_valid_dependency_order.md

- 16_dynamic_programming_as_state_decomposition.md

- 17_0_1_knapsack_and_pseudopolynomial_behavior.md

- 18_edit_distance_and_sequence_alignment_conventions.md

- 19_euclidean_algorithm_modular_arithmetic_and_proof_witnesses.md

- 20_exact_rational_computation_and_representations.md

- 21_binary_floating_point_and_catastrophic_cancellation.md

- 22_conditioning_stability_and_error_budgets.md

- 23_bisection_and_proof_of_root_existence.md

- 24_interval_arithmetic_and_uncertainty_containment.md

- 25_finite_state_reachability_and_bounded_model_checking.md

- 26_inductive_invariants_and_loop_correctness.md

- 27_termination_rankings_and_bounded_progress.md

- 28_shannon_entropy_information_and_physical_uncertainty.md

- 29_prefix_codes_kraft_inequality_and_recoverable_archives.md

- 30_parallelism_amdahl_s_law_and_synchronization_cost.md

- 31_sampling_variability_and_bernoulli_evaluation_intervals.md

- 32_algorithm_evaluation_correctness_efficiency_and_generalization.md

- 33_preservation_grade_software_and_scientific_reconstruction.md

- 34_domain_boundaries_and_future_cross_disciplinary_reuse.md

- 35_disjoint_set_union_and_equivalence_classes.md

- 36_minimum_spanning_forests_and_kruskal_s_algorithm.md

- 37_maximum_flow_and_minimum_cut_duality.md

- 38_discrete_fourier_transform_and_radix_two_fft.md

- 39_convolution_spectral_multiplication_and_aliasing.md

- 40_exact_linear_equations_rank_and_pivoting.md

- 41_numerical_conditioning_and_iterative_linear_solvers.md

- 42_randomized_algorithms_las_vegas_and_monte_carlo.md

- 43_concentration_bounds_and_statistical_identification.md

- 44_complexity_classes_p_np_and_careful_reductions.md

- 45_approximation_algorithms_and_objective_guarantees.md

- 46_vector_clocks_causality_and_concurrency.md

- 47_transactions_durability_and_exactly_once_effect_limits.md

- 48_canonical_serialization_text_encoding_and_preservation.md

- 49_cryptographic_assumptions_and_post_quantum_agility.md

- 50_type_systems_specifications_and_proof_carrying_software.md


---


# Chapter 01 — Computation is a rule-governed transformation

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A computation is a sequence of state transformations carried out according to an effective, finite description of rules. Separating the program, the state, and the environment clarifies what an algorithm actually promises. A finite machine may possess unbounded mathematical storage in its model, while any physical computer has finite memory, finite energy, and a failure-prone clock. The input specification determines what is represented: bit strings, integers, rational numbers, measured reals, or structured graphs. The output specification determines what counts as a result, including error, refusal, and nontermination. A program executable on a laptop is not thereby a proof of the function it computes; its semantics, preconditions, and adversarial cases must be examined. The same observed output may arise from different internal programs. A constructive representation requires state, instruction syntax, transition rules, and a stopping condition. The Computation Atlas treats all those elements as evidence fields, not optional implementation details.

## Formal statement, symbols, and units

Transition: s_(t+1)=delta(s_t,i_t). Partial function: f:X ⇀ Y. A total algorithm returns an output for every input in its declared domain.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A deterministic interpreter supplies a transition relation and can reproduce a finite trace. To infer a universal property from a finite trace is a quantifier error: “these cases stopped” does not entail “all cases stop”. An encoding must be injective if exact reconstruction is expected; otherwise two distinct states might share a representation. Machine specifications also expose the resource model: what constitutes one step, one memory cell, and one cost unit? Different models can preserve computability but change practical performance.

## Reconstruction exercise with independently checkable output

Write a three-state deterministic machine, list each state and outgoing transition, then execute the initial state by hand. Confirm that the interpreter follows the same steps. Change the input encoding while preserving the decoded meaning and check whether the output remains invariant.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not confuse successful execution, decidability, feasibility, correctness, and performance. A program can halt and return the wrong answer. A correct algorithm can require impractical time. Two finite observations cannot decide a universal termination property.

## Source orientation

- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 02 — Counter machines and explicit instruction semantics

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A two-counter machine is a small universal-style model using two nonnegative integer registers and three instruction forms: increment with branch, decrement-if-positive with branch, and halt. A formal instruction grammar makes its behavior analyzable without a general-purpose programming language. Each step is deterministic when the program counter is valid. A bounded interpreter can execute a finite prefix of any run, record the registers and program counter, and distinguish normal halting from a step-budget cutoff. This distinction prevents a simulation from presenting an undecidable judgment as an experimental finding. The mathematical model allows unbounded counters; the reference implementation uses finite machine memory, so actual runtime and overflow limitations remain separate.

## Formal statement, symbols, and units

Program P = (I_0,…,I_(m-1)); configuration C=(pc,r0,r1). Step relation C→C′. A run is C_0→C_1→… until HALT or external budget exhaustion.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

An induction on step count establishes that register values remain nonnegative, provided the initial counters are nonnegative and decrement only occurs when the selected register is positive. It does not establish that the run halts. A loop that continually increments counter zero is a valid finite program whose observed finite prefixes never halt. A budget of B steps certifies only those B steps. The words “unknown” and “non-halting” carry materially different epistemic meanings.

## Reconstruction exercise with independently checkable output

Use computation_atlas.models.counter_machine to run a halt program, a decrement program, and an increment loop. Record all outputs with program bytes and step budget. Repeat with increasing budgets; do not mislabel the persistent loop as universally non-halting solely from experiments.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The interpreter is deliberately not a secure virtual machine for arbitrary untrusted code; it accepts a tiny instruction language. Any universality statement requires the formal unbounded-counter model, not this finite Python execution.

## Source orientation

- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 03 — The Church–Turing thesis and its limits

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The Church–Turing thesis relates an informal idea—an effective procedure—to formal mathematical computability. Several formal systems, including Turing machines and lambda calculus, identify the same class of computable functions. Their equivalence is a mathematical result; the interpretation of every intuitively effective process is a thesis rather than an ordinary theorem about a previously formalized concept. This thesis is not the claim that every physical event can be efficiently simulated on today's computers, nor that all imaginable physical processes obey a particular digital implementation. Conflating computability with speed, parallelism, or physical determinism produces misleading forecasts. A human reconstructing the field needs three separate questions: can a function be computed in principle; what resources does it require; and can a particular physical system realize it?

## Formal statement, symbols, and units

Computable(f) means there exists a finite effective program P such that, for every x in dom(f), P(x) returns f(x) in finitely many steps. Cost(P,x) is a separate function.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

There are countably many finite programs but uncountably many mathematical functions from natural numbers to bits. Thus some such functions have no finite program representation. That counting argument is not an explicit method for identifying a specific uncomputable function; diagonal constructions provide one. The equivalence of formalisms does not erase assumptions about encodings, memory, or effectivity. A finite register machine's physical execution is bounded even if its mathematical semantics admit unbounded storage.

## Reconstruction exercise with independently checkable output

Write definitions of effective computation and polynomial-time computation in separate boxes. Construct a diagonal countability argument for binary functions, then compare it with the explicit self-reference proof in the next chapter.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Reject claims that a large GPU, quantum hardware, neural model, or novel encoding automatically escapes undecidability. New architectures can change resource requirements without deciding every arbitrary program's halting behavior.

## Source orientation

- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 04 — The halting problem and undecidable specifications

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The halting problem asks for an algorithm that correctly determines for every program and input whether execution eventually stops. A diagonal proof shows no such total algorithm exists under a universal computation model. This is not a warning that no practical termination checker can ever help. Static analyzers may prove termination for important restricted programs; runtime budgets may stop runaway execution; proof assistants may verify a supplied well-founded ranking function. What fails is a universal complete decision procedure for arbitrary programs. This distinction guides how to describe software test outcomes and AI agent recovery: “not shown to terminate”, “terminated under bound B”, “proved terminating for a restricted model”, and “observed not to finish” are different evidence states.

## Formal statement, symbols, and units

Assume H(P,x) decides halting. Define D(P): if H(P,P) says halt then loop, else halt. Evaluate D(D) to obtain a contradiction.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The proof uses self-reference: if H predicts that D halts on its own description, D is defined to loop; if H predicts a loop, D halts. This contradicts H's assumed correctness. Note what the proof does not say: that every individual termination property is unprovable, or that real bounded systems cannot be exhaustively searched. For a finite transition system with a finite complete state enumeration, reachable loops can be checked. The class of arbitrary programs is strictly larger than the finite models under inspection.

## Reconstruction exercise with independently checkable output

Document a restricted finite loop with states {0,1,2}, exhaust reachable transitions, then compare the finite proof with a budgeted counter-machine run. Use the tool output “unknown_budget_exhausted” when the budget is insufficient.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Never describe a timeout as proof of undecidability or nontermination. The finite-state model checker in this archive establishes properties only inside a supplied complete model, not arbitrary Python programs.

## Source orientation

- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/
- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 05 — Asymptotic complexity, concrete cost, and evidence

**Domain:** Complexity. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Algorithm analysis distinguishes input-size growth from empirical wall-clock measurements. Worst-case, average-case, amortized, and smoothed complexity answer different questions. O(g(n)) is an eventual asymptotic upper bound, not a claim that every run takes g(n) seconds. Omega and Theta express lower and tight asymptotic bounds. Constants and cache effects matter enormously for realistic inputs; the asymptotic notation intentionally abstracts some of them away. A faithful report states the computational model, the variable n, input distribution assumptions, and memory accounting. Counting comparisons is not the same as counting CPU cycles, energy, branch misses, or external I/O. A finite timing chart can falsify some models but cannot prove an asymptotic theorem for all n.

## Formal statement, symbols, and units

T(n) ∈ O(g(n)) iff ∃c>0,n0∀n≥n0: T(n)≤c g(n). For Θ(g), require both asymptotic upper and lower bounds.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

For a loop performing n operations, construct a step-count bound with chosen primitive costs. To show a divide-and-conquer recurrence, account separately for the branch work and merge work, not just recursion depth. Distinguish complexity of the *problem* (best algorithm known, lower bounds) from complexity of a *particular implementation*. An NP-complete problem can have fast solutions for special instances; the worst-case label does not predict a particular input's runtime.

## Reconstruction exercise with independently checkable output

Count primitive comparisons for merge sort on increasing n and compare with n log2(n). Record hardware, interpreter, implementation, and random seed for any timings. Provide both a mathematical upper-bound argument and empirical measurements without conflating them.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Beware benchmark extrapolation across architectures, claiming practical speed from Big O alone, and mislabeling pseudopolynomial algorithms as polynomial in input bit-length.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 06 — Recurrences and divide-and-conquer algorithms

**Domain:** Complexity. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Divide and conquer reduces a problem to smaller subproblems, solves them, and combines the answers. A recurrence records the cost structure. Binary search discards half the candidate interval at each step; merge sort splits the input in two and merges ordered halves. Recurrences need base cases and a definition of how n is measured. Uneven splitting, data movement, and allocation can change practical cost without overturning the high-level proof. An algorithm's return-value invariant should be stated independently of its recurrence: a quickly terminating wrong sort is not saved by having T(n)=O(n log n). For stable sorting, merge equal-key elements from the left half before the right half.

## Formal statement, symbols, and units

T_merge(n)=2T(n/2)+Θ(n) ⇒ Θ(n log n). T_binary(n)=T(⌊n/2⌋)+Θ(1) ⇒ Θ(log n).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The merge sort recurrence follows because the two halves recursively sort and merging scans each element a bounded number of times. At recursion level k, all subproblems together contain at most n elements; O(log n) levels yield O(n log n). The usual lower-bound argument for comparison sorting assumes arbitrary keys and a decision-tree model. Specialized integer sorting changes the model and may outperform comparison bounds under additional constraints.

## Reconstruction exercise with independently checkable output

Construct a merge-tree trace for eight distinct and repeated keys, listing comparisons at each level. Verify left-biased equal-key merging preserves original order. Compare recurrence predictions with measured comparisons, not machine time alone.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not apply comparison lower bounds to counting sort or assume the Master Theorem covers every recurrence without checking its regularity requirements.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 07 — Machine models: RAM, cache, memory traffic, and energy

**Domain:** Architecture. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The random-access machine model treats certain operations as unit cost. Real machines fetch memory through a hierarchy: registers, caches, main memory, storage, and sometimes remote nodes. Locality—spatial and temporal—can dominate performance. External-memory algorithms count block transfers; work–span models describe available parallelism; roofline-style models compare arithmetic throughput to memory bandwidth. No single model is universally correct. A survivor reconstructing a computational result should know whether reported complexity measures primitive operations, bits, cache misses, wall-clock time, monetary cost, or joules. The size of a bit representation matters when arbitrary-precision arithmetic is used. A constant-time step for an unbounded integer is an abstraction, not a literal hardware fact.

## Formal statement, symbols, and units

Work W = total primitive operations; span S = longest dependency chain; ideal time on p processors T_p ≥ max(W/p,S). Data movement often adds a separate constraint.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

If two algorithms have identical O(n) arithmetic work but one streams sequentially while the other randomly accesses a large table, cache-miss behavior can diverge. Use this to resist interpreting time measurements as universal computational superiority. The effective hardware model changes with accelerators and memory pressure; the logical answer may be invariant while latency and energy are not.

## Reconstruction exercise with independently checkable output

Compare sequential and strided memory traversal in an explicitly described environment. Repeat multiple times, record temperature and load, and treat observations as local performance results. Work out a simple work–span DAG by hand without measuring hardware.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

No physical energy-efficiency claim can be inferred from count of Python-level operations alone. Bitwork-style geometric representations later require hardware and workload-level evidence rather than rhetorical savings.

## Source orientation

- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 08 — Binary search and the invariant of an ordered interval

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Binary search locates a target in a sorted sequence or identifies an insertion boundary. The sortedness assumption is essential; on unsorted input the same code may return a plausible but wrong answer without warning. A lower-bound implementation maintains a half-open candidate interval [lo,hi) whose elements could still contain the first key >= target. At each step, the midpoint splits the candidate interval into two pieces. Because one piece is discarded, the interval size decreases and termination follows from a nonnegative integer rank function. Duplicate keys expose the difference between “an occurrence” and “the first occurrence”. An empty array is a valid case when returning an insertion index.

## Formal statement, symbols, and units

Invariant: ∀i<lo, a_i<target; ∀i≥hi, a_i≥target. Variant: hi−lo decreases on each loop. At exit lo=hi is the insertion point.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Initially lo=0 and hi=n, so both quantified statements are vacuously true. If a_mid<target, all entries before and including mid are below target by sortedness, so lo becomes mid+1. Otherwise all entries from mid onward are at least target, so hi becomes mid. Each update preserves both conditions and decreases the interval length. The combination of induction and rank decrease proves correctness and termination for sorted finite arrays.

## Reconstruction exercise with independently checkable output

Run computation_atlas.models.lower_bound on [1,1,2,2,4] for 0,1,2,3,5. At every iteration, write the two invariant partitions. Then violate sortedness and observe that the guarantee no longer applies.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Never treat a few passing lookup tests as proof that a caller supplied sorted data. Sortedness can be checked in O(n) or maintained by a trusted upstream process; that cost belongs in the system specification.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 09 — Stable sorting and comparison lower bounds

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A sorting algorithm returns values ordered by a declared key. Correctness has two parts: the output is ordered and it contains exactly the input multiset. Stability adds a third: items with equal keys preserve original relative order. Merge sort meets these properties with an O(n log n) comparison bound under appropriate ordering assumptions. Sorting algorithms differ across in-place memory use, worst-case bounds, adaptivity, and key domains. A finite certificate can check that one output is sorted and a permutation of one input; it cannot prove that the implementation behaves correctly for every future input. A custom key that violates transitivity invalidates many algorithmic proofs.

## Formal statement, symbols, and units

Permutation: multiset(output)=multiset(input). Order: ∀i<n−1, key(out_i)≤key(out_(i+1)). Stability: equal-key original indices remain in increasing order.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Merge sort's stability follows inductively if each recursively sorted half is stable and ties at merge choose the left element first. The logarithmic-depth recursion and linear merges give O(n log n). Comparison sorting must distinguish n! permutations; a binary decision tree requires height Ω(log2(n!))=Ω(n log n). Integer keys in a constrained range allow counting sort and invalidate the decision-tree premise.

## Reconstruction exercise with independently checkable output

Create tagged duplicate keys and trace the merge at each level. Check multiset preservation independently using a frequency map; verify that the order of equal-tag groups is maintained.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The certificate implemented here relies on hashable elements and Python comparison semantics. Data corruption, inconsistent comparators, locale-dependent rules, or missing input items may escape a mere sortedness check.

## Source orientation

- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 10 — Heaps, priority queues, and ordering versus identity

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A binary heap is an array-based complete binary tree with local parent-child ordering. Insert and delete-min run in O(log n) in the worst case; peeking at the minimum is O(1). A heap is not a sorted array, and iterating its internal storage does not produce sorted output. A priority queue supports best-first algorithms such as Dijkstra when keys are valid. Implementations without decrease-key commonly add duplicate entries and discard stale ones when popped; correctness depends on comparing the popped priority against the current best known value. Tie-breaking must be deterministic when reproducibility matters. A task scheduler also needs fairness and liveness criteria; heap order alone does not ensure that every lower-priority task eventually executes.

## Formal statement, symbols, and units

Heap invariant: parent(i)≤child(i), with parent(i)=⌊(i−1)/2⌋. Heap operations modify O(log n) ancestor/descendant levels.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A heap's local invariant implies the root is globally minimal by transitivity along parent chains. Insert restores the property by bubbling upward; delete-min replaces the root and pushes down. A stale heap entry is safe to ignore if a more recent smaller distance is already recorded. Stable tie-breaking in a scheduler requires an explicit sequence counter, not incidental memory addresses.

## Reconstruction exercise with independently checkable output

Represent the heap [1,3,2,7,5,4] as a binary tree, verify each parent-child inequality, then insert 0 and trace swaps. Compare with the priority queue used by the shortest-path reference.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not infer starvation freedom from a valid heap invariant. Priority queues model ordering, not policy fairness, progress, or correct authority boundaries for dispatched work.

## Source orientation

- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 11 — Hashing, collision resolution, and adversarial keys

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A hash table maps keys to buckets using a hash function and capacity. Expected O(1) operations depend on assumptions about hash distribution, load factor, and adversarial inputs. Collisions are unavoidable when the key universe exceeds the bucket count; collision handling is part of correctness, not an optional optimization. Separate chaining stores multiple keys per bucket, while open addressing probes alternative slots. A hash digest used for data integrity has different security properties from the hash function used for table indexing. Cryptographic hash collision resistance does not authenticate the party who created a file or guarantee that a scientific claim is true. Hashable-key equality and hashing must be consistent for dictionary invariants to hold.

## Formal statement, symbols, and units

Load factor α=n/m for n keys and m buckets. Index h(k) mod m. Pigeonhole principle: if n>m then at least one collision exists.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

In a chaining table, lookup examines the indexed bucket and must compare full keys because different keys may hash alike. Rehashing at a threshold can yield amortized insertion bounds even though an individual resize costs O(n). Under adversarial collision patterns, many operations can degrade to linear time. Comparing the expected-case claim against worst-case input shows why the model's distribution assumption matters.

## Reconstruction exercise with independently checkable output

Construct a toy table of five buckets, insert keys 1,6,11 and inspect their shared bucket. Search for each key and a missing colliding key. Repeat the design with open addressing to analyze deletion semantics.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not mistake SHA-256 for an identity signature, conflate record revision hashes with experimental validation, or use a non-cryptographic checksum as a security proof.

## Source orientation

- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- NIST FIPS 180-4 Secure Hash Standard: https://csrc.nist.gov/pubs/fips/180-4/upd1/final

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 12 — Graph representations and traversal semantics

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A graph consists of vertices and edges; a directed graph distinguishes ordered pairs. Adjacency lists use space proportional to vertices and edges, while adjacency matrices use quadratic space in the vertex count. Breadth-first search explores unweighted graphs in increasing number of edges from the source. Depth-first search follows branches and supports component analysis, topological ordering, and cycle detection. Edge direction, multigraph conventions, self-loops, and duplicate edges must be declared. An unreachable vertex is a mathematical result only relative to the given graph snapshot. In a distributed system whose graph changes during analysis, that snapshot may already be stale. The representation matters because a missing vertex key in an adjacency dictionary can silently remove edges if the implementation does not validate the whole node set.

## Formal statement, symbols, and units

Adjacency-list traversal work O(|V|+|E|), provided each node and edge is processed O(1) times. Unweighted distance dist(v)=number of edges on shortest source–v path.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

BFS maintains a FIFO frontier. All vertices at distance k are dequeued before those first discovered at distance k+1. Induction on layer k establishes that the first assigned distance is minimal. DFS uses a stack and does not generally discover minimum-length routes. Strongly connected components require checking reachability in both directions; treating a directed edge as undirected changes the problem.

## Reconstruction exercise with independently checkable output

Represent the same four-node graph as an adjacency list and matrix, enumerate edges, then execute BFS by hand and compare the cost of checking a missing edge in each representation.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

A path found by DFS is not generally the shortest path. Declaring a graph with omitted vertices, mixed edge directions, or inconsistent weights invalidates downstream guarantees.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 13 — Dijkstra’s algorithm and shortest-path certificates

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

For a graph with nonnegative edge weights, Dijkstra's algorithm maintains tentative distances from a source and extracts the smallest next distance. Once a vertex is extracted with the current minimum, nonnegative edges guarantee that no undiscovered alternative can improve its distance. A practical heap implementation may contain stale entries, discarded when their priority exceeds the current recorded value. Predecessor links provide a path witness, but a path witness alone proves only an upper bound on distance. A stronger certificate combines valid predecessor chains with inequalities across every edge. That is valuable for independent checking: a producer may be buggy, while a simple verifier can still reject an invalid distance table.

## Formal statement, symbols, and units

Relaxation: d(v)←min(d(v),d(u)+w(u,v)). Certificate: d(s)=0; each finite v has an s→v predecessor chain matching d(v), and ∀(u,v), d(v)≤d(u)+w(u,v).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Every actual s→v path supplies an upper bound on the true shortest distance. Edge inequalities imply that the proposed d(v) is no greater than any path length when telescoped along edges. A predecessor chain of equalities shows the proposed d(v) is achieved by a concrete path. Together they establish equality. For vertices claimed unreachable, closedness of the reachable set under outgoing edges must be satisfied. Negative edges invalidate Dijkstra's greedy-choice proof even when no negative cycle exists.

## Reconstruction exercise with independently checkable output

Run the four-vertex example in the casebook, record heap contents after each extraction, then deliberately alter a distance or predecessor. Confirm the independent shortest_path_certificate rejects it.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The reference verifier uses a floating tolerance: near-ties and extreme magnitudes may require exact rational arithmetic. It is not a cryptographic receipt proving how a worker obtained the answer.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- SciPy reference, sparse graph shortest paths: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 14 — Negative edges, Bellman–Ford, and cycle detection

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Negative edge weights arise in transformed optimization problems, potential-based graph methods, and some economic or energy accounting models. Negative edges are not by themselves a failure, but they break the greedy logic of Dijkstra. Bellman–Ford repeatedly relaxes all edges and, after |V|−1 passes, finds finite shortest paths if no negative cycle reachable from the source exists. A further successful relaxation indicates a reachable negative cycle, making shortest-path cost unbounded below for vertices reachable from that cycle. Unreachable negative cycles do not invalidate distances from a source that cannot reach them. Status codes must therefore distinguish finite distances, unreachable vertices, and reachable negative cycles.

## Formal statement, symbols, and units

After k complete passes, d(v) is no greater than the minimum path length using at most k edges. A simple finite shortest path has ≤|V|−1 edges.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

If a finite minimum path contained a repeated vertex, the repeated segment would form a cycle. Removing any nonnegative cycle cannot make it worse, so a simple path of at most |V|−1 edges exists when no relevant negative cycle spoils the optimum. This supports the pass count. If relaxation remains possible after that, the path can continue to improve via a negative cycle. The proof is relative to a static graph, exact weights, and reachable subgraph.

## Reconstruction exercise with independently checkable output

Construct a source connected to a two-node negative cycle; record distances after each pass and reject a finite shortest-path claim. Move that cycle to a disconnected component and verify finite source distances remain valid.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not infer a negative cycle merely because a numerical optimization failed to converge. Floating-point comparisons and malformed graphs require separate diagnosis.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 15 — Directed acyclic graphs and valid dependency order

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A directed acyclic graph (DAG) admits a topological order: every directed edge points from an earlier to a later vertex. This structure supports build systems, dataflow computation, scheduling, and dynamic programming. Kahn's algorithm tracks indegrees, repeatedly removes a zero-indegree vertex, and detects a cycle when unprocessed vertices remain. Cycles are not necessarily errors in all dynamical systems, but they invalidate an acyclic dependency interpretation unless some feedback or iterative semantics is explicitly supplied. A dependency graph also needs a completion contract. Receiving a worker result is not necessarily satisfying the prerequisite if the result has not been validated, admitted, or published.

## Formal statement, symbols, and units

Topological order π satisfies π(u)<π(v) for each edge u→v. A finite directed graph admits π iff it has no directed cycle.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

In a finite DAG there exists at least one vertex of indegree zero: otherwise following predecessor edges indefinitely repeats a vertex, creating a directed cycle. Remove a source, apply induction to the remaining DAG, and prepend it. Conversely, a directed cycle would require π(v1)<π(v2)<…<π(v1), an impossibility. The proof gives existence; a queue or heap chooses one among many valid orders.

## Reconstruction exercise with independently checkable output

Topologically sort a six-task graph and record every zero-indegree candidate at each step. Introduce a single back edge and confirm the algorithm refuses a topological order. Specify whether edges mean “must finish” or “must be independently verified”.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

One valid order does not prove optimal makespan or fair execution. The graph is a model of declared dependencies, not a complete worker-runtime guarantee.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 16 — Dynamic programming as state decomposition

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Dynamic programming solves problems with overlapping subproblems and a valid optimal-substructure relation. The designer selects a state representation and recurrence, defines base cases, and decides whether to memoize recursively or fill a table iteratively. The dominant danger is a wrong state: a short table cannot represent a hidden dependency that the recurrence actually needs. A state must contain all information relevant to future decisions. Dynamic programming is not an optimization oracle and does not make hard problems polynomial in input *bit length*. Storage can sometimes be compressed when only previous rows are required, but recovering an optimal action sequence may require parent pointers or recomputation.

## Formal statement, symbols, and units

Bellman principle: V(s)=opt_a {r(s,a)+V(T(s,a))} under a declared acyclic/finite-horizon dependency relation. State and transition design determine correctness.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Prove a recurrence by dividing optimal solutions according to a final or first decision. If every feasible solution falls in exactly one case and the recurrence considers all cases without allowing invalid combinations, induction on state order establishes optimality. For a tabulated 0/1 knapsack, the final item is either excluded or included, which motivates two alternatives. For some domains, decisions are history-dependent unless that history is encoded in the state.

## Reconstruction exercise with independently checkable output

Write a three-item knapsack table with capacities zero through five, trace the include/exclude transition, and reconstruct selected item indices. Explain why the value table alone cannot be applied to a divisible-item problem without changing the recurrence.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Beware hidden state, circular recurrences without a convergence theorem, accidental use of an item more than once, and declaring O(nW) polynomial in the input length when W is encoded in binary.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 17 — 0/1 knapsack and pseudopolynomial behavior

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The 0/1 knapsack problem selects whole items to maximize value under a weight capacity. Its standard dynamic programming algorithm uses capacity as an array index, which is viable only for bounded nonnegative integer weights. An item is selected at most once. A fractional variant would require a different formulation, and a negative weight invalidates the usual recurrence. The table can be exact for a finite input but enormous when capacity is a large binary integer. This is an explicit example of pseudopolynomial complexity. An engineering-grade algorithm must enforce memory and work caps before allocating a table, and return a refusal rather than exhausting the host.

## Formal statement, symbols, and units

D(i,c)=max[D(i−1,c), v_i + D(i−1,c−w_i)] if w_i≤c; otherwise D(i,c)=D(i−1,c). Base D(0,c)=0.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The recurrence follows by partitioning feasible solutions according to inclusion of item i. If the item is included, the remaining capacity is c−w_i and prior items are the only choices; if excluded, the prior problem is unchanged. Induction on i proves the table value equals optimum for the declared finite instance. Reconstructing choices by comparing successive rows gives a witness. A separate exhaustive subset enumerator provides an independent oracle for small n.

## Reconstruction exercise with independently checkable output

For item weights [2,3,4], values [3,4,5], capacity 5, enumerate all eight subsets and verify optimum 7 using items 0 and 1. Increase capacity to a very large binary value while keeping item count small and analyze memory blowup.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

A runtime cap is a host resource policy, not a proof the optimization problem is intractable. Approximation schemes and branch-and-bound should be studied separately in later editions.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 18 — Edit distance and sequence alignment conventions

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Levenshtein edit distance counts the minimum number of unit-cost insertions, deletions, and substitutions needed to transform one sequence into another. The recurrence compares the final characters and chooses the cheapest operation. It supports spelling correction, string matching, and a simplified view of biological sequence alignment. Real bioinformatics often uses weighted substitution matrices, affine gap penalties, and quality scores; the unit-cost educational model cannot replace those domain-specific algorithms. An implementation may store only two dynamic-programming rows for linear auxiliary space, but a full alignment witness requires backtracking information.

## Formal statement, symbols, and units

D(i,j)=min[D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+1[x_i≠y_j]]. D(i,0)=i, D(0,j)=j.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Any final edit operation must be a deletion, insertion, or match/substitution, and each leads to a strictly smaller pair of prefixes. Assuming optimal values for all shorter prefixes yields the recurrence. Every path through the edit grid defines a legal edit sequence with the corresponding cost; the minimum path is therefore the edit distance. Symmetry follows because unit-cost insertion and deletion can be inverted, and substitution is symmetric. Triangle inequality follows by concatenating edit sequences.

## Reconstruction exercise with independently checkable output

Compute a table for “kitten” and “sitting”, showing the three operations. Compare the two-row implementation to a full table for strings of length 1000. State whether characters mean bytes, Unicode code points, grapheme clusters, or biological residues.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Unicode normalization, transpositions, weighted costs, and domain-specific matching change the metric. Never compare distances with different tokenization without declaring the transformation.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 19 — Euclidean algorithm, modular arithmetic, and proof witnesses

**Domain:** Mathematics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The Euclidean algorithm computes the greatest common divisor by repeatedly replacing (a,b) with (b,a mod b). The extended form also finds integers x,y such that ax+by=gcd(a,b), called Bézout coefficients. This constructive witness is useful for modular inverses, the Chinese remainder theorem, and elementary cryptography. Proof relies on the invariant that dividing a by b leaves the set of common divisors unchanged. Termination follows because the nonnegative remainder is strictly smaller than the previous divisor. Negative inputs require a sign convention, and a=b=0 conventionally returns gcd zero without a unique Bézout pair.

## Formal statement, symbols, and units

gcd(a,b)=gcd(b,a mod b). Bézout identity: ax+by=gcd(a,b). Inverse of a mod m exists iff gcd(a,m)=1.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Each quotient step satisfies a=q b + r; any common divisor of a and b divides r, and any common divisor of b and r divides a. Thus the gcd is invariant. Record each remainder as an integer linear combination of the original pair and unwind at the end to obtain x,y. An ordinary machine-int implementation could overflow intermediate coefficients; this Python reference uses arbitrary-precision integers while acknowledging physical memory limits.

## Reconstruction exercise with independently checkable output

Run extended_gcd(-54,24), verify the returned gcd is 6, and explicitly multiply the coefficients to reconstruct 6. Use the output to determine whether 12 has an inverse modulo 35 and modulo 36.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not treat integer arithmetic as constant time when numbers have millions of bits. Cryptographic constant-time behavior is a separate side-channel property, not furnished by the Euclidean result alone.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 20 — Exact rational computation and representations

**Domain:** Numerics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Computers represent rational numbers exactly using integer numerators and nonzero integer denominators, normalized by greatest common divisor. Addition and multiplication can remain mathematically exact despite intermediate growth in bit-length. This avoids binary floating-point rounding for problems such as financial ratios, rational interval bounds, and small symbolic models. It does not solve all numerical problems: arbitrary real numbers may require algebraic, interval, or approximate representations; exact rational numerators can grow exponentially in size across transformations. The input format matters: Fraction(0.1) represents the exact rational value of the already-rounded binary float, not the decimal 1/10. Fraction('0.1') expresses the intended decimal exactly.

## Formal statement, symbols, and units

a/b + c/d = (ad+bc)/bd; a/b × c/d = ac/bd; gcd(|a|,|b|)=1 after normalization.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Exactness follows from the field operations on rational numbers, assuming arbitrary-precision integer arithmetic and nonzero denominators. Equality is exact after canonical reduction. Computational cost increases as operand bit-length grows; normalization requires gcd work. An interval [a,b] with rational endpoints encloses values exactly under rational arithmetic, which creates an audit-friendly reference against floating-point implementations.

## Reconstruction exercise with independently checkable output

Compare Fraction(1,10), Fraction('0.1'), and Fraction(0.1). Add ten copies of each, observe the integer numerator/denominator representation, then build a rational interval product with negative endpoints.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not use a decimal-looking printed float as evidence that a mathematical rational was stored exactly. The cost of arbitrary-precision arithmetic must be accounted for in performance studies.

## Source orientation

- Python documentation, fractions — Rational numbers: https://docs.python.org/3/library/fractions.html
- Python documentation, Floating-Point Arithmetic: Issues and Limitations: https://docs.python.org/3/tutorial/floatingpoint.html
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 21 — Binary floating-point and catastrophic cancellation

**Domain:** Numerics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Standard binary floating-point represents a finite set of numbers. Most decimal fractions, including one tenth, have no finite binary representation and must be rounded. Arithmetic generally rounds at each operation; the order of operations can therefore affect a result. Catastrophic cancellation occurs when subtracting nearly equal approximations, potentially destroying significant digits. Large and small magnitude terms also expose accumulation error. Compensated summation algorithms such as Kahan's often reduce error, but they do not make arbitrary calculations exact. A robust scientific result reports precision, operation order, tolerances, conditioning, and whether an independent high-precision calculation was performed.

## Formal statement, symbols, and units

Floating model: fl(x op y)=(x op y)(1+δ) for suitably normal operations, |δ|≈≤u. For binary64, u≈2^−53; underflow/overflow need special handling.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The relative-error model is an approximation with exceptions, including subnormal results, overflow, and nonfinite values. For subtraction of close large numbers, the absolute rounding error may be small but relative error in the tiny difference enormous. Reordering a sum can change which low-order bits survive. The archive explicitly demonstrates a naïve left-to-right sum unlike algorithms with more sophisticated compensation in modern language runtimes.

## Reconstruction exercise with independently checkable output

Calculate 0.1+0.1+0.1 and compare to 0.3; report the exact stored fraction if available. Sum [10^16,1,1,−10^16] in naive order, then with math.fsum and arbitrary rational arithmetic.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not infer that every float operation is inaccurate or that decimal arithmetic is universally correct. Requirements may be satisfied by documented bounds and independent checks; changing representation also changes performance and semantics.

## Source orientation

- Python documentation, Floating-Point Arithmetic: Issues and Limitations: https://docs.python.org/3/tutorial/floatingpoint.html
- Python documentation, math.fsum: https://docs.python.org/3/library/math.html#math.fsum
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 22 — Conditioning, stability, and error budgets

**Domain:** Numerics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Conditioning describes how a mathematical problem's output changes when its input changes; numerical stability describes how an algorithm's computation responds to rounding and perturbations. They must not be conflated. An ill-conditioned problem can defeat even a stable algorithm if input uncertainty dominates; an unstable algorithm can squander accuracy on a well-conditioned problem. Forward error measures distance between computed and true output, while backward error asks whether the computed result solves a nearby problem. Engineering error budgets include measurement uncertainty, model approximation, discretization, floating rounding, and stopping tolerance. These components are not necessarily independent or additive without justification.

## Formal statement, symbols, and units

Condition number κ≈(relative output perturbation)/(relative input perturbation) for sufficiently small changes. Backward stability: computed y=f(x+Δx) with small Δx.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Consider subtracting x and y where x≈y: a small relative perturbation in either operand can produce a large relative perturbation in x−y. This is conditioning of the subtraction problem, not merely a defect in one code implementation. Scaling, algebraic reformulation, exact arithmetic, and interval enclosures can mitigate different causes. A reproducible analysis specifies which error notion is being bounded and which assumptions justify a bound.

## Reconstruction exercise with independently checkable output

Compare sqrt(x+1)−sqrt(x) with the algebraically equivalent 1/(sqrt(x+1)+sqrt(x)) for large x. Use high-precision rational or decimal reference and report absolute and relative errors separately.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

A tiny residual does not automatically guarantee a tiny solution error in an ill-conditioned problem. Synthetic oracle agreement under one distribution does not certify global accuracy or physical measurements.

## Source orientation

- Python documentation, Floating-Point Arithmetic: Issues and Limitations: https://docs.python.org/3/tutorial/floatingpoint.html
- SciPy reference, optimization and root finding: https://docs.scipy.org/doc/scipy/reference/optimize.html
- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 23 — Bisection and proof of root existence

**Domain:** Numerics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The bisection algorithm brackets a root of a continuous real-valued function when endpoint values have opposite signs. Each iteration evaluates the midpoint and retains a half-interval whose endpoints still straddle zero. The intermediate value theorem supplies existence, while shrinking interval length supplies a location bound. Without continuity the sign change can be caused by a jump discontinuity without any root, so the continuity assumption must be explicit. A finite implementation can test signs and width, but it cannot generally prove that an arbitrary caller-supplied function is continuous. A bracket can be more defensible than a single estimate because it communicates residual uncertainty.

## Formal statement, symbols, and units

After k ideal iterations, width(b_k−a_k)=(b_0−a_0)/2^k. Under continuity and opposite signs, ∃r∈[a_k,b_k] with f(r)=0.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The proof proceeds by induction: the initial bracket satisfies the sign condition, and because midpoint is between endpoints, one of the two halves continues to have opposite endpoint signs. Interval width halves each step, so the midpoint estimate converges to a root under the stated assumptions. Finite precision may stall midpoint movement, so production implementations must detect that case. Newton-type methods may converge faster locally but need derivative information and stronger hypotheses.

## Reconstruction exercise with independently checkable output

Bracket sqrt(2) between 1 and 2 and halve until the width is under 10^-8. Independently square the endpoints and verify they straddle 2. Then attempt a discontinuous sign function and record why the continuity requirement refuses a proof.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The reference asks callers to confirm continuity; that declaration is not independently certified. NaN evaluations, endpoint errors, and untrusted function side effects remain outside this controlled educational model.

## Source orientation

- SciPy reference, scipy.optimize.bisect: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html
- SciPy reference, optimization and root finding: https://docs.scipy.org/doc/scipy/reference/optimize.html
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 24 — Interval arithmetic and uncertainty containment

**Domain:** Numerics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

An interval [a,b] denotes every number between two endpoints, not a probability distribution. Interval addition and multiplication produce enclosures of all possible results when operations and input domains satisfy the stated algebra. Exact rational endpoints make containment straightforward to verify in a small reference model. Floating-point interval arithmetic requires directed outward rounding to avoid accidentally shrinking the true range. Dependency is a serious limitation: evaluating x−x with x in [0,1] using naïve independent interval rules produces [−1,1], although the exact result is zero. Intervals therefore provide conservative bounds, not necessarily tight inference. A confidence interval has a different interpretation and should not be substituted for a deterministic uncertainty enclosure.

## Formal statement, symbols, and units

[a,b]+[c,d]=[a+c,b+d]; [a,b]×[c,d]=[min(ac,ad,bc,bd),max(ac,ad,bc,bd)].

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Containment follows because addition is monotone in both arguments and a bilinear product achieves extrema at rectangle corners. The exact rational implementation avoids rounding under-enclosure. For correlated operands, treating repeated occurrences as independent can make bounds too wide. For non-rational or measured input, a separate acquisition bound is required before claiming that real values lie in the interval. This is analogous to uncertainty tubes in Control Atlas, but the computational reference makes no statement about actuator or physical-system safety.

## Reconstruction exercise with independently checkable output

Multiply [-1/2,3/2] by [-2,3], enumerate all four corner products, then sample 100 rational interior pairs to confirm each lies in the enclosure. Next evaluate x−x using both a symbolic simplification and naïve intervals.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not use normal floating-point endpoint calculations as strict enclosures without outward rounding. A bounding box is not a statistical confidence guarantee and may be far too loose for decision-making.

## Source orientation

- Python documentation, fractions — Rational numbers: https://docs.python.org/3/library/fractions.html
- Python documentation, Floating-Point Arithmetic: Issues and Limitations: https://docs.python.org/3/tutorial/floatingpoint.html
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 25 — Finite-state reachability and bounded model checking

**Domain:** Verification. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Model checking explores explicitly represented states and transitions to answer properties about a declared model. Reachability can find a concrete path witness to a goal. Exhaustive failure to find a goal establishes non-reachability only if the reachable state graph has been completely explored and the model faithfully represents the system. State explosion can make exhaustive enumeration impossible; a resource limit produces an unknown verdict, not a false property. Model checking is distinct from running a real distributed system: clock timing, nondeterministic environment input, network loss, and memory corruption may be absent from the abstraction. A preservation-grade report must identify the model boundary and whether the search was complete.

## Formal statement, symbols, and units

Reach(initial,goal) ⇔ ∃ path s0→s1→…→sk with s0=initial and goal(sk). A visited set prevents infinite re-exploration of finite graph cycles.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Breadth-first traversal discovers shortest witnesses by edge count in an unweighted finite graph. If the exploration queue empties after every legal successor has been considered, no path reaches the goal in the stated graph. If the queue remains when the budget expires, non-reachability has not been established. This is a finite exact result that does not contradict the general undecidability of arbitrary-program halting.

## Reconstruction exercise with independently checkable output

Supply states {0,1,2}, transitions 0→1 and 1→2, and a goal predicate state==2. Compare the full exploration result with one limited to a single expansion; the latter must return unknown.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not equate a bounded model checker with a universal proof engine. Unmodeled state dimensions or outside-world actions can invalidate the model-level guarantee.

## Source orientation

- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 26 — Inductive invariants and loop correctness

**Domain:** Verification. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

An invariant is a property of system states preserved by every allowed transition. An inductive invariant requires initialization and step preservation. It is a sufficient proof principle: if the invariant holds initially and no transition leaves it, every reachable state satisfies it. A proposed invariant may fail induction because it is too weak even when the target safety property is true; strengthening is often needed. In an explicitly finite universe, a checker can enumerate transitions and validate an invariant. If a successor leaves the declared universe, rejecting the model is more honest than silently ignoring the transition. The specific set of transitions must be preserved for later auditors to reproduce the proof.

## Formal statement, symbols, and units

Initialization P(s0); consecution ∀s,t: P(s)∧T(s,t) ⇒ P(t). Then ∀ reachable s, P(s).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Prove by induction on trace length. The base case follows from initialization. For any length-k trace ending in a P-state, the transition property ensures the successor also satisfies P, establishing length k+1. This logical skeleton is broadly useful in algorithms, protocol design, and control. The finite checker performs a universal check only over *its supplied state universe*. The relation to the physical system is an independent modeling obligation.

## Reconstruction exercise with independently checkable output

For states 0–3 and transition s→min(s+1,3), prove 0≤s≤3 inductive. Replace the property with s==0 and identify the one-step counterexample. Explain why a true but noninductive property may require auxiliary state.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Unit tests of typical transitions are not inductive proofs. Neither proof scripts nor hashes authenticate the source of the model unless independently controlled.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 27 — Termination rankings and bounded progress

**Domain:** Verification. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A ranking function maps nonterminal states to a well-founded set and decreases on every transition. A natural-number rank that strictly decreases cannot decrease forever, proving termination when each transition follows the model and no stuck nonterminal state is allowed. A ranking proof is stronger than observing that many runs stop, but it is conditional on complete state and transition descriptions. Real applications may use lexicographic ranks, multisets, ordinals, or fairness assumptions. An agent's “determination” or intent cannot replace these progress conditions. Distinguish a proof that every step reduces a rank from a scheduler promise that steps will eventually be executed.

## Formal statement, symbols, and units

Rank ρ:S→ℕ with ρ(s′)<ρ(s) for every transition from nonterminal s. No infinite descending chain exists in ℕ.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

If an infinite execution existed, its ranks would form an infinite strictly descending sequence of nonnegative integers, impossible by well-ordering. A finite checker may validate an applicant's rank function over all declared transitions. But the proof applies only if transition selection actually follows the model and all nonterminal states can take a step; otherwise deadlock may prevent the intended terminal condition. Progress and safety are distinct classes of property.

## Reconstruction exercise with independently checkable output

Model a countdown 4→3→2→1→0 using rank ρ(s)=s. Prove each transition decreases. Add a self-loop at 2 and observe the checker refutes the rank. Compare that refutation with mere step-budget exhaustion.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not claim a retry policy guarantees completion when retries can cycle, external side effects are uncertain, or the environment does not eventually respond.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 28 — Shannon entropy, information, and physical uncertainty

**Domain:** Information. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Information theory quantifies expected surprise under a declared probability distribution. Shannon entropy H measures average self-information in bits when the logarithm base is two. It does not measure truth, intelligence, understanding, meaning, or scientific evidence quality. A perfectly random source can have high entropy while carrying no useful explanatory content; a compact theorem can have few bytes while conveying profound knowledge to someone with the prerequisites. For compression, probability assumptions and code constraints matter. Empirical frequency estimates introduce sampling uncertainty that should not be hidden inside an exact-looking entropy number. A physical thermodynamic entropy is related in some settings but not interchangeable with Shannon entropy without a specific model.

## Formal statement, symbols, and units

H(X)=−Σ_i p_i log₂(p_i), with 0 log 0 defined as 0. For a fair binary distribution H=1 bit; for a certain outcome H=0.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Expected surprise is obtained by averaging −log₂ p_i with respect to p_i. Entropy is maximized by a uniform distribution on a finite alphabet. Jensen's inequality or constrained optimization gives the maximum bound log₂(n). It quantifies distributional uncertainty, not the epistemic confidence of a human citation or the accuracy of a classifier.

## Reconstruction exercise with independently checkable output

Compute H for [1,0], [1/2,1/2], and [1/4]*4. Then construct two messages of the same length with different semantic value, explaining why byte count alone cannot determine usefulness to future scientists.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Never use “information density” as a validated cognitive-performance measure without defining its operational units, baseline, and independent held-out tasks. Entropy estimates based on unrepresentative samples can mislead.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 29 — Prefix codes, Kraft inequality, and recoverable archives

**Domain:** Information. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A prefix-free binary code has no codeword that begins another codeword. Such a code can be decoded greedily without explicit separators when the codebook is known. This does not by itself ensure efficient compression; code lengths should reflect symbol probabilities, and metadata overhead matters. Huffman coding produces an optimal binary prefix code for a specified finite symbol distribution under ordinary codeword-length cost, but not necessarily an optimal code under streaming, edit resilience, or CPU constraints. Archive survival depends on storing the codebook, version, bit ordering, and integrity metadata. A file that cannot be decoded without a vanished proprietary codec is not meaningfully preserved.

## Formal statement, symbols, and units

Kraft inequality: Σ_i 2^(−l_i)≤1 for a binary prefix code with lengths l_i. Average length L=Σ_i p_i l_i≥H(X).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A prefix-free code corresponds to leaves of a binary tree. A codeword of length l occupies 2^(−l) of the conceptual depth-infinite tree's capacity, and disjoint leaves cannot sum to more than one. Entropy provides a lower bound on expected code length, but finite codewords and integer lengths can introduce overhead. For survival archives, the decoder specification must be present in independent human-readable form.

## Reconstruction exercise with independently checkable output

Check that [0,10,11] is prefix-free and [0,01] is not. Compute Kraft sums, then describe how a bitstream of symbols can be decoded by walking a binary tree. Record the exact code assignment with the archive.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Checksums detect accidental corruption under assumptions, but do not correct it; parity or error-correcting codes serve a different purpose. Compression is not encryption and not provenance authentication.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 30 — Parallelism, Amdahl’s law, and synchronization cost

**Domain:** Architecture. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Parallel computing divides work among processors, but dependencies and coordination limit speedup. Amdahl's law models fixed-size work: a fraction remains serial, and the rest can be parallelized ideally. Parallel overhead, data transfer, contention, load imbalance, and memory capacity often make real speedup smaller. Gustafson-style scaling considers larger problems as resources grow, answering a different question. Amdahl's law is not evidence that a particular distributed agent swarm will run proportionally faster. Tasks may share bottlenecks, retry failed work, contend for a provider, or duplicate efforts. Measuring total compute, wall-clock critical path, and quality separately is essential.

## Formal statement, symbols, and units

Idealized speedup S(p)=1/[(1−f)+f/p+o(p)] where f is parallelizable fraction, p workers, and o(p) is overhead expressed relative to serial baseline.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The denominator separates serial time, parallelized time, and overhead. As p→∞ and o(p)=0, speedup approaches 1/(1−f) when f<1. Even without serial work, overhead may dominate at large p. Work–span analysis gives a complementary lower bound on parallel runtime. A synchronization barrier can cause idle workers, and independent throughput is not the same as critical-path latency for one request.

## Reconstruction exercise with independently checkable output

Calculate idealized speedup for f=0.9 and p in {1,2,4,8,16}. Repeat with overhead 0.1 and show a case where more workers no longer help. Record that these are assumed parameters, not measurements from PEGASUS or any other live system.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

No benchmark speedup claim follows from the model alone. Amdahl is also not a universal law of all optimization: workload scaling and changed algorithms alter the question.

## Source orientation

- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 31 — Sampling variability and Bernoulli evaluation intervals

**Domain:** Statistics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A binary test outcome provides one Bernoulli observation only after a clear success criterion, sampling design, and task scope are fixed. A sample proportion is not automatically an estimate of general AI performance or scientific truth. Confidence intervals describe repeated-sampling procedures under declared assumptions. Wilson score intervals often behave better than naïve normal intervals near zero or one successes, but neither removes sampling bias, dependence between tasks, evaluator leakage, or measurement error. Paired experimental designs control task difficulty when comparing two agents or algorithms; independent Bernoulli proportions are inappropriate if the same tasks are used with correlated outcomes. Reporting both denominator and missing trials is essential.

## Formal statement, symbols, and units

p̂=k/n. Wilson center=(p̂+z²/(2n))/(1+z²/n); half-width=[z/(1+z²/n)]√(p̂(1−p̂)/n+z²/(4n²)).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The Wilson interval comes from inverting an approximate score test. Its advertised coverage depends on independent and identically distributed Bernoulli trials and the confidence-level convention encoded in z. The formula is an interval estimator, not a guarantee that a specific unknown probability is inside the computed range. Random seeds, task versions, grader rules, and exclusions must be logged before interpreting the numbers.

## Reconstruction exercise with independently checkable output

Compute the Wilson interval for 7 successes in 10 attempts and compare with 70 in 100. Hold the observed proportion fixed and observe that uncertainty decreases with larger n under independence assumptions.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not score repeated trials on the same contaminated task as independent evidence of broad generalization; do not report success rate when failures or missing labels were excluded without declaration.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 32 — Algorithm evaluation: correctness, efficiency, and generalization

**Domain:** Methodology. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

An algorithm should be evaluated against its stated contract, not a convenient benchmark alone. Unit tests check examples and boundary cases; property-based tests examine invariants on many generated inputs; independent oracles use a mathematically or implementationally separate route; differential tests compare systems; formal proofs establish quantified results under assumptions. These forms of evidence have different strengths. Randomized trial counts do not automatically measure independence: two algorithms could share the same bug, and a large number of correlated trials can exaggerate certainty. A benchmark specification should include input generator, distribution, seeds, environment, hardware, compiler versions, numerical tolerances, and expected outputs before results are observed.

## Formal statement, symbols, and units

Observed failure rate = failures/eligible_trials, with eligibility and denominator defined in advance. Property for sorting: sorted(out) ∧ multiset(out)=multiset(in).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The logical quantifiers differ: a test asserts ∀x in a finite checked set, property(x); universal correctness requires ∀x in the declared domain. An independent oracle increases confidence but does not change the quantifier unless it is itself a proof checker with verified soundness. A benchmark also needs honest selection: a method chosen after seeing held-out task results is no longer evaluated under a sealed holdout.

## Reconstruction exercise with independently checkable output

Generate 100 seeded random graphs, test dijkstra against an independent Bellman–Ford implementation, and record any disagreement with the exact graph. Include adversarial disconnected graphs, tie weights, and very large weights. Keep the oracle separate from production code.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not equate 10,000 passing synthetic tests with field validation, cross-architecture reproducibility, or scientific peer review. Test logs are evidence of execution, not of the truth of all source claims.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- SciPy reference, sparse graph shortest paths: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 33 — Preservation-grade software and scientific reconstruction

**Domain:** Methodology. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A preservation library must remain understandable when the original cloud services, package managers, websites, and author are gone. Store human-readable algorithms and proofs beside machine-executable reference programs. Record exact source and dataset bytes when legally permitted, cryptographic file hashes, licensing, encoding, source versions, and transformation histories. Preserve compilers and interpreters where licensing and storage permit, but do not make them the only way to understand the theory. Explicitly state which results are exact math, which are synthetic experiments, which are empirical reproductions, and which have independent human review. Redundant copies stored in separate failure domains improve survivability but must be tested with actual restoration drills.

## Formal statement, symbols, and units

Integrity: SHA256(file_bytes)=expected_hash. Authenticity requires a trusted signature/channel; scientific validity requires independent evidence. These three propositions are not equivalent.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A content hash detects a changed file only when the expected hash is obtained from a trusted earlier record. If both payload and expected hash are replaced together, hashing alone does not authenticate the original publisher. A link-only source card is useful navigation today but cannot reconstruct the primary document after network loss. A survival ledger should therefore count original source bytes separately from source citations and provide an acquisition plan. A fully replayed ZIP test supports software restorability, but not all dependency or platform portability.

## Reconstruction exercise with independently checkable output

Disconnect the network, extract the collection to a new directory, verify file inventory, run tests, open markdown chapters, execute the casebook, and inspect the original-source ledger. Repeat on distinct hardware when available. Record any dependency requiring a missing wheel, key, or remote service.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not advertise an archive as containing “all of humanity's knowledge.” Scope is necessarily finite. Structural test counts and locally written explanations cannot replace original scientific measurements, expert review, archival rights clearance, or geographic redundancy.

## Source orientation

- NIST FIPS 180-4 Secure Hash Standard: https://csrc.nist.gov/pubs/fips/180-4/upd1/final
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 34 — Domain boundaries and future cross-disciplinary reuse

**Domain:** Methodology. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Computation Atlas supplies algorithms and mathematical reasoning primitives to later nodes without becoming a runtime router. Control uses numerically stable solvers and proof obligations; Materials requires measured units, physical constitutive assumptions, and interpolation limits; Agent uses evidence receipts, dependency graphs, and statistical evaluation; Causal requires counterfactual assumptions; Measurement constrains numerical input uncertainty. The same algorithm can be correct in an abstract mathematical domain and inappropriate in a physical one. Cross-node relations describe dependency and applicability, not proof that an integration improves models. A knowledge node should expose structured records and source closure but avoid silently executing retrieved text or granting untrusted references control over tools.

## Formal statement, symbols, and units

Safe composition requires typed interfaces, dimensional consistency, valid preconditions, and evidence-preserving transformations. If A guarantees Q under P, downstream consumers must establish P before relying on Q.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Consider Dijkstra as a component in a physical routing problem: the graph algorithm proves shortest path for a static nonnegative weighted graph, not that the graph reflects current road conditions or that edge weights represent physical travel time. Similarly a numerical controller may prove bounds under a model while sensor calibration is unknown. Reconstructability depends on preserving both the method and the mapping between symbolic input and real world.

## Reconstruction exercise with independently checkable output

Trace a single formula from Computation into a Control uncertainty calculation, identifying each additional assumption: units, finite precision, model mismatch, and observation validity. Store these as qualifiers in the common Atlas schema, never as a new automatic router.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not connect Bitwork routing now. The project requires all 30 research domains to be complete, then a separate, measured routing implementation, independent evaluation, and eventual desktop transfer.

## Source orientation

- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.



---


# Chapter 35 — Disjoint-set union and equivalence classes

**Area:** Algorithms. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

An equivalence relation partitions a set into nonoverlapping classes. Disjoint-set union (DSU), also called union–find, maintains this partition under merge and membership queries. Each element points toward a representative root. With union by size and path compression, a long sequence of operations is extremely efficient in amortized analysis; that does not imply every individual operation is constant-time. The abstract state is the partition, not the layout of parent pointers. Different parent forests can encode the same partition; correctness should be checked against an independent equivalence relation.

## Mathematical contract

Invariant: find(x)=find(y) exactly when x and y are in the same maintained component. Union(x,y) merges exactly those two equivalence classes. Amortized complexity is O(α(n)) per operation under classical union-by-rank/size and path compression assumptions.

## Derivation and reasoning

Initially each element forms a singleton class. A union changes one representative's parent to the other, so all members of the old class share the new representative without splitting any class. Path compression changes pointers only to ancestors within the same class; therefore it preserves membership. The complexity bound uses amortized sequence analysis and should not be read as a worst-case bound for one find operation.

## Worked reconstruction and independent check

Start with elements {0,1,2,3,4}. Merge (0,1) and (1,2), then query (0,2) and (0,3). The first must be true and the second false. Verify component count decreases only on a merge of two different classes. Repeatedly query find to inspect path compression without changing the logical partition.

## Limitations, falsification, and invalid use

Do not interpret path-compressed pointers as an actual organizational hierarchy, or claim the amortized bound for unbounded integers and dynamic allocations without a cost model. The reference implementation uses a finite list of integer labels. A malformed or foreign element is refused.

## Cross-domain meaning

Minimum spanning forest and graph connectivity use DSU, but its usefulness for an AI swarm does not prove correct task ownership or user authorization.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT 6.006 Introduction to Algorithms, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 36 — Minimum spanning forests and Kruskal’s algorithm

**Area:** Algorithms. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

A spanning forest connects each connected component of an undirected weighted graph without cycles. A minimum spanning forest minimizes total selected edge weight over all such forests. Kruskal's algorithm considers edges in nondecreasing order, accepting an edge precisely when it joins previously separate components. DSU makes that component test efficient. Negative finite edge weights are allowed in this undirected objective, unlike Dijkstra's shortest paths. Self-loops cannot improve connectivity and are excluded.

## Mathematical contract

Find forest F minimizing Σ_(e∈F) w(e), subject to F acyclic and connecting every original connected component. Repeatedly accept minimum not-yet-considered edge joining distinct DSU components.

## Derivation and reasoning

The cut property gives the greedy argument: if an edge is lightest across a cut respected by the current forest, some optimum forest contains it. Exchanging the edge with one crossing the same cut preserves a spanning forest without increasing cost. An accepted edge never creates a cycle because its endpoints are in separate DSU classes. When no edges remain, every original component is connected.

## Worked reconstruction and independent check

On vertices 0–3 with edges (0,1,1), (1,2,2), (0,2,5), (2,3,1), the algorithm accepts indices 0,3,1 and reports total weight 4. A separate NetworkX oracle computes the same forest weight on randomized inputs, including disconnected graphs.

## Limitations, falsification, and invalid use

This proof concerns exact graph edges and fixed costs. It does not choose shortest paths, minimize maximum end-to-end delay, or resolve hidden energy, temporal, geographical or authorization constraints. Weight ties can produce multiple correct forests.

## Cross-domain meaning

Spanning trees provide inexpensive connectivity abstractions for distributed architectures, but a reliable network protocol also requires failure handling and temporal semantics.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT 6.006 Introduction to Algorithms, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


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



---


# Chapter 38 — Discrete Fourier transform and radix-two FFT

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

The discrete Fourier transform (DFT) expresses a finite sequence in a frequency basis of complex exponentials. The direct computation has quadratic arithmetic cost in sequence length. The radix-two fast Fourier transform (FFT) recursively decomposes even and odd indices into smaller transforms, yielding O(n log n) operations for n a power of two. Both compute the same mathematical DFT, aside from numerical rounding. Fourier coefficients are not automatically physical resonant modes: sample rate, windowing, boundary conditions and measurement geometry affect interpretation.

## Mathematical contract

X_k=Σ_(n=0)^(N−1) x_n exp(−2πikn/N). The inverse is x_n=(1/N)Σ_k X_k exp(+2πikn/N). For N=2^m, radix-two FFT work is O(N log₂N).

## Derivation and reasoning

Split the DFT sum into terms with even index 2j and odd index 2j+1. Both subsets are transforms of length N/2. The odd transform is multiplied by a twiddle factor exp(−2πik/N); combining one pair of N/2 transforms costs O(N). Thus T(N)=2T(N/2)+O(N), yielding O(N log N). The inverse changes the exponential sign and divides by N.

## Worked reconstruction and independent check

Take [1,2,3,4]; calculate its four complex DFT coefficients by hand and recover the input using the inverse transform. Compare the pure-Python iterative FFT with NumPy's FFT on seeded complex arrays. The tests include round trips, real and imaginary components, and several powers of two.

## Limitations, falsification, and invalid use

Non-power-of-two lengths require another FFT variant or padding. Rounding can accumulate; tiny imaginary residuals after real-valued convolution do not imply a physical imaginary signal. No claim of instrument frequency calibration is made.

## Cross-domain meaning

Signal and Cymatics Atlases depend on correct transform mathematics, but the FFT itself does not establish a physical mechanism or measured acoustic resonance.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare 18.S191 Introduction to Computational Thinking](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 39 — Convolution, spectral multiplication and aliasing

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Linear discrete convolution combines two finite sequences and is central to filtering, impulse responses, polynomial multiplication and imaging. The convolution theorem permits a fast implementation using Fourier-domain multiplication, provided the transform length is large enough to avoid circular wraparound. Naively using an N-point transform for a linear convolution longer than N computes circular convolution and aliases tail terms into earlier samples. Zero-padding is therefore a mathematical requirement, not an optional performance tweak.

## Mathematical contract

(a*b)[k]=Σ_j a[j]b[k−j], where out-of-range indices contribute zero. DFT(a*b)=DFT(a)·DFT(b) for zero-padding length N≥len(a)+len(b)−1.

## Derivation and reasoning

Expanding the DFT of the convolution and exchanging the finite sums yields the product of individual DFTs. The DFT implements periodic extension, so the pointwise product corresponds to circular convolution unless the zero-padded period exceeds the linear result length. With enough padding, circular and linear results coincide within the needed output range.

## Worked reconstruction and independent check

Convolve [1,2,3] with [2,1]. The correct linear result is [2,5,8,3]. The reference method pads to the next power of two, multiplies FFT spectra, inverses and truncates to the linear length. Compare against NumPy's direct convolution rather than another FFT implementation.

## Limitations, falsification, and invalid use

The output of floating-point convolution is approximate. Frequency-domain multiplication can overflow or magnify conditioning problems. For massive sparse kernels, direct/sparse methods may outperform FFT due to overhead. No physical filter response is established without sampling and boundary-condition evidence.

## Cross-domain meaning

This is a mathematical bridge to Cymatics and Signal Atlases, not an implementation of a cross-domain Bitwork router.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare 18.S191 Introduction to Computational Thinking](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 40 — Exact linear equations, rank and pivoting

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

A system Ax=b represents linear constraints. Gaussian elimination applies invertible row operations to find an equivalent echelon system; back-substitution then recovers solutions where pivots exist. In exact rational arithmetic, an invertible square matrix yields a unique solution and a zero residual certificate. A singular matrix may have no solutions or infinitely many, neither of which should be silently represented by a guessed inverse. Numerical floating-point elimination additionally needs pivot strategies and condition analysis because small pivots can amplify rounding.

## Mathematical contract

Elementary row operation preserves the solution set. For square nonsingular A, x=A^(−1)b, and exact residual r=Ax−b=0. Rank(A)=n is sufficient for uniqueness in an n×n system.

## Derivation and reasoning

Swapping rows, adding a scalar multiple of one row to another, or scaling a row by a nonzero scalar preserves the simultaneous-equation solution set. Gauss–Jordan eliminates every nonpivot coefficient and normalizes pivots to one. When no nonzero pivot exists in a required column, the supplied square matrix is singular and the unique-solution contract fails. Exact arithmetic avoids cancellation error but increases integer numerator/denominator size.

## Worked reconstruction and independent check

Solve 2x+y=5 and x−y=1, obtaining x=2, y=1. Then solve with coefficients 1/10 and 3 using Fraction strings to preserve decimal intent. The reference also refuses [[1,2],[2,4]] under a uniqueness contract. Compare non-singular integer systems against SciPy at moderate condition numbers.

## Limitations, falsification, and invalid use

Exact rational solutions can be extremely expensive for large systems. `Fraction(0.1)` captures an already-rounded float, whereas `Fraction("0.1")` represents one tenth exactly. A zero residual in the model does not prove that measured coefficients came from a valid scientific experiment.

## Cross-domain meaning

This supports Causal regression and Control linear systems, but their model identification, input units and physical uncertainty are independent evidence obligations.

## Source orientation and recoverability

- [MIT 18.06 Linear Algebra, course syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) — original publisher bytes unavailable in this package.
- [Python documentation, fractions — Rational numbers](https://docs.python.org/3/library/fractions.html) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 41 — Numerical conditioning and iterative linear solvers

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Solving Ax=b with finite-precision arithmetic requires consideration of sensitivity. The condition number measures how a small perturbation of the matrix or right-hand side can change the solution. A solver can have a small residual ||Ax−b|| yet a large forward error when A is ill-conditioned. Iterative methods such as Jacobi, Gauss–Seidel and conjugate gradient use repeated updates, often exploiting sparsity. Their convergence depends on properties such as diagonal dominance or positive definiteness and cannot be promised for arbitrary inputs.

## Mathematical contract

Residual r_k=b−Ax_k; forward error e_k=x_k−x*. Condition estimate for nonsingular A: ||e||/||x*|| ≲ κ(A)(||δA||/||A||+||δb||/||b||) under suitable small-perturbation conditions.

## Derivation and reasoning

An approximate solution is validated by the residual but interpreted with a condition estimate. For positive definite quadratic energy, conjugate gradient can use Krylov subspaces and orthogonality to converge rapidly under good conditioning; exact arithmetic may terminate in at most n steps, while floating point complicates the ideal theorem. Sparse matrix–vector products can dominate computation and data movement rather than scalar multiplication count.

## Worked reconstruction and independent check

Take A=[[1,1],[1,1+ε]] with ε small. Compare the numerical solution after slightly perturbing b. Record residual and difference from an exact Fraction calculation. Vary ε through several orders of magnitude and show why a tiny residual alone is insufficient.

## Limitations, falsification, and invalid use

The current v0.2 code implements only bounded exact elimination, not a full sparse iterative solver or condition estimator. The chapter is conceptual and its mathematical claims require independent source review before a safety-critical application.

## Cross-domain meaning

Future Control and Measurement integrations must carry sensor uncertainty, physical units and condition numbers along with numerical estimates.

## Source orientation and recoverability

- [MIT 18.06 Linear Algebra, course syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) — original publisher bytes unavailable in this package.
- [Python decimal module: rounding, context and arithmetic](https://docs.python.org/3/library/decimal.html) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 42 — Randomized algorithms, Las Vegas and Monte Carlo

**Area:** Probability. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Randomization can affect runtime, output correctness, or both. A Las Vegas algorithm always returns a correct result when it terminates, but runtime can vary randomly. A Monte Carlo algorithm has bounded or controlled runtime and may return an incorrect result with a quantified probability under its probability model. Randomized pivot selection, sampling, primality tests and hash tables illustrate different uses. A pseudorandom generator with a fixed seed helps reproduce software tests but does not turn correlated or adversarial outputs into independent unbiased samples.

## Mathematical contract

For independent indicator errors E_i with P(E_i)≤p, repeating a valid independent test k times can reduce joint error to ≤p^k under independent trials. Without independence, this multiplication is unjustified.

## Derivation and reasoning

A probability bound is conditional on the algorithm's distributional assumptions. If an adversary can predict the generator seed, or if random events share hidden state, repeated outcomes may be correlated. A randomized algorithm still needs a specification of success, failure and the random-variable distribution. Correctness proofs for Monte Carlo methods usually bound error over random choices, not over every sequence of choices.

## Worked reconstruction and independent check

Construct a randomized selection process with a declared probability of a bad pivot and repeat using a fixed seed. Distinguish observed failure frequency from a theoretical bound and include the seed, generator algorithm and test inputs. Compare two independent generators only if their statistical independence is justified.

## Limitations, falsification, and invalid use

A stochastic language model's different prompts or temperature settings do not automatically produce independent benchmark tasks or evaluators. Randomized tests support software confidence, not an empirical proof of agent generalization.

## Cross-domain meaning

Agent Atlas can use randomized evaluations later, but the benchmark's sampling and outcome authority must be independently established.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare, Mathematics for Computer Science](https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 43 — Concentration bounds and statistical identification

**Area:** Probability. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Concentration inequalities relate sample averages to expected values under probability assumptions. Hoeffding's inequality supplies a bound for independent bounded random variables. Its algebra is straightforward, but applying it to model evaluations or manufacturing measurements requires evidence that observations are independent, properly bounded and sampled from a relevant stable process. Repeated trials of one fixed task are not the same as fresh independently sampled tasks. A confidence bound also does not authenticate an evaluator or correct for selection bias.

## Mathematical contract

For independent Xi∈[0,1] with common mean μ, P(|X̄−μ|≥ε) ≤ 2exp(−2nε²). For confidence parameter δ, ε=sqrt(ln(2/δ)/(2n)).

## Derivation and reasoning

The exponential bound follows by applying an exponential-moment inequality to bounded deviations and then optimizing the moment parameter. Inverting it yields a conservative half-width. Clipping the resulting interval to [0,1] respects the parameter range without changing the bound's conditional interpretation. The right variable may be a sequence of independently sampled tasks, not individual actions within one correlated session.

## Worked reconstruction and independent check

For 100 independent binary outcomes, compute the 95% bound radius and compare it to the radius for n=400. The v0.2 method reports a conditional interval and explicitly sets `coverage_verified_for_actual_data=False`. Repeating a deterministic self-graded answer 100 times should not be presented as 100 independent evidence sources.

## Limitations, falsification, and invalid use

Hoeffding is not a generic “95% chance my answer is true” statement. Unmodeled dependence, missing outcomes, adaptive model selection, or dishonest rewards can invalidate the intended interpretation. No actual model-performance dataset is analyzed in this edition.

## Cross-domain meaning

This qualification connects to Measurement uncertainty and Agent evaluation, without completing any empirical cross-domain test.

## Source orientation and recoverability

- [MIT OpenCourseWare, Mathematics for Computer Science](https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare 18.S191 Introduction to Computational Thinking](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 44 — Complexity classes P, NP and careful reductions

**Area:** Theory. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Complexity classes describe families of formal decision problems under explicit machine models and input encodings. P contains languages decided by a deterministic algorithm in polynomial time; NP contains languages with polynomial-size certificates verified in polynomial time, equivalently accepted by a nondeterministic polynomial-time machine. NP-hardness is established by suitable reductions from already-hard problems, not by a problem merely seeming difficult. A problem can be NP-hard without belonging to NP, while NP-completeness requires both NP membership and NP-hardness.

## Mathematical contract

P⊆NP. A language L is NP-complete when L∈NP and ∀K∈NP, K≤_p L. A many-one polynomial reduction f must satisfy x∈K iff f(x)∈L and compute f in polynomial time.

## Derivation and reasoning

The reduction preserves yes/no membership in both directions. Without the reverse direction, a mapping can produce misleading evidence of hardness. To show a problem is NP-complete, provide a certificate verifier with polynomial bound and a reduction from a known NP-complete problem. The still-unresolved P versus NP question must not be treated as settled by performance observations, large LLMs or heuristic solvers.

## Worked reconstruction and independent check

Encode subset sum as a decision problem, define the input length in bits, and show why an O(nW) dynamic program can be pseudopolynomial rather than polynomial in input length. Explain what a correct reduction to a different decision problem would need to preserve. Do not claim to have proved a new completeness result.

## Limitations, falsification, and invalid use

Worst-case difficulty is not the predicted cost of one ordinary input. Empirical runtime failure cannot prove NP-hardness or undecidability. Complexity class definitions alone do not specify hardware energy or online provider latency.

## Cross-domain meaning

Complexity theory constrains Computation and Agent planning, but it does not prove an AI architecture has achieved general reasoning or improved any task distribution.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [Stanford Encyclopedia of Philosophy, Computability and Complexity](https://plato.stanford.edu/entries/computability/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 45 — Approximation algorithms and objective guarantees

**Area:** Optimization. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

For difficult optimization problems, an algorithm may provide a feasible solution with a provable quality ratio, even when exact optimum is expensive to compute. An approximation guarantee compares objective values to the best possible solution under a specified problem instance class. It is distinct from a heuristic benchmark: an average observed score over examples is not a worst-case approximation proof. Some approximation schemes become computationally impractical as the desired accuracy increases, so the dependence on ε must be stated.

## Mathematical contract

For nonnegative minimization cost, ρ-approximation means ALG(I)≤ρ·OPT(I), ρ≥1. For maximization, ALG(I)≥OPT(I)/ρ. A PTAS has polynomial input-time for each fixed ε>0, but may grow rapidly as ε→0.

## Derivation and reasoning

The greedy set-cover algorithm can be analyzed by charging each newly covered element a portion of the selected set's cost. Comparing these charges to an optimal set cover leads to a logarithmic performance factor. The proof depends on set coverage and cost assumptions; translating arbitrary scheduling or memory retrieval into set cover requires an explicit reduction and a correct objective. A ratio against a nonoptimal baseline is not an approximation guarantee.

## Worked reconstruction and independent check

Construct a four-element set-cover example and enumerate all feasible covers. Compare the greedy cover to exact optimum and identify whether the guarantee holds for the declared cost model. Explain why a case with an impressive ratio does not establish the theorem for all inputs.

## Limitations, falsification, and invalid use

No universal approximation ratio is claimed for Bitwork routing, source retrieval or agent collaboration. Even a proven approximation algorithm can produce unsafe choices if the mathematical objective excludes a real-world constraint.

## Cross-domain meaning

The future router can use approximate search once its evidence-loss and cost objectives are explicitly defined and independently evaluated.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT 6.006 Introduction to Algorithms, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 46 — Vector clocks, causality and concurrency

**Area:** Distributed Systems. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Distributed processes do not necessarily share an exact global wall clock. Event causality is better described through local order and message transmission: an event happens before another if they occur in order on one process, if the first sends a message received by the second, or by transitive closure. Lamport logical clocks respect this ordering but cannot infer causality merely from a smaller scalar timestamp. Vector clocks extend the idea with one counter per participant, allowing a partial-order test under fixed participants and correct message propagation.

## Mathematical contract

Vector clocks a,b: a→b iff a_i≤b_i for every i and a_j<b_j for at least one j. If neither a≤b nor b≤a, the events are concurrent. Equal vectors are not independent identity proof.

## Derivation and reasoning

Local events increment one component; receipt merges component-wise maxima with the received timestamp, then increments the local component. These rules preserve causality because message receipt vector components dominate the sender's state. For two independent local events from (0,0), resulting vectors (1,0) and (0,1) are concurrent; comparing their physical time stamps cannot establish a causal relationship without additional evidence.

## Worked reconstruction and independent check

Start with two actors A and B. Tick A to (1,0), independently tick B to (0,1). Their events are concurrent. Let B receive A's message, merge to (1,1), then increment B to (1,2): A's earlier event happened before the receipt. Run the bounded vector-clock methods to reproduce these relations.

## Limitations, falsification, and invalid use

A vector clock does not authenticate actors or ensure a provider operation succeeded. Dynamic membership, malicious timestamps and missing messages require additional protocols. Never turn a comparison of timestamps into an authorization decision.

## Cross-domain meaning

Agent parent/worker handoff and SYMBIOTE learning exchange may benefit from causal envelopes, but no runtime connection is implemented here.

## Source orientation and recoverability

- [Lamport, Time, Clocks and the Ordering of Events in a Distributed System](https://lamport.org/pubs/time-clocks.pdf) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare 18.S191 Introduction to Computational Thinking](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 47 — Transactions, durability and exactly-once effect limits

**Area:** Distributed Systems. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Atomicity, consistency, isolation and durability describe transactional guarantees under documented storage semantics. A database transaction may commit while the client loses the acknowledgment, creating an ambiguous external outcome. Exactly-once message delivery is a phrase that often hides the distinction between transport retries and unique external effects; safe idempotent application requires a provider-side contract or transactionally coordinated state. A caller-generated request ID alone does not prove deduplication. Two identical payloads may be intentional separate operations, and two nonidentical payloads may be retries of one logical operation.

## Mathematical contract

For idempotent operation f: f(f(x))=f(x) under the declared state and identity semantics. Exactly-once effect requires an authorization and deduplication boundary that survives crashes; mere at-least-once delivery does not imply exactly-once effects.

## Derivation and reasoning

If the service stores the request ID and its committed effect atomically, duplicate requests with that same logical ID can return the stored response rather than re-execute. If the client times out after submission and lacks authoritative provider reconciliation, retrying with a new ID can duplicate the action. A local event journal that is not itself durable or trusted cannot prove what the provider did.

## Worked reconstruction and independent check

Construct a simulated ledger with prepared, submitted, committed and acknowledgment-lost states. Ask whether the caller may safely retry under (a) no dedupe contract, (b) a provider-enforced idempotency token, and (c) unknown token-retention window. Document decisions as conditional rules, not as a live API implementation.

## Limitations, falsification, and invalid use

This content is a protocol-level explanation only. The archive does not implement a production database, distributed consensus protocol, trusted authorization, or two-phase commit; no live transaction is performed.

## Cross-domain meaning

A future Agent/Computation integration will need actual signed receipts and a host-controlled lifecycle, separate from reference reading.

## Source orientation and recoverability

- [Lamport, Time, Clocks and the Ordering of Events in a Distributed System](https://lamport.org/pubs/time-clocks.pdf) — original publisher bytes unavailable in this package.
- [AWS Builders Library, Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 48 — Canonical serialization, text encoding and preservation

**Area:** Information. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Knowledge preservation requires deterministic interchange formats and explicit text encoding. A computer stores bytes, not abstract characters. Unicode code points, normalization, grapheme clusters and UTF-8 sequences must be distinguished before claiming that two text strings are equal. Canonical serialization aims to give one deterministic byte representation for a specified data model, making content hashes comparable across software versions. Sorting JSON keys is helpful but is not a complete standard for every number, Unicode or floating-point edge case. The exact canonicalization specification must be named and preserved.

## Mathematical contract

Digest = SHA256(canonical_bytes(record)). Byte equality under the same canonicalization implies equal digest; digest equality does not prove source authenticity or semantic truth. For UTF-8, one Unicode scalar may occupy multiple bytes.

## Derivation and reasoning

A content-addressed record can preserve revision identity only when canonicalization rules are stable and the expected hash is trusted. A file and its listed hash can both be replaced; cryptographic hashing alone does not authenticate its original publisher. Unicode normalization can change byte sequences while preserving some user-visible text. Differences may be important for search, source citations and author names; the archive should preserve original bytes and separately record normalized views.

## Worked reconstruction and independent check

Serialize {"b":2,"a":1} and {"a":1,"b":2} under the exact sorted-key subset and confirm the same digest. Then serialize a NaN and confirm the implementation refuses non-JSON values rather than silently using implementation-specific tokens. Compare composed and decomposed accented letters as UTF-8 bytes.

## Limitations, falsification, and invalid use

The `canonical_json_digest` reference is intentionally not a full RFC 8785 implementation and should never be labeled interoperable JCS. Signing and archival authorization need separate issuer identity and key lifecycle.

## Cross-domain meaning

This is essential for ATLAS FORGE source closure and future Bitwork context packets, but it does not change the current router.

## Source orientation and recoverability

- [Python decimal module: rounding, context and arithmetic](https://docs.python.org/3/library/decimal.html) — original publisher bytes unavailable in this package.
- [NIST FIPS 180-4 Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 49 — Cryptographic assumptions and post-quantum agility

**Area:** Security. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Cryptographic integrity, authenticity, confidentiality and key agreement are different properties. Hashing verifies consistency relative to a trusted expected digest; a digital signature binds a message to a signing key under a security assumption; encryption hides content subject to a threat model; a key-encapsulation mechanism allows two parties to derive a shared secret via a public channel. Standards and algorithms require exact versions, parameter choices, key custody, interoperability tests and consideration of future cryptanalytic developments. Modern post-quantum designs respond to quantum threats but are not a promise of unconditional security.

## Mathematical contract

A KEM has KeyGen→(pk,sk), Encaps(pk)→(ciphertext,shared_secret), Decaps(sk,ciphertext)→shared_secret or a defined failure behavior. Security depends on the scheme, parameters, adversary model and implementation.

## Derivation and reasoning

NIST FIPS 203 specifies ML-KEM and parameter sets 512, 768 and 1024. Published documentation includes a November 2025 errata planning note, which is a reminder that a standards citation is versioned rather than timeless. Strong algorithm design does not prevent side-channel, random-number, key-reuse or API misuse vulnerabilities. This Atlas does not implement ML-KEM or invent a new quantum-resistant scheme; it preserves the distinctions and standards locators for future authorized implementers.

## Worked reconstruction and independent check

Create a conceptual table of hash digest, signature, encryption and KEM: what property each claims and what it does not. Verify a file hash against a separately stored trusted digest, then explain why the digest alone does not prove the publisher identity. Inspect FIPS 203 edition and recorded errata before any security claim.

## Limitations, falsification, and invalid use

Do not use the small teaching code for cryptographic deployment. Do not infer authenticity from matching SHA-256 fields or equate a KEM with digital signatures. Standards can be revised, and compliance is a system-level question.

## Cross-domain meaning

Future preservation may rely on signatures and key custody, but the current archive is not an authenticated global storage network.

## Source orientation and recoverability

- [NIST FIPS 180-4 Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — original publisher bytes unavailable in this package.
- [NIST FIPS 203 ML-KEM key encapsulation standard](https://csrc.nist.gov/pubs/fips/203/final) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Chapter 50 — Type systems, specifications and proof-carrying software

**Area:** Formal Methods. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Type systems classify program expressions and may rule out certain invalid operations before runtime. Contracts and refinements strengthen that classification with preconditions, postconditions and invariants. A type checker usually proves a restricted property about syntax under a formal semantics; it does not prove that the algorithm meets a human's intended specification, that a compiler implements the language correctly, or that an external tool has permission to perform its action. Proof-carrying software separates an executable artifact from a checkable evidence object, with the consumer verifying a stated property under a small trusted checking base.

## Mathematical contract

Judgment Γ⊢e:τ means expression e has type τ in environment Γ. Hoare triple {P} C {Q} claims that if P holds and command C terminates normally, Q holds, under the command semantics and environmental assumptions.

## Derivation and reasoning

A sound typing rule is justified by preservation of well-typed execution and progress or an explicit stuck-state classification, relative to a formal language. Hoare logic uses inference rules to derive correctness properties; a checked proof remains conditional on the rule semantics. A program may be well-typed and still compute the wrong tax, wrongly classify a scientific state, or leak information through an authorized but unsafe API.

## Worked reconstruction and independent check

Take expression 1+2 and derive its integer type using an addition rule. Try true+2 and show why the rule rejects it, rather than coercing values silently. For a simple counting loop write an invariant and a decreasing rank, then separate termination evidence from postcondition correctness. Describe what a proof checker must trust and how a human could reconstruct the derivation.

## Limitations, falsification, and invalid use

This edition presents proof obligations and finite examples, not a certified general-purpose compiler, theorem prover, or formal verification of the full ATLAS runtime. Source code and proof text are independently auditable, but a formal kernel has not been trusted or reviewed.

## Cross-domain meaning

Agent evidence receipts may eventually carry proof objects, but those require explicit semantics and a host-owned verifier before operational use.

## Source orientation and recoverability

- [MIT OpenCourseWare, Mathematics for Computer Science](https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/) — original publisher bytes unavailable in this package.
- [Stanford Encyclopedia of Philosophy, Computability and Complexity](https://plato.stanford.edu/entries/computability/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.



---


# Bibliographic source access and edition caveats

# Computation Atlas — source register

Primary-source preservation level: **L0/L1 only**. This first release does not include verified original publisher bytes. Author-site CC BY licenses and publisher editions may differ; never merge rights states.

| Source | Inspected extent | Rights / offline gap |
|---|---|---|
| [NIST-DADS](https://www.nist.gov/publications/dictionary-algorithms-and-data-structures) | publisher_page_inspected; original bytes not archived; Publisher description and dictionary scope; original DADS site hosts fundamental algorithm definitions | U.S. federal agency site; exact per-item reuse rights not determined; original bytes absent |
| [ODS](https://www.opendatastructures.org/) | publisher_site_inspected; original bytes not archived; Author site states the text and source code are under a Creative Commons Attribution license; distinctions between author site and AU Press edition matter | Author site CC BY statement; separate AU Press edition is CC BY-NC-ND 2.5 CA; do not assume same license across editions; original bytes absent |
| [MIT-MCS](https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/) | publisher_resource_inspected; original bytes not archived; Open textbook resource describing proof methods, graphs, induction, counting and probability | Check original MIT OCW attribution and license before redistribution; original bytes absent |
| [MIT-6006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) | publisher_course_page_inspected; original bytes not archived; Publisher course description and lecture list covering algorithms, data structures, graph paths and dynamic programming | MIT OpenCourseWare course terms apply; no lecture PDFs mirrored; original bytes absent |
| [MIT-6006-2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) | publisher_course_page_inspected; original bytes not archived; Course lecture list includes graph, optimization, dynamic programming and complexity topics | MIT OCW rights apply; original PDFs not archived; original bytes absent |
| [SEP-CTURING](https://plato.stanford.edu/entries/church-turing/) | scholarly_page_selected_sections_inspected; original bytes not archived; Selected technical scope about informal effectivity and formal machine models | Stanford Encyclopedia original text copyright; only original explanation retained; original bytes absent |
| [SEP-COMPUTABILITY](https://plato.stanford.edu/entries/computability/) | scholarly_page_selected_sections_inspected; original bytes not archived; Selected technical scope about halting undecidability and diagonal arguments | Scholarly article remains copyrighted; bibliographic reference only; original bytes absent |
| [PY-FLOAT](https://docs.python.org/3/tutorial/floatingpoint.html) | official_docs_selected_section_inspected; original bytes not archived; Selected public reference on binary64 approximation, rounding and math.fsum | PSF documentation terms apply; no original documentation bytes retained; original bytes absent |
| [PY-FRACTIONS](https://docs.python.org/3/library/fractions.html) | bibliography_link_only; no original bytes; Bibliographic pointer for exact rational representation and Fraction semantics | PSF documentation terms apply; content not verified line by line; original bytes absent |
| [PY-MATH](https://docs.python.org/3/library/math.html#math.fsum) | bibliography_link_only; no original bytes; Bibliographic pointer for compensated summation behavior | PSF documentation terms apply; original bytes absent |
| [SCIPY-BISECT](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html) | official_docs_selected_section_inspected; original bytes not archived; Selected documentation requires continuity and opposite signs for classical root bracketing | SciPy documentation rights retained; original bytes absent |
| [SCIPY-OPT](https://docs.scipy.org/doc/scipy/reference/optimize.html) | official_docs_selected_section_inspected; original bytes not archived; Selected table of root finders and convergence distinctions | SciPy documentation rights retained; original bytes absent |
| [SCIPY-CSPATH](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html) | bibliography_link_only; no original bytes; Bibliographic pointer for an independent numerical graph implementation | SciPy documentation rights retained; original bytes absent |
| [MIT-COMPUTE](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) | publisher_course_page_inspected; original bytes not archived; Publisher course description about modeling algorithms and data across scientific domains | MIT course CC BY-NC-SA terms may apply; no video or text mirrored; original bytes absent |
| [NIST-FIPS180](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) | bibliography_link_only; no original bytes; Bibliographic standards pointer for SHA-2 digest interpretation; hash not proof of authorship | Original standard not mirrored; status and version must be independently checked; original bytes absent |

## New v0.2 source cards — public scopes only

### MIT-6046

- URL: https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/
- Inspected scope: Official lecture-note index covers minimum spanning trees, FFT, randomized algorithms, flow, union-find, NP-completeness, approximation and compression
- Rights caveat: MIT OCW course terms; no PDF mirrored
- Original publisher bytes archived: **no**. Independent methods review: **no**.

### MIT-1806

- URL: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/
- Inspected scope: Official course syllabus covers elimination, pivots, matrix rank, null spaces and factoring A=LU
- Rights caveat: MIT OCW course terms; no textbook bytes mirrored
- Original publisher bytes archived: **no**. Independent methods review: **no**.

### LAMPORT-1978

- URL: https://lamport.org/pubs/time-clocks.pdf
- Inspected scope: Author-hosted paper abstract covers happened-before partial orders and logical clocks; original ACM copyright remains with publisher
- Rights caveat: ACM 1978 rights; citation and original paraphrase only, no paper mirrored
- Original publisher bytes archived: **no**. Independent methods review: **no**.

### PY-DECIMAL

- URL: https://docs.python.org/3/library/decimal.html
- Inspected scope: Official Python documentation describes decimal contexts, precision, flags and exact/inexact traps; current documentation version is mutable
- Rights caveat: PSF documentation license applies; no source text mirrored
- Original publisher bytes archived: **no**. Independent methods review: **no**.

### AWS-IDEMPOTENCY

- URL: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
- Inspected scope: Official article by Malcolm Featonby describes caller-provided intent IDs, atomic provider idempotency sessions and late-request semantics
- Rights caveat: AWS documentation retains original copyright; no text or PDF mirrored
- Original publisher bytes archived: **no**. Independent methods review: **no**.

### NIST-FIPS203

- URL: https://csrc.nist.gov/pubs/fips/203/final
- Inspected scope: Official final standard published 2024-08-13; planning note 2025-11-17 identifies errata for later correction; three ML-KEM parameter sets
- Rights caveat: NIST primary publication status/errata check; original bytes not mirrored
- Original publisher bytes archived: **no**. Independent methods review: **no**.



# Known scientific and engineering omissions

# Computation Atlas — coverage and gaps v0.1.0

| Area | Chapters | Reference status | Main unresolved debt |
|---|---:|---|---|
| Algorithms | 11 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Architecture | 2 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Complexity | 2 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Foundations | 4 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Information | 2 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Mathematics | 1 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Methodology | 3 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Numerics | 5 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Statistics | 1 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |
| Verification | 3 | Original derivations + reconstructable procedures | Original primary-source copies, independent expert review, advanced topic depth |

**Not yet comprehensive:** quantum algorithms, full compiler architecture, complexity completeness proofs, numerical linear algebra at scale, distributed fault models, external-memory algorithms, randomized algorithms, program refinement calculus, verified machine arithmetic, hardware reproducibility. Related domains have their own future slots in the 30-domain roadmap.

**No automatic routing or Bitwork integration is included.**

