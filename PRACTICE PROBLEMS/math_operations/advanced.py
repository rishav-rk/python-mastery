# advanced.py

import math

def power(base, exponent):
    return base ** exponent

def logarithm(value, base=math.e):
    if value <= 0:
        raise ValueError("Logarithm only defined for positive values")
    return math.log(value, base)
