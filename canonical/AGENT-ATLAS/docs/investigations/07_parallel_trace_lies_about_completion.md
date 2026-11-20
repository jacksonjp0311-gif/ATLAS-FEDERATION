# Investigation 07 — Two parallel workers, one missing verification

**All event metadata below are invented for this case.** A root agent span runs from 0 to 250 milliseconds. Subagent A runs 20–160 ms; Subagent B runs 40–145 ms; a tool span under A reports success with a provided evidence reference; a model span under B returns output; an incomplete verifier runs 165–200 ms. The parent UI claims success.

`analyze_trace` verifies parent lineage, clock ordering and interval containment. The root elapsed time is 250 ms. Naively adding the subagent durations gives 245 ms, but they overlapped heavily; this is not their combined contribution to wall time. The complete sum across nested spans is even less meaningful as elapsed duration. The analyzer records a `success_claim_without_verification_record` diagnostic and an `incomplete` status. Its output sets `semantically_verified=false` regardless of the superficial completion claim.

What this **does** prove: supplied metadata are internally coherent and there is no successful evidence-bearing verifier span in the declared trace. What it **does not** prove: the workers' solutions were wrong or the final goal was unmet. The verifier may have been omitted from logging. The next task is to inspect the independently observable goal predicates, final artifact hash, test results, and evaluator identity.

A trace with several concurrently running workers must distinguish clock domains, top-level elapsed time, child operation time, and actual token/cost meters. Parent spans include their children, so summing them is not a cost measure. The schema deliberately contains no untrusted raw commands or prompts.

**Source:** OpenAI Agents tracing docs on hierarchical spans and concurrent subagent timing. This example is not an exported OpenAI trace.
