# 51. Formal languages, automata and the difference between recognition and understanding

A *formal language* is a set of sequences over a declared alphabet. Finite-state automata give exact recognition procedures for regular languages; the model's alphabet can consist of characters, phonological segments, tokens or other explicitly encoded symbols. This is a mathematical object, not a universal explanation of natural-language grammar. People frequently understand sentences with recursive and long-distance dependencies that a particular regular finite-state model cannot represent. A finite automaton can nevertheless model lexical patterns, restricted morphological systems and parts of speech-processing pipelines when its coverage is described honestly.

## Reconstruction

Let Q be a finite state set, Σ an alphabet, q0 a start state, F accepting states, and δ⊆Q×(Σ∪{ε})×Q a transition relation. A nondeterministic finite automaton accepts input x1…xn when some run reaches a state in F after consuming all input. The ε-closure C(S) contains all states reachable from S by zero or more ε moves. Start in C({q0}), and after token xi replace S with C({q':(q,xi,q')∈δ for q∈S}). A finite closure computation terminates because each state can enter a visited set at most once per closure. This constructs acceptance under a specified machine; it cannot certify speaker grammaticality, meaningfulness, or discourse appropriateness.

The reference `finite_acceptor` supports at most 100 named states, 500 transitions, and 100 supplied tokens. It checks duplicate and malformed transitions and returns the state set after each symbol. The output `accepted_by_declared_machine` is intentionally not named *grammatical*. For a transparent exercise use states A,B,C and transitions A—x→B, B—y→C, with C accepting. The sequence x,y is accepted; y,x is not. Adding an ε-transition from A to B permits input y. A machine that rejects a novel but grammatical sentence illustrates the error of elevating model coverage into universal language judgment.

## Scientific boundary

The mathematical closure algorithm is fully reproducible; the selection of a real-language grammar, lexical units, and the treatment of morphology are empirical linguistic decisions. Phonotactics, syntax and pragmatics can require distinct representations. A measured model comparison needs held-out speaker and corpus validation, not only agreement with authored strings. An unsuccessful finite search can prove rejection only for the declared finite transition system, not that no human language admits the sequence.

**Sources:** prior Atlas language grammar chapters; Universal Dependencies v2 and foundational theory of finite automata (see Computation Atlas). The executable grammar is original and constructed, not imported from a speech corpus.
