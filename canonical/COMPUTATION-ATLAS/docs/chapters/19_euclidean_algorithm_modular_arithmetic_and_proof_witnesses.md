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
