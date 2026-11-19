# Causal Atlas depth manual 0.2.0

Eight original reference chapters and three investigations. This persistent reading copy retains source links. For relative template/record links, use the complete source archive. No real data or independent scientific validation is claimed.



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
