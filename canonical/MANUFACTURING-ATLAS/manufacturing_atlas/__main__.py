from .models import tolerance_fit
from .v02_models import wilson_yield_interval
print('ATLAS FORGE Manufacturing v0.2.0 — original reconciled fourteen-node federation')
print('Finite sample 100/100 pass Wilson 95% bound:',wilson_yield_interval(100,100)['lower'])
