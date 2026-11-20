# 30. Energy economics, discounted cost, and LCOE

**Area:** Economics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Levelized cost of energy compares discounted lifecycle cost to discounted energy output under a specified project model. It can be useful for alternatives but does not by itself value when electricity is available, how reliably it meets peak demand, local grid constraints or the external impacts of a project. Capital cost, financing, capacity factor, fuel, maintenance, decommissioning, salvage and policy can change results. Real and nominal discount rates must not be mixed with inflation assumptions. A single cost figure cannot represent affordability for every community or determine technology desirability without service and risk analysis.

## Fundamental relationship, symbols and SI dimensions

`LCOE=(C0+Σ_t C_t/(1+r)^t)/(Σ_t E_t/(1+r)^t), in currency/kWh if E in kWh and currency units consistent.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Discounting expresses time preference and financing assumptions by placing future costs and output on a common present-value basis. The formula is an accounting ratio, not a physical law. If production is zero the denominator vanishes, making a numeric cost per kWh undefined. A model that reports LCOE without the generation series, assumptions and full time horizon is not reconstructible.

## Reconstruct the example without external AI

Choose illustrative capital cost 1000 units and ten years of 100 units annual cost and 1000 kWh output, with discount .05. Recompute using the reference code and then reduce generation 30% to see the increase. Do not present synthetic currency units as market prices.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A lower LCOE does not automatically mean lower total system cost. Firm capacity, grid reinforcement, reliability and external impacts are outside this simple formula.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Levelized Cost of Electricity Glossary](https://www.eia.gov/tools/glossary/index.php?id=levelized_cost) — inspected: Definition of real levelized cost; project-specific assumptions needed
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
