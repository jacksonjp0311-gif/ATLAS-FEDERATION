## 21 — Cost-model drift, regret, and explain-plan evidence

An optimizer selecting a low estimated-cost plan can be wrong when statistics, cost parameters, or workload characteristics have drifted. For candidate plans `i`, define predicted costs `c_i` and separately observed costs `t_i` on the **same controlled workload**. The chosen plan is `argmin_i c_i`. A simple regret diagnostic is `regret = t_chosen - min_i t_i >= 0`. This quantifies loss from the estimator on the supplied observations; it does not measure anything by itself.

**Worked example:** predicted costs `(1,2)` choose plan 0, while controlled measured costs `(100,1)` imply regret `99` measured-cost units. `db_extended.plan_regret` computes that number and marks model certification `False`. In a real engine, changing only the plan must preserve the **bag-semantic output**; verify query-result equality separately before comparing latency. SQLite `EXPLAIN QUERY PLAN` is a human-readable debug interface, not a stable machine protocol; its output can change between releases.

**Procedure:** compare index/scan model output against actual SQLite planner decisions on a constructed dataset; use `ANALYZE`, record SQLite version and index definitions, and run several isolated repetitions if evaluating timings. Keep predicted, observed and independently verified result sets separate. Do not invent measurements where no physical query execution occurred.

**Negative control:** a plan that runs faster but returns a different set or multiplicity of rows is invalid; a cost curve from estimated row counts cannot be used as if it were measured latency. Parameter sensitivity, warm-cache bias, blocked transactions and plan output instability require explicit handling.

**Sources:** `https://www.sqlite.org/eqp.html`, `https://www.sqlite.org/optoverview.html`, PostgreSQL `https://www.postgresql.org/docs/current/sql-explain.html`.
