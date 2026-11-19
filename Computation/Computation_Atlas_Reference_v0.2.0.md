# Computation Atlas — Research Reference v0.2.0

**Preservation-first, offline reference.** Contains 46 chapters, 30 reproducible investigations, and source-linked records. Eleven algorithms are not evidence of universal computability, and 17,589 checks are constructed software comparisons rather than scientific peer review. First authenticated original software assets comprise two MIT-licensed program files and their license. No copied peer-reviewed paper is archived.

## Historical v0.1 research material (immutable original chapters)

# Computation Atlas — Reconstruction Reference v0.1.0

An original, offline-readable research and teaching atlas. This is domain 6 of the planned 30-domain foundational collection.

**Read this without proprietary services:** Python 3.10+, plaintext Markdown, JSON Lines, and explicit proofs. The text stands independently of code; code demonstrates only bounded declared models.

**Evidence:** Cited publisher materials are bibliographic pointers, not original publisher files; source acquisition is explicitly incomplete. No scientific result below has been independently reviewed or demonstrated in a physical lab.

## How to use the manual

Every chapter contains: foundations, mathematical specification, proof or derivation, reconstruction procedure, failure boundaries, and a source locator. These are separate because a runnable script is not a mathematical proof and a reference URL is not an offline source archive.

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


---

# Version 0.2.0 original mathematical extensions

# 35. Exact linear systems and the difference between algebra and measurement

**Domain:** numerics  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

A linear system A x = b is not just an instruction to run a solver. It is a claim about the domain of coefficients, the rank of a matrix, and the meaning of its right-hand side. Over rational numbers the determinant, row rank, and equality are exact algebraic objects. For measured data, entries of A and b are uncertain, and rational exactness cannot remove that uncertainty. Model the matrix as m rows and n columns, and explicitly distinguish inconsistent systems (no x), underdetermined systems (many x), and unique systems (rank n with consistent equations). A rectangular system can have a unique solution; a singular square matrix cannot. A displayed floating-point answer to Ax=b is not a proof of uniqueness unless rank and error are justified.

## Constructive procedure and derivation

Use Gauss-Jordan elimination over Fraction. Scan columns from left to right, find a nonzero pivot in the rows not yet used, swap the pivot row upward, normalize by its nonzero pivot, and eliminate that column from all other rows. Exact zero pivot means algebraic zero, not a floating-point tolerance. After elimination inspect any row whose coefficients all vanish: if its RHS does not vanish, declare inconsistency. Otherwise rank less than n means free variables. Only rank n yields a unique vector. For measured floating-point systems use scaling and a condition analysis; explicitly carry uncertainty instead of converting measurements to exact fractions and treating the result as physically exact.

**Central relationship:** `A x=b; rank(A)=n and consistent iff unique x`.

## Worked investigation and counterexample

A=[[2,1],[1,-1]], b=[4,1] gives x=(5/3,2/3). The pair of equations x+y=2 and 2x+2y=5 is inconsistent; replacing 5 by 4 makes it underdetermined. A 2×2 matrix with determinant ε may have a mathematically unique solution but extremely sensitive floating-point behavior when ε is small. Try A=[[1,1],[1,1+10^-12]] and perturb b: measured uncertainty can dominate the result.

## Reconstruct this without ATLAS software

Reconstruct a solver by hand: write the augmented matrix, record each swap, divide by a pivot, eliminate, track rank, and substitute the returned rational vector into the original equations. Reject NaN, infinite input, over-large matrices, and exact-coefficient interpretations of noisy instruments. The reference implementation caps dimensions at eight and returns no arbitrary free-variable parameterization; such a limit is an implementation scope, not a claim that bigger systems are impossible.

## Evidence and preservation boundaries

Upstream record locators: `NIST-DADS`, `MIT-MCS`, `SCIPY-LA`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 36. Quadratic formulas and catastrophic cancellation

**Domain:** numerics  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

The algebraic roots x=(-b ± sqrt(b²−4ac))/(2a) are mathematically correct over exact real arithmetic, but one sign may subtract nearly equal floating-point numbers. That can erase almost all significant digits in one of the two roots. The issue is algorithmic stability, not an inherent lack of a real solution. An operation's relative conditioning and an algorithm's rounding propagation are distinct quantities. Report both coefficient domain and the ability to form the discriminant without overflow or underflow; mathematical equivalence of formulas does not imply numerical equivalence.

