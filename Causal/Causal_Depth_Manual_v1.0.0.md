> Public derivative notice: the affected historical numeric example has been removed; the unchanged original remains privately preserved.

# CAUSAL ATLAS — scientific reference depth manual v1.0.0

**James Paul Jackson · 12 November 2026 · bounded research reference edition**

> Source-linked explanations, assumptions, methods, examples and unresolved questions. A v1 content release is not proof of empirical identification, independent scientific review or complete coverage of causal inference.


---

# 1 Define the question before choosing an estimator

A causal question is a comparison between specified interventions in a specified population over a specified time. A column named `treatment` is not that specification. In a factory example, “use the new process” might mean changing a machine setting, retraining operators, or assigning work to a different machine. Those are different interventions even when a database records them under one label. This chapter supplies an original investigation workflow; it does not certify any actual process.

## The object we want to learn

Let A be a binary intervention and Y a pass indicator measured after a fixed follow-up. Write Y(1) and Y(0) for the outcomes under the two interventions. An average treatment effect in target population T is

`ATE_T = E_T[Y(1) - Y(0)]`.

The target population is part of the definition. It is not a cosmetic label appended after fitting a model. The observed treated group, the entire study sample, and a future production mix can have different distributions of relevant conditions. They need not have the same average effect.

Our original heterogeneous-effect example makes this explicit. Suppose the benefit is +0.10 for easy jobs and +0.40 for difficult jobs. A target containing 80% easy jobs has effect `0.8*0.10 + 0.2*0.40 = 0.16`. A target containing 80% difficult jobs has effect `0.2*0.10 + 0.8*0.40 = 0.34`. No estimator failed and no measurement changed. The question changed. These calculations are reproduced by `python -m causal_atlas investigations`.

## Design a comparison people can interpret

For an actual investigation, record eligibility, each intervention, assignment, time zero, follow-up, outcome measurement, target contrast, and analysis plan before inspecting which analysis gives a preferred result. The target-trial literature supplies a source anchor for organizing these decisions: [Hernán and Robins 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/), named portions recorded in the source register. Our blank [study specification](../templates/TARGET_STUDY.md) turns these decisions into fields without filling them with fictitious observations.

An implementable production question might be: “Among eligible batches entering one specified machine family during a declared period, what would the difference in final pass probability be if every batch were assigned the new validated setting rather than the existing setting, with the same inspection definition and a fixed follow-up?” That wording still needs domain review. It is much better defined than “did quality improve?” because an analyst can now identify excluded jobs, incompatible outcomes, and changes in intervention version.

## Keep time zero coherent

Consider this original timeline. A batch becomes eligible at entry; process assignment occurs at entry; inspection follows. If the analyst instead calls a batch ‘treated’ only when it remains in production for three more shifts, membership now depends on future survival or continuation. Comparing that selected group with all control batches does not answer the entry-time assignment question. The fix is not a special coefficient: first repair the group definitions and timeline.

