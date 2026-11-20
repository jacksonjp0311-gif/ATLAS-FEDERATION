# 53. Quantifier scope, compositional meaning, and unknown facts

Natural-language meanings can differ when the same quantifiers take different scope. “Every person read a book” can be interpreted so that each person may have read a different book (∀x∃y) or so that one book was read by everyone (∃y∀x). Neither reading should automatically be selected merely because the sentence has one string. Formal semantics maps a syntactic interpretation to a logical formula and then evaluates that formula in a declared model. Syntax, world knowledge and discourse can influence which reading is appropriate; the truth value of a formula is a separate question.

## Reconstruction

For nonempty finite sets A of agents and B of objects and a relation R⊆A×B, compare `∀a∈A ∃b∈B R(a,b)` against `∃b∈B ∀a∈A R(a,b)`. Let A={Ada,Bea} and B={X,Y}. If Ada read X, Bea read Y, and the cross-pairs are explicitly false, then the first formula is true and the second false. These judgments are relative to the stated model; they do not report anything about real people. Under an open-world record, an unreported pair is not automatically false.

The `quantifier_scope_contrast` method uses Strong Kleene truth values T,F,U. Existential quantification is T if any witness is T, F if every candidate is F, otherwise U. Universal quantification is F if any counterexample is F, T if all are T, otherwise U. This avoids inventing a false statement merely because a corpus failed to record a relation. Inputs must declare known positives and negatives separately, and contradictory declarations are refused. The method returns truth under each **supplied** scope; it never guesses which scope a human speaker intended.

## Scientific boundary

Quantifiers in natural language include proportions, numerals, negative concord, scope islands and context-dependent domain restriction not covered by this miniature first-order example. Native-speaker judgments and discourse experiments are needed for a specific language. A formal semantic proof is valid under its logical premises; it is not automatically a psychological model of comprehension.

**Source:** Stanford Encyclopedia of Philosophy, *Generalized Quantifiers*, revised 2024, selected public exposition; publication link in the source register.
