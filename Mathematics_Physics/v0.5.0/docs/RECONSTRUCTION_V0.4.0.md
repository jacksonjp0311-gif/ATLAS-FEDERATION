# Reconstructing the v0.4.0 electrostatics numerical reference

**Prerequisites:** locally available Python >=3.10, basic arithmetic/calculus/linear algebra knowledge from chapters 01–48. The model and all six cases execute without a network connection.

```sh
python -m math_physics_atlas
python -m unittest discover -s tests -q
python tools/independent_oracle_v04.py  # optional NumPy 2.x
```

**Example:**

```python
from math_physics_atlas.v04_models import poisson2d_problem,solve_poisson2d_cg
model=poisson2d_problem(15, 15, 1., 1., 8.8541878188e-12, 0.,lambda x,y:x)
result=solve_poisson2d_cg(model,rtol=1e-10,maxiter=2000)
assert result['converged']
print(result['residual_l2'],result['gauss_balance_residual_C_per_m'])
```

**Reconstruction sequence:** first check the unit system, grid dimensions and boundary-inclusion conventions; second construct harmonic ε face weights and an interior-only positive-definite stencil; third move known boundary voltages into b; fourth compare a dense independent solve on tiny grids; fifth solve with PCG, inspect the TRUE residual and failure status; sixth compare conserved charge/flux and a separate exact manufactured-solution refinement. The observed flux balance is a property of the **discrete** model, not proof that a constructed dielectric field matches the world.

The stored Library incremental ZIP requires an exactly SHA-256-verified full v0.3 baseline archive (recoverable from existing older releases). The restore helper verifies predecessor hash, every changed file and the exact expected reconstructed ZIP hash, then the collection test runner verifies the extracted source tree. No Bitwork router is involved.
