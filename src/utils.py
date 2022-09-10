import math
from re import T

def percentile(p, t):
    index  = math.ceil(len(p) * t/100.0) - 1
    return p[index]

def copy(t):
    if not isinstance(t, dict):
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return dict(u)
