# 47. Observer error bounds are conditional information, not sensor integrity

A feedback design that assumes the state is directly known may cease to satisfy its original theorem when the controller uses estimates. One response is to construct a model of the observer error and explicitly carry its uncertainty. A Luenberger observer is an example of a prediction plus measurement correction, not an oracle that discovers the physical truth from a single sensor. This chapter gives a bounded scalar, discrete-time error calculation. The fuller theory includes multivariable observers, observability, Kalman estimation, set-membership filters and unknown-input observers. None of those general problems is claimed solved here.

## Time-ordering matters

Let the physical state follow `x[k+1]=a x[k]+b u_applied[k]+w[k]`. The sensor reports `y[k]=x[k]+v[k]` at that same indexed time. An observer uses the **known applied input** and updates `h[k+1]=a h[k]+b u_applied[k]+L(y[k]-h[k])`. The estimation error `e[k]=x[k]-h[k]` then satisfies `e[k+1]=(a-L)e[k]+w[k]-L v[k]`. This exact identity follows from the declared equations and is independent of the chosen feedback gain K because plant and observer use the same applied input.

If `|e[0]|<=E0`, `|w[k]|<=W`, and `|v[k]|<=V`, an interval recurrence gives `E[k+1]=|a-L| E[k]+W+|L|V`. If `|a-L|<1`, the sufficient stationary bound is `(W+|L|V)/(1-|a-L|)`. These quantities are **deterministic bounds** conditional on true input noise limits, not probabilistic confidence intervals. Uniform probability distribution or Gaussian assumptions are unnecessary, but actual bounded disturbances and timing alignment must be established externally. A probability standard deviation is not an almost-sure maximum.

For stipulated a=0.8, L=0.6, W=0.02 and V=0.01, the limiting radius is 0.0325 model units. An observer that converges in the zero-noise model does not make this bound vanish when disturbance and sensor noise remain. If `|a-L|>=1`, a finite-horizon recurrence can still be calculated but no finite stationary certificate follows from this argument. The implementation reports that absence rather than substituting a favorable value.

## When the proof fails

The equation uses *applied* input, not an unsaturated command or an incorrect timestamp. Unknown actuator lag, delayed sensors, asynchronous packets, silent measurement changes and bias beyond the declared V alter the error dynamics. A measurement consistency check can reveal that some assumed bound fails, but that does not identify whether the sensor, plant model, parameter range or timing is responsible. The observation equation itself is a hypothesis requiring evidence.

**Source scope:** MIT *Underactuated Robotics*, Chapter 19 *State Estimation*, official online table of contents and selected section https://underactuated.csail.mit.edu/ ; Mayne et al. (2006) *Robust output feedback model predictive control of constrained linear systems*, publisher abstract https://www.sciencedirect.com/science/article/pii/S0005109806001221 . The scalar recurrence here is an original transparent derivation, not the complete methods of the papers.
