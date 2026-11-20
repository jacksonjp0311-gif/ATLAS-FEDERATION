# 44. Genealogical and geographic dependence in language typology

Cross-linguistic samples violate naïve statistical independence in several ways. Language varieties share inherited properties through common ancestry, borrow innovations through contact, and respond to social/ecological contexts. Databases overrepresent languages with extensive scholarship and may encode categories differently between studies. An observation count is therefore neither a random sample of all human languages nor a direct statement of a universal probability.

The World Atlas of Language Structures introduction explicitly considers genealogical and areal diversity when selecting reference samples. It notes missing documentation and differing representation among families. Any feature survey should preserve the definition of each variable, original judgments, source pages, language IDs and genealogical classification revision. Missingness should be kept distinct from absence.

## Two descriptive estimands

A naïve known-value fraction weighs each observed language once. An equal-family fraction weighs each represented family's internal known-value fraction once. More sophisticated estimators may account for phylogenetic trees, contact networks, geography, measurement error and unequal sampling weights. None can be inferred merely from a database's family names. The two simple fractions serve a **sensitivity check**: if they differ markedly, assumptions about which unit receives equal weight are consequential.

`typology_by_family` returns both values and preserves unknown feature counts. It validates one row per language ID and Boolean/unknown feature values. Its family labels are caller-supplied, not verified phylogeny. Equal weighting can itself distort a population estimand when family classification is disputed or many families lack data. Areal correlation is not removed by equal family weighting.

## Case-based explanation

If three related languages show a feature and one unrelated language does not, an observed 3/4 rate can become a 1/2 equal-family rate. If the missing values are more common in one family, both numbers can be biased. A future analyst should state which population is being estimated and why a particular sampling scheme provides warranted inference.

**Sources:** WALS Introduction by Comrie, Dryer, Gil and Haspelmath; CLDF source/provenance conventions. Both are scoped publicly available publisher references; this release includes no original typological dataset rows.
