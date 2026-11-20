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