## Constructive procedure and derivation

Let Δ=b²−4ac and q=−(b+sign(b)sqrt(Δ))/2. Then x1=q/a and, when q≠0, x2=c/q from the identity x1 x2=c/a. This form avoids cancellation in the small root on many common inputs. Treat a=0 as a different linear problem; Δ<0 as no real roots; q=0 as a repeated zero root. Bounds on absolute error still depend on coefficient condition, floating-point range, and whether Δ itself can be formed accurately. The reference does not implement a fully scaled coefficient normalization or interval root enclosure.

**Central relationship:** `D=b^2-4ac; q=-(b+sign(b)*sqrt(D))/2; roots q/a and c/q`.

## Worked investigation and counterexample

For x²+10^8x+1=0, naive evaluation of the small root loses information because sqrt(10^16−4) rounds close to 10^8. The stable q formula returns approximately −10^-8 and −10^8. Substitute the roots back into the polynomial to check a residual, but small residual does not automatically imply small forward error in ill-conditioned cases. This is an instructive difference between backward and forward error.

## Reconstruct this without ATLAS software

Reconstruct the q formula from Viète's product of roots. Show explicitly when q=0 and prove the product identity under the assumed arithmetic. Try three test families: well-separated roots, nearly repeated roots, and discriminant overflow. The last must refuse rather than silently return a fabricated value. Never translate a successful double-precision computation into a universal proof for all coefficient magnitudes.

## Evidence and preservation boundaries

Upstream record locators: `PY-FLOAT`, `PY-MATH`, `MIT-MCS`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 37. Horner evaluation, rounding models, and error certificates

**Domain:** numerics  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

A polynomial p(x)=c0 x^n+c1 x^(n−1)+...+cn is an exact symbolic object. Computing its value on a finite machine requires an evaluation order. The naive formula separately constructs powers, often multiplying and rounding more times than necessary. Horner's scheme rewrites the polynomial as (...((c0 x+c1)x+c2)...)+cn. This reduces multiplications to n, but even Horner may suffer severe cancellation or overflow for certain coefficient and argument ranges. Never treat one numerically successful output as an exact algebraic proof.

## Constructive procedure and derivation

Initialize y=0 and repeat y←y·x+c from the leading coefficient through the constant term. Algebraic induction proves that after processing k coefficients, y represents the prefix polynomial. A standard floating-point analysis uses fl(a∘b)=(a∘b)(1+δ) with |δ|≤u when the operation is normal, finite, and correctly rounded; the resulting bound uses γ_k=ku/(1−ku) for ku<1. This model needs explicit qualifications regarding subnormals, fused multiply-add, overflow, and input representation. Our function returns a floating result, not a machine-checked rounding certificate.

**Central relationship:** `p(x)=(((c_0 x+c_1)x+c_2)...)+c_n`.

## Worked investigation and counterexample

For p(x)=(x−1)^3 with coefficients [1,−3,3,−1], Horner at x=2 gives 1. At x near 1, terms nearly cancel and relative error may be enormous even when the absolute residual is small. Compare a rational Fraction evaluation to floating-point Horner on x=1+2^-24 to see the difference between mathematical and represented inputs.

## Reconstruct this without ATLAS software

To reconstruct, derive the nested form by repeated factoring, then write the loop invariant after each coefficient. Count n multiply-add rounds. Compare results against arbitrary precision and NumPy for bounded random cases and construct a cancellation counterexample. Do not promise a tight error bound unless arithmetic semantics, rounding mode and non-overflow constraints are also supplied.

## Evidence and preservation boundaries

Upstream record locators: `PY-FLOAT`, `PY-MATH`, `MIT-MCS`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 38. Strong connectivity as an equivalence relation

**Domain:** algorithms  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

A directed graph is not fully described by undirected connected components. Two vertices belong to the same strongly connected component precisely when each is reachable from the other. This mutual-reachability relation is reflexive (zero-length path), symmetric by definition, and transitive by concatenating directed paths, so it partitions the vertex set into equivalence classes. The component condensation graph is acyclic; otherwise its cycle would imply the components could be merged. This structural theorem is useful in dependency graphs, program analysis, state machines, and network reliability.

## Constructive procedure and derivation

