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
