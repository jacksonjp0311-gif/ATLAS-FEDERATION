# 9 Instrumental variables: distinguish the invitation from the treatment

## Begin with two decisions, not one coefficient

Suppose a factory wants to evaluate optional operator training. Supervisors offer priority places by a documented lottery, but some invited operators do not attend and some non-invited operators obtain training elsewhere. There are two interventions: offering the place and receiving training. Define `Z` as the offer, `D` as attendance, and `Y` as the outcome at a prespecified time. Assignment to an offer and attendance are not interchangeable exposures. A comparison by actual attendance can reintroduce the selection problem the lottery was intended to avoid.

This is a proposed investigation, not a description of James's workplace. Before using it, document who was eligible, the assignment mechanism, the time order, the training received, the outcome definition, spillovers and missing outcomes. Ask whether an invitation also changes supervision, motivation, access to equipment or reporting. Those routes matter even when assignment was genuinely random.

The literature distinguishes an instrument-induced local effect from a population average. The inspected Angrist–Imbens working paper gives conditions and a ratio expression for the effect among units whose participation changes with the instrument. Its monotonicity condition is individual-level, not merely a positive average first stage. See [IA1991](../SOURCE_REGISTER.md#ia1991), §3 Conditions 1–2 and Theorem 1; §4, printed pp. 5–10. The following finite construction is original to this Atlas and makes the target distinction explicit.

## Derive the ratio from a specified population

Write `D(0), D(1)` for attendance under each offer and `Y(0), Y(1)` for the outcome under each treatment. For this derivation stipulate independent assignment of `Z`, no interference, consistent treatment versions, and exclusion: the offer changes the outcome only through attendance. Then

`Y given Z=z = Y(0) + D(z)[Y(1)-Y(0)]`.

Taking the difference of the two assignment-arm expectations gives

`DeltaY = E[(D(1)-D(0))(Y(1)-Y(0))]`.

Let `pC` be the share who attend only when offered, and `pF` the share who attend only when not offered. With their respective mean treatment effects `tauC` and `tauF`,

`DeltaY = pC*tauC - pF*tauF`, and `DeltaD = pC-pF`.

If nobody is a defier (`pF=0`) and some people respond to the offer (`pC>0`), the ratio `DeltaY/DeltaD` equals `tauC`. Never-takers and always-takers contribute no attendance change. Their treatment effects need not be zero; the offer comparison simply does not reveal them. This derivation explains why the ratio is not automatically the effect of training everyone.

The code's `iv_population` takes all potential values as supplied synthetic inputs. It cannot fill in both potential outcomes or both potential attendance choices for a real operator. Its compliance labels describe stipulated model types, not people identified by one observed attendance decision.

## A numerical target mismatch worth retaining

Use shares 0.30 never-takers, 0.20 always-takers and 0.50 compliers. Set their treatment effects to −0.10, +0.10 and +0.30 respectively. The fully specified population average is `0.30*(-0.10)+0.20*0.10+0.50*0.30 = 0.14`. The offer increases attendance by 0.50 and outcomes by 0.15, so the ratio is 0.30. Both numbers are correct for different questions.

A result packet should therefore name the instrument, treatment, complier definition, population and period. It must not replace “effect for people induced to attend by this offer” with “effect for all operators.” A different offer can induce a different set of attendees. Transport to the whole factory requires further information about treatment-effect heterogeneity and population composition.

## Challenge the design before calculating

Independence asks whether the offer is independent of potential attendance and outcomes, perhaps conditional on prespecified baseline strata. Exclusion asks whether any outcome pathway bypasses attendance. Relevance asks whether attendance changes. Monotonicity rules out opposite-direction responses for the instrument contrast being used. Consistency asks whether “training” and “offer” refer to sufficiently well-defined actions. None is established by the four means alone.

Record an evidence entry for each condition: mechanism documents, baseline timing, alternative pathways, and unresolved objections. A balanced table of observed characteristics is not proof about all unmeasured causes. A positive average attendance change does not exclude a mixture of compliers and defiers. A random invitation does not prohibit a direct motivation effect.

For a sample, `wald_summary` calculates the ratio of supplied means and retains their origin. Its required `minimum_first_stage` is an operator-selected arithmetic guard. It is not an estimated first-stage F statistic, a calibrated strength threshold or a p-value. Sample uncertainty remains unimplemented in this teaching tool.

## Deliver the right answer type

Return the offer contrast and attendance contrast even when their ratio is unsupported. They are different quantities with different interpretations. Explain whether the ratio is a numerical summary, a stipulated-model effect, or an effect justified by a separately reviewed design. Report the first stage, not just the ratio. For an unresolved design, ask for the specific missing evidence rather than decorating the calculation with a confidence claim.

Continue with [failure analysis](10_iv_failures_and_sensitivity.md) and the [training-offer investigation](../investigations/04_training_offer.md). No real experiment is contained in this chapter.