An easily reconstructable finite method computes a reachability set from each vertex using depth-first search, then groups nodes u,v with u∈Reach(v) and v∈Reach(u). That approach is straightforward, though slower than Tarjan's or Kosaraju's O(V+E) algorithms. Its complexity is roughly O(V(V+E)) with adjacency lists. It is intentionally restricted to at most 100 nodes, enabling transparent inspection of every reachability relationship.

**Central relationship:** `u~v iff u reaches v AND v reaches u`.

## Worked investigation and counterexample

For edges a→b, b→a, b→c, the components are {a,b} and {c}. A topological order of the condensed graph exists, but the original graph itself has a directed cycle. If an algorithm declares all three vertices strongly connected because c is reachable from a, it has confused one-way reachability with mutual reachability.

## Reconstruct this without ATLAS software

Reconstruct the partition by calculating three reachable sets, checking mutual membership, proving that groups do not overlap, then drawing the condensation edges. Reject undeclared target vertices instead of silently creating phantom states. For larger graphs use Tarjan or Kosaraju and compare their output to the pedagogical oracle; this implementation does not claim large-scale algorithmic efficiency.

## Evidence and preservation boundaries

Upstream record locators: `NIST-DADS`, `MIT-6006-2020`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 39. Minimum spanning forests, cuts, and disconnectedness

**Domain:** algorithms  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

An undirected weighted graph may or may not be connected. A minimum spanning tree exists only in a connected graph. A minimum spanning forest chooses a minimum-cost tree for each connected component. Its total weight is the sum across components. Negative edges do not invalidate the combinatorial problem, whereas directed edges change it to a different optimization problem. An edge list without declared vertices cannot represent isolated nodes accurately, so the vertex set is part of the input specification.

## Constructive procedure and derivation

Kruskal's algorithm orders undirected edges by increasing weight, breaking ties deterministically, and adds an edge exactly when its endpoints lie in different current components. The disjoint-set union structure maintains that equivalence. The cut property justifies a minimum-weight edge crossing a valid cut as safe in some optimum; exchange arguments establish correctness of the greedy selection. Sorting costs O(E log E) and near-constant amortized union/find operations require path compression and union by size or rank.

**Central relationship:** `minimize sum_{e in F} w_e subject to acyclic spanning forest`.

## Worked investigation and counterexample

For edges a-b of weight 1, a-c of weight 2, b-c of weight 7, the spanning tree weighs 3. If d is declared as a vertex but has no incident edge, the result is a forest with two components; reporting it as one spanning tree would be false. A negative-weight edge should still be selected if it joins components, because it reduces the total.

## Reconstruct this without ATLAS software

Reconstruct by writing the disjoint-set parent relation after each candidate edge, recording accepted and rejected edges, and checking acyclicity and component count. Compare total weight to NetworkX on constructed finite instances. These tests validate the implementation on samples; they do not prove every possible weighted graph has been tested.

## Evidence and preservation boundaries

Upstream record locators: `NIST-DADS`, `MIT-6006-2020`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 40. All-pairs shortest paths and negative-cycle refusal

**Domain:** algorithms  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

The all-pairs shortest-path problem asks for the least total path weight between every ordered pair of vertices. A negative edge is not inherently invalid; a reachable negative cycle makes the infimum of some path lengths unbounded below, and a finite shortest-path value is then undefined for affected pairs. A global all-pairs implementation can conservatively refuse a graph with any negative cycle. Missing paths must be represented as unreachable, not cost zero or an invented large number.

## Constructive procedure and derivation

Floyd-Warshall maintains d_k(i,j), the best path from i to j whose internal vertices lie among the first k labels. Its recurrence is d_k(i,j)=min(d_{k-1}(i,j),d_{k-1}(i,k)+d_{k-1}(k,j)). Initialize diagonal costs to zero and direct edges to their minimum weights; absent edges remain infinite. In-place updates work for the standard recurrence in the absence of negative cycles. After all k, any negative d(i,i) witnesses a negative cycle. Our implementation uses exact Fraction arithmetic for small graphs and None for unreachable pairs.

**Central relationship:** `d_k(i,j)=min(d_(k-1)(i,j),d_(k-1)(i,k)+d_(k-1)(k,j))`.

## Worked investigation and counterexample

