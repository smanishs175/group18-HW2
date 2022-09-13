import math
from re import T

def o(t):

    if type(t) != dict:
        return str(t)
    
    out = ""
    for k,v in t.items():
        temp = f"{k}: {v}"
        # concat
        out += " " + temp
    
    return out

def oo(t):
    print(o(t))
    return t

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

def push(t,x):
    t.append(x)
    return x

def rnd(x, places=2):
    mult = pow(10, places)
    return math.floor(x * mult + 0.5) / mult
