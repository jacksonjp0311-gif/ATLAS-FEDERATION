# Investigation 06. A perfectly fitted teaching plant may still identify nothing real

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

Supply an authored noise-free sequence satisfying `x[k+1]=0.8*x[k]+0.3*u[k]` over several deliberately varied input values. A two-column least-squares fit recovers a and b and gives a residual sum of squares near zero. That is correct for the constructed dataset, not evidence that a manufacturing process has those dynamics. The data were generated from the same model being fitted, so no independent model validation has occurred.

Set every input and state to zero and infinitely many a/b pairs reproduce the same data. The regression matrix is rank deficient; a numerical solver could return finite coefficients but they would not be identified. The Atlas refuses this case. In closed-loop physical data, input commands may correlate with disturbances, biasing naive least squares even when the matrix has full rank. A credible study should use safe excitation, calibration, timestamp synchronization and separate testing periods across operating regimes.

**Source:** MathWorks System Identification Workflow and data-quality requirements. **Refusal:** in-sample fit is not a causal or robust plant identification certificate.