For a→b=1/3 and b→c=1/6 with direct a→c=1, the shortest path a→c has exact cost 1/2. For a→b=−2, b→a=1, a negative cycle of total −1 exists; the method returns negative_cycle rather than an arbitrary finite distance. The implementation does not isolate the exact affected pairs in such a graph; it refuses globally.

## Reconstruct this without ATLAS software

Reconstruct the recurrence by dividing candidate paths into those that avoid k and those that pass through k. Evaluate the three-vertex table by hand and compare with an independent graph library. State explicitly whether input edge costs are exact rationals or measurements; passing Fraction(float) does not recover an unknown physical rational value.

## Evidence and preservation boundaries

Upstream record locators: `NIST-DADS`, `MIT-6006-2020`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 41. Bézout witnesses and modular inverse construction

**Domain:** mathematics  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

An integer a has a multiplicative inverse modulo m>1 exactly when gcd(a,m)=1. A modular inverse x satisfies ax ≡ 1 (mod m). The extended Euclidean algorithm constructs coefficients s,t with as+mt=gcd(a,m). When that gcd is one, the residue of s modulo m is an inverse; when it exceeds one, no inverse exists. Existence is a theorem, not a heuristic based on repeated trial. The gcd and coefficients are exact integer quantities; there is no floating-rounding problem if arithmetic is unbounded.

## Constructive procedure and derivation

Run Euclid on remainders r0=a,r1=m. Track coefficients s0=1,s1=0 such that each remainder is a linear combination of a and m. At each step quotient q=floor(r0/r1) and replace r0,r1 by r1,r0−q r1, with the same update to coefficients. The invariant r_i=a s_i+m t_i is proved by induction. When r1=0, r0 (up to sign) is gcd(a,m). Return inverse s0 mod m only for gcd ±1; otherwise return no_inverse.

**Central relationship:** `a*s+m*t=gcd(a,m); a*s mod m=1 iff gcd=1`.

## Worked investigation and counterexample

For a=3,m=11, 3·4≡1 (mod11), so inverse is 4. For a=4,m=8 no inverse exists because gcd is 4. For a negative residue, e.g. −3 modulo 11, the inverse 7 satisfies −21≡1 (mod11). The published educational source snapshot in this edition provides a second implementation for careful study but is not executed as trusted external code.

## Reconstruct this without ATLAS software

Reconstruct a Bézout table by hand and verify as+mt=g. Then compute ax %m to validate the resulting inverse for several positive and negative integers. Reject modulus m≤1 in this bounded reference implementation; other modular conventions may define degenerate cases differently, so record them explicitly before reuse.

## Evidence and preservation boundaries

Upstream record locators: `MIT-MCS`, `PYALGO-EGCD`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 42. Huffman prefix-code lengths and recoverability

**Domain:** information  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

A prefix-free binary code assigns bit strings so that no codeword begins another. This allows a decoder to identify symbol boundaries without separators. The Kraft inequality states that prefix-code lengths ℓ_i satisfy Σ 2^{-ℓ_i} ≤ 1. Given positive symbol weights, Huffman's algorithm yields a prefix tree minimizing total weighted codeword length among binary prefix codes. The code-length distribution does not by itself specify a unique encoded bitstream: tree shape, tie rules, symbol ordering, and canonical assignment must be recorded for byte-for-byte recovery.

## Constructive procedure and derivation

Initialize a forest of weighted leaves. Repeatedly remove the two smallest weights, join them under a new parent of combined weight, and repeat until one tree remains. Each join increases every leaf depth in both joined subtrees by one. An exchange argument shows that two smallest-frequency symbols can occupy sibling leaves in some optimal code, reducing the problem recursively. Our method returns lengths, not bit patterns. It selects a deterministic merge order for ties but stops short of an archival encoder/decoder.

**Central relationship:** `sum_i 2^(-length_i)<=1`.

## Worked investigation and counterexample

For frequencies a:100, b:3, c:3, a has length 1 and b,c have length 2; the weighted length is 112 bits per 106 symbol instances. If a code generator accidentally assigns both symbols the same bit pattern, length optimality would not ensure decodability. File-format survival requires a complete encoder, decoding rules, and end-of-stream/length metadata.

## Reconstruct this without ATLAS software

