# 46. Agent evaluation: distinguish performance from a memorized answer

An agent can perform better on a known benchmark without becoming more capable on new problems. The benchmark may contain examples leaked into training or retrieved context, brittle evaluators, unrepresentative tasks, incomplete environments or favorable retry policies. A reliable claim requires the question “better at what, under which conditions, compared with what, and how was success established?” as well as a documented answer.

## Evaluation design

Define a task distribution, environment version and initial conditions. Choose independent tasks not seen in training, development, prompt design or memory construction. Precommit the success oracle and failure categories. Hold constant the model, tool capability, cost and time budget when possible; otherwise report the differences. Use paired tasks to reduce task-difficulty noise, but count every uncertain, cancelled or incomplete run distinctly rather than silently treating it as success or removing it from the denominator.

A task outcome usually has levels: a model-generated self-report; successful submission/receipt; locally verified artifact; and independently measured external effect. A scoring script can have defects. Independent human or domain review should audit a sample of *both passes and failures*, especially for tasks where many correct solutions could differ syntactically. OpenAI's February 2026 analysis of SWE-bench Verified documents both contaminated tests and tests that can reject functionally correct solutions. That source concerns a particular benchmark, not a universal proof about all agent benchmarks; it illustrates why evaluator quality must be audited rather than assumed.

## Paired binary outcomes

Suppose the same n tasks are attempted by baseline B and candidate C, producing success/failure labels. The discordant pair counts matter: `n10` = candidate-only passes, `n01` = baseline-only passes. Under the null that the two methods are exchangeable on discordant pairs, an exact sign-test/McNemar-style calculation can describe the imbalance. A p-value from caller-supplied labels is not evidence that the labels are correct or that the trial was blinded. Repeated prompt tuning on the test set invalidates simple test-set inference.

For continuous metrics, keep units and dependencies: elapsed wall time, provider time, dollars, tokens, CPU, energy and operator labor are not substitutable without explicitly chosen weights. A longer reasoning trace may consume more resources while improving one narrowly defined success measure. A lower latency result can be confounded by model caching or changing external service load. Publish uncertainty and confidence intervals appropriate to the actual sample and correlation structure, not only best-run numbers.

## What proves learning

A memory or routing change is a *candidate improvement* until it passes an independent, precommitted evaluation on unseen tasks with a verified outcome. If memory stores the task's gold solution, a higher score is leakage. If an evaluator changes between baseline and candidate, an apparent improvement may reflect rubric drift. If a task was excluded after failure, the denominator changed. Preserve all these conditions in the evidence packet.

**Sources:** OpenAI, *Why we no longer evaluate SWE-bench Verified* (23 Feb 2026), https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ ; Liu et al., *AgentBench*, ICLR 2024, https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html ; MAST 2025, publisher abstract. This project has not run an independent live held-out model evaluation.
