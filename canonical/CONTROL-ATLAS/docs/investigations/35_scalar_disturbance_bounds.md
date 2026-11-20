# Investigation 35 — One-dimensional interval certificate and its limits

For `x[k+1]=g x[k]+w[k]`, assume `|x|≤r`, `|w|≤d`, and ideal feedback command magnitude `|u|=|k x|` capped at U. The interval is robust invariant under the supplied scalar model exactly when `|g|r+d≤r`, and requested inputs remain admissible exactly when `|k|r≤U`. These are worst-case inequalities over independent closed intervals, not statistical probabilities.

With stipulated `g=0.7`, `r=1`, `d=0.2`, `k=0.2`, `U=0.3`, the worst successor magnitude is 0.9 and the actuator command bound 0.2. The model condition passes. Change `g` to 1.1 without updating the interval and the invariant candidate fails. This does not establish safety or failure for any real machine. The actual plant may have an unmodeled state, delay or different disturbance bound, and physical units of the state matter for interpretation.

Use this as a falsifiable mathematical worked example: demand source and derivation for g, k and d before treating its status as more than a calculation. The higher-dimensional certificate generalizes the same philosophy, not every possible control system.
