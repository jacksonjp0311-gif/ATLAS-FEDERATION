# Reconstruct the scientific calculations offline

This guide assumes Python 3.10+ and a verified extraction of the standalone Mathematics/Physics Atlas. **No API tokens, network, cloud models, Bitwork router, compiler toolchain or lab equipment are needed for the bounded numerical references.**

```
cd MATHEMATICS-PHYSICS-ATLAS
python -m unittest discover -s tests -p 'test_v1_*.py' -q
python -m math_physics_atlas
```

Read Chapter 57 and inspect `math_physics_atlas/v1_models.py`. To run a steady two-carrier case:

```python
from math_physics_atlas.v1_models import device_problem,solve_device,physical_scaling
scale=physical_scaling(300,1e-6,1.04e-10,1e21)
problem=device_problem(16,scale['lambda_sq'],doping=.05,voltage=(0.,.35),
                       electrons=(.8,.9),holes=(1.1,1.0))
result=solve_device(problem,tol=1e-9,relax=.3)
print(result.iterations,result.residuals['poisson'])
```

If it fails, the deliberate nonconvergence is part of the contract: check the model domain, boundary assumptions and update strategy. Do not reinterpret a failure as a physical prediction.

The optional independent oracle requires NumPy and SciPy already installed from trusted local wheels:

```
python tools/independent_oracle_v1.py
```

The original 56 chapters and v0.5 release-specific tests are preserved. Within the federation `tools/check_collection.py` executes all 21 historical/current test suites with version-specific snapshots. `python tools/check_manifest.py verify .` and `python tools/survival_audit.py --root . --check-files` verify archive structure; their success does not authenticate scientific claims. The release folder contains a direct predecessor delta restore script with exact checksums.
