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
