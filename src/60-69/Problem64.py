from math import sqrt
import numpy as np
from decimal import Decimal, localcontext

def get_cont_fract(D):

    a_out=[]

    u=0
    v=1
    a=int(sqrt(D))
    a0=int(sqrt(D))

    a_out.append(a)

    while a != 2*a0:
        u=a*v-u
        v=(D-u**2)/v
        a=int((a0+u)/v)
        
        a_out.append(a)

    return a_out


N=10000

odd=0
for n in range(1,N+1):
    if(int(sqrt(n)) != sqrt(n) and len(get_cont_fract(n))%2==0):
        odd+=1

print(odd)
