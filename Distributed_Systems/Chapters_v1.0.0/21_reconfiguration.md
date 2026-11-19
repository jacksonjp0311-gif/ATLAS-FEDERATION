# 21 — Membership changes and cross-configuration quorum safety

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 21**

## Scientific question

What breaks if an archive cluster silently changes voter sets?

## Mathematical and engineering foundation

For a fixed voter configuration C, majority quorums overlap because their cardinalities exceed half of |C|. During a configuration change, a majority of C_old need not intersect a majority of C_new if voters are added or removed without a joint protocol. E.g. old={A,B,C}, new={D,E,F}; both have quorum size 2 but share no voter. A safe reconfiguration procedure must enforce overlap of committing quorums across the transition or use a proven joint-consensus/log-entry rule, with terms and activation order persisted.

## Derivation and formal invariant

For any two allowed decision quorums Q_old and Q_new, a necessary intersection constraint is Q_old ∩ Q_new != empty for conflicting values. A joint-config rule may require separate majorities from both old and new voter sets. However, this numerical condition alone does not prove reconfiguration correctness: leadership terms, log match, commit index and stale configuration fencing need independent proof.

## Worked constructed investigation

Worked example: old voters A,B,C and new C,D,E. Old majority A,B and new majority D,E are disjoint despite one common *member* C. Therefore mere overlapping membership does not imply all quorums intersect. A design that casually overwrites the voter list can split decisions. Preserve old configuration until an agreed transition entry is committed and recovered.

## Reproduction procedure and negative control

Reconstruction exercise: enumerate all old/new voter majority subsets, compute minimum intersection and report disjoint witnesses. Use a historical log with original voter-set revision and deployment epochs; treat all output as a necessary numerical precondition, not a deployed algorithm.

## Assumptions, evidence class and known failures

No executable dynamic-membership consensus or Raft joint-consensus implementation is provided; this chapter is a documented hazard and acceptance gap.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `docs/chapters/21_reconfiguration.md`. Bibliographic source card: `distributed-systems-atlas:source:RAFT_DISSERTATION2014` at exact revision `49ce4c200d48777a71b082959fe23660bea955f7fd613711bcf2f9bc2c04c888`. Full source locator: https://github.com/ongardie/dissertation. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.
