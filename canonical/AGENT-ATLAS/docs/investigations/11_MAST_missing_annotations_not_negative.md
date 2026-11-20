# Investigation 11 — A dataset annotation marked null is not evidence of absence

This case uses **three constructed rows**, formatted to resemble the publicly documented 14-code MAST-Data annotation schema. One label code is known for each row; another code is missing in all three. Treating missing as a negative would claim an apparent zero failure frequency on that code. The correct program reports `known=0`, `unknown=3` and `fraction_positive_among_known=null`.

The MAST dataset card documents 1,642 traces from several frameworks and tasks, with model-judge annotations and a separate small human-annotation study. The current example is **not drawn from those 1,642 traces** and cannot establish any empirical prevalence. In addition, the human-annotation study reportedly changed the taxonomy between rounds: merging incompatible code versions would be a second source of invalid statistics.

Before using an actual MAST corpus in Agent Atlas, acquire the exact pinned source bytes under its stated rights, verify the original hash and row counts, inspect the annotation version and missingness patterns, decide how to stratify by framework/task/model, and independently review a subset. The model's own labels are research hypotheses, not human-verified failures or causal mechanisms.

**Sources:** MAST NeurIPS abstract and the mcemri/MAST-Data public dataset card. This release reviewed documentation only and loaded zero original MAST traces.
