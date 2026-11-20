# 41. Renewable variability, seasonality and adverse scenarios

**Area:** Survival Systems · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

A single annual solar-energy average cannot establish that a system survives an extended winter storm or a series of cloudy days. Weather, resource availability and demand are temporally correlated; a high mean generation figure may hide a prolonged zero-output period. A robust first step is to preserve ordered time series of resource and demand under named scenarios, compute shortages and reserve depletion, then ask what range of unobserved conditions remains. The worst outcome among a small set of user-authored scenarios is not a statistical worst case for the local climate. Actual resilience engineering needs representative long-term measured data, correlation, uncertainty, equipment failures and plans for replenishment. The source data should include timestamp, measurement units, location/conditions, original bytes, sensor and version rather than only smooth charts.

## Equation, symbols and dimensional units

`For each scenario s: U_s = sum_i unmet_load_(s,i)*Delta t_i; U_worst_supplied=max_{s in S} U_s. This is a deterministic scenario statistic, not an expected shortage or a bound over every possible scenario.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

The max operation compares only the scenarios actually provided. Probability of failure requires a defensible sampling distribution over events, not a collection of plausible anecdotes. A chronological battery model must respect earlier charging and depletion; reordering the same daily totals can change unserved energy. A simulation that reports 0 unmet energy but lacks an islanding inverter, protection or a valid start condition cannot establish real uptime.

## Hand reconstruction and independent calculation

Compare two invented two-hour cases with 2 kWh initial capacity, a 1 kW discharge cap, and 0.9 efficiency: (A) load 1 kW, generation 2 kW; (B) load 3 kW, generation 0. Run both and identify the case with greater unserved energy. Add a third case with a two-day sequence to show why the order of wind/solar supply matters.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

“Worst of our tests” is not “worst imaginable weather.” Without actual resource measurement and equipment state, the profile cannot determine the safety of a site. Do not extrapolate from 2–3 illustrative intervals to multi-season survival.

## Life safety and operational boundary

This is scenario arithmetic only; emergency preparedness decisions require site data, qualified design and alternate safe evacuation/assistance plans.

## Source navigation and preservation debt

- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **DOE Solar Photovoltaic Technology Basics:** https://www.energy.gov/cmei/systems/solar-photovoltaic-technology-basics — Solar cell, module, arrays, and DC/AC system concept

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
