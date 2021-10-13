import math

def b(p):
    return -(math.cos(math.pi * p) - 1.0)/2

def si(p):
    return math.sin(math.pi * p/2)

def so(p):
    return -(math.sin(math.pi * (0.5 + p/2)) - 1.0)

def qi(p):
    return p*p

def qo(p):
    return -(p * (p - 2))

def ci(p):
    return p*p*p

def co(p):
    return (p-1)**3 + 1