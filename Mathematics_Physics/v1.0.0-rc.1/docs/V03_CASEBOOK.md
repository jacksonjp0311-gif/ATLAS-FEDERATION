# Mathematics & Physics Atlas 0.3.0 — four constructed investigations

All numeric values are synthetic educational fixtures, not measured scientific data.

## Case 29 — Rank-deficient least squares

Choose A=[[1,2],[2,4],[3,6]], b=[1,2,3]. Verify exactly one nonzero singular value sqrt(70) and minimum-norm parameter x=(0.2,0.4). Construct x=(1,0) as a distinct fit of equal quality. **Interpretation:** fit does not imply parameter identifiability. Execute `svd_least_squares` and compare with a full-rank test. Reject claims of improved AI performance.

## Case 30 — Underdetermined inverse and minimum norm

A=[[1,0,0],[0,1,0]], b=[4,5] gives x=(4,5,0). Every (4,5,c) is equally observationally consistent. Verify the minimum norm choice and the pseudoinverse cutoff. Perturb singular directions and document sensitivity to rank_rtol before claiming parameters.

## Case 31 — Constant-charge electrostatic slab

At L=1 m, epsilon=1 F/m and constant rho=2 C/m^3 with grounded Dirichlet boundaries, V(x)=x(1-x) volt. These teaching parameters are intentionally artificial. For 19 interior nodes calculate V, face E and displacement D and verify telescoped Gauss balance. The matching residual validates the discrete model implementation, not vacuum permittivity or semiconductor devices.

## Case 32 — Implicit diffusion sine mode

Initialize sin(pi x/L) at 41 nodes with zero boundary temperatures. Run backward Euler, compare against discrete eigenmode amplification and check monotone decay of the fundamental. Repeat with Crank–Nicolson at a large Fourier number, demonstrating that unconditional von Neumann stability need not exclude sign oscillations in stiff high-frequency modes. Never use these simulated temperatures to claim heat-transfer calibration.

## Reproduce

```sh
python -m math_physics_atlas
python -m unittest discover -s tests -p 'test_v03_*.py' -q
python tools/independent_oracle_v03.py  # optional NumPy numerical checks
```

The cases explicitly distinguish algebraic invariants, floating-point comparisons, model assumptions and original measured evidence.
