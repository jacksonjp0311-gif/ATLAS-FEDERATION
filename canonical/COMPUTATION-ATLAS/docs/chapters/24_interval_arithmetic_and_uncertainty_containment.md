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
