"""Bounded SI unit algebra and explicit quantity-kind conversion.

Grammar: atom [^ signed_integer] joined by * or /. No implicit multiplication,
parentheses, automatic prefix guessing, logarithmic units, or arbitrary eval.
A dimensional match does not establish quantity-kind or physical equivalence.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import re
from typing import Any

Dimensions = tuple[int, int, int, int, int, int, int]  # L M T I Theta N J
ZERO: Dimensions = (0, 0, 0, 0, 0, 0, 0)


def number(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f'{label} must be a finite real JSON number')
    try:
        result = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f'{label} is outside floating point range') from exc
    if not math.isfinite(result):
        raise ValueError(f'{label} must be finite')
    return result


@dataclass(frozen=True)
class Unit:
    symbol: str
    dimensions: Dimensions
    scale: float = 1.0
    offset: float = 0.0
    atoms: tuple[str, ...] = ()


# Exact scale definitions are represented in binary floating point at runtime.
CATALOG: dict[str, Unit] = {}

def _add(symbol: str, dims: Dimensions, scale: float = 1.0, offset: float = 0.0):
    CATALOG[symbol] = Unit(symbol, dims, scale, offset, (symbol,))

for symbol, dims in {
    '1':ZERO,'m':(1,0,0,0,0,0,0),'kg':(0,1,0,0,0,0,0),
    's':(0,0,1,0,0,0,0),'A':(0,0,0,1,0,0,0),'K':(0,0,0,0,1,0,0),
    'mol':(0,0,0,0,0,1,0),'cd':(0,0,0,0,0,0,1),
    'Hz':(0,0,-1,0,0,0,0),'Bq':(0,0,-1,0,0,0,0),
    'N':(1,1,-2,0,0,0,0),'Pa':(-1,1,-2,0,0,0,0),
    'J':(2,1,-2,0,0,0,0),'W':(2,1,-3,0,0,0,0),
    'C':(0,0,1,1,0,0,0),'V':(2,1,-3,-1,0,0,0),
    'Ohm':(2,1,-3,-2,0,0,0),'rad':ZERO,'sr':ZERO,
}.items(): _add(symbol, dims)
_add('g', CATALOG['kg'].dimensions, 1e-3)
_add('L',(3,0,0,0,0,0,0),1e-3)
_add('min',CATALOG['s'].dimensions,60.0)
_add('h',CATALOG['s'].dimensions,3600.0)
_add('%',ZERO,0.01)
_add('degC',CATALOG['K'].dimensions,1.0,273.15)
# Deliberately bounded registry, not all SI prefixes or all legal SI expressions.
for symbol in ('m','g','s','A','K','mol','Hz','Bq','N','Pa','J','W','C','V','Ohm','L'):
    base=CATALOG[symbol]
    for prefix, scale in [('n',1e-9),('u',1e-6),('m',1e-3),('c',1e-2),('k',1e3),('M',1e6),('G',1e9)]:
        key=prefix+symbol
        if key not in CATALOG: _add(key,base.dimensions,base.scale*scale)

KIND_DIMS: dict[str, Dimensions] = {
    'length':CATALOG['m'].dimensions,'area':(2,0,0,0,0,0,0),
    'volume':(3,0,0,0,0,0,0),'mass':CATALOG['kg'].dimensions,
    'time':CATALOG['s'].dimensions,'current':CATALOG['A'].dimensions,
    'temperature':CATALOG['K'].dimensions,'amount':CATALOG['mol'].dimensions,
    'luminous_intensity':CATALOG['cd'].dimensions,'frequency':CATALOG['Hz'].dimensions,
    'activity':CATALOG['Bq'].dimensions,'angular_velocity':CATALOG['Hz'].dimensions,
    'velocity':(1,0,-1,0,0,0,0),'acceleration':(1,0,-2,0,0,0,0),
    'force':CATALOG['N'].dimensions,'pressure':CATALOG['Pa'].dimensions,
    'energy':CATALOG['J'].dimensions,'torque':CATALOG['J'].dimensions,
    'power':CATALOG['W'].dimensions,'charge':CATALOG['C'].dimensions,
    'voltage':CATALOG['V'].dimensions,'resistance':CATALOG['Ohm'].dimensions,
    'density':(-3,1,0,0,0,0,0),'kinematic_viscosity':(2,0,-1,0,0,0,0),
    'angle':ZERO,'solid_angle':ZERO,'ratio':ZERO,
}
ATOM_RE = re.compile(r'(1|%|[A-Za-z]+)(?:\^([+-]?\d{1,2}))?\Z')


def parse_unit(expression: str) -> Unit:
    if not isinstance(expression,str) or not expression or len(expression)>128:
        raise ValueError('unit must be a nonempty string of at most 128 characters')
    s=expression.replace('\u03bc','u').replace('\u00b5','u').replace('°C','degC')
    s=s.strip()
    # Permit whitespace around operators, but never merge separate unit tokens.
    s=re.sub(r'\s*([*/^])\s*',r'\1',s)
    if any(c.isspace() for c in s):raise ValueError('use explicit * for multiplication')
    if s in CATALOG:return CATALOG[s]
    pieces=re.split(r'([*/])',s)
    if not pieces or len(pieces)>31 or len(pieces)%2!=1:
        raise ValueError('unsupported unit grammar')
    dims=list(ZERO);scale=1.0;atoms=[];sign=1
    for i,piece in enumerate(pieces):
        if i%2:
            sign=1 if piece=='*' else -1
            continue
        m=ATOM_RE.fullmatch(piece)
        if m is None or m[1] not in CATALOG:raise ValueError('unknown unit or unsupported grammar: '+piece)
        atom=CATALOG[m[1]];power=sign*int(m[2] or 1)
        if abs(power)>12:raise ValueError('unit exponent outside supported range -12..12')
        if atom.offset:raise ValueError('affine degC must stand alone; use K for algebra')
        try:scale*=atom.scale**power
        except OverflowError as exc:raise ValueError('unit scale overflow') from exc
        if not math.isfinite(scale) or scale==0:raise ValueError('unit scale overflow/underflow')
        dims=[x+power*y for x,y in zip(dims,atom.dimensions)]
        if any(abs(x)>24 for x in dims):raise ValueError('composite dimension outside supported range')
        if power!=0: atoms.extend(atom.atoms)
    return Unit(s,tuple(dims),scale,0.0,tuple(atoms))


def validate_kind(unit: Unit, quantity_kind: str) -> None:
    if not isinstance(quantity_kind,str) or quantity_kind not in KIND_DIMS:
        raise ValueError('explicit supported quantity_kind required')
    if unit.dimensions!=KIND_DIMS[quantity_kind]:raise ValueError('unit dimensions do not match quantity_kind')
    # Dimensional identity is insufficient for frequencies, angles and ratios.
    atoms=unit.atoms
    has_hz=any(a.endswith('Hz') for a in atoms)
    has_bq=any(a.endswith('Bq') for a in atoms)
    if quantity_kind=='frequency' and (has_bq or 'rad' in atoms or 'sr' in atoms):
        raise ValueError('frequency is not activity or angular velocity; use an explicit physical relation')
    if quantity_kind=='activity' and (has_hz or 'rad' in atoms or 'sr' in atoms):
        raise ValueError('activity is not frequency or angular velocity')
    if quantity_kind=='angular_velocity' and ('rad' not in atoms or has_hz or has_bq or 'sr' in atoms):
        raise ValueError('angular_velocity requires explicit rad per time')
    if quantity_kind=='angle' and ('rad' not in atoms or 'sr' in atoms):raise ValueError('angle requires explicit rad')
    if quantity_kind=='solid_angle' and ('sr' not in atoms or 'rad' in atoms):raise ValueError('solid angle requires explicit sr')
    if quantity_kind=='ratio' and ('rad' in atoms or 'sr' in atoms):raise ValueError('angle units are not an untyped ratio')


def convert_quantity(value: float, from_unit: str, to_unit: str, *, quantity_kind: str,
                     uncertainty: float | None = None, interval: bool = False) -> dict:
    """Convert a declared quantity and optional standard uncertainty; no inference of kind."""
    x=number(value,'value');u=None if uncertainty is None else number(uncertainty,'uncertainty')
    if u is not None and u<0:raise ValueError('uncertainty must be nonnegative')
    if not isinstance(interval,bool):raise ValueError('interval must be boolean')
    a,b=parse_unit(from_unit),parse_unit(to_unit)
    validate_kind(a,quantity_kind);validate_kind(b,quantity_kind)
    if a.dimensions!=b.dimensions:raise ValueError('incompatible dimensions')
    if interval and quantity_kind!='temperature':raise ValueError('interval flag is only supported for temperature')
    canonical=x*a.scale+(0.0 if interval else a.offset)
    if quantity_kind=='temperature' and not interval and canonical<0:
        raise ValueError('negative thermodynamic temperature outside this conversion model')
    y=(canonical-(0.0 if interval else b.offset))/b.scale
    uy=None if u is None else u*abs(a.scale/b.scale)
    if not math.isfinite(y) or (uy is not None and not math.isfinite(uy)):raise ValueError('converted value outside finite range')
    return {'schema':'measurement.quantity-conversion/1','value':y,'standard_uncertainty':uy,
            'from_unit':a.symbol,'unit':b.symbol,'quantity_kind':quantity_kind,'dimensions':list(a.dimensions),
            'temperature_interval':interval,'quantity_kind_basis':'explicit_caller_declaration_not_inferred',
            'limitations':['Finite unit catalog and explicit product/quotient/integer-power grammar only.',
                           'Unit compatibility is not validation of a physical measurement or calibration.']}
