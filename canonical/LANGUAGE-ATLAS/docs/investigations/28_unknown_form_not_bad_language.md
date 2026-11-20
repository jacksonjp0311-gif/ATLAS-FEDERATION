# Investigation 28: A missing lexicon entry is unknown, not ungrammatical

**Origin:** constructed offline study unless otherwise stated. No human participant or original media data was acquired.

The toy PCFG recognizes “birds sing” and assigns zero probability to “birds speak” because `speak` is not in its lexicon. If a teacher concluded that the second sentence is ungrammatical English, they would be mistaking a model limitation for a human linguistic judgment.

The same epistemic distinction appears in finite morphology, segmentation, and semantics: a form not recorded in a dataset is not disproven; a translation missing from one reference is not inherently wrong; a feature unknown for a language is not Boolean false. A preservation archive must keep these states distinct at every processing stage.

**Method:** build negative controls that are linguistically valid but absent from the stipulated grammar, and compare parser acceptance to independently evaluated speaker judgments on permissioned data. No speaker judgments were obtained here.

**Evidence status:** This is a reproducible bounded algorithm/method example. Human-language validity and independent review are not established.
