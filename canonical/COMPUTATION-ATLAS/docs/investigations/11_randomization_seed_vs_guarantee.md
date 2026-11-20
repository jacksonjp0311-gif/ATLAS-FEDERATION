# Investigation 11 — A reproducible random seed is not a probabilistic guarantee

**Origin:** original methodological example, not a sample of an external AI system. A pseudorandom algorithm can produce the same sequence when seeded, permitting exact debugging. That does not make its estimates unbiased, guarantee independent tasks or establish cryptographic unpredictability. A Las Vegas method always returns a correct answer under its assumptions but has variable cost; a Monte Carlo method may use a fixed budget and accept a bounded probability of wrong output. Repeating one seed a thousand times does not generate a thousand independent trials.

**Adversarial check:** compare randomized pivot choices under two seeded policies on a skewed input. Record the exact generator and seed; state the input distribution and any independence assumption before applying a probability bound. The algorithmic claim and an observed finite run are separate types of evidence.

**Source scope:** MIT 6.046J randomization lectures; original text not mirrored.
