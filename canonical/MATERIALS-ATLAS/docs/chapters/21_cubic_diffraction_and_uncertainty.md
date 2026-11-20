# 21. Indexed cubic diffraction: recovering a lattice parameter without overclaiming

**Status:** bounded first-order diffraction arithmetic from supplied peak assignments. It does not identify an unknown crystal, perform Rietveld refinement, validate instrument calibration, or certify a sample.

## The measurable and the inferred quantities

A powder diffraction instrument reports intensity against a scattering angle, often denoted **2theta**. The Bragg angle theta is half that value. For first-order Bragg scattering, `lambda=2*d*sin(theta)`. For a cubic lattice whose reflection has already been indexed as (h,k,l), `d=a/sqrt(h²+k²+l²)`, so

`a=lambda*sqrt(h²+k²+l²)/(2*sin(theta))`.

The wavelength lambda and resulting lattice parameter a must use the same length unit. The Atlas accepts angstroms, degrees for 2theta, and integer h,k,l; it converts the half-angle to radians internally. It requires nonzero hkl and `0<2theta<180°`. The first-order convention does not by itself establish whether the assigned reflection is allowed by the lattice's space group.

The IUCr explains why the 1D powder pattern compresses 3D reciprocal-space information and why peak overlap and indexing ambiguity matter. An apparent set of lattice parameters from a few assigned peaks is not proof of material identity. Distinct phases can overlap; texture, microstrain, sample displacement and instrument aberrations can shift or reshape peaks. A serious phase identification needs independent structure-factor and pattern evidence.

## Multiple peaks and independent angular errors

If several independent indexed peaks produce estimates `a_i` with first-order angle standard uncertainties `u_i`, the inverse-variance estimate is `a_bar = sum(a_i/u_i²)/sum(1/u_i²)`, with angle-only standard uncertainty `1/sqrt(sum(1/u_i²))`. For one peak, the absolute first-order sensitivity to the **full** scan angle 2theta expressed in degrees is

`|da/d(2theta_deg)| = |a*cot(theta)*pi/360|`.

The factor `pi/360` includes both the degree-to-radian conversion and the halving of 2theta. Omitting either doubles or otherwise distorts the uncertainty. Our code rejects missing or zero uncertainty and repeated equivalent cubic reflection families because those inputs would need a covariance model rather than independent weights.

## A common uncertainty is not another independent observation

Every peak in one scan typically uses the same nominal wavelength. Its uncertainty is a shared component, not independent per peak. Under small-error linear propagation, `u_a,lambda = |a_bar/lambda| * u_lambda`. The combined standard uncertainty in this restricted model is `sqrt(u_a,angle² + u_a,lambda²)` when the two components are independent. Adding more peaks may reduce the random-angle contribution; it does **not** divide the common wavelength contribution by the square root of the peak count. The same logic applies to many shared calibration effects, although this implementation does not model instrument zero offset or peak-to-peak angular covariance.

The program reports `chi²=sum(((a_i-a_bar)/u_i)²)` and degrees of freedom `n-1`. A large chi-square may signal underestimated errors, bad indexing, noncubic symmetry, or unmodeled systematic effects. It is a diagnostic; the software does not silently scale the uncertainties to force a good fit. A small chi-square is not proof that the specimen is phase-pure.

## Practical study template

Record specimen identifier, composition, processing history, scan date, radiation/wavelength and its uncertainty, temperature, peak extraction method, independently justified hkl indexing, each 2theta and uncertainty, instrument correction method, excluded peaks and reasons, covariance assumptions, fitted a and diagnostics, and all remaining uncertainty contributors. A publication-quality crystallographic refinement requires substantially more than this teaching calculator.

**Sources and scope:** IUCr Dictionary, *Bragg’s law*, https://dictionary.iucr.org/Bragg%27s_law ; IUCr *International Tables for Crystallography* Vol. C §1.2.6 cubic crystal system, https://it.iucr.org/Cb/ch1o2v0001/sec1o2o6/ ; IUCr educational pamphlet §4.1 cubic structures, https://www.iucr.org/what-we-do/education/pamphlets/study-of-metals-and-alloys-x-ray-powder-diffraction-methods . These specific public sections were inspected; no restricted tables were mirrored.
