import numpy as np
from math import sqrt
from decimal import *

sols=[]

arg_maxim = 0
maxim=2

def get_cont_fract(D):
    
    a_out=[]

    u=0
    v=1
    a=int(sqrt(D))
    a0=int(sqrt(D))

    a_out.append(a)

    r=0

    while a != 2*a0:
        u=a*v-u
        v=(D-u**2)/v
        a=int((a0+u)/v)
        
        a_out.append(a)
        r+=1

    return r-1, a_out


def cont_fraction(D):

    global arg_maxim

    h0 = 0
    h1 = 1

    r, a_s=get_cont_fract(D)

    a_s=a_s+a_s[1:]+[a_s[1]]

    N = r if(r%2==1) else 2*r+1

    for x in range(N+1):
        h2=a_s[x]*h1+h0

        h0=h1
        h1=h2
        
    return h1
    
lim = 1000

for D in range(2, lim+1): 
    
    if(sqrt(D) != int(sqrt(D))): 
        comp=cont_fraction(D)

        if(comp>arg_maxim):
            arg_maxim=comp
            maxim=D

print(arg_maxim)
print(maxim)
