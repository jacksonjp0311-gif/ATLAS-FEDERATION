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