Reconstruct a three-symbol tree by hand, count depths, test the Kraft bound, then enumerate all small-length assignments to confirm optimal weighted length on toy inputs. The reference demonstrates optimality of lengths for positive finite weights but is not a production compression format and does not establish hardware storage reliability.

## Evidence and preservation boundaries

Upstream record locators: `NIST-DADS`, `MIT-6006-2020`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 43. Uniform reservoir sampling, pseudorandomness, and reproducibility

**Domain:** statistics  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

A stream of n items may be too large to retain entirely. Reservoir sampling of a single item can give each input position probability 1/n using constant storage. The statement concerns a probability model and independently uniform random choices, not an observed uniform histogram from a handful of seeds. A deterministic pseudorandom generator is valuable for repeatable experiments; it is not a cryptographic source of secrecy or unpredictable physical randomness.

## Constructive procedure and derivation

Initialize the reservoir with the first item. For the i-th item, i≥2, replace the sample with probability 1/i. By induction, a prior item has survival probability ((i−1)/i) times 1/(i−1)=1/i, while the new item has direct probability 1/i. The implementation uses Python Random(seed) and randrange(i), retaining one item and not requiring storage proportional to n. This deterministic replay is for teaching and testing, and cryptographic sampling requires different primitives and threat assumptions.

**Central relationship:** `P(reservoir_item_i survives step n)=1/n`.

## Worked investigation and counterexample

Consider stream [A,B,C,D]. At step 2 replace with probability 1/2; at step 3 replace with probability 1/3; at step 4 replace with probability 1/4. Each original item has probability 1/4 at the end under ideal uniform draws. A 4,000-seed empirical histogram may fluctuate; it cannot prove the mathematical guarantee nor characterize unknown generator bias at every scale.

## Reconstruct this without ATLAS software

Reconstruct the inductive proof and replay a fixed seed to reproduce a single result. Test an empty stream as invalid input. Record generator version, seed, stream order, population definition, and sampling model before comparing experiments. This model does not perform privacy-preserving, cryptographic, or adversarially unpredictable selection.

## Evidence and preservation boundaries

Upstream record locators: `PY-RANDOM`, `MIT-MCS`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 44. Authenticated open-source originals and license boundaries

**Domain:** methodology  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

A scientific archive must distinguish an authored explanation, a bibliographic pointer, a copied publisher file, and a locally verified original artifact. A hash of a file proves byte identity relative to that digest, but not the correctness of the material, its originality, or the legal rights to redistribute it. Git object names bind file bytes under Git's blob serialization; they do not certify the social or scientific reliability of the repository. The license and historical revision must be preserved together with the exact source file. Per-item rights can override broad website assumptions.

## Constructive procedure and derivation

For the first preservation pilot, pin a GitHub repository to a full commit hash and read its directory tree. Acquire two original small educational source-code files and the MIT LICENSE.md from that same revision. Independently calculate SHA-1 of the bytes prefixed with b"blob <length>\0" and compare to the published Git blob ID; also record SHA-256 for local corruption detection. Retain original file names, source URLs, commit, byte lengths, license file and verification receipt. Exclude any third-party document whose rights cannot be established.

**Central relationship:** `GitBlobSHA1=SHA1(b"blob "+len+b"\0"+raw_bytes)`.

## Worked investigation and counterexample

The archived repository is TheAlgorithms/Python at commit 30507bbe41397065728167fb09aa820f9fce8dc7. Two code files and LICENSE.md match pinned published blob IDs. This is an authenticated software provenance pilot, NOT the acquisition of research articles or validation of a general algorithm theorem. NIST DADS licensing explicitly excludes some third-party CRC Press definitions, so indiscriminate mirroring would be unjustified.

## Reconstruct this without ATLAS software

Reconstruction drill: disconnect from the network, read ACQUISITION_RECEIPT.json, compute the local hashes, compare all three files, and reproduce the simplest code example from your own trusted interpreter. Then alter one byte and confirm the audit fails. Preserve the source rights note and never execute externally obtained code automatically. The rest of the 390 original bibliography cards remain unarchived under this rule.

## Evidence and preservation boundaries

Upstream record locators: `NIST-DADS-RIGHTS`, `PYALGO-JUMP`, `PYALGO-EGCD`, `PYALGO-LICENSE`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 45. Cost models, adversarial inputs, and performance extrapolation

**Domain:** complexity  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

