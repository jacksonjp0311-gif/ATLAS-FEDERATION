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


# Computation v0.2 — fourteen new reproducible investigations

These additions run in pure Python from `computation_atlas.v02_cases.casebook_v02(node_root)`. They cover exact linear systems, inconsistent and underdetermined systems, quadratic cancellation, Horner evaluation, SCC membership, Kruskal MST and disconnected forest, Floyd-Warshall path and negative cycle, modular inverses, Huffman code lengths, deterministic reservoir sampling, and verified preservation of pinned licensed source bytes.

All case examples are constructed. None demonstrates a world-changing discovery or improvement in AI model intelligence. Re-run and inspect `tests/test_advanced.py`, including tampered-byte refusal tests.
