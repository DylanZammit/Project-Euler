from decimal import *
import numpy as np

def sqrt(x, iters):
    act=np.sqrt(x)
    if act == int (x):
        return act
    l=2
    while l*l<x:
        l+=1

    s=l-1

    for _ in range(iters):
        t=Decimal(s+l)/Decimal(2)
        if Decimal(t*t) < x:
            s=t
        else:
            l=t
        
    return t

getcontext().prec = 110

out = 0

for i in range(1, 101):
    val = sqrt(i, 400)

    if val != int(val):
        out+=int(val)
        val = str(val)
        out+=sum([int(x) for x in val[2:101]])
        

print(out)
