# Computation Atlas v1.0.0 — Executable and Conceptual Casebook

**32 total investigations**: 16 original v0.1 cases and 16 additional bounded cases. All scenarios are authored, not samples from production devices, LLMs or external measurements.

## New casebook decision points
### 17. kruskal-cut-proof
- Passed: True
- Observation: `{"selected_edge_indices": [0, 3, 1], "total_cost": 4.0, "components": 1, "status": "minimum_spanning_forest_for_declared_graph", "limitations": ["Only declared undirected graph, not hidden network costs", "Finite tested inputs are not a universal proof of source interpretation"]}`
- Limit: Undirected graph and weights are supplied

### 18. flow-cut-equality
- Passed: True
- Observation: `{"max_flow": 5.0, "min_cut_capacity": 5.0, "source_side": [0], "augmentations": 3, "flow_cut_gap": 0.0, "status": "flow_cut_match_under_declared_network", "limitations": ["Capacities are caller-supplied; no external effects", "Float precision and near-zero residual tolerance may matter for extreme inputs"]}`
- Limit: No real transport capacity tested

### 19. exact-linear-residual
- Passed: True
- Observation: `{"solution": ["2", "1"], "exact_residual_zero": true, "status": "unique_solution_for_supplied_rational_matrix", "limitations": ["No floating-point conditioning estimate or large sparse solver", "Input conversion from binary float preserves its rounded value"]}`
- Limit: Only supplied rational coefficients

### 20. fft-inverse
- Passed: True
- Observation: `{"max_err": 5.721188726109833e-18}`
- Limit: Not a physical resonant-mode measurement

### 21. linear-convolution-no-alias
- Passed: True
- Observation: `{"out": [2.0, 5.0, 8.0, 3.0]}`
- Limit: Pad for linear convolution

### 22. concentration-conditional
- Passed: True
- Observation: `{"radius": 0.13581015157406195}`
- Limit: Independence is not established by code

### 23. concurrent-events
- Passed: True
- Observation: `{"a": [1, 0], "b": [0, 1]}`
- Limit: No real message or authorized event

### 24. happened-before-receive
- Passed: True
- Observation: `{"prior": [1, 0], "merged": [1, 2]}`
- Limit: Vector clocks do not authenticate messages

### 25. json-key-canonical-subset
- Passed: True
- Observation: `{"equal": true}`
- Limit: Not a complete RFC 8785/JCS implementation

### 26. singular-system-refusal
- Passed: True
- Observation: `{"refused": true}`
- Limit: Uniqueness cannot be asserted

### 27. fft-size-refusal
- Passed: True
- Observation: `{"refused": true}`
- Limit: Only radix-two bounded input

### 28. negative-capacity-refusal
- Passed: True
- Observation: `{"refused": true}`
- Limit: Capacity must be nonnegative

### 29. complexity-claim-not-from-tests
- Passed: True
- Observation: `{"empirical_NP_completeness_claim": false}`
- Limit: Complexity relies on formal reductions and defined input model

### 30. postquantum-reference-not-implementation
- Passed: True
- Observation: `{"ML_KEM_implemented": false}`
- Limit: Read NIST FIPS203 and verify errata before deployment

### 31. source-link-not-local-file
- Passed: True
- Observation: `{"publisher_original_bytes_archived": false}`
- Limit: Bibliographic card is not a recoverable original primary publication

### 32. formal-type-judgment-limited
- Passed: True
- Observation: `{"type_safety_certified": false}`
- Limit: No proof kernel or external code execution was implemented


## Earlier cases

# Computation Atlas: original executable investigations

All cases are constructed mathematical examples; no empirical claims or model quality claims.

## Investigation 01: two-counter halts

**Observation:** `{"status": "halted", "steps": 2, "registers": [0, 0], "pc": 2}`

**Limit:** bounded input program only

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 02: budget is not a nonhalting oracle

**Observation:** `{"status": "unknown_budget_exhausted", "steps": 8, "registers": [8, 0], "pc": 0}`

**Limit:** unknown not nonhalting

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 03: stable sorting

**Observation:** `[["d", 0], ["b", 1], ["c", 1], ["a", 2]]`

**Limit:** one finite input

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 04: leftmost binary insertion

**Observation:** `"leftmost index 0"`

**Limit:** requires sorted input

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 05: graph shortest path certified

**Observation:** `{"A": 0, "B": 2, "C": 1, "D": 3}`

**Limit:** nonnegative weights only

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 06: negative cycle refused

**Observation:** `"negative cycle reachable"`

**Limit:** no finite shortest path

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 07: dependency cycle refused

**Observation:** `"cycle rejection"`

**Limit:** does not prove general workflow liveness

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 08: edit distance

**Observation:** `3`

**Limit:** unit costs and textual units are characters

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 09: knapsack pseudo polynomial

**Observation:** `{"value": 7.0, "indices": [0, 1], "capacity": 5}`

**Limit:** runtime depends on capacity numeric value

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 10: Bezout identity

**Observation:** `[6, -1, -2]`

**Limit:** arbitrary precision integers

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 11: rational enclosure

**Observation:** `["-3", "9/2"]`

**Limit:** requires exact rational endpoints

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 12: bisection interval under declared continuity

**Observation:** `{"interval": [1.4142135605216026, 1.4142135679721832], "estimate": 1.414213564246893, "iterations": 28, "status": "bounded_bracket_under_declared_continuity"}`

**Limit:** caller continuity claim not independently proved

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 13: floating point accumulation risk

**Observation:** `{"naive_left_to_right": 0.0, "fsum": 2.0}`

**Limit:** Kahan not always exact; built-in sum may compensate

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 14: Shannon entropy binary fair

**Observation:** `1`

**Limit:** requires declared probability distribution

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 15: finite certificate catches wrong sort

**Observation:** `"rejected invalid output"`

**Limit:** certificate covers only the inspected input

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.

## Investigation 16: prefix-free code

**Observation:** `"correct prefix decision"`

**Limit:** no optimality claim

Reproduce by calling `python -m computation_atlas`. Check the result independently by deriving expected outputs with the relevant chapter.


## v0.2.0 — Ten additional reproducible investigations

- [Investigation 17: equivalence-class union](investigations/17_equivalence_class_union.md)
- [Investigation 18: minimum spanning forest](investigations/18_minimum_spanning_forest.md)
- [Investigation 19: max flow meets min cut](investigations/19_max_flow_meets_min_cut.md)
- [Investigation 20: exact linear system with rational residual](investigations/20_exact_linear_system_with_rational_residual.md)
- [Investigation 21: FFT round trip](investigations/21_fft_round_trip.md)
- [Investigation 22: zero-padded linear convolution](investigations/22_zero_padded_linear_convolution.md)
- [Investigation 23: bounded-sample concentration inequality](investigations/23_bounded_sample_concentration_inequality.md)
- [Investigation 24: concurrent vector clocks](investigations/24_concurrent_vector_clocks.md)
- [Investigation 25: message merge creates causal relation](investigations/25_message_merge_creates_causal_relation.md)
- [Investigation 26: canonical JSON key order](investigations/26_canonical_json_key_order.md)

The 26 combined cases are **original constructed examples**, not empirical measurements or a learning benchmark. All listed caveats are retained in the machine casebook.