The source-level principle is that eligibility, assignment and follow-up start must be aligned; future information used to define treatment can introduce selection. See [Hernán and colleagues 2016, §2 and §3](https://pmc.ncbi.nlm.nih.gov/articles/PMC5124536/). This Atlas does not implement trial emulation, censoring weights or adherence-effect estimation. It supplies the design questions and a boundary check.

## Separate assignment from receipt

An assignment effect asks about the policy of assigning the process, including nonadherence as it occurs. An effect of actually following the process asks a different question. Replacing assignment with receipt in an analysis can require additional assumptions because receipt may depend on information collected after assignment. Record which question is intended; do not silently switch when compliance is disappointing.

Likewise, interference and multiple intervention versions must be considered rather than buried in a generic consistency label. One machine's treatment may affect a shared line or operator schedule. This node has no interference estimator. A genuine spillover problem must remain a design limitation or be routed to a future explicitly defined method, not forced into the binary point-treatment calculator.

## Completion check

Before estimating, an investigator should be able to name the unit, interventions, outcome window, target mix, and comparison. Unknown answers belong in the assumption ledger. A precise question does not establish identification, but it prevents a precise calculation from answering the wrong question.

**Related records:** `estimand`, `target-population-example`, `coherent-entry`, `survivor-restriction`, `time-labelled-variables`.

---

# 2 Identify an effect before estimating it

An estimator converts observed inputs into a number. Identification explains why a particular function of observed information would equal the desired causal quantity under stated assumptions. These jobs must stay separate. A highly accurate numerical routine can estimate an association that answers no causal question.

## A counterexample an AI must retain

The new exact example constructs two binary models with identical observations. In Model A, a fair hidden variable U sets both A and Y: `A=U` and `Y=U`. In Model B, A is fair and `Y=A`. Both produce half their observations at `(A=0,Y=0)` and half at `(A=1,Y=1)`. Thus the observed difference between treatment groups is one in both.

Under an intervention setting A, Model A leaves U and Y unchanged, giving causal effect zero. Model B changes Y, giving effect one. The code enumerates the joint distributions and interventions with the existing finite-model engine. It does not merely hard-code the two effects.

This is an original nonidentification demonstration for this observation set and these allowed models. It shows why a perfect observed predictor is insufficient by itself. It is not an impossibility claim about every additional experiment or source of information. Random assignment, substantive constraints, or other evidence could distinguish the models.

## What the current graph tools can do

A directed acyclic graph states assumed directional relationships and omissions. The local separation algorithm checks graphical paths. The sufficient back-door checker asks whether a supplied adjustment set contains prohibited treatment descendants and blocks back-door paths in the supplied graph. It does not learn the graph, prove that omitted causes do not exist, or implement every identification criterion. Formal definitions and algorithm anchors remain in the retained [Pearl 2010 source record](https://pmc.ncbi.nlm.nih.gov/articles/PMC2836213/) and DAGitty documentation.

Three small graphs are useful for reasoning:

* `L -> A`, `L -> Y`, `A -> Y`: L is a proposed common cause; suitable adjustment can remove that path under the graph and other identification assumptions.
* `A -> M -> Y`: M lies on the pathway. Blocking it does not generally preserve the total-effect question.
* `A -> C <- Y`: selecting or conditioning on C can open an association absent before selection.

Do not interpret the first pattern as an instruction to adjust for every available baseline variable. Timing is necessary context, not a sufficient selection rule. A pre-exposure variable can have a different graphical role. Write why it belongs in the adjustment set.

## Derive the standardized target

Let L denote a fully specified baseline stratum. Under consistency, conditional exchangeability of the relevant potential outcomes and treatment given L, and positive treatment support in all target-relevant strata,

`E_T[Y(a)] = sum_l E[Y | A=a,L=l] * P_T(L=l)`

when the conditional outcome responses are applicable to that target. To see the logic, average the potential outcome within each stratum, replace its conditional mean with the corresponding treatment-group mean using exchangeability and consistency, then average over the target weights. Moving to a different population requires an additional reason that those conditional responses carry over; target weights alone do not prove transportability.

The implementation accepts explicitly supplied stratum counts and target weights. An unsupported positive-weight stratum is not filled with a guessed rate. The source anchor for conditional randomization and standardization is [Hernán and Robins 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2652882/). The displayed derivation is our own short explanation of the identification substitutions, not a reproduced publication passage.

## Model omissions belong in the result

A graph with `U -> A` and `U -> Y`, where U is unobserved, may have no observed set satisfying this package's sufficient back-door check. The output says exactly that. It must not say every causal question is impossible, nor that a sophisticated estimator automatically solves the hidden-variable problem.

Keep alternative plausible graphs when substantive evidence cannot decide among them. When a conclusion depends on removing an edge, record the evidence for that removal. A data-driven graph candidate is an assumption object to review, not a scientifically authenticated map of the system.

**Related records:** `identification`, `dag-assumptions`, `pretreatment`, `mediator`, `collider`, `no-set`, `observational-equivalence-example`.

---

# 3 Weighting, standardization and what diagnostics can establish

The local tools now compare outcome regression, two inverse-probability weighting conventions and augmented weighting on the same inputs. They require supplied nuisance predictions; they do not fit propensity models. Every output preserves whether the caller described those inputs as a design probability, external prediction, out-of-fold prediction, in-sample fit or synthetic oracle. The label is recorded, not authenticated.

## Two weighting formulas, not one interchangeable number

For individual observations i, let e_i be the supplied probability of A_i=1. The Horvitz–Thompson difference implemented here is

`HT = mean(A_i*Y_i/e_i - (1-A_i)*Y_i/(1-e_i))`.

The Hájek version divides each arm's weighted sum by its own sum of weights and subtracts the normalized means. These quantities can differ in a finite sample. Naming both simply ‘IPW’ loses information needed to reproduce an analysis. [Austin and Stuart 2015, §2.2](https://pmc.ncbi.nlm.nih.gov/articles/PMC4626409/) identifies these estimator conventions; our code states the chosen formula in its result.

The HT expectation identity is short enough to inspect directly. If e(L) is the true conditional treatment probability, then `E[A*Y/e(L) | L] = E[Y | A=1,L]`. The control expression follows analogously. This is an observed-data identity. Equating those conditional means with potential-outcome means additionally needs the causal assumptions from Chapter 2.

## Read the synthetic process example correctly

The retained table has 100 new-process jobs and 100 old-process jobs, with markedly different easy/difficult proportions. With the generating propensities 1/5 for easy jobs and 4/5 for difficult jobs, weighting gives each arm an equal target difficulty mix. The unadjusted difference is −0.26; the standardized and correctly weighted differences are +0.10 in this constructed example.

Those exact equalities are properties of the deliberately chosen counts. In an ordinary sample, a correct propensity model does not force exact finite-sample balance or exact equality to a population effect. The code therefore labels sample estimates separately from population-expectation checks.

## Inspect concentration before interpreting an estimate

An original three-row diagnostic uses arm weights `[1000,2,2]`. Their sum is1004; the largest normalized weight is `1000/1004 = 250/251`, about99.6%. The diagnostic effective sample size is

`ESS = (sum w)^2 / sum(w^2) = 126002/125001`, approximately1.008.

This flags near-total domination by one row. It is not a formal count of independent information, an uncertainty interval, or proof the weights are wrong. Repeated observations, clustering and the study design may invalidate any interpretation based on independent units.

The sample calculator reports propensity extrema, weight totals, maxima, largest normalized weights and one declared covariate's weighted and unweighted mean difference. It does not silently clip. A user who changes weights must label the new analysis and examine its implications; the source discussion of truncation treats it as a bias–variance choice, not an automatic repair ([Cole and Hernán 2008, Weight truncation](https://pmc.ncbi.nlm.nih.gov/articles/PMC2732954/)).

## Balance is not identification

A zero difference in a measured covariate mean is not sufficient. Two weighted groups can have the same mean but different distributions. For an original counterexample, values `[0,2]` and `[1,1]` both have mean1 but different spread. If the outcome responds nonlinearly to this covariate, means alone can miss a relevant imbalance. The reference source recommends examining richer observed-covariate balance diagnostics ([Austin and Stuart 2015, §4.1](https://pmc.ncbi.nlm.nih.gov/articles/PMC4626409/)).

Nothing about balancing observed variables demonstrates the absence of unobserved common causes. The software's diagnostic therefore explicitly states that it does not test unmeasured confounding. Missing support is also not fixed by a large weight: there must be actual or defensibly modeled information for the target question. Zero supplied probabilities are rejected for this bounded estimator rather than replaced by arbitrary small constants.

## Interface boundary

`estimate` takes individual rows with unique IDs. Aggregate counts must be expanded or analyzed using the existing grouped standardization interface, not misrepresented as single equally weighted people or jobs. Clustered and longitudinal records require other designs; a duplicated ID is rejected, not treated as another independent unit.

**Related records:** `ipw-estimator-choices`, `ipw-expectation-identity`, `balance-audit`, `truncation-tradeoff`, `weight-concentration`, `sample-versus-population`.

---

# 4 Augmented weighting with a derivation and falsification cases

Let m_a(L) be a working conditional outcome mean and g(L) a working treatment probability. The sample implementation uses this residual-form score:

`phi = m1(L)-m0(L) + A/g(L)*(Y-m1(L)) - (1-A)/(1-g(L))*(Y-m0(L))`.

Its estimate is the sample mean of phi. The models are supplied by the caller. There is no automatic nuisance fitting, cross-fitting, statistical interval or empirical correctness claim in this release.

## Why this form is useful to audit

The score consists of a predicted contrast plus a treated residual correction minus a control residual correction. When every outcome and both outcome predictions are increased by the same constant, residuals and contrasts remain unchanged. Swapping treatment labels, exchanging m0 and m1 and replacing g with1-g should negate the result. These are testable invariants. They are not evidence that a real causal model is correct, but they catch common algebraic and implementation errors.

The literature includes a correction notice for the control-group augmentation in an AIPW tutorial ([Kurz article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8793316/); [publisher corrigendum](https://journals.sagepub.com/doi/10.1177/0272989X221075672)). The notice and exact inspected scope are retained separately. We derive and test the residual form rather than asserting that every web-rendered equation or the publisher's analysis code has been independently verified. The publisher's assurance about its code remains an attributed statement.

## Derive the conditional bias

In a fully stipulated synthetic population, write e for the generating treatment probability and mu_a for the generating outcome mean in a stratum. Conditional expectation of the score is

`m1-m0 + e/g*(mu1-m1) - (1-e)/(1-g)*(mu0-m0)`.

Subtract the true stratum contrast `mu1-mu0`. Collecting the treated and control residuals gives

`bias(L) = (e-g) * ((mu1-m1)/g + (mu0-m0)/(1-g))`.

Average this expression with the explicit target-stratum probabilities. If g=e, the conditional bias vanishes for arbitrary working outcome means. If both m_a=mu_a, it vanishes for arbitrary interior working g. If neither condition holds, the terms need not cancel. This is an algebraic expectation result for the declared model, not a statement that fitted nuisance functions are correct or that any one sample returns the exact target.

Causal interpretation adds the identification assumptions; large-sample inference with fitted functions adds further regularity and estimation requirements that are not implemented here. “Doubly robust” does not mean protected against an unmeasured common cause, an undefined treatment, an inapplicable target population, or arbitrary misuse of reused training outcomes. The inspected source discusses the conditional model robustness rather than a universal guarantee.

## Four exact experiments

The original population has two equally common job difficulties, generating propensities0.2 and0.8, and process outcome means `(0.8,0.9)` for easy and `(0.2,0.3)` for difficult work. The target ATE is+0.10.

| Working inputs | Population score result | Interpretation |
|---|---:|---|
| Both correct | +0.10 | Baseline algebra check |
| Correct propensity, wrong outcome means | +0.10 | One conditional bias factor is zero |
| Correct outcome means, wrong propensity | +0.10 | Both outcome residual means are zero |
| g=0.5 everywhere, m0=0.5 and m1=0.6 everywhere | −0.26 | Both wrong; bias is −0.36 |

The last row is not a failure hidden by a test pass. The test passes **because it correctly reproduces the known failure of those working models**. The numerical result is kept beside the true synthetic effect and the bias identity, so a consumer cannot mistake successful code execution for successful causal identification.

## What supplied predictions do and do not allow

A file of m0, m1 and g values is enough to compute the score. It is not enough to evaluate how those values were obtained. An actual analysis must retain training populations, feature timing, loss functions, fit diagnostics, fold assignment if applicable, transformations, model revisions and sampling design. The `nuisance_origin` field makes missing provenance visible but cannot verify a caller's claim of out-of-fold fitting.

Do not choose the estimate that looks most favorable when OR, HT, Hájek and AIPW disagree. Investigate normalization, weights, overlap, modeling, units, target and finite-sample behavior. Report the prespecified primary analysis and separately labeled sensitivity analyses. Agreement across methods also need not reveal a shared identification mistake.

**Related records:** `aipw-method`, `double-robust-limits`, `aipw-correction`, `aipw-residual-identity`, `aipw-bias-identity`, `constant-outcome-test`, `conflicting-method-results`.

---

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

---

# 6 Before and after is not automatically a causal design

The node's main implemented estimators concern a binary point exposure. This chapter adds a bounded two-period arithmetic investigation and distinguishes it from methods not implemented. It is not a replacement for a full panel-data, instrumental-variable or longitudinal analysis.

## A four-mean contrast

Suppose a treated production line changes from0.80 to0.90 pass probability, while a comparison line changes from0.70 to0.75. The before–after difference in the treated line is+0.10. Subtracting the comparison-line change produces

`D = (0.90-0.80) - (0.75-0.70) = 0.05`.

That arithmetic is observable from the four means. To interpret D as the treated line's causal effect, assumptions must connect the comparison line's change with what would have happened to the treated line without the intervention. The implemented function does not validate that connection.

## Put the unobserved trend into the equation

Define delta as the untreated treated-line trend minus the comparison line's untreated trend. Under the rest of the stipulated design, the causal contrast is `D-delta`. With delta0, it is+0.05. With delta+0.08, it is−0.03. Both scenarios have exactly the same four observed means. They disagree about the untreated counterfactual, which is not observed for the treated line after its intervention.

This original sensitivity calculation shows what the identifying assumption does. It does not estimate delta or give it a probability distribution. A plausible range needs substantive evidence about production mix, measurement changes, common shocks, spillovers, selection and timing. More preperiod observations may help examine a design, but a visually flat past difference does not logically determine future untreated differences.

The inspected multi-period difference-in-differences paper states distinct comparison-group, anticipation, overlap and parallel-trend conditions ([Callaway and Sant'Anna, version4, §2.3–2.4](https://arxiv.org/html/1803.09015v4)). The Atlas stores those bounded source claims; the local four-mean function does not reproduce that paper's estimators or inference.

## Why a staggered rollout needs another method

If lines adopt a setting at different times, a unit used as a comparison may already be treated. The treatment effect can also vary by adoption cohort or elapsed time. Collapsing every treated observation into one indicator can change what is being compared. This reference identifies the issue and keeps the multi-period source as an entry point. It does not label a two-period arithmetic result as a validated staggered-adoption analysis.

A future node increment should specify the cohort-time targets, admissible comparison observations, aggregation weights, anticipation window and uncertainty procedure before adding an estimator. The current coverage matrix lists this as limited reference depth, not an implemented capability.

## Time-varying treatment is not repeated point treatment

A variable measured after an initial treatment may affect both later treatment and outcome while itself being affected by the earlier treatment. Treating each row as a new independent person and applying the point-treatment function ignores the history. The inspected weighting source explicitly concerns such histories ([Cole and Hernán2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2732954/)). The present individual-row interface rejects duplicate IDs and makes no longitudinal inference claim.

## What remains deliberately unfinished

Instrumental variables, regression discontinuity, mediation, censoring/survival methods, interference and transportability require their own identification definitions, diagnostics, inference and source review. They are not inferred by a graph search failing to find a back-door set. They remain gaps rather than being represented by a method name and a false completion flag.

For an analyst, the immediate useful action is to describe why ordinary baseline adjustment is inadequate and identify what additional design information is available. The Atlas can preserve that unresolved question without pretending the problem has been solved.

**Related records:** `did-assumptions`, `staggered-comparison`, `did-trend-sensitivity`, `longitudinal-warning`, `scope-maturity`.

---

# 7 Report uncertainty without hiding identification assumptions

Every calculation in this checkpoint is reproducible, but reproducibility alone does not turn it into an empirical causal finding. A report should separate what was observed, what was assumed, what was computed, and which claim that supports.

## Three distinct uncertainty questions

First, sampling uncertainty concerns variability from observing a finite sample under a declared sampling or assignment design. Second, nuisance-model uncertainty concerns the fitted predictions or scores used by an estimator. Third, identification uncertainty concerns assumptions connecting an observed-data function to the causal target. A confidence interval for the first two does not automatically cover violations of the third.

The current sample calculator returns no confidence interval. This is intentional: the file does not establish independent sampling, clustering, prediction-training provenance or a justified variance estimator. Adding a familiar standard-error formula would conceal rather than resolve those missing design inputs. This release is useful as an exact calculation and review tool, not a complete inferential package.

## Use the exact output labels

`computed_conditional_on_inputs` means a computation was performed with the supplied rows. It does not mean treatment was randomized. `synthetic_stipulated_population` means the generating distribution was authored and known. `bounded_not_identified` means an interval of possible values follows from supplied counts, not that a repeated-sampling confidence level was calculated.

The old graph outputs also retain their boundaries: no back-door set found is scoped to the supplied graph and implemented criterion. A graph-validation pass is not an authentication of the causal graph. When preparing model context, preserve these labels rather than shortening them to “verified effect.”

## A report that can be challenged

An original study report should state the target population and intervention; eligibility and follow-up; data origin and exclusions; outcome definition and units; plausible causal structure; the precise identification argument; estimator and normalization; nuisance-model provenance; overlap and balance diagnostics; missingness handling; primary and sensitivity results; and unresolved alternatives. The blank [result report](../templates/RESULT_REPORT.md) makes these fields explicit.

Write the main conclusion at the strength supported by the record. “The standardized difference in the declared target is0.10 under the supplied strata and assumptions” is different from “the process improves every line by10%.” The first may be a computational description; the second adds causal transport and effect-homogeneity claims that the numbers do not establish. For binary probabilities, distinguish a0.10 difference, ten percentage points, a relative risk and a percent change. Do not interchange them.

## Preserve disagreements among analyses

In the synthetic process investigation, crude and adjusted results differ in sign for a documented reason: the job mix is deliberately unbalanced. In the model-failure investigation, two wrong working models produce an augmented result−0.26 even though the stipulated truth is+0.10. Neither disagreement should be discarded. The first illustrates a successful correction under assumptions; the second illustrates that method sophistication does not guarantee success.

An actual analyst does not have access to the true generating means. Agreement between estimators can reflect shared assumptions, while disagreement can reflect finite-sample noise, target changes, normalization, misspecification or bugs. A frozen analysis plan helps avoid choosing a result simply because it supports the desired narrative. Changing the plan is allowed, but it should create a dated exploratory branch rather than silently rewrite the primary question.

## What the test suite establishes

The exact-fraction tests check known answers, invalid inputs and invariances. The separate numerical comparison checks another arithmetic implementation on generated cases. The retained graph comparison checks algorithmic agreement. All are authored development evidence. None is an independently authored held-out AI benchmark, peer review, real-world intervention or calibration of causal confidence.

The proposed learning rubric asks a consumer to distinguish these objects, reconstruct calculations and request missing information. It is development material and can be inspected with the answers. It must not later be described as an unseen benchmark.

**Related records:** `sample-versus-population`, `uncertainty-ledger`, `frozen-analysis-plan`, `conflicting-method-results`, `scope-maturity`.

---

# 8 Build an investigation from evidence, not from an impressive method name

The Atlas contains two kinds of explanatory work: short claims linked to inspected source portions, and original derivations, protocols and synthetic examples. Both are useful, but their evidential roles differ. The source register says which portion was inspected. An abstract check is not a methods audit; a bibliographic page is not a reproduced dataset; an original example is not an experiment.

## A practical use sequence

Begin with the question and data definition, not a search for the most advanced estimator. Read Chapter1 to specify the target. Use Chapter2 to examine the identification argument and alternate graphs. Only then use Chapters3–4 to choose and calculate an observed-data function. Chapter5 handles one explicitly bounded missing-outcome problem; Chapter6 exposes how a trend assumption affects a before–after comparison. Chapter7 controls how the output is described.

For the manufacturing investigator, this creates an actionable path: identify the intervention version; establish that measurements precede or follow assignment as claimed; compare the population mix; state what adjustment removes and what it cannot; investigate missing outcomes; calculate prespecified estimates; and retain evidence against the preferred explanation. There are genuine stopping points. An incomplete assignment history or unsupported target stratum is not solved by adding context length.

## Reusable context should preserve the reasoning conditions

A useful package for “did the process change help?” should contain the target definition, relevant method records, source links, data constraints, assumptions and limitations. A result should retain whether its numbers came from actual observations, an authored case or a completely specified probability model. Relationships such as `qualifies` bind methodological claims to these limits.

This checkpoint adds reference content and relations through the existing common contract. It does not add navigation algorithms, train a language model, or invoke Bitwork. The shared runtime remains unchanged. Exact source-linked records remain authoritative; the human chapter is a guide to reading them, not a substitute evidence source for unsupported claims.

## Corrections stay visible

The AIPW tutorial's correction is stored as its own source card and a bounded review record. The local residual formula is derived and tested independently of the visual rendering of a publisher equation. This is a small example of the broader rule: a later clarification must not disappear merely because an earlier source was already indexed. The original eight source cards and34 old records retain their exact revisions in this release; new relations add context without rewriting old bytes.

No external full publication, participant dataset or figure has been mirrored. URLs, author/version metadata, inspected locators, original short capsules and our own examples provide the current evidence path. Raw-source archival capture and independent source review remain separate future tasks.

## Build depth without pretending to finish the field

The [coverage matrix](../COVERAGE_MATRIX.md) distinguishes implemented tools, worked reference depth, limited summaries and absent topics. It is deliberately not a percentage score: one source card on a large subject does not imply a fixed amount of completeness. Future work should be selected by representative questions that the current material cannot answer.

The next substantial gaps are real documented data reanalysis with reusable rights, inference under fitted nuisance models, experimental designs beyond simple assignment, and deeper quasi-experimental and longitudinal methods. New domains are not opened merely because the present node acquired more files. Causal remains the active build until its declared reference scope is substantively developed; final system deployment, desktop testing and independent evaluation are tracked separately.

**Related records:** `evidence-first-investigation`, `scope-maturity`, `aipw-correction`.

---

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

---

# 10 Instrumental variables: failures, sensitivity and identification limits

## Do not confuse a calculable ratio with a defensible effect

The instrument route can fail in several different places. If the instrument does not change treatment, division is undefined. If it changes treatment only slightly, perturbations in a small numerator or denominator can dominate the ratio. If it affects outcomes through another path, exclusion fails. If some units respond in the opposite direction, the ratio can become a signed mixture rather than a complier average. These are distinct problems; one diagnostic cannot clear all of them.

Staiger and Stock's weak-instrument research analyzes why conventional approximations can be unreliable when instrument–treatment relationships are weak. The Atlas inspected the introduction, not every theorem or an implementation of their inference procedures. See [SS1997](../SOURCE_REGISTER.md#ss1997), pp. 557–559. Our small-denominator guard is a computational choice, not a replacement for that statistical analysis.

## Direct-path contamination: an exact constructed example

Reuse the population in Chapter 9, whose true complier effect is 0.30. Add an outcome improvement of 0.05 from the invitation itself for every type: perhaps the synthetic mechanism includes extra attention independently of actual training. Now the offer contrast is 0.20, while the attendance contrast remains 0.50. The ratio becomes 0.40. Arithmetic is correct, but interpreting it as the training effect introduces a 0.10 error.

For this specified additive mechanism,

`DeltaY = theta*DeltaD + gamma`,

where `gamma` is the direct contribution to the assignment contrast. Thus

`theta(gamma) = (DeltaY-gamma)/DeltaD`.

If the investigator assumes `gamma` lies between 0 and 0.05, the scenario range is [0.30, 0.40]. The bounds are conditional on the supplied interval and the additive decomposition. They are neither estimated from the four means nor a confidence interval. They do not cover arbitrary dependence violations, heterogeneous direct effects with a different target, or missing-outcome mechanisms by magic.

`exclusion_sensitivity` preserves the input bounds, signs, first stage and equation. When the denominator is negative it orders the resulting endpoints correctly. It never clips an uncomfortable estimate to a convenient range. When the denominator is zero or fails the declared operational guard, the result remains unresolved.

## Defiers can reverse a ratio even when every type benefits

Construct three types: 0.40 compliers with effect +0.10, 0.30 defiers with effect +0.90, and 0.30 never-takers with effect +0.20. Take the offer to be independent and exclusion to hold within this model. The first stage is `0.40-0.30=0.10`, which is positive. The reduced form is `0.40*0.10-0.30*0.90=-0.23`. The ratio is −2.30 even though every individual type has a positive treatment effect and the population mean effect is +0.37.

This does not refute the local-effect theorem. It violates one of its conditions. The numerator is a signed effect mixture, and the denominator subtracts the shares of oppositely responding types. The common record links the ratio example to the monotonicity qualification so a future consumer cannot retrieve the impressive negative number without its cause.

A ratio outside the possible range of a binary-outcome average is a warning in this constructed example, not a universal rule proving which empirical assumption failed. Sampling error can also produce out-of-range estimates. Never use clipping to conceal an identification problem.

## Weak numerical support is not evidence of a large effect

Take treatment-arm means 0.200 and 0.201, so the first stage is 0.001. Let the outcome contrast be 0.0003. The ratio is 0.30. An additive perturbation of just 0.001 to that outcome contrast changes the ratio to 1.30. This is a deterministic sensitivity illustration, not a repeated-sample distribution or a weak-IV test.

Three separate outputs matter: the small first stage, the selected refusal threshold, and the absence of sampling inference. A threshold of 0.005 rejects this ratio. A threshold of zero permits the arithmetic but still does not call it identified. The tool must not silently select a threshold after looking at the result. A strong denominator would not rescue an instrument that directly affects the outcome.

## What an empirical extension must add

Before real use, specify the sampling unit and assignment process, the exact instrument contrast, covariates and missingness rules. Retain both reduced-form and first-stage estimates, their uncertainty and their dependence. Choose an appropriate weak-identification-aware inferential method and compare it to the ordinary approximation. Predefine what happens when the evidence cannot support a useful interval; an unbounded or very wide answer can be more honest than a finite but misleading one.

This version does not implement two-stage least-squares model fitting, Anderson–Rubin tests, generalized method-of-moments estimators, cluster-robust covariance or instrument selection. Naming these methods is not claiming support. The bounded deliverable is exact finite-model reasoning, supplied-mean ratios and explicit direct-contribution sensitivity.

Use [IV_DESIGN_REVIEW.md](../templates/IV_DESIGN_REVIEW.md) to document the study, and attach the finite-model counterexamples to any explanation of why the assumptions matter.

---

# 11 Regression discontinuity: learn at a boundary, not everywhere

## Identify an actual rule

A score threshold can create a useful comparison only when it belongs to the assignment mechanism. Suppose a maintenance program is assigned when an inspection score reaches 50. Define the score as it existed before assignment, the threshold, the eligible equipment, the intervention and a fixed outcome window. Retain any exceptions, rerating, rounding, overrides or other changes at the same cutoff. A visually convenient breakpoint chosen after seeing outcomes is not the documented rule in this proposal.

Cattaneo and Titiunik distinguish continuity-based and local-randomization interpretations, as well as sharp and fuzzy designs. The inspected source portions are §2.1–2.2, pp. 824–828. See [CT2022](../SOURCE_REGISTER.md#ct2022). This Atlas's implemented calculation is a local-line point estimate; it does not establish either identification framework from a dataset.

## Continuity gives a target at the cutoff

Let `X` be the running score and `c` the threshold. With sharp receipt `D=1[X>=c]`, the observed right-side limit concerns treated outcomes and the left-side limit concerns untreated outcomes. A continuity argument compares their limits at the same value `c`, not their means over the entire treated and untreated populations. Its target is a treatment effect at that boundary under the design's assumptions.

For an original example, take the untreated response near zero to be `1+2x` and the treated response to be `6-x`. The boundary values are 1 and 6, so the cutoff effect is 5. Farther away, their difference changes with `x`. Claiming a constant benefit of five everywhere would add an assumption not present in these curves.

The separate local-randomization framework treats assignment within a declared neighborhood as having a justified randomization structure. It is not obtained merely by using a small bandwidth. The source's finite-window assumptions and the limiting continuity assumptions answer related but different questions. This release does not implement randomization inference or window selection.

## The implemented weighted-line calculation

For each side use `u=(x-c)/h` with a caller-selected positive bandwidth `h`. Include rows satisfying `abs(x-c)<h`; assign `x=c` to the right. Choose either uniform weights or triangular weights `w=1-|u|`. Fit an intercept and slope separately on each side by minimizing the weighted sum of squared residuals.

Define `S0=sum(w)`, `S1=sum(w*u)`, `S2=sum(w*u*u)`, `T0=sum(w*y)` and `T1=sum(w*u*y)`. With `Delta=S0*S2-S1*S1`, the fitted boundary intercept is

`a=(S2*T0-S1*T1)/Delta`.

The scaled-coordinate slope is `(S0*T1-S1*T0)/Delta`; divide by `h` for the slope per score unit. The reported jump is `a_right-a_left`. This two-by-two weighted-line solution is an original explicit derivation of the implemented arithmetic. Fraction arithmetic avoids roundoff for the bounded input class; it does not eliminate scientific uncertainty.

The equivalent weight on observation `i` in the intercept is `w_i*(S2-S1*u_i)/Delta`. These weights sum to one and their weighted score sum is zero. Some can be negative because the boundary intercept is an extrapolated local-line value. The tool reports them rather than silently clipping them. Kernel-weight effective sample size is a concentration diagnostic, not the number of independent causal observations.

The local-polynomial construction and bandwidth/inference distinction are described in the primary [CCT2014](../SOURCE_REGISTER.md#cct2014) paper, pp. 2296–2297. Its bias-corrected uncertainty procedure is not implemented here. Returning a plausible line fit is not equivalent to delivering a defensible confidence interval.

## Fuzzy uptake changes the interpretation again

When crossing the threshold changes treatment receipt from a probability below one to another probability, compute both an outcome jump and a treatment-probability jump. Their ratio is a local Wald-type quantity. A local complier interpretation needs additional assumptions, including an appropriate exclusion condition and monotonicity, beyond calculating both jumps.

The authored case creates seven score levels and ten constructed records per level. Two of ten receive treatment below the threshold, and seven of ten above it. With `Y=2+x/10+3D`, the outcome jump is 1.5 and the treatment jump is 0.5, giving a ratio of 3. This is an exactly specified teaching population. It does not prove that an empirical discontinuity satisfies the mechanism.

`fuzzy_local_ratio` uses the same rows, bandwidth and kernel for both fits. It reports unsupported or tiny first stages according to an explicit guard. Local linear treatment-probability predictions can leave [0,1]; they are flagged, not clipped. The function never reports a confidence interval or automatically labels the ratio a validated local average effect.

## A complete output includes its boundary

Save cutoff units, score timing, bandwidth, kernel, counts, distinct score values, nearest observed score on each side, excluded row IDs and equivalent weights. State whether the target is assignment or receipt, and whether the result is a point summary or justified causal finding. Distinguish the observed data range from the exact boundary. Many repeated scores cannot replace missing score support.

Read the [threshold investigation](../investigations/05_threshold_policy.md) and [validation chapter](12_rd_validation_and_reuse.md) before making a substantive claim.

---

# 12 Threshold design validation: preserve competing explanations

## Start from the mechanism, then examine the data

A discontinuity in an outcome is evidence of a discontinuity in the observed regression function. Deciding what caused it requires a defensible assignment design. Maintain a dated record of the threshold rule, the scoring procedure, who could influence it, when the score was recorded, and whether another policy changed at the same value. A familiar estimator cannot repair an undocumented intervention.

A density discontinuity can provide evidence relevant to sorting of the running variable; McCrary's primary paper develops such a test. Only its publisher abstract and bibliographic description were inspected for this release, not its full proof or implementation. See [MC2007](../SOURCE_REGISTER.md#mc2007). We implement no density test. Counting observations in arbitrary bins should not be relabeled as the McCrary procedure.

The practical guide by Imbens and Lemieux is recorded as an implementation reference, with an abstract-only inspection limit for the newly added card. See [IL2007](../SOURCE_REGISTER.md#il2007). The stronger evidence for detailed statements in this module comes from the specifically inspected full-text source portions and our original derivations, not from claiming that an entire guide was reviewed.

## A perfectly fitted jump can still answer the wrong question

Construct observed curves `Y=1+2X` below zero and `Y=6-X` at or above zero. World A assigns the jump to training. World B gives training zero effect but assigns a second intervention at exactly the same threshold and attributes the jump to it. Both worlds produce the same observed `X,Y,D` table when `D` labels training eligibility. The numerical jump is five in either world.

This is an identification counterexample, not a diagnostic failure in line fitting. Another design, separately changing assignment, or substantive evidence excluding the competing pathway is needed to distinguish the explanations. A perfect residual fit and stable estimates across bandwidths cannot supply that missing information.

A data package should therefore contain an explicit coincident-interventions field, with “unknown” allowed. Do not convert an empty checklist into “none exist.” Unresolved mechanisms should appear next to the numerical estimate, not in a footnote dropped during AI context assembly.

## Bandwidth sensitivity is informative but not a proof

Our curved example has a true limiting jump of five. The left untreated curve uses a small quadratic term and the right treated curve a larger one. Fitting separate local lines with triangular weights gives 4.925 at bandwidth 1, 4.775 at bandwidth 2, and approximately 4.3901 at bandwidth 4. The deterministic curvature bias changes with the fitting window. There is no sampling noise in this construction, so none of these deviations can be called a standard error.

The example does not establish that smaller bandwidth is always preferable. In a real sample a smaller window can have fewer independent units, less support, greater sampling variability or no estimable slope. `bandwidth_sensitivity` reports every requested window, including unsupported ones, and never selects the result closest to a preferred answer.

High-order global polynomial fits are criticized by Gelman and Imbens for sensitivity and inferential behavior; the inspected record here is their primary indexed abstract, not a replication of their simulations. See [GI2014](../SOURCE_REGISTER.md#gi2014). Our implementation deliberately remains a local linear calculator rather than growing a generic polynomial-fitting system. That is a bounded engineering choice, not a claim that all possible alternatives are invalid.

## Distinct support and score precision matter

Three rows at score −1 and three at score +1 do not identify two independent intercept-and-slope regressions. More copies at those same values do not resolve that rank deficiency. The tool requires at least three positive-weight rows and two distinct score values on each side. That minimum permits arithmetic; it is not a recommended statistical sample size.

If an instrument rounds scores to whole units, report the gap around the cutoff and how many distinct values exist. Exact rational arithmetic preserves reported values, not the latent unrounded scores. Do not infer density continuity or a shrinking-bandwidth argument merely because the output is numerically exact. The reference explicitly defers dedicated discrete-running-variable methods and clustered inference.

## Falsification asks where a design could fail

Useful checks should be motivated before seeing the preferred outcome result: prespecified baseline covariates, outcomes the intervention should not affect, known administrative breaks, score-generation records and alternative windows. Their interpretation depends on power, multiple testing, measurement quality and the substantive mechanism. A nonsignificant check is not a certification of all assumptions. The validation discussion in [CT2022](../SOURCE_REGISTER.md#ct2022), §4, treats these as indirect checks.

Separate design validity from estimator precision. A narrow sampling interval cannot rule out a second treatment at the cutoff. Conversely, a well-justified design can be too imprecise for a useful conclusion. The current tools leave uncertainty uncomputed rather than reuse ordinary line-fit standard errors as if they were robust RD inference.

## Human and AI handoff

A reusable package must retain the question, cutoff, treatment definition, local target, selected window, omitted rows, method, assumptions, negative findings and missing information. Include a statement that the generated numerical examples are constructed, not measurements. Source passages remain linked to immutable records; our software derivations and test fixtures have a different origin label.

Use the [threshold review template](../templates/RD_DESIGN_REVIEW.md). The next substantive step is a rights-cleared empirical reanalysis with a separately checked assignment story and appropriate inference. No such empirical study is claimed by this edition, and Materials remains queued.

---

# 13. Target trial emulation: define the experiment before analyzing records

A causal investigation begins with a decision question, not an estimator. An observational database contains a mixture of past decisions, measurements, censoring, and survival conditions. Before comparing outcomes, articulate the randomized trial whose result would matter, even if that trial cannot be conducted. This is the target-trial approach of Hernán and Robins (2016), not a procedure for converting arbitrary historical associations into randomized evidence.

## Specify the protocol

Name the eligibility criteria, time zero, strategies, assignment procedures, outcomes, follow-up duration, causal contrast, and analysis plan. Write a date- or event-specific rule for each field. Avoid criteria determined after assignment: selecting only units that completed treatment can exclude early failures and introduce selection bias. An exposure that is defined as “received treatment for at least six months” cannot be assigned at baseline unless one simultaneously specifies what happens to units who stop or die before six months. A treatment is a strategy over time; “ever treated” is usually not a precise intervention.

Consider an industrial intervention to replace a valve in one of two production lines. **Time zero** could be the timestamp when a machine becomes eligible for replacement, not the time of first completed good batch. Eligibility might require a scheduled maintenance interval and an eligible part number. Strategies could be replacement at that interval versus scheduled replacement at the next interval. Outcomes might be defects per 1,000 attempted parts over a prespecified follow-up, with machine shutdowns counted explicitly. The analysis should not eliminate a shutdown simply because it produced no acceptable units. This is a *design template*, not a claim about any observed plant.

## Assignment versus compliance

An intention-to-treat contrast concerns assignment to strategies; a per-protocol contrast concerns following them. In an observational emulation, assignment is not necessarily recorded and treatment initiation is not identical to randomized offer. Changing adherence can be associated with prognostic history. If those histories are affected by prior treatment, ordinary baseline-only adjustment can be inadequate; a suitable longitudinal g-method may be required.

Define both the eligible population and the population represented by observed records. Exclusions at time zero change the target. For a matched cohort, each unit's baseline window must be aligned with its comparison's baseline window. Explicitly specify the handling of repeated eligibility and follow-up until outcome, censoring, or a fixed horizon. State when a strategy could not have been implemented or when exposure information is missing.

## Validity checklist

- Could both strategies realistically have been assigned to each eligible unit at time zero?
- Does every outcome and covariate timestamp precede or follow assignment as required?
- Are baseline confounders distinguishable from postbaseline consequences?
- Do records contain sufficient support for the compared strategies in the target population?
- Were exclusions, censoring, competing events, and deviations from strategy handled consistently?
- Could the same question be answered by a stronger design, such as randomization, interrupted time-series with credible controls, or a prospective instrument?

Passing this checklist is not proof of exchangeability. Report unmeasured causes, measurement error, adherence definitions, and target population differences. A target-trial diagram is a discipline for identifying what to learn, not a certificate of causal identification.

**Source scope:** Hernán and Robins, *Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available*, 2016, [full published PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/), sections defining target-trial protocol and baseline alignment. The Atlas paraphrases selected passages and does not redistribute the paper. See also [BMJ target trial primer](https://www.bmj.com/content/378/bmj-2022-071108).

---

# 14. Longitudinal g-methods and treatment-confounder feedback

At two or more decision times, a variable may predict future treatment and outcome while itself being changed by earlier treatment. A baseline-only model can leave confounding, but naïvely conditioning on the post-treatment variable can block parts of the earlier treatment effect or create collider bias. Longitudinal g-methods address this structure under explicit assumptions. They do not eliminate the need for information about the treatment-assignment mechanism or the outcome process.

## Two-decision mathematical reference

Let L0 be baseline, A0 the first treatment, L1 the intermediate state, A1 the second treatment, and Y the outcome. For a **static strategy** (a0,a1), a finite longitudinal g-formula is:

```
R(a0,a1) = Σ_l0 P(l0) Σ_l1 P(l1 | l0,a0) E[Y | l0,a0,l1,a1]
```

As an *identification formula from observational data*, this requires sequential exchangeability at both decisions, consistency, positivity, and adequate models or nonparametric empirical support. The local `longitudinal` command does not fit these ingredients. Instead, it accepts them as fully stipulated probabilities, enumerates binary L1, and reports the resulting four strategy risks and requested contrast.

In the synthetic worked example, early treatment changes the probability of an intermediate high-risk state from 1/5 to 3/5, while both treatment decisions also change the outcome probabilities. The computed (1,1) versus (0,0) risk difference is 17/50. This is a property of the declared model, not an estimate from factory or patient data.

## Weighting and g-estimation

Marginal structural models may use inverse probabilities of observed treatment histories, multiplying appropriate treatment and censoring factors across time. Those weights require models and positivity for each history. Rare treatment sequences can produce extreme weights, reducing precision. Report support, distribution of weights, rules for truncation, and sensitivity of results to those rules. Clustering and repeated measurement require suitable uncertainty estimates. Longitudinal g-estimation can target structural nested models, but it has a different parameterization and is not interchangeable with a simple weighted average.

## Common failures

Do not adjust for every post-treatment measurement just because it predicts outcome. Conversely, do not assume two treatment decisions are independent merely because the first was assigned. No procedure should manufacture data for an unobserved treatment sequence: missing positivity makes that strategy comparison nonidentified in relevant strata without external assumptions. Time-varying censoring may be informative. A stable fitted model is not evidence that all relevant history was captured.

For a real project, preserve the complete measurement timeline, time stamps, strategy definitions, adherence status, censoring reasons, treatment mechanisms, supported histories, and code/version for outcome estimation. Then test whether the assumptions are plausible and whether a negative control or alternative design disagrees.

**Sources:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook), especially the authors' description of Part III and their chapter on treatment-confounder feedback; [Hernán and Robins target-trial article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/), per-protocol and postbaseline sections. The code here implements a bounded finite formula, not a full longitudinal estimator.

---

# 15. Staggered-adoption difference-in-differences: group-time comparisons

A policy may reach different groups in different years. A single treated-versus-control line can conceal effects that vary with treatment timing or exposure duration. Two-way fixed-effects coefficients can become difficult to interpret under heterogeneous dynamic effects. A useful reference identifies cohort-specific effects for a cohort first treated in period g and an outcome observed at period t, then makes the comparison group explicit.

## Declare the target before aggregating

A group-time target ATT(g,t) is the average effect at period t for members whose first treatment was period g, normally for t ≥ g. A basic group-time difference in changes is:

```
D(g,t) = [Ybar_g,t − Ybar_g,g−1] − [Ybar_C,t − Ybar_C,g−1]
```

Interpretation as ATT(g,t) requires no anticipation, a defensible untreated counterfactual trend for group g represented by C, consistency, valid measurement and appropriate selection/censoring assumptions. The local `staggered-did` tool computes the arithmetic from user-supplied group-period means, **not** a causal ATT estimator with covariate adjustment or sampling inference.

Two comparison policies are exposed. `never` uses only never-treated groups. `not_yet` includes groups first treated after the comparison period (as well as never-treated groups), if they have appropriate untreated outcomes. Groups already treated by period t are excluded from the control set. If no eligible comparison exists, the result contains an explicit unavailable entry rather than a constructed effect.

## A fully specified teaching panel

Periods are 0, 1, and 2. Never-treated means are 0,1,2. The early cohort begins in period 1 and records 0,3,5. The late cohort begins in period 2 and records 1,2,6. Under no anticipation and a stipulated untreated +1 trend, the early period-1 contrast is +2, early period-2 is +3, and late period-2 is +3. The tool reports all three with their baseline period and comparison-group IDs. The assumptions were authored to fit the values; these are not observed effects.

## What makes applied estimation harder

A real study should verify who was exposed when, whether treatment is absorbing or reversible, the policy's eligibility rules, survey weights and attrition, repeated outcomes, cluster boundaries and common shocks. Parallel trends for an untreated outcome is not testable from a post-treatment trajectory alone. Preperiod checks can reveal certain contradictions but cannot prove future counterfactual trends. Cohort composition may change over time. Anticipatory effects require shifting eligibility and baseline definitions.

For uncertainty, account for sampling and cluster dependence; consider simultaneous confidence bands when many groups and horizons are compared. Preserve aggregation weights and do not compress heterogeneous cohort effects into one number without stating whose average it is. A policy result should carry sensitivity to trend differences, group selection, timing definitions and measurement units.

**Source scope:** Callaway and Sant'Anna (2021), *Difference-in-Differences with Multiple Time Periods*, [journal abstract](https://doi.org/10.1016/j.jeconom.2020.12.001); [official `did` package method documentation](https://search.r-project.org/CRAN/refmans/did/help/att_gt.html) for comparison-group options. This Atlas tool is a simpler descriptive teaching comparison, not a reproduction of their estimator.

---

# 16. Mediation: direct and indirect contrasts require their own interventions

An exposure may change an intermediate variable, which may then affect the outcome. Calling the observed treatment association a “direct effect” after controlling for that mediator can be incorrect: the mediator may be affected by exposure, share causes with the outcome, or be related to post-exposure variables that are also affected by exposure. What causal contrast is desired must be stated precisely.

## Stochastic-intervention definition

For a binary exposure A and mediator M, suppose q_a(m) describes a proposed **mediator distribution under exposure a**, and μ(a,m) is an outcome risk under interventions on A and M. Define R(a,q_b)=Σ_m μ(a,m) q_b(m). Then a particularly simple decomposition is:

```
Total   = R(1,q1) − R(0,q0)
Direct  = R(1,q0) − R(0,q0)
Indirect= R(1,q1) − R(1,q0)
Total = Direct + Indirect
```

These are **interventional distribution contrasts** and not individual-level natural direct or indirect effects. Other equally valid mediation decompositions choose different reference distributions and need different interpretations. The local `mediation` tool computes the above identity from supplied mediator probabilities and outcome means; it cannot infer q or μ from observational records or check the cross-world assumptions sometimes required for natural effects.

In the synthetic example, exposure changes P(M=1) from 1/5 to 3/5. Four stated outcome risks generate a total contrast of 6/25, split into a 3/25 direct component and a 3/25 indirect component under the declared decomposition. These numbers are mathematical consequences of supplied probabilities. A statistically stable mediator regression would not, on its own, establish these as mechanisms in the physical system.

## Identification and timing hazards

Even interventional mediation contrasts require conditional exchangeability or other identification conditions for outcome and mediator models in a particular study. Post-treatment mediator-outcome confounders affected by exposure require careful definitions and methods; this two-variable tool has no such confounder. Distinguish exposure-induced intermediate causes, baseline confounders, competing pathways, multiple mediators, measurement error and downstream selection. Natural effects can require conditions involving combinations of counterfactuals; they are not automatically identified when an interventional contrast is calculable.

A practical mediation protocol should state the exposure strategy, mediator measurement time, feasible mediator intervention, outcome window, baseline covariates, exposure-induced confounders, choice of direct/indirect definition and what intervention on the mediator would actually mean. If the mediator is only a proxy, label it a proxy. If intervening on a mediator would change other downstream variables, make that restriction explicit.

**Source scope:** [Nguyen et al., *Clarifying causal mediation analysis for the applied researcher*](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496983/), interventional-effect definitions; [Díaz et al., stochastic interventions](https://pmc.ncbi.nlm.nih.gov/articles/PMC10345989/), overview. This chapter paraphrases the accessible discussions rather than mirroring their papers. The tool addresses a narrow static binary model only.

---

# 17. Interference and spillovers: another unit's treatment can matter

The familiar potential-outcome notation Y_i(a_i) assumes one unit's outcome does not depend on everyone else's treatment assignment. This no-interference simplification is implausible for contagious disease, social networks, learning effects, machine lines sharing a resource, or teams whose members coordinate. Under interference, one must define exposure at the relevant group or network level and decide which treatments are inside the causal unit.

## Explicit two-person cluster model

A small cluster with two units has four joint assignments: 00, 01, 10 and 11. Let Y0(a0,a1) be the first unit's outcome under both assignments. A **direct effect at neighbor status 0** is Y0(1,0)−Y0(0,0). At neighbor status 1 it is Y0(1,1)−Y0(0,1). A **spillover while own status is 0** is Y0(0,1)−Y0(0,0). These can differ. Compressing all four into one treatment effect can destroy information about the policy being evaluated.

The `interference` command accepts the complete table of two outcomes under all four assignments, checks bounded outcomes and reports these contrasts. In the synthetic example, the first unit's own-treatment effect with neighbor untreated is 3/10 and spillover on the first unit with own treatment off is 1/5. Because the table is stipulated, no estimation or randomization occurred. The tool's role is to teach how an estimand changes under spillovers.

## Partial interference and policy design

A common practical simplification is partial interference: effects may propagate inside a declared cluster, but not between clusters. A two-stage randomized design can randomize cluster exposure policies and within-cluster assignments; appropriate designs can identify direct and indirect effects under their assignment conditions. If units move between clusters or share a supply chain, partial interference may fail. Network exposure mappings may help define effects of neighbors or coverage proportions, but the mapping itself is a scientific assumption.

For a manufacturing network, a process change in one machine might divert maintenance staff, alter material queues or shift temperatures in shared equipment. A control machine may therefore cease to be truly untreated. The evidence plan should retain machine dependency maps, resource-sharing logs, timing, measured spillovers and candidate mechanisms. This is a hypothetical scenario; no actual factory observations are bundled.

## Reporting contract

Specify unit of assignment, unit of outcome, interference boundary, exposure mapping, causal target, assignment probabilities, cluster count, sampling units and dependence-aware uncertainty. If a study uses individual standard errors under shared clusters, mark a model limitation. A null direct effect does not imply no spillover effect. A network result cannot be transported to a different graph without further assumptions.

**Source:** Hudgens and Halloran (2008), [*Toward Causal Inference With Interference*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/), abstract and full article overview. This Atlas implements only a complete, stipulated two-unit potential-outcome table, not interference estimation from observed network data.

---

# 18. Transportability: what changes when the target population changes?

An average effect estimated in a trial population need not be the average effect in the population facing the decision. If effects vary with age, baseline condition, machine type or environment and these characteristics occur with different frequencies in the target population, averages will differ. The central task is to determine which conditional causal response functions can be carried across populations and which selection mechanisms make that transfer invalid.

## A narrow stratum-standardization identity

Suppose Z is a pre-intervention categorical effect modifier. Under a justified transfer assumption for conditional causal risks μ_a(z), the target effect is:

```
ATE_target = Σ_z P_target(z) [ μ_1,source(z) − μ_0,source(z) ]
```

Every stratum with positive target weight requires source support or an explicit extrapolation model. The local `transport` command requires strictly positive source mass for any positive target-mass stratum, checks both mass distributions sum to one, and computes the source and target contrasts separately. It does not test that source outcome response functions are causal or invariant across settings.

In the constructed example, a source population is three quarters low-risk and one quarter high-risk; the target reverses those proportions. The stratum effects are 0.10 and 0.30. The source average is 0.15; the target average is 0.25. Both numbers can be arithmetically correct. Neither can be applied to an actual institution unless effect modifiers, study conditions, outcomes and intervention versions are comparable.

## Reasons transfer fails

Different intervention versions, outcome measurement, follow-up, exposure support, calendar conditions and unmeasured effect modifiers can make source estimates unsuitable. A selection diagram may formalize which processes differ across settings; a general graphical transportability algorithm is not implemented here. Sampling weights estimated from available covariates do not eliminate unmeasured differences. The presence of a source stratum with observations does not guarantee enough precision or valid conditional causal identification.

Document the source inclusion criteria, target inclusion criteria, calendar and geographic scope, measured effect modifiers, outcome definitions, intervention versions, support overlaps and uncertainty in the source contrasts. If a target subgroup is absent from the source and the needed response is unknown, the comparison should be marked `unsupported`, not assigned a convenient estimate.

**Source scope:** Bareinboim and Pearl, [*Transportability of Causal Effects: Completeness Results*](https://ojs.aaai.org/index.php/AAAI/article/view/8232), publisher abstract; [*Meta-Transportability of Causal Effects*](https://proceedings.mlr.press/v31/bareinboim13a.html), conference overview. The code computes only a finite weighted average conditional on supplied response functions; it is not the published complete selection-diagram algorithm.

---

# 19. An authentic descriptive reproduction: Berkeley admissions in 1973

> Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.

## Reproduce the published marginals

> Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.

## What the table does not tell us

It contains no randomly assigned sex, no information on qualifications within departments, no broader applicant pool outside the six departments and no full institutional assignment process. Applying to a department is itself a decision influenced by applicant preferences, credentials, advice and constraints. A comparison holding department fixed can answer a different descriptive question from the crude comparison. It does not necessarily isolate a causal contribution of sex or discrimination, nor does the reversal establish that no discrimination occurred. Historical labels and classifications must remain attributed to the source.

Even if the calculation is exact, the scientific question may be underdetermined. A causal analysis would require an explicit intervention or well-defined treatment contrast, relevant outcome, substantive identification assumptions, potential mediators or colliders, and appropriate unit-level data where needed. Do not call the standardized result an “adjusted causal effect” on the strength of arithmetic alone.

## Reproducibility and provenance

> Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.

**References:** [R base datasets documentation, UCBAdmissions](https://cloud.r-project.org/doc/manuals/r-release/packages/datasets/refman/datasets.html), [teaching reproduction with the 24 numeric cells](https://utstat.utoronto.ca/~brunner/oldclass/312f22/lectures/312f22ContingencyTables-R.pdf), [Rdatasets source and licensing statement](https://github.com/vincentarelbundock/Rdatasets). The 1975 Bickel, Hammel and O'Connell Science paper is cited in R documentation; the full article is not mirrored or independently audited here.

---

# 20. Estimation uncertainty is not causal identification

Statistical precision and causal identification answer different questions. A confidence interval describes variability of an estimator under a sampling and model framework; it does not establish that its target is a causal contrast, that an intervention is well defined, or that confounding has been removed. Conversely, a validly randomized intervention can still have a very imprecise estimate when samples are small or outcomes are noisy.

## Independent binary samples

For independent samples with binary outcomes, a basic descriptive risk difference is p1−p0. An introductory large-sample estimated variance is p1(1−p1)/n1+p0(1−p0)/n0. The tool `binomial-interval` applies a named normal quantile to this standard error. It requires two integer count groups, at least 30 observations per arm and non-extreme proportions; even with these guards, Wald intervals can have poor coverage, particularly near boundaries or when the independence assumptions fail. The package does not claim this method is universally recommended.

For a constructed case with 60 successes in 100 control observations and 75 in 100 treated observations, the observed difference is 0.15 and an approximate nominal 95% interval is about [0.0219, 0.2781]. This is a **descriptive independent-binomial calculation**, not a randomized experiment or causal effect. It also is not an interval for any of the observational Berkeley effects, which require an appropriate data and design analysis.

## Why generic standard errors fail

A matched-pair design, a cluster-randomized trial, a repeated-measures panel and an event study have different dependence structures. Treating all observations as independent under cluster assignment may substantially understate uncertainty. Estimators with nuisance models can require influence-function or resampling methods; nonregular settings such as weak instruments or cutoff discontinuities may need specialized inference. Large sample size does not fix bad measurement, missing outcomes, flawed identification or model extrapolation.

In difference-in-differences, standard errors must respect the level of treatment assignment and serial correlation. In longitudinal IPW, rare histories generate volatile weights. In regression discontinuity, bandwidth choice and model bias matter. In IV, a denominator close to zero can make conventional ratio intervals behave badly. These are *distinct* failures and should not be papered over by one generic “95% CI” command.

## What a citation-ready result requires

For each reported effect and uncertainty estimate, record: target population, treatment contrast, sample selection, design, target estimand, estimator, analytic or bootstrap method, clustering/repeated-measures structure, uncertainty level, degrees of freedom where relevant, multiple testing policy, and unresolved identification assumptions. If these inputs cannot be justified, report the numerical contrast with limitations rather than calling its interval decision-ready.

**References:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook) for separate treatment of random variation and causal assumptions; [Callaway and Sant’Anna 2021](https://doi.org/10.1016/j.jeconom.2020.12.001) for staggered-DiD inference scope. This chapter does not implement their full inference procedures.

---

# 21. Negative controls and sensitivity analyses: try to falsify your explanation

In observational work, the central problem is often not computing the adjustment but determining whether its assumptions could be wrong. A negative control is an exposure or outcome chosen to make certain confounding, measurement, selection or analytic biases visible. It does not guarantee that an undetected bias is absent, and an unsuitable control can falsely reassure an analyst.

## Choose a control with a clear exclusion rationale

A negative-control outcome should plausibly share some bias mechanisms with the outcome of interest while, under a substantive theory, not being causally affected by the proposed intervention. A negative-control exposure should plausibly share drivers of treatment assignment while not causally affecting the primary outcome. A genuine control requires explicit timing, selection and measurement conditions. A nonzero association can reveal trouble, but a zero association cannot prove a no-confounding assumption unless strong additional completeness assumptions justify that interpretation.

For a mechanical change purportedly lowering a product defect caused by pressure instability, a reasonable investigative question might be whether another quality measure that should not be affected by the pressure mechanism nevertheless shifts after the change. That is an example of how to frame a candidate negative control, not a verdict that the candidate is actually valid. Shared sensor recalibration or a line-wide software update might change both outcomes and destroy the proposed exclusion assumption.

## Sensitivity with explicit alternative models

A useful analysis reports how the estimate changes under plausible deviations from an identifying condition. The existing Atlas includes finite examples of an instrumental-variable exclusion violation, missing-outcome bounds, and difference-in-differences trend deviations. Each takes a declared sensitivity parameter and reveals the result; none estimates the parameter's true value. Sensitivity should explore practical ranges informed by domain knowledge, not only values close to zero.

If one unmeasured cause can plausibly change both assignment and outcome, document how strong its relationships would need to be to alter the decision. Negative-control and sensitivity methods have different assumptions; they should be chosen according to the bias mechanism, not as decorative robustness checks. Use multiple credible analyses with genuinely different failure modes rather than repeated variants of the same biased model.

## Evidence decision protocol

Record which biases each diagnostic could detect, what is expected under a valid design, whether thresholds were prespecified, every result (including inconvenient ones), and remaining blind spots. A failed control may call for redesign instead of a larger sample or more sophisticated estimator. If the available data do not distinguish two plausible explanations, report that lack of identification as a research result.

**Reference:** Lipsitch, Tchetgen Tchetgen and Cohen (2010), [*Negative Controls: A Tool for Detecting Confounding and Bias in Observational Studies*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/), abstract and paper's distinction between exposure and outcome controls. This local library does not implement a general negative-control bias-calibration estimator.

---

# 22. Missingness, measurement error and selection are part of the causal model

The variables in a dataset are recorded measurements, not direct access to underlying scientific states. Treating recorded exposure and outcome values as exact can create or reverse associations. Inclusion in the dataset itself may depend on treatment, outcome, survival, or unrecorded causes. An apparently clean regression can then estimate an association in a selected group unlike the original target population.

## Measurement error is structural

A pressure sensor can be biased by calibration drift, temperature, or software changes. An interview measure can be affected by recall and by outcome status. In both cases, measurement error is not necessarily independent or nondifferential. A classical error model that attenuates a linear slope does not apply to every exposure, outcome type, timing or missingness mechanism. Draw the measurement process explicitly alongside the substantive causal graph, with observed and latent nodes separated.

Record measurement units, sensor/instrument versions, calibration dates, blinding if relevant, resolution, missing flags, sampling protocols and changes across treatment groups. The Measurement Atlas should supply technical metrology concepts, but its uncertainty calculation cannot by itself repair unmeasured confounding. Shared identifiers and provenance let the nodes complement each other while keeping their evidence statuses separate.

## Missing outcomes are not zeros

The current `missing-bounds` tool offers sharp arithmetic bounds for completely counted binary arm populations when missing outcomes can be either 0 or 1. If n observations were expected and only o are observed, with s successes, the risk lies between s/n and (s+n−o)/n. The difference interval follows by subtracting the extreme arm risks. It is not a confidence interval and requires no imputation. Real studies often have additional assumptions, sampling uncertainty and dependence that these simple bounds do not represent.

Complete-case selection can bias comparisons if loss to follow-up depends on treatment or outcome. Assigning zero to a missing outcome is an explicit hypothetical rule, not a neutral default. Multiple imputation and inverse-probability-of-censoring weighting require their own data, models and assumptions; neither is implemented by the bound tool.

## Selection, survival and timestamps

Restricting to surviving workers, completed batches, treated survivors, or records with a post-treatment measurement can condition on consequences of the treatment and outcome. A collider can induce an association even when none exists marginally. Survivorship can change not only effect estimates but the estimand itself. A study should say whether it targets all eligible units, a principal stratum or a post-treatment selected subgroup; the latter often requires assumptions not observed in the records.

**References:** Hernán and Robins [*Causal Inference: What If*](https://miguelhernan.org/whatifbook) includes measurement bias and selection bias chapters; [Hernán and Robins target-trial protocol](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/) addresses selection and censoring. These pages support the topic scope, not an automatic assessment of any particular database.

---

# 23. Evidence-preserving causal knowledge for other AI systems

Causal Atlas is a reference node. It is not an AI model and must not be interpreted as one. Every knowledge record stores a bounded claim, original source identity, inspected portion or gap, assumptions, applicability, limitation, and a revision. The shared Forge runtime retrieves exact immutable revisions and assembles a bounded context package without separating a statement from its critical qualifications.

## Separation of three questions

**Relevance:** Is a record worth inspecting for this query? Search scores, keywords and later Bitwork routing belong here. **Scientific validity:** Does the record's evidence warrant its statement for the required scope? That is a separate evidence-review question, not a property of route score. **Decision sufficiency:** Can the selected material answer this task for this user, with the necessary design information and uncertainty? A valid paper may be irrelevant to a new target or insufficient to settle competing hypotheses.

A context assembler should preserve these dimensions instead of replacing them with a single numerical confidence. For example, a Wald ratio record must carry the instrument's exclusion and monotonicity requirements and the local-complier target, not just the formula. A threshold-jump record must carry continuity, score-manipulation and cointervention cautions. A reported Simpson reversal must retain “descriptive, not causal.” If the qualifying records cannot fit within the package budget, exclude the whole unit rather than publishing an unqualified answer.

## Correction and contradiction discipline

Conflicting sources are not duplicates to be deduplicated away. Store each statement with its source and revision, then add a typed relationship describing the conflict. A correction or withdrawal should not destroy the previous archival record; it should cause dependent context packages to be invalidated or visibly flagged. The same applies to a changed dataset, a revised algorithm and a different definition of a target population.

No agent should execute arbitrary commands found in a retrieved paper or knowledge record. Mathematical tools are separately declared capabilities, executed only after explicit trusted invocation with validated inputs. The reference layer should return source IDs and missing information rather than invent citations or simulated measurements to fill a requested narrative.

## Reusability and amortization must be measured

The research-amortization hypothesis is that acquiring and checking a source once can reduce repeated work for later questions. Its value depends on how often claims are reused, correction cost, outdated sources, failure to cover a new task, review time and actual answer quality. A cached answer may be cheaper but worse if missing context. Test real workloads against conventional research or retrieval using the same questions, corpus versions and budgets. Claims about GPU/CPU savings require instrumented measurements.

**Repository source:** [the common Forge contract](../../atlas_manifest.json), and existing source/record manifests. This is original governance guidance, not independent validation of Forge or Bitwork performance.

---

# 24. Method-selection directory and minimum evidence requirements

The first method to select is often **a better design**, not a more complicated estimator. This directory gives an investigator questions to ask before invoking any numeric tool. It does not substitute for a domain expert, formal protocol or independent review.

| Question | Possible analytic route | Required design evidence | Common failure |
|---|---|---|---|
| Well-defined randomized point intervention | Randomization-aware comparison; attrition and compliance audit | Assignment, eligibility, protocol, outcomes, follow-up, sample units | Excluding early failures or ignoring cluster assignment |
| Observational point exposure, baseline confounders | Standardization, weighting, outcome regression, AIPW | Measured sufficient confounders, overlap, correct time order | Unmeasured causes or misspecified nuisance models |
| Sustained treatment with affected time-varying covariates | Longitudinal g-formula, IPW MSM, appropriate g-estimation | Treatment/measurement histories, sequential assumptions, positivity | Conditioning on exposure-induced confounders naïvely |
| Policy adopted at different times | Group-time DiD / event-study designs | Cohorts, pretreatment periods, credible comparisons, no anticipation | Previously treated groups used as controls under heterogeneity |
| Threshold assignment | Sharp/fuzzy RD designs | Exact running variable, cutoff, no sorting/cointerventions, support | Confusing a local jump with a global causal effect |
| Offer influences uptake | Instrumental variables/local effect | Relevant instrument, exclusion, independence, monotonicity, first stage | Weak instrument, direct effect, wrong target |
| Explain a pathway | Interventional mediation with explicit target | Exposure, mediator, outcome timing, mediator-outcome confounders | Naïve mediator adjustment |
| Neighbor/cluster effects | Interference-aware design | Cluster or network boundaries, assignment mechanism, exposure map | Assuming no interference |
| Transfer to new population | Stratum standardization or formal transportability analysis | Source causal effects, target modifiers and positive support | Ignoring effect modification or new intervention version |
| Missing outcomes | Bounds or censoring/selection model | Full eligible count, missingness mechanism and data origin | Complete-case or missing-as-zero bias |
| Descriptive historical table | Stratified rates and standardization | Authentic counted data, documented target weights | Calling observed disparity a causal intervention effect |

## One-question interrogation sequence

1. Define the intervention, comparison, outcomes, target population and baseline time.
2. Sketch variables and their timing; list plausible confounders, mediators, colliders, and measurement channels.
3. Ask whether a randomized or natural experiment is feasible or whether the existing data justify a specified identification strategy.
4. Inspect treatment support and missingness. If an estimand is not identified, record why before fitting models.
5. Choose an estimator and its sampling-inference procedure under the *actual* data structure. Keep estimation precision separate from identification.
6. Compare alternative assumptions and negative controls where defensible.
7. Write a result with sources, data version, population, uncertainty, limitations and a falsification agenda.

A result cannot be upgraded from descriptive to causal by improving the fit or adding decimal places. The reference must allow a final answer of “the available data do not identify this effect.”

**Source navigation:** Hernán and Robins, [*Causal Inference: What If*](https://miguelhernan.org/whatifbook); Callaway and Sant'Anna, [staggered DiD journal record](https://doi.org/10.1016/j.jeconom.2020.12.001); Hudgens/Halloran, [interference](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/); Bareinboim/Pearl, [transportability](https://proceedings.mlr.press/v31/bareinboim13a.html); Bickel et al. via [R UCBAdmissions documentation](https://cloud.r-project.org/doc/manuals/r-release/packages/datasets/refman/datasets.html).

# Worked investigations


---

# Investigation A A process improves within groups but looks worse overall

**Data origin: original synthetic example. No workplace measurements.**

## Question and design

The target is the difference in pass probability under two assigned processes for a population with equal easy/difficult job shares. Difficulty is defined before assignment. The example stipulates that difficulty is the only needed adjustment variable; an actual investigation would need evidence for that omission assumption, consistent process versions and stable inspection definitions.

| Difficulty | Existing jobs | Existing successes | New jobs | New successes |
|---|---:|---:|---:|---:|
| Easy | 80 | 64 | 20 | 18 |
| Difficult | 20 | 4 | 80 | 24 |

The existing process passes68/100 jobs, while the new process passes42/100. The crude difference is−0.26. Within easy jobs the difference is0.90−0.80=0.10; within difficult jobs it is0.30−0.20=0.10. Equal target weighting gives0.60−0.50=0.10. The new process was deliberately assigned disproportionately to difficult work.

## Compare the implemented estimators

The shipped `examples/process_rows.json` expands these counts into200 synthetic units. Each row includes a declared baseline covariate, the generating propensity, and generating outcome means. The runtime does not infer those functions from the outcomes. Under these supplied inputs, OR, HT, Hájek and AIPW all produce0.10. This is a designed arithmetic identity, not an empirical competition between methods.

```sh
python -m causal_atlas estimate examples/process_rows.json --nuisance-origin synthetic_oracle
python -m causal_atlas population examples/process_population.json
python -m causal_atlas investigations
```

The sample and population functions are deliberately separate. The first uses observed rows and supplied predictions; the second integrates over a fully authored distribution whose truth is known. A finite sample from a correct model need not reproduce every expectation exactly.

## What could break the real investigation?

If operators decide treatment using a condition not in difficulty, the comparison may remain confounded. If difficult jobs cannot ever receive the existing process, the proposed equal-mix target lacks support. If treatment changes how difficulty is recorded, the stratification is no longer baseline adjustment. If inspection criteria changed, Y itself may not be the same outcome. If only surviving jobs appear in the file, selection needs separate analysis.

A real application should fill the target-study and assumption-ledger templates before using an estimator. At minimum it needs assignment timestamps, intervention versions, baseline-variable definitions, outcome completeness and a reason to believe the adjustment set is sufficient. None is established by this toy table.

## Useful conclusion and forbidden conclusion

The defensible statement is that ignoring a stipulated job-mix difference reverses the contrast in this constructed model, and the declared adjustment recovers its known target. It is not evidence that the user's actual process is beneficial, that every reversal is confounding, or that standardization always fixes a production dataset.

**Evidence:** retained case definitions; original formulas in Chapters2–4; source records HR2006 and AS2015. **Review state:** authored derivation and computation, no external scientific sign-off.

---

# Investigation B Deliberately break the working models

**Data origin: the same original finite population as Investigation A.**

## Why known truth is useful here

A real observational analysis does not reveal its true propensity and both potential outcome means. A deliberately authored population does. That makes it suitable for falsification exercises, not for proving real-world effectiveness. We vary the working functions while keeping the generating distribution fixed.

The truth is ATE=1/10. The generating propensity is1/5 for easy work and4/5 for difficult work. Generating outcome means are(4/5,9/10) and(1/5,3/10). The input file distinguishes generating `e,mu0,mu1` from working `g,m0,m1`; overwriting the former to fit the latter would erase the test.

## Exact checks

With either the true propensity or both true outcome means, the AIPW population expectation equals1/10. With both working components wrong—g=1/2 for both groups and outcome means m0=1/2,m1=3/5 for both groups—the result is−13/50, or−0.26. The bias is−9/25, or−0.36.

The runtime checks the independently derived algebraic expression for that bias in every synthetic population. It also checks constant-outcome shifts and treatment-label reversals on sample scores. These tests target different errors; simply recomputing one reference value with the same formula would be weaker evidence.

```sh
python -m causal_atlas population examples/process_both_models_wrong.json
```

## Do not repair a failed model by renaming the result

The −0.26 result is retained with `propensity_exact: false`, `outcome_means_exact: false`, the known true effect and the bias. A test passes when it reproduces that failure faithfully. It does not change the example's status to an identified causal answer.

In real data the exactness flags cannot be obtained by looking at outcome fit alone. A propensity score can predict treatment well while creating extreme weights, and a good prediction score need not justify causal adjustment. Conversely, a disappointing prediction score does not by itself invalidate every target contrast. Those are different questions requiring design, diagnostics and statistical theory.

## A second nonidentification exercise

The exact binary engine evaluates two models that share the same observed joint distribution: a hidden common cause determines both A and Y, or A directly determines Y. Both show an observed difference of1; their intervention effects are0 and1. This is a separate failure mode from bad nuisance fitting. No choice among the four estimators can infer which of these two mechanisms is true from their identical observation table alone.

## Review prompt

Explain which assumption changed in each test and whether more sample size would necessarily solve it. Distinguish model-estimation error from identification ambiguity. A reader who reports “AIPW is wrong” without those distinctions has not understood the example; a reader who reports “doubly robust means safe” has also failed the review.

**Evidence:** local residual-score derivation, exact finite-model enumeration, retained source correction notice. **Unperformed:** fitted-model benchmark, sampling inference, independent human review.

---

# Investigation C The same observations permit opposite conclusions

**Data origin: original counts and four-mean scenarios; neither is a real study.**

## Part one Missing inspection outcomes

The treated arm has100 total units,60 observed outcomes and48 observed passes. Control has100 total,90 observed and54 passes. The observed-only difference is0.80−0.60=0.20. Without assumptions about unobserved binary outcomes, full-arm differences range from−0.16 to+0.34.

```sh
python -m causal_atlas missing-bounds examples/missing_outcomes.json
```

The algorithm computes these endpoints from successes and missing counts. It is not a95% confidence interval and does not decide that missingness is random. The uncertainty is about unseen outcomes in the supplied counted set. Causal identification, measurement validity and sampling uncertainty remain separate.

The sign becomes positive only under restrictions strong enough to make `-0.06+0.40*r1-0.10*r0 > 0`, where r1 and r0 describe the missing treated and control outcomes. Those probabilities are not estimated here. A reviewer should examine why the allowed range is plausible, not merely select a favorable pair.

## Part two Before–after production comparison

The treated line rises from0.80 to0.90 and control from0.70 to0.75. The four-mean contrast is+0.05. The function `two_period_contrast` accepts an explicit sensitivity value delta for the untreated trend difference. Delta0 gives+0.05; delta0.08 gives−0.03. No observed mean changes between scenarios.

This is a controlled demonstration of an identification assumption. It does not show that delta0.08 is plausible for any actual line. The function has no regression, panel clustering, pretrend test, staggered-adoption method or interval estimator.

## Build a better data request

For the missingness problem, request outcome accounting by arm, time, reason for missingness and baseline strata, plus any independently recovered outcomes. For the trend problem, request assignment rationale, preintervention series, changes in product mix, contemporaneous shocks, inspection revisions and possible spillovers. Each item should be tied to a proposed alternative explanation rather than collected indiscriminately.

More information may narrow the analysis but need not settle it. A source-backed reference must be able to return “not determined under the supplied information.” That is a useful outcome when the alternative is a falsely precise recommendation.

## Deliverable

Use the result-report template to record both the primary descriptive contrast and all declared sensitivity scenarios. Keep unknowns visible. Do not label the bounds as experimental uncertainty, the adjusted DiD scenario as an observed effect, or a successful JSON response as scientific approval.

---

# Investigation 4: an offer changes attendance, but whose outcome effect is identified?

## Question and scope

This original synthetic investigation separates the effect of an invitation from the effect of actually receiving training. It is not an account of the user's employer or a real participant dataset. The substantive question is whether training helps the people induced to attend by a particular offer, and whether that conclusion can be extended to everybody. Treating these as the same question is the deliberate trap.

The constructed population contains three types. Never-takers have mass 0.30 and potential outcome means 0.60 without training and 0.50 with training. Always-takers have mass 0.20 and means 0.20 and 0.30. Compliers have mass 0.50 and means 0.40 and 0.70. Assignment to the offer is stipulated independent of these types. Initially the offer has no direct effect on the outcome and there are no defiers.

## Derive, do not guess, the comparison

Without an offer the attendance mean is 0.20. With an offer it is 0.70. The first stage is 0.50. Expected outcomes are 0.44 without the offer and 0.59 with it, giving an offer contrast of 0.15. Dividing 0.15 by 0.50 yields 0.30, exactly the complier effect. The full-population effect is instead 0.14 because the effects in the never- and always-taking groups differ.

The tool reports both quantities because they are known in this fully specified model. In an actual study the potential outcome pair for each type would not be observed. A real reference packet could report the identified local target but must not pretend that this fixture teaches it the factory-wide effect. Changing the invitation can also change who complies.

## Deliberately violate exclusion

Now add 0.05 directly to the outcome whenever a place is offered. The first stage remains 0.50; the reduced form becomes 0.20. The ratio becomes 0.40 although the underlying training effect among compliers remains 0.30. Random assignment of the offer is still stipulated. Randomization did not remove the invitation's direct outcome pathway.

A scenario assuming direct contribution between zero and 0.05 produces a training-effect range of [0.30,0.40]. It is not a sampled confidence interval and cannot be interpreted as one. The source of those assumptions must be part of an empirical analysis record.

## Deliberately violate monotonicity

A second model contains 0.40 compliers with effect 0.10, 0.30 defiers with effect 0.90, and 0.30 never-takers with effect 0.20. Everyone benefits from treatment, but the outcome contrast is −0.23 and uptake contrast is +0.10. Their ratio is −2.30. A positive average first stage did not establish individual monotonicity.

## Evidence needed for real work

Request the allocation protocol, actual attendance records, eligibility timing, definition of training, an outcome collection plan, and evidence about alternative pathways and cross-worker spillovers. Identify the assignment unit; individual records do not create independent samples when a supervisor or shift receives the invitation as a group. Establish how missing outcomes are handled before selecting a model. None of this evidence is supplied by the constructed table.

Run `python -m causal_atlas quasi-casebook` or `python -m causal_atlas iv-population examples/iv_training_types.json`. The output preserves the supplied mechanism, compliance masses, local effect, population effect and exact decomposition. For the theorem's scope see [Chapter 9](../chapters/09_instrumental_variables.md); for assumptions and refusal behavior see [the IV design form](../templates/IV_DESIGN_REVIEW.md).

---

# Investigation 5: the jump is real in the table, but what caused it?

## Define a boundary investigation

Imagine a program assigned at a prespecified score threshold. The question concerns the effect at that threshold, not a global average for all cases. This investigation constructs a score cutoff of zero and two outcome functions: `1+2x` below the cutoff and `6-x` at or above it. The slopes differ, but the right and left boundary values are 6 and 1. The jump is exactly five.

Use scores −3, −2, −1, 0, 1, 2 and 3. Their outcomes are −5, −3, −1, 6, 5, 4 and 3. These are arbitrary continuous response units, not binary outcomes or measurements. A triangular window of width four includes all rows with positive kernel weights. Separate local weighted lines recover the boundary intercepts exactly. The zero residual in this construction is a property of the stipulated piecewise-linear functions.

## Compare indistinguishable explanations

World A attributes the outcome jump to the intervention of interest. World B gives that intervention zero effect but applies an additional policy at exactly the same threshold; the additional policy causes the jump. The same observations, score, cutoff and intervention-assignment indicator appear in both worlds.

The local-line estimator returns five in both worlds because it receives the same data. That is not a software defect. It demonstrates why evidence excluding coincident changes belongs to the causal design rather than the curve-fitting routine. Infinite precision in the fit cannot distinguish observationally identical mechanisms.

For a real maintenance policy, collect operating procedures, rollout dates, threshold exceptions, changes in equipment allocation and outcome-recording rules. The relevant check is not “the curve looks smooth”; it is whether the alternative outcome pathway is excluded or explicitly part of the target intervention. A bundled-policy effect can be a legitimate target, but it should be named as such rather than assigned entirely to one component.

## Allow imperfect receipt

The fuzzy case places ten synthetic units at each score. Two take the intervention below the cutoff and seven take it above. Their response is defined as `2+x/10+3d`. The fitted outcome jump is 1.5 and the fitted uptake jump is 0.5. The ratio is three, matching the specified receipt effect.

If uptake is changed to two of ten on both sides, the denominator vanishes and the ratio remains unresolved. The program does not choose another outcome, bandwidth or threshold to recover a finite answer. It preserves the first-stage failure and the original inputs.

## Read the diagnostic output

The point calculator reports intercepts, side-specific slopes, row counts, distinct score counts, omitted IDs, nearest-score gaps and equivalent weights. These allow another implementation to reproduce the arithmetic. It does not produce confidence intervals, select an optimal window, test density manipulation, discover a causal graph, or certify the policy assignment.

Run `python -m causal_atlas rd examples/sharp_rd.json` and `python -m causal_atlas fuzzy-rd examples/fuzzy_rd.json`. Read the unchanged common reference runtime's context alongside the numerical output; neither replaces the other. The [threshold review template](../templates/RD_DESIGN_REVIEW.md) prompts the missing design evidence, and [Chapter 11](../chapters/11_regression_discontinuity.md) derives the exact estimator. The result is useful computational groundwork, not an empirical effect estimate.

---

# Investigation 6: sensitivity and unsupported calculations are part of the result

## Do not optimize the story after seeing the answer

A scientific reference should show a method's limits before a user encounters them in expensive real work. This investigation deliberately creates three limitations: small IV support, curvature under a local-line RD fit, and too few distinct scores. All data are constructed. No tuning criterion, empirical winner or statistical interval is claimed.

For IV, compare uptake means 0.200 and 0.201. The denominator is 0.001. An outcome contrast of 0.0003 gives a ratio of 0.30. Perturb that contrast by 0.001 and the ratio becomes 1.30. The absolute perturbation is small while the effect-scale change is large because division amplifies it. The illustration is deterministic; it provides no first-stage F statistic, uncertainty estimate or calibrated rejection threshold.

A guard of 0.005 refuses the ratio; a guard of zero permits the arithmetic. Neither setting certifies an instrument. Record which setting was selected and why. Do not hide a failed ratio behind an unchanged successful process exit code: the JSON result expressly says `unresolved_first_stage`.

## Curvature creates a different kind of approximation error

Take quarter-step score values from −3 to +3, omitting zero. Below zero the response is `2+x+0.1x^2`; above zero it is `7+x+0.5x^2`. The exact difference of limiting boundary values is five. There is no random disturbance.

Triangular local-line fits at bandwidths 1, 2 and 4 yield 197/40, 191/40 and 41267/9400, approximately 4.925, 4.775 and 4.3901. The larger-window approximation has more curvature bias for this particular construction. A separate NumPy weighted least-squares calculation checks the implementation; it does not validate the causal interpretation.

In real data, making the window smaller changes precision and support as well as approximation bias. We report every requested window, including failures, rather than select the estimate closest to five. Five is available only because the mechanism is constructed. An empirical analyst would not know the true cutoff effect in advance.

## Repeated rows are not continuous support

Supply three observations at score −1 and three at score +1. Two independent lines each require a slope, but each side has only one distinct score. The tool refuses rather than silently fitting an intercept-only model. Repeating each row a hundred times would not add distinct score support.

This is an algebraic requirement, not a complete analysis of discrete-score RD designs. Such designs can need different assumptions and inferential methods; no claim is made that the underlying causal problem is universally impossible. The output identifies the unsupported local-line calculation, not an impossibility theorem about all methods.

## Prepare an auditable handoff

A usable result should show the full bandwidth grid, exact rule for including the cutoff, data exclusions, whether the jump in treatment is supported, and a statement of which diagnostics were not run. Preserve the caller's assumptions as assumptions. Keep approximation error, sampling uncertainty and identification uncertainty separate.

Run `python -m causal_atlas rd-bandwidths examples/rd_bandwidths.json`. Unsupported windows stay in the returned list. The shared context system can retain the associated method restrictions without any new navigation code. Before advancing to a real reproduction, specify the dataset, rights, original assignment rule, sampling unit and inferential method. This checkpoint closes a teaching and computational gap, not the empirical-reproduction or final Causal v1 requirements.

---

# Investigation 07. A treatment changes the next treatment decision

**Question:** What would happen to the outcome if every unit followed two particular treatment decisions, when the first decision changes a covariate that affects the second?

Imagine an equipment maintenance program measured at the start of each interval. At baseline a unit has L0. The team makes an initial choice A0. Later, a new diagnostic L1 is measured. A1 is then chosen based partly on L1. The outcome Y is the probability of a specified defect during follow-up. This example is a synthetic process model; it contains no machine observations.

A naive model that adjusts for the post-A0 diagnostic as though it were an ordinary baseline covariate can remove pathways through which A0 influences Y, or change the population being compared. A longitudinal g-formula instead constructs risks for *intervention regimes* through the intermediate-state transition and the final outcome model. This is not a claim that a real study satisfies exchangeability.

**Run:** `python -m causal_atlas longitudinal examples/longitudinal.json`.

The model specifies baseline mass 1, P(L1=1|A0=0)=1/5, P(L1=1|A0=1)=3/5, and risks `1/10 + A0/10 + A1/5 + L1/10`. It computes a 17/50 risk contrast between the static strategies (1,1) and (0,0). The four output risks and the provenance `stipulated_binary_transition_and_outcome_probabilities` allow independent arithmetic inspection. The result is not an observational estimator.

A real investigation needs documented treatment decisions, past outcomes, intermediate covariate histories, censoring, the strategy a unit could have followed, and support for those histories. It must justify the temporal ordering and conditional exchangeability at *each* decision. If an intermediate state is almost never observed under one treatment history, estimates may rely on unstable extrapolation. Preserve these limitations in the context package with the numerical contrast.

**Reference:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook), Part III on time-varying treatment and treatment-confounder feedback; [chapter 14](../chapters/14_longitudinal_gmethods.md).


## Investigative follow-up

A practical data request would ask for an event log showing when each decision occurred, what diagnostic history was visible at that moment, what intervention was feasible, and what outcomes were recorded or censored. It should also request the data schema, treatment-rule revisions and evidence about changing process conditions. A sensitivity check can ask how the risk contrast changes when the intermediate transition probabilities are changed over a stated range. This is evidence acquisition, not a substitute for collecting observations under the proposed treatment strategies.

---

# Investigation 08. Different groups adopt a change at different times

**Question:** Does a policy change cause better outcomes when adoption is staggered and the comparison group changes over time?

Consider three synthetic groups observed in periods 0, 1, and 2. One is never treated, one begins in period 1, and one begins in period 2. Observed group means are:

| Group | First treated | Period 0 | Period 1 | Period 2 |
|---|---:|---:|---:|---:|
| Never | — | 0 | 1 | 2 |
| Early | 1 | 0 | 3 | 5 |
| Late | 2 | 1 | 2 | 6 |

Assume in this constructed world that untreated outcomes would each rise by one per period. With `not_yet` controls, the early cohort at period 1 can compare with both the never and late groups; at period 2, late is already treated and must not be a control. The calculated change differences are +2, +3, and +3 for early t1, early t2 and late t2 respectively. These are not real policy effects; the assumptions were built into the example.

**Run:** `python -m causal_atlas staggered-did examples/staggered_did.json`.

The tool reports comparison IDs and baseline periods, not merely a pooled coefficient. If every available comparison group is already treated, it returns an unavailable result. An analyst cannot treat a group as an untreated comparison simply because it received treatment in a different year.

For real data, require first-treatment dates, eligible cohort definitions, preperiod outcomes, evidence about anticipation, missingness, differential shocks, and support for credible comparisons. Estimate uncertainty at the level of assignment; if groups are counties or factories, the number of independent assignment units may be much smaller than the number of individual records. A pretrend plot is diagnostic, not proof of future parallel trends.

**References:** [Callaway–Sant’Anna 2021](https://doi.org/10.1016/j.jeconom.2020.12.001) and the [`did` package control-group documentation](https://search.r-project.org/CRAN/refmans/did/help/att_gt.html); [chapter 15](../chapters/15_staggered_adoption_did.md).

---

# Investigation 09. Is improvement carried through an intermediate variable?

**Question:** If a change affects an intermediate diagnostic and then the outcome, how should “through the mediator” be defined?

A synthetic system assigns exposure A, measures an intermediate M, and later records a binary outcome Y. The mediator probability changes from P(M=1|A=0)=1/5 to P(M=1|A=1)=3/5. The outcome risk under an *intervention* on A and M is stipulated as 0.1, 0.3, 0.2, 0.5 for (A,M)=(0,0),(0,1),(1,0),(1,1).

**Run:** `python -m causal_atlas mediation examples/mediation.json`.

The exact standardization produces a total contrast 6/25, an interventional direct component 3/25 under the baseline mediator distribution, and an interventional indirect component 3/25 at A=1. The decomposition is an algebraic property of the declared probability model, not proof that a measured mediator transmitted a real effect.

For actual evidence, measure the mediator at an appropriate time, identify baseline and exposure-induced mediator–outcome confounders, state a feasible stochastic intervention on its distribution, and determine how shifting that distribution would alter other variables. Distinguish stochastic interventional effects from individual-level natural direct/indirect effects; the latter can impose additional counterfactual independence requirements.

Two plausible causal models can reproduce the same regression but imply different mechanistic interpretations. Data that track only A, M and Y cannot resolve every hidden variable or mediator measurement error. A regulator or engineer should not infer an actionable mechanism simply because the mediator coefficient is nonzero.

**References:** [interventional mediation definitions](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496983/); [chapter 16](../chapters/16_interventional_mediation.md).


## Investigation stopping conditions

Do not attribute the output to a mediator if there is no credible intervention that would alter the mediator as modeled, or if the mediator was recorded after the outcome. Ask whether the exposure itself affects how the mediator is measured, and whether shared hidden factors could affect both mediator and outcome. Prespecify the mediator target distribution before comparing outcomes. If two plausible mechanisms fit the records equally well, report ambiguity and propose an experiment aimed at distinguishing the mechanisms rather than declaring the “indirect effect” a physical pathway.

---

# Investigation 10. A treatment on one line affects the nominal control

**Question:** What does a two-line comparison mean if the lines share maintenance staff, temperature control, or a material queue?

Consider two synthetic units in one cluster. Each is either treated (1) or untreated (0), giving joint assignments 00, 01, 10 and 11. We supply both units’ outcomes under each assignment, rather than assuming each outcome depends only on its own treatment.

**Run:** `python -m causal_atlas interference examples/interference.json`.

For focal unit 0, own-treatment effect when the neighbor is untreated is 3/10, and the neighbor's treatment effect while focal 0 remains untreated is 1/5. The first quantity is a direct contrast conditional on neighbor status, while the second is a spillover contrast. Neither is an estimate from observed equipment records. If spillovers are possible, the control unit's outcomes cannot be understood by its own assignment alone.

A genuine experiment needs a declared interference boundary. Machine clusters, shifts, operators, maintenance teams and materials must be mapped to shared resources; treatment timing may create crossover. The unit of randomization may be a cluster rather than a component. A claim of partial interference must be evaluated: people, power supply and ambient conditions sometimes connect supposedly separate sites.

Potential interventions include treating one of two units, treating both, or assigning a fraction of a cluster. These are different policy questions. A single pooled coefficient cannot answer them all without explicit restrictions on how outcomes depend on others’ treatments. Spillover estimates also require a design with appropriate assignment probabilities and dependence-aware uncertainty.

**Reference:** [Hudgens and Halloran, 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/); [chapter 17](../chapters/17_interference_and_spillovers.md).


## Investigation stopping conditions

If cluster boundaries are not independently defined, the estimated spillover target itself may be ambiguous. Before treating two machines as independent, ask whether they share maintenance staff, batch material, electricity, ventilation or process scheduling. A separate control machine supplied by the same cooling loop could be affected even with its own treatment set to zero. Under such conditions, a simpler randomized study with whole-cluster assignment might give stronger information than a complicated correction to a compromised individual-machine comparison. The required design is specific to the actual network.

---

# Investigation 11. Transfer a result to a different population

**Question:** A process appears beneficial in a demonstration facility. Does the same average benefit apply across a different machine fleet?

Two synthetic strata have different response contrasts: the easy stratum improves by 0.10 and the difficult stratum by 0.30. The source is 75% easy and 25% difficult; the target is 25% easy and 75% difficult. Both stratum response functions are stipulated and held fixed between settings. The source average contrast is 0.15, and the target contrast is 0.25.

**Run:** `python -m causal_atlas transport examples/transport.json`.

The tool requires source support for every positive target stratum, reports both averages and refuses unsupported target mass. It is a finite weighted average and cannot demonstrate that response functions are invariant. The result is not evidence that a change actually produces either response in real machines.

Before transporting a real effect, list effect modifiers and how they were measured, source/target eligibility, outcome calibration, intervention versions, machine and material differences, follow-up windows, and selection into the source. Some factors may be unmeasured and matter precisely because the two settings differ. If the target contains a machine class never studied in the source, no amount of weighting can supply its unknown response without extrapolation.

A valid external-validity argument can be stronger than one dataset, but it requires a scientific model of what changes across settings. Preserve the target distribution, source strata, missing support and differences in the mechanism as part of any exported context.

**Reference:** [Bareinboim and Pearl, transportability framework](https://proceedings.mlr.press/v31/bareinboim13a.html); [chapter 18](../chapters/18_transporting_effects.md).


## Investigative evidence packet

For an actual fleet deployment, preserve machine model, maintenance age, production mix, operator mix, climate, load range, intervention dose and measurement system as candidate effect modifiers. Retain both source and target population counts, including missing categories. Identify which variables were measured only after assignment, because treating them as baseline modifiers can change the target. If a source and target use distinct definitions of a defect, a weighted average cannot repair that mismatch. Report assumptions needed to transport the effect separately from those needed to identify it in the source.

---

# Investigation 12. Real historical data can reverse after stratification

**Question:** Do the overall and department-standardized admissions rates tell the same story in the historical Berkeley data?

> Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.

A causal interpretation is not identified by these counts. The table is observational, includes only six departments, lacks detailed applicant characteristics, and does not specify a well-defined intervention on sex. Conditioning on department answers a different descriptive question, and application choices are themselves selected. The adjusted contrast is not proof that bias was absent or that a causal effect of sex was favorable. Nor does the crude gap alone establish intentional discrimination in each department.

> Historical UCBAdmissions numerical data and derived results are unavailable in this public derivative pending redistribution clearance.

**Sources:** [R base UCBAdmissions documentation](https://cloud.r-project.org/doc/manuals/r-release/packages/datasets/refman/datasets.html); [public numerical table reproduction](https://utstat.utoronto.ca/~brunner/oldclass/312f22/lectures/312f22ContingencyTables-R.pdf); [Rdatasets rights notice](https://github.com/vincentarelbundock/Rdatasets). The numerical comparison is reproducible but is not a causal study replication.

---

# Investigation 13. A narrow confidence interval does not prove a cause

**Question:** What extra information is required to turn two independently observed binary outcome proportions into a causal effect claim?

A constructed case reports 60 successes out of 100 observations in one group and 75 out of 100 in another. The difference is +0.15. The large-sample normal interval from the tool is about [0.02185, 0.27815] at a nominal 95% confidence level under **independent binomial sampling** assumptions. The program can compute this accurately even if the treatment assignment process is entirely unknown.

**Run:** `python -m causal_atlas binomial-interval examples/binomial_interval.json`.

An identification analysis asks whether treatment status is exchangeable with unobserved potential outcomes, whether the outcome was measured comparably, and whether the groups are drawn from the intended target. A perfect interval for an observational difference remains an interval for the *association*, not an intervention effect, if confounding or selection cannot be ruled out.

The method also is not a universal confidence interval. It uses a Wald approximation which can have inadequate coverage near 0 or 1 and ignores clustering and pairing. The tool rejects extreme proportions and small groups, but this does not guarantee coverage under arbitrary real data. A factory trial randomized by machine would need an analysis that respects machine-level assignment; 10,000 individual parts from two machines are not 10,000 independent randomization units.

Record which uncertainty sources are counted and which causal uncertainties remain unquantified. An evidence-preserving context package must carry both; it should not flatten a standard error and a causal verdict into one confidence number.

**Reference:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook), treatment of random variability and causal identification; [chapter 20](../chapters/20_sampling_and_uncertainty.md).


## What the interval cannot establish

Even a nominal interval that excludes zero can coexist with severe unmeasured confounding. An observational association can become statistically “significant” with enough data despite being a poor estimate of a causal effect. Conversely, a randomized small experiment with an inconclusive interval does not prove the intervention has no effect. Ask for the original assignment mechanism, baseline comparability, outcome definition, missingness, clustering and chosen sampling units before interpreting the contrast. If key design information is absent, the result should be labeled a descriptive difference with an approximate interval, not a verified treatment effect.

---

# Source register

# Source register

Eight v0.1 source cards are retained unchanged. Eight new primary-source portions were read for v0.2. No whole paper, publisher image, or external dataset is mirrored. Source review is by this assistant, not independent human verification.

## DAGITTY

[DAGitty reference manual](https://jtextor.r-universe.dev/dagitty/doc/manual.html)

Authors: Johannes Textor; Benito van der Zander; Ankur Ankan. Version: 0.3-4, accessed 2026-11-12.

Inspected: Covariate Adjustment Sets; d-Separation; Variable Statuses.

Status: primary_portion_checked_by_assistant. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## EW2014

[Endogenous Selection Bias: The Problem of Conditioning on a Collider Variable](https://pmc.ncbi.nlm.nih.gov/articles/PMC6089543/)

Authors: Felix Elwert; Christopher Winship. Version: 2014.

Inspected: §2 Identification versus estimation; §3 DAGs in brief; §4 sources of association.

Status: primary_portion_checked_by_assistant. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## HR2006

[Estimating causal effects from epidemiological data](https://pmc.ncbi.nlm.nih.gov/articles/PMC2652882/)

Authors: Miguel A. Hernán; James M. Robins. Version: 2006.

Inspected: Computation of causal effects via (conditional) randomisation; Standardisation; The randomised experiment paradigm for observational studies.

Status: primary_portion_checked_by_assistant. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## HR2016

[Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/)

Authors: Miguel A. Hernán; James M. Robins. Version: 2016.

Inspected: Table 1 component names; Emulating the target trial; Defining time zero; Causal contrasts of interest.

Status: primary_portion_checked_by_assistant. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## NETWORKX

[NetworkX is_d_separator documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.d_separation.is_d_separator.html)

Authors: NetworkX developers. Version: stable documentation accessed 2026-11-12.

Inspected: Signature, return value, and exceptions; version of the installed oracle is recorded separately.

Status: primary_portion_checked_by_assistant. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## PEARL2010

[An Introduction to Causal Inference](https://pmc.ncbi.nlm.nih.gov/articles/PMC2836213/)

Authors: Judea Pearl. Version: 2010.

Inspected: §2.1; §3.1 Definition 1; §3.2.3 Corollary 1; §3.3.1 Definition 3; §4.1–4.3.

Status: primary_portion_checked_by_assistant. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## WC2010

[Invited Commentary: Positivity in Practice](https://pmc.ncbi.nlm.nih.gov/articles/PMC2877454/)

Authors: Daniel Westreich; Stephen R. Cole. Version: 2010.

Inspected: Opening definition and structural/random nonpositivity discussion; Table 2 discussion.

Status: primary_portion_checked_by_assistant. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## WHATIF

[Causal Inference What If author resource page](https://miguelhernan.org/whatifbook)

Authors: Miguel A. Hernán; James M. Robins. Version: author landing page accessed 2026-11-12.

Inspected: Landing-page scope and links only; book chapters not inspected in this build.

Status: navigation_only_not_full_text_review. Rights boundary: Bibliographic metadata and link only; publisher terms apply.

## AS2015

[Moving towards best practice when using inverse probability of treatment weighting](https://pmc.ncbi.nlm.nih.gov/articles/PMC4626409/)

Authors: Peter C. Austin; Elizabeth A. Stuart. Version: 2015.

Inspected: §2.2 equations for unnormalized and normalized IPW; §4.1 balance diagnostics.

Status: primary_portion_checked_by_assistant. Rights boundary: CC BY-NC-ND notice on page; metadata, original brief summary and link only

## CH2008

[Constructing Inverse Probability Weights for Marginal Structural Models](https://pmc.ncbi.nlm.nih.gov/articles/PMC2732954/)

Authors: Stephen R. Cole; Miguel A. Hernán. Version: 2008.

Inspected: Abstract; Positivity; Weight truncation as a means to tradeoff bias and variance.

Status: primary_portion_checked_by_assistant. Rights boundary: All rights reserved notice; no full text or third-party data copied

## KURZ2022

[Augmented Inverse Probability Weighting and the Double Robustness Property](https://pmc.ncbi.nlm.nih.gov/articles/PMC8793316/)

Authors: Christoph F. Kurz. Version: Online 2021; issue 2022; correction notice retained.

Inspected: AIPW Estimator; correction note; Discussion and Conclusion.

Status: primary_portion_checked_by_assistant. Rights boundary: CC BY-NC notice; local original summary and derivation only; no article or data mirror

## CORR2022

[Corrigendum to Augmented Inverse Probability Weighting and the Double Robustness Property](https://journals.sagepub.com/doi/10.1177/0272989X221075672)

Authors: Medical Decision Making / correction to Christoph F. Kurz. Version: 2022-01-17.

Inspected: Correction paragraphs identifying the control-group augmentation term; author assurance is attributed, not independently established.

Status: primary_portion_checked_by_assistant. Rights boundary: CC BY-NC notice; bibliographic link and original brief notice only

## TIME2016

[Specifying a target trial prevents immortal time bias and other self-inflicted injuries](https://pmc.ncbi.nlm.nih.gov/articles/PMC5124536/)

Authors: Miguel A. Hernán; Brian C. Sauer; Sonia Hernández-Díaz; Robert Platt; Ian Shrier. Version: 2016.

Inspected: §2 Emulating the target trial; §3.1 and §3.4 time-zero failures.

Status: primary_portion_checked_by_assistant. Rights boundary: Link and original bounded summary only; no source text mirrored

## NC2010

[Negative Controls: A Tool for Detecting Confounding and Bias in Observational Studies](https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/)

Authors: Marc Lipsitch; Eric J. Tchetgen Tchetgen; Ted Cohen. Version: 2010.

Inspected: Abstract; Definitions of negative controls; Discussion paragraphs on detection and bias magnitude.

Status: primary_portion_checked_by_assistant. Rights boundary: Link and original bounded summary only

## MI2009

[Multiple imputation for missing data: potential and pitfalls](https://pmc.ncbi.nlm.nih.gov/articles/PMC2714692/)

Authors: Jonathan A. C. Sterne and colleagues. Version: 2009.

Inspected: Consequences of missing data; Box 1; What is multiple imputation; Pitfalls.

Status: primary_portion_checked_by_assistant. Rights boundary: CC noncommercial notice; no publication/data mirror

## CS2020

[Difference-in-Differences with Multiple Time Periods](https://arxiv.org/html/1803.09015v4)

Authors: Brantly Callaway; Pedro H. C. Sant’Anna. Version: arXiv v4, 2020-12-01; journal 2021.

Inspected: Introduction; §2.3 Assumptions 3–6; §2.4 Remark 3.

Status: primary_portion_checked_by_assistant. Rights boundary: Author-deposited version; link and original brief summary only; full paper not redistributed

## Equation rendering caution

The Kurz correction notice is retained as source evidence. The estimator is implemented from the locally derived residual form. No claim is made that every HTML-rendered equation, the source code supplement, or the empirical results in that article were independently reproduced. The constant-outcome identity and separate rational enumeration check the local implementation.


## v0.3.0 quasi-experimental source additions

Original descriptions, equations and worked cases are separated from source-specific summaries. No third-party full text is mirrored. Access failures below were not silently promoted to full-text checks.

### IA1991

**Identification and Estimation of Local Average Treatment Effects**. Joshua D. Angrist; Guido W. Imbens. NBER Technical Working Paper 118, December 1991; inspected version, not the later journal typography. DOI: `10.3386/t0118`.

[Primary source](https://www.nber.org/system/files/working_papers/t0118/t0118.pdf)

Inspected: Sections 3-4: Conditions 1-2, Theorem 1 and binary ratio, printed pp. 5-10. Selected parsed PDF passages; image inspection of printed pp. 7 and 10. No full empirical replication.

Checked 12 November 2026 by the assistant. Independent review: not performed. Rights: metadata, original short descriptions and links only.

### SS1997

**Instrumental Variables Regression with Weak Instruments**. Douglas Staiger; James H. Stock. Econometrica 65(3), 1997, 557-586. DOI: `10.2307/2171753`.

[Primary source](https://scholar.harvard.edu/files/stock/files/instrumental_variables_regression_with_weak_instruments.pdf)

Inspected: Introduction, pp. 557-559. Parsed PDF introduction; web screenshot failed with 503 twice. No visual equation audit or full theorem review.

Checked 12 November 2026 by the assistant. Independent review: not performed. Rights: metadata, original short descriptions and links only.

### CT2022

**Regression Discontinuity Designs**. Matias D. Cattaneo; Rocio Titiunik. Annual Review of Economics 14, 2022, 821-851. DOI: `10.1146/annurev-economics-051520-021409`.

[Primary source](https://rdpackages.github.io/references/Cattaneo-Titiunik_2022_ARE.pdf)

Inspected: Sections 2.1-2.2 (pp. 824-828) and 4 opening / 4.1 (pp. 842-843). Selected parsed passages; page images 824, 826 and 827 checked. Not a whole-literature audit.

Checked 12 November 2026 by the assistant. Independent review: not performed. Rights: metadata, original short descriptions and links only.

### CCT2014

**Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs**. Sebastian Calonico; Matias D. Cattaneo; Rocio Titiunik. Econometrica 82(6), 2014, 2295-2326. DOI: `10.3982/ECTA11757`.

[Primary source](https://rdpackages.github.io/references/Calonico-Cattaneo-Titiunik_2014_ECMA.pdf)

Inspected: Introduction, pp. 2295-2297, local-polynomial and bias-corrected inference discussion. Parsed introduction and page image 2296 inspected; no reproduction of coverage tables or robust-inference implementation.

Checked 12 November 2026 by the assistant. Independent review: not performed. Rights: metadata, original short descriptions and links only.

### GI2014

**Why High-order Polynomials Should not be Used in Regression Discontinuity Designs**. Andrew Gelman; Guido Imbens. NBER Working Paper 20405, August 2014. DOI: `10.3386/w20405`.

[Primary source](https://www.nber.org/papers/w20405)

Inspected: Primary-site indexed abstract. Direct page/PDF access returned 403; indexed primary abstract only, not full text.

Checked 12 November 2026 by the assistant. Independent review: not performed. Rights: metadata, original short descriptions and links only.

### MC2007

**Manipulation of the Running Variable in the Regression Discontinuity Design: A Density Test**. Justin McCrary. NBER Technical Working Paper 334, January 2007; journal version 2008. DOI: `10.3386/t0334`.

[Primary source](https://www.nber.org/papers/t0334)

Inspected: Primary-site indexed abstract and publisher abstract. Direct NBER PDF returned 403. Scope limited to indexed primary abstract and publisher abstract; test equations not audited.

Checked 12 November 2026 by the assistant. Independent review: not performed. Rights: metadata, original short descriptions and links only.

### IL2007

**Regression Discontinuity Designs: A Guide to Practice**. Guido Imbens; Thomas Lemieux. NBER Working Paper 13039, April 2007; journal version 2008. DOI: `10.3386/w13039`.

[Primary source](https://www.nber.org/papers/w13039)

Inspected: Primary-site indexed abstract and publication metadata. Direct PDF returned 403; indexed primary abstract only. Full practice guide not claimed reviewed.

Checked 12 November 2026 by the assistant. Independent review: not performed. Rights: metadata, original short descriptions and links only.


## v1.0.0 content edition — source navigation and access limits

These cards are bounded to the stated inspected portion. Most original papers are not fully reviewed and no third-party full text is mirrored.

### causal-atlas:source:HRBOOK

[Published record](https://miguelhernan.org/whatifbook)  
**Inspected:** Book author page describing Parts I-III and downloadable materials; not entire book text  
**Status:** `author_overview_only`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:CS2021

[Published record](https://doi.org/10.1016/j.jeconom.2020.12.001)  
**Inspected:** Journal publisher abstract only  
**Status:** `publisher_abstract_only`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:DIDR

[Published record](https://search.r-project.org/CRAN/refmans/did/help/att_gt.html)  
**Inspected:** att_gt description, comparison policy and anticipation parameter documentation  
**Status:** `method_documentation_checked`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:HH2008

[Published record](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/)  
**Inspected:** Abstract and open article overview of interference effects and partial interference  
**Status:** `selected_html_portions_checked`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:MED2020

[Published record](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496983/)  
**Inspected:** Full HTML section defining interventional direct and indirect effects; not complete manuscript audit  
**Status:** `selected_html_effect_definitions_checked`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:BP2012

[Published record](https://ojs.aaai.org/index.php/AAAI/article/view/8232)  
**Inspected:** Published abstract and metadata; graphical proof and full algorithm not reviewed  
**Status:** `publisher_abstract_only`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:BP2013

[Published record](https://proceedings.mlr.press/v31/bareinboim13a.html)  
**Inspected:** Conference publication abstract only  
**Status:** `publisher_abstract_only`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:UCBR

[Published record](https://cloud.r-project.org/doc/manuals/r-release/packages/datasets/refman/datasets.html)  
**Inspected:** UCBAdmissions description, format and count totals for six departments  
**Status:** `official_dataset_manual_checked`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:RDL

[Published record](https://github.com/vincentarelbundock/Rdatasets)  
**Inspected:** README Licensing section: source code GPL-3; underlying datasets licensing unresolved by distributor  
**Status:** `repository_rights_notice_checked`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:NEG2010

[Published record](https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/)  
**Inspected:** Abstract and exposure/outcome negative controls distinction in accessible HTML  
**Status:** `selected_html_portions_checked`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.

### causal-atlas:source:BMJ2022

[Published record](https://www.bmj.com/content/378/bmj-2022-071108)  
**Inspected:** Introduction; target-trial protocol components, baseline eligibility and follow-up excerpts  
**Status:** `selected_full_html_portions_checked`  
**Reviewed by:** assistant only; independent science review absent. **Raw document archived:** no.


