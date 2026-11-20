# 5 Missing outcomes and honest sensitivity analysis

An observed pass rate answers a question about observed outcomes. It does not automatically answer a question about every assigned unit. This chapter uses exact binary bounds to make that distinction visible without inventing a missingness model.

## The complete-case comparison

Suppose the treated arm has100 units,60 observed outcomes and48 observed successes. Its observed-only success rate is48/60=0.80. The control arm has100 units,90 observed outcomes and54 successes, for54/90=0.60. The observed-only difference is+0.20.

Now consider every assigned unit. For treated units, at least48 succeeded; at most48+40=88 succeeded. The full treated-arm risk is therefore within[0.48,0.88]. For controls it is within[0.54,0.64]. Subtracting endpoints gives a full-arm difference within

`[0.48-0.64, 0.88-0.54] = [-0.16, 0.34]`.

The sign is not determined by the supplied counts. This is not a confidence interval. It is an exact arithmetic range for unknown binary outcomes among these counted units, allowing all assignments to those unknown outcomes. Sampling uncertainty and treatment confounding are separate questions. The tool returns `bounded_not_identified` rather than choosing a midpoint or filling missing outcomes with zeros.

## Why bounds are useful even when wide

Wide bounds tell an investigator what missing information costs. To narrow them, a reason is needed: recover additional outcomes, justify restrictions on missing outcomes, or adopt and defend a statistical model. The chosen restriction belongs in the result. The software does not infer that missing treated units are comparable to observed treated units merely because their available baseline columns look similar.

For the example, write r1 for the success probability among the40 missing treated outcomes and r0 for that among the10 missing controls. The difference becomes

`(48+40*r1)/100 - (54+10*r0)/100 = -0.06 + 0.40*r1 - 0.10*r0`.

This explicit two-parameter surface lets a reviewer ask which assumptions produce benefit, no effect or harm. At r1=0 and r0=1 the difference is−0.16; at r1=1 and r0=0 it is+0.34. A selected scenario is an assumption, not a measurement.

## Do not turn missingness labels into observed facts

The inspected multiple-imputation reference explains missingness assumptions and their limitations, including that assumptions about unobserved outcomes cannot generally be decided from observed values alone ([Sterne and colleagues2009, Box1 and discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC2714692/)). This release does not implement multiple imputation. Its source cards explain why completing a dataset is not itself a validity argument; the implemented tool is the narrower binary arithmetic bound.

In an actual causal study, distinguish loss to follow-up, unavailable inspection results, exclusions after assignment, and structurally undefined outcomes. Do not mix all four into one missing flag. Some change the population or outcome definition rather than merely remove a value. Record why each unit disappears and at which point in the time sequence.

## Negative controls are probes, not certificates

A negative-control design uses an exposure or outcome chosen so the target causal pathway should be absent while relevant biases may still appear. The primary source presents this as a way to detect certain confounding and selection problems, not a universal bias-correction formula ([Lipsitch and colleagues2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/)). A null finding does not prove all bias absent: the control may be irrelevant to the suspected mechanism or too imprecisely measured.

For an original manufacturing design proposal, a change in historical inspection scores recorded before a new setting could flag group-composition or data-processing differences. But it would not estimate the new setting's effect and might be a poor control if the old and new groups were selected differently for entirely known reasons. The proposed control needs a rationale, expected null pathway and a stated bias mechanism it can diagnose.

## Sensitivity results must remain separate from estimates

Use the [assumption ledger](../templates/ASSUMPTION_LEDGER.md) to retain each missingness or bias scenario. Do not silently overwrite the primary estimate with a favorable sensitivity setting. Report which conclusions survive a declared plausible range and which change sign. The package does not claim to determine that range from the data alone.

**Related records:** `binary-missing-bounds`, `missingness-assumption`, `imputation-limit`, `negative-control-design`, `negative-control-null`, `uncertainty-ledger`.
