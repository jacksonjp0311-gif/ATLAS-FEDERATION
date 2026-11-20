# Investigation 24 — Refusal of stale or invalid sensor input is not a safety certificate

A synthetic five-step trace asks an offline supervisor to evaluate commands. The first sensor reading is fresh, valid and consistent, so the requested output is retained. The next reading is stale; the third is flagged invalid; the fourth has an innovation larger than the caller's threshold; the fifth is fresh and passes. The program blocks exactly three of the five commands and substitutes a *caller-provided* fallback.

This deterministic calculation never actuates a device. A zero fallback can be dangerous on some real processes; the application must identify an actual safe state and independent physical interlocks. Sensor freshness does not prove accuracy, and a small innovation can result from shared model/sensor bias. No hazard analysis, safety-rated watchdog, emergency-stop function, timing deadline guarantee or industrial standard compliance is claimed. The only verified result is explicit software rejection under a declared policy.

A useful evidence packet would record sensor capture timestamps, input provenance, clock drift, innovation model, thresholds, fault rates, actuator commands versus observed actuation, safe-state feasibility and operator oversight. These data are not present in the synthetic trace.
