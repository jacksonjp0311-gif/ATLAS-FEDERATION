# Control Atlas v1 candidate — exact future experimental handoff

1. Obtain authorized OpenMCT v2 raw file bytes through the original Mendeley listing (DOI 10.17632/5xvg43r9r8.2), preserve SHA-256 and original license/filename, and run the offline `openmct-review` command. The current archive contains no raw log.
2. Verify columns, sampling semantics, timestamps, motor/encoder calibration, applied PWM, any clock resets, DMM uniqueness and delayed reads against the publisher's procedure; do not assume the strict parser works on all raw logs without checking actual bytes.
3. Select a holdout split by time and preferably by entire run. Run open-loop and closed-loop system-identification designs separately; evaluate excitation, sample/closed-loop bias, saturation, one-step/free-run prediction, perturbations and parameter uncertainty.
4. Have a qualified engineer assess which claims are supported, what physical bounds are empirical, and what tests remain before hardware deployment.
5. Confirm the package on Windows only at the final integrated transfer stage, with external I/O disabled by default.

**Status now:** documentation and software tooling complete as a candidate; experimental raw-data fit and external scientific acceptance not performed.
