# 57. Two-state, two-sensor observer uncertainty without hidden safety claims

A model-based state estimate `xhat` is not the physical state `x`. For a linear sampled plant `x[k+1]=A x[k]+B u_applied[k]+w[k]`, observations `y[k]=C x[k]+v[k]`, and observer `xhat[k+1]=A xhat[k]+B u_applied[k]+L(y[k]-C xhat[k])`, the error `e=x-xhat` obeys

`e[k+1]=(A-LC)e[k]+w[k]-L v[k]`,

**but only** when the plant and observer use the same *known applied* input, identical time indices, and known A,C,L. The `u` term cancels exactly under that premise; if the actuator applies an unknown lagged value while the observer uses its requested command, this equation is wrong. This edition implements **2×2 A, C and L**, corresponding to two-dimensional state and two measured outputs.

Given componentwise **hard** bounds `|e0|≤E0`, `|w|≤W`, `|v|≤V`, the deterministic recurrence `E[k+1]=|A-LC| E[k]+W+|L|V` bounds each component for a requested finite horizon. An arbitrary Gaussian standard deviation is **not** a hard bound. The implementation checks every input matrix, refuses nonfinite/negative bounds, and returns the radius sequence, F=A−LC and qualifying assumptions. The algorithm operates on normalized/stated unit-compatible states; if states or output channels have different physical dimensions, the matrix entries and bounds must carry a dimensionally valid identification model.

## Distinguish finite bounds and sufficient long-term conditions

A finite sequence of radii proves **only** that the stipulated model's sampled observer error lies within the numerical envelope through the requested steps. The simple condition `max_i Σ_j |F_ij|<1` is a sufficient contraction criterion; when it passes, the code reports a conservative common infinity-norm radius `max_i(W+|L|V)_i/(1-max_row_sum)`. The condition is not necessary for asymptotic stability: certain rotations are stable while this particular interval norm test fails. Returning `stationary=None` is a refusal to *prove* it by this sufficient argument, not proof of physical instability.

## Consistency is not diagnosis

For measurement y and predicted C*xhat, the expected componentwise sensor envelope is `C*xhat ± (|C|E+V)`. Readings outside it contradict at least one declared assumption—sensor, timing, state, plant, applied input or noise bounds. They cannot identify a faulty sensor without independent redundancy and diagnostic evidence. Two apparently consistent readings also do not prove the sensors are authentic. No hardware or safety interlock is operated by this reference tool.

**Sources:** Stanford and MIT observer introductions on Luenberger error dynamics, and NIST's final OT guidance on separating integrity and operational safety. This chapter contains original finite interval derivations, not a third-party experiment.
