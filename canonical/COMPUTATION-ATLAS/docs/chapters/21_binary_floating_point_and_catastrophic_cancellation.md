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
