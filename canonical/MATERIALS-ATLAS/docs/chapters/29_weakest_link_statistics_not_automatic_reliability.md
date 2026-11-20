# 29. Weibull strength fits versus a physical weakest-link model

## Separate a distribution from its mechanism

The ordinary two-parameter Weibull distribution is a flexible probability law for a random variable. Fitting it to a collection of measured strengths does not automatically justify the *weakest-link fracture theory* needed to scale from a test coupon to a larger component. An explicit methodological discussion appears in *Statistics of ceramic strength: Use ordinary Weibull distribution function or Weibull statistical fracture theory?*, *Ceramics International* 46 (2020), DOI 10.1016/j.ceramint.2020.05.024. [Accessible publisher abstract](https://www.sciencedirect.com/science/article/pii/S0272884220313092).

## Conditional volume scaling

If the model assumes independent, identically distributed elemental volumes and spatially uniform stress, a simplified conditional volume survival law is `S(σ,V)=exp[−(V/V0)(σ/σ0)^m]`. Here `σ` and `σ0` are in the same stress units (the calculator uses MPa), V and V0 are in the same volume units (mm³), and m is dimensionless. The model assumes an actual **bulk flaw population** appropriate for volume scaling. Surface flaws, stress gradients, nonuniform microstructures and shape differences require other formulations. The model is not established by fitting an ordinary Weibull CDF alone.

## What the simulator demonstrates

Given assumed σ=120 MPa, σ0=200 MPa, m=5, V=V0=1000 mm³, conditional survival is approximately **0.9252**. Doubling the volume under the *declared independent bulk-flaw model* yields survival approximately **0.8560**, equal to the original survival squared. These numbers are constructed parameter illustrations, not reliability estimates for a real ceramic. The software requires an explicit `physical_weakest_link_assumed=True` argument to prevent accidental application of volume scaling to arbitrary empirical strength distributions.

## Why an estimate is not a qualification

Estimating shape and scale requires representative specimens, failure censoring policy, fracture origin characterization, machining and surface finish, residual stress and a defensible statistical sampling model. Test fixture, loading mode, environment, stressed area/volume, temperature, time-dependent slow crack growth and manufacturing defects all matter. Use appropriate design and fracture standards and independent review for certification or safety-critical sizing. The program does not estimate Weibull parameters from sample strengths, does not implement design allowables, and makes no component reliability guarantee.

The safest default for an unknown flaw model is to **refuse transfer across volumes**. When the physical weakest-link hypothesis is unsubstantiated, report the empirical fitted distribution and its specimen domain separately. A numerical probability output should carry its experimental basis, uncertainties, failure definition and source limitations intact.

**Connections:** Chapter 17 crack mechanics, Chapter 10 degradation and service, and Measurement Atlas for reliability/uncertainty interpretation.
