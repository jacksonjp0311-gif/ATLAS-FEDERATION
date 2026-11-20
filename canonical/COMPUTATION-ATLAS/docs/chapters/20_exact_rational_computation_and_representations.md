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
