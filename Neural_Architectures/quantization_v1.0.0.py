"""Symmetric per-tensor int8 educational quantization; not calibrated LLM quantization."""
import math

def quantize_int8(values):
    if not isinstance(values,(list,tuple)) or not values or not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) for v in values):
        raise ValueError('finite nonempty calibration vector required')
    peak=max(abs(v) for v in values)
    scale=peak/127 if peak>0 else 1.0
    q=[max(-127,min(127,round(v/scale))) for v in values]
    return scale,q

def dequantize(scale,q):
    if not isinstance(scale,(float,int)) or not math.isfinite(scale) or scale<=0 or not all(type(v) is int and -127<=v<=127 for v in q):
        raise ValueError('invalid signed calibration')
    return [scale*v for v in q]
