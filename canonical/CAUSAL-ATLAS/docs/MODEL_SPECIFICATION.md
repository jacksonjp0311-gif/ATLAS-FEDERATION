# Executable method specification

## Graph operations

Input: a JSON object with `nodes` and `edges`, where an edge `["A","Y"]` states A points to Y. Node names are bounded ASCII identifiers. Duplicate nodes/edges, unknown endpoints, self-loops and directed cycles are rejected. At most 20 nodes and 190 edges are supported.

Separation uses the ancestral-moral-graph criterion. Compute ancestors of queried and conditioned nodes, retain that induced graph, join co-parents and remove direction, then remove conditioned nodes and test connectivity. This yields a graph property, not a truth estimate. Query sets must be nonempty where applicable and pairwise disjoint.

For one exposure, the sufficient back-door check excludes exposure descendants and checks separation after deleting outgoing exposure edges. Candidate sets are drawn only from the caller's observed variables. Minimal-set enumeration is limited to 12 eligible variables. Failure means failure of this sufficient criterion, not general nonidentifiability.

The optional graph oracle compares another implementation rather than importing its code into the runtime. No NetworkX or DAGitty code is vendored.

## Finite binary mechanisms

A BinaryModel has at most 12 nodes. Each node has a complete conditional-probability table. Parent keys use alphabetically sorted parent names; root key is the empty string. Entries give the probability of value one; zero uses its complement.

For each binary assignment, multiply the specified conditional probabilities. Under a fixed intervention, omit the assigned node's original factor and impose its fixed value. Sum over assignments for the requested event and normalize conditional queries. A zero-probability conditioning event is an error. The probability arithmetic uses exact fractions derived from the supplied strings, not floating-point sampling.

The supplied graph is a causal claim, not verified evidence. Missing common causes, changing mechanisms or incorrect tables invalidate external interpretation. An observational Bayesian network is not automatically a causal model.

## Grouped standardization

Rows require `stratum`, `treatment` (integer zero/one), `n`, and `successes`. Counts are validated nonnegative integers and successes cannot exceed n. Explicit nonnegative target weights must sum exactly to one. All positive-weight target strata need nonzero support in both treatments. The result retains the target weights, refuses silent interpolation and supplies no automatic confidence interval.

The returned standardized difference is a descriptive functional until identification assumptions are justified externally. The crude result describes the supplied sample and can refer to a different population than the weighted target.

## Excluded in this edition

No causal discovery, feedback-cycle model, arbitrary code/equation execution, front-door or instrumental-variable identification, sensitivity estimator, time-varying treatment engine, mediation estimator, clinical decision rule, empirical data certification, or automatic source correction monitoring is implemented.
