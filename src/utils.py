import math

def percentile(p, t):
    index  = math.ceil(len(p) * t/100.0) - 1
    return p[index]