Asymptotic complexity describes the growth of a cost function under a chosen model, not a promise of observed speed on an arbitrary machine. O(n log n) hides constants, memory locality, data representation, caching and scheduler effects. Worst-case, expected-case, amortized and high-probability guarantees answer different questions. A deterministic proof of an algorithm's bound does not give a runtime forecast in seconds without hardware and workload measurements. Conversely, a fast benchmark does not prove an asymptotic bound.

## Constructive procedure and derivation

State a unit-cost RAM model, define input size in bits or items, count primitive operations, and derive a recurrence or charging argument. Comparison-based sorting requires Ω(n log n) comparisons in the worst case for distinct items, while counting sort can be linear in n plus key range because its model uses bounded integer keys. Union-find's almost-constant amortized bound requires particular heuristics. Floyd-Warshall's triple loop costs O(V³) and O(V²) storage; the reachability-based SCC reference intentionally sacrifices asymptotic efficiency for explanatory transparency.

**Central relationship:** `T(n)=O(n log n) under declared comparison cost model, not wall-clock`.

## Worked investigation and counterexample

A bubble-sort implementation may beat a sophisticated sort on three items because overhead dominates, yet scale poorly at 10^6 items. A hash table with adversarial collisions can deteriorate to long chains. One observed microbenchmark does not determine a distribution of adversarial inputs. When inputs are drawn from an unknown workload, record the sampling mechanism before inferring any average-case behavior.

## Reconstruct this without ATLAS software

Reconstruct the cost with two columns: mathematical operation count and real measured resource consumption. For small n, count exact comparisons or graph relaxations from a trace. For physical machines, repeat trials, report variance, machine configuration, and energy if measured. Avoid extrapolating a performance ratio as proof of universal algorithmic improvement.

## Evidence and preservation boundaries

Upstream record locators: `MIT-6006-2020`, `NIST-DADS`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.


---

# 46. Cross-domain survival: from algorithms to scientific instruments

**Domain:** methodology  
**Version:** 0.2.0  
**Scope:** Original mathematical reconstruction, not external experimental certification.

## Foundational statement and precise assumptions

A preserved algorithm matters only if future readers can recover the representation of its inputs, the semantics of its outputs, and the scope of its proof. A string edit-distance value depends on character encoding and the definition of insertion/deletion cost; a shortest path depends on edge weights, directionality and negative cycles; numerical roots depend on coefficient representation. Scientific instruments add calibration uncertainty, timestamping, sampling and synchronization. The common ATLAS record contract can carry these qualifications without claiming a router or agent has used them successfully.

## Constructive procedure and derivation

A preservation-grade chapter should include formal definitions, a constructive procedure, proof assumptions, one valid example, one failure counterexample, exact source citations, a reconstructable test suite, resource limits and rights. Retain original source bytes with license when permitted. Preserve the distinction between offline recoverability and scientific peer review. Cross-node relations may point to other versioned records in the complete federation, but standalone packages must omit or explicitly package dependencies they cannot resolve.

**Central relationship:** `preserved_claim=definition+assumptions+sources+derivation+tests+limitations`.

## Worked investigation and counterexample

The Computation v0.1 package had five valid cross-node relationships that broke standalone loading. The standalone export now contains only internally closed relations, while the full collection retains the bridges. The v0.2 methods add an authenticated original-software pilot. Neither repair says that every needed scientific source can be reconstructed after network loss; the preservation debt ledger remains open.

## Reconstruct this without ATLAS software

Reconstruct from a clean disconnected machine: extract the archive, verify inventories, install the wheel, run tests, read an original source file and its license, and verify its SHA-256 and Git blob SHA-1. Repeat on a different operating system before claiming portability. Only after all 30 domains are built should routing, Bitwork integration, and end-to-end model evaluations be added.

## Evidence and preservation boundaries

Upstream record locators: `MIT-COMPUTE`, `NIST-FIPS180`, `NIST-DADS`. Each locator is versioned in the source register. Original educational content and source quotations are not interchangeable. Where original GitHub software bytes are archived, Git blob and SHA-256 matching authenticate those bytes relative to the pinned repository; they do not validate the code, license globally, or establish a new scientific discovery. Outside the three-file pilot, upstream original publisher files remain unavailable in this archive. No independent mathematical expert review has been completed.
