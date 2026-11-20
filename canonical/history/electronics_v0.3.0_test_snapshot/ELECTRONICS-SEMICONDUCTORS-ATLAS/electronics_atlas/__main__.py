from .models import thermal_voltage
from .v02_models import ripple_adder_unsigned
print('ATLAS FORGE original federation — Electronics & Semiconductors v0.2.0')
print('Thermal voltage at 300 K [V]:',thermal_voltage(300))
print('4-bit example 13+6 ->',ripple_adder_unsigned(13,6,4))
