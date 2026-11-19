# Chapter 24: Datum frames connect drawings to measured coordinates

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`[X,Y]ᵀ = t + s R(θ)[x,y]ᵀ`

## Scientific derivation and engineering reasoning

Part dimensions become meaningful only relative to defined datums and coordinate systems. A planar rigid-body transform rotates a point through angle θ and translates it by t. Optionally, an isotropic scale factor can represent a declared calibration correction. Rotation is orthogonal: RᵀR=I and preserves lengths when scale=1. The inverse transform applies Rᵀ to the translated observation and divides by scale.

The model checks finite coordinates and a positive scale, and the independent oracle uses a separately assembled NumPy rotation matrix. It does not identify a coordinate transform from noisy observations, which would require calibration targets and an uncertainty model. A perfect numerical inverse of a declared transform cannot prove a machine's actual axes are perpendicular, free of backlash, or stable with temperature.

Constructed test: point (1,0), 90° rotation and translation (3,5) gives (3,6) within floating rounding. Random inverse-transform cases recover the original coordinates. If inspection results are compared without consistent frames, an otherwise conforming part can be falsely rejected or a bad part falsely accepted.

Future manufacturing releases should add measured 3D transformations, squareness, probe offsets, artefact registration and coordinate covariance, all with authentic calibration evidence.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.datum_rigid_transform_xy`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

A mathematical frame transform is not a physically calibrated CMM or machine-tool coordinate system.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
