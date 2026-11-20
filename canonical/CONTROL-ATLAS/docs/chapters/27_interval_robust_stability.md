# 27. Robust scalar stability under bounded parameter uncertainty

A nominal feedback pole is not evidence that a real loop is stable under uncertainty. Consider the *specified* scalar sampled-time model `x[k+1]=a x[k]+b u[k]`, `u[k]=-K x[k]`. Then the closed-loop pole is `p=a-bK`, and the exact nominal asymptotic-stability criterion is `|p| < 1`. This statement requires that the model is linear time-invariant, its variables refer to one scalar state, the state is measured without delay, and no saturation or nonlinear modes occur. A stable mathematical pole does not establish the stability or safety of real equipment with missing dynamics.

## From a point to a parameter interval

Suppose a ranges independently within `[a_min,a_max]` and b within `[b_min,b_max]`. Because p is affine in the two independent parameters, the maximum of `|a-bK|` over the **assumed rectangular uncertainty set** is attained at a corner. Evaluate the four combinations of endpoints. If *every* vertex has pole magnitude strictly below one, then the entire set of scalar models is asymptotically stable under the stated fixed feedback law. If one vertex fails, the declared parameter box contains an unstable member; that does not prove the actual machine is unstable unless its parameters are known to inhabit that part of the box.

With the constructed bounds a∈[0.9,1.1], b∈[0.25,0.45] and K=1, all possible poles lie between 0.45 and 0.85, hence the strict test passes. The answer is conditional on **independence and completeness** of the parameter box. A plant with hidden time delay, friction, integral action or actuator saturation cannot be declared robust merely because this affine rectangle passed.

## Failure of an unjustified bound

Take a∈[1.35,1.8] and b∈[0.05,0.25], K=1. The largest pole magnitude is 1.75. One or more admissible scalar models are unstable. The program reports the worst-case corner and every vertex so another system can audit the numerical result. It does not project whether an actual motor will break or how an operator should respond.

A trustworthy range must be identified from physical experiments or justified design specifications, with units, timebase, uncertainty, sensor loading and sampling conditions. Correlated parameter uncertainty may form a nonrectangular set; using a rectangular overapproximation can be conservative. Parameter estimation errors are not interchangeable with an a priori guaranteed interval. A mean ± one standard deviation is not a hard uncertainty bound.

**Scientific connection:** Åström and Murray, *Feedback Systems*, second edition, author-maintained [FBSwiki](https://fbswiki.org/) and [Princeton Press second edition](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems), stability and robustness chapters (source-page scope, not an independently reviewed full-book derivation). The rectangle criterion is derived algebraically for this explicitly limited scalar case.
